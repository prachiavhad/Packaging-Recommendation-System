from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import sqlite3

app = Flask(__name__)
CORS(app)

# ------------------ INDUSTRY RULES ------------------
INDUSTRY_RULES = {
    "Food": {"min_strength": 40, "ban": []},
    "Healthcare": {"min_strength": 70, "ban": ["Cork", "Jute"]},
    "Electronics": {"min_strength": 80, "ban": ["Cork", "Paper"]},
    "Cosmetics": {"min_strength": 50, "ban": []},
    "Fashion": {"min_strength": 40, "ban": []},
    "Toys": {"min_strength": 60, "ban": ["Glass"]},
    "Home Appliance": {"min_strength": 90, "ban": ["Paper", "Cork"]}
}

# ------------------ INDUSTRY WEIGHTS ------------------
INDUSTRY_WEIGHTS = {
    "Food": {"strength": 0.3, "cost": 0.3, "co2": 0.4},
    "Healthcare": {"strength": 0.5, "cost": 0.2, "co2": 0.3},
    "Electronics": {"strength": 0.6, "cost": 0.2, "co2": 0.2},
    "Fashion": {"strength": 0.3, "cost": 0.4, "co2": 0.3},
    "Cosmetics": {"strength": 0.2, "cost": 0.3, "co2": 0.5},
    "Toys": {"strength": 0.4, "cost": 0.3, "co2": 0.3},
    "Home Appliance": {"strength": 0.6, "cost": 0.25, "co2": 0.15}
}

# ------------------ API ------------------
@app.route('/api/recommend', methods=['POST'])
def recommend():
    try:
        data = request.json
        industry = data.get("industry", "Food")
        user_strength = int(data.get("strength", 50))

        rules = INDUSTRY_RULES.get(industry, INDUSTRY_RULES["Food"])
        weights = INDUSTRY_WEIGHTS.get(industry, INDUSTRY_WEIGHTS["Food"])

        min_strength = max(user_strength, rules["min_strength"])

        conn = sqlite3.connect("materials.db")

        df = pd.read_sql("""
            SELECT
                material_name,
                MAX(strength) AS strength,
                AVG(unit_cost) AS unit_cost,
                COALESCE(AVG(co2_emission_score), 0) AS co2_emission_score,
                AVG(biodegradability_score) AS biodegradability_score,
                AVG(recyclability_pct) AS recyclability_pct
            FROM materials
            WHERE strength >= ?
            GROUP BY material_name
        """, conn, params=(min_strength,))

        conn.close()

        if df.empty:
            return jsonify({"status": "error", "message": "No materials found"})

        # Remove banned materials
        df = df[~df['material_name'].isin(rules["ban"])]
        if df.empty:
            return jsonify({"status": "error", "message": "No industry-compliant materials"})

        # ------------------ METRICS ------------------
        df['predicted_cost'] = df['unit_cost'] * 83

        df['predicted_co2'] = (
            df['co2_emission_score'] * 0.6 +
            (100 - df['biodegradability_score']) * 0.4
        ) / 10

        # Normalization (safe)
        df['cost_norm'] = df['predicted_cost'] / df['predicted_cost'].max()
        df['co2_norm'] = df['predicted_co2'] / (df['predicted_co2'].max() or 1)
        df['strength_norm'] = df['strength'] / df['strength'].max()

        # ------------------ INDUSTRY-AWARE SCORING ------------------
        df['suitability_index'] = (
            weights["co2"] * (1 - df['co2_norm']) +
            weights["cost"] * (1 - df['cost_norm']) +
            weights["strength"] * df['strength_norm']
        ) * 10

        df = df.sort_values("suitability_index", ascending=False).head(10)

        return jsonify({
            "status": "success",
            "recommendations": df.round(2).to_dict(orient="records")
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
