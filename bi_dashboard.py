import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

# ---------------- FOLDERS ----------------
os.makedirs("reports", exist_ok=True)
os.makedirs("static/plots", exist_ok=True)


def run_bi_pipeline():
    # ---------------- LOAD DATA ----------------

    # ---------------- LOAD DATA ----------------
    conn = sqlite3.connect("materials.db")

    df = pd.read_sql(
        """
        SELECT
            material_name AS material,
            AVG(unit_cost) AS cost,
            AVG(co2_emission_score) AS co2,
            AVG(biodegradability_score) AS biodegradability,
            AVG(recyclability_pct) AS recyclability,
            (SELECT COUNT(*) FROM selection_logs l WHERE l.material_name = materials.material_name) AS usage_count
        FROM materials
        GROUP BY material_name
        """,
        conn
    )
    conn.close()

    # Normalize column names ONCE
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    print("COLUMNS IN DF:", df.columns.tolist())

    # ---------------- KPIs ----------------
    baseline_co2 = 8.5
    baseline_cost = 65

    avg_co2 = df["co2"].mean()
    avg_cost = df["cost"].mean()

    print("Average cost:", avg_cost)
    print("Baseline cost:", baseline_cost)

    co2_reduction_pct = round(
        max(((baseline_co2 - avg_co2) / baseline_co2) * 100, 0), 2
    )
    cost_savings = round(max(baseline_cost - avg_cost, 0), 2)

    print("CO2 Reduction %:", co2_reduction_pct)
    print("Cost Savings (Rs):", cost_savings)

    # ---------------- PLOTS ----------------

    # Chart 1: Material Usage (Plotly)
    fig_usage = px.bar(
        df,
        x="material",
        y="usage_count",
        title="Material Usage Trends",
        labels={"usage_count": "Usage Frequency", "material": "Material"}
    )
    fig_usage.show()

    # Chart 1: Material Usage (Matplotlib)
    plt.figure()
    plt.bar(df["material"], df["usage_count"])
    plt.title("Material Usage Trends")
    plt.ylabel("Usage Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("static/plots/usage.png")
    plt.close()

    # Chart 2: Cost vs CO₂ (Plotly)
    fig_tradeoff = px.scatter(
        df,
        x="cost",
        y="co2",
        size="biodegradability",
        color="material",
        title="Cost vs CO₂ Footprint Trade-off"
    )
    fig_tradeoff.show()

    # Chart 2: Cost vs CO₂ (Matplotlib)
    plt.figure()
    plt.scatter(df["cost"], df["co2"])
    plt.xlabel("Cost")
    plt.ylabel("CO₂")
    plt.title("Cost vs CO₂ Trade-off")
    plt.tight_layout()
    plt.savefig("static/plots/tradeoff.png")
    plt.close()

    # Chart 3: Recyclability (Plotly)
    fig_radar = px.line_polar(
        df,
        r="recyclability",
        theta="material",
        line_close=True,
        title="Recyclability Index by Material"
    )
    fig_radar.show()

    # Chart 3: Recyclability (Matplotlib)
    plt.figure()
    plt.plot(df["material"], df["recyclability"], marker="o")
    plt.title("Recyclability Index")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("static/plots/radar.png")
    plt.close()

    # ---------------- EXCEL ----------------
    excel_path = "reports/sustainability_report.xlsx"
    df.to_excel(excel_path, index=False)
    print("Excel report generated:", excel_path)

    # ---------------- PDF ----------------
    pdf_path = "reports/sustainability_report.pdf"
    c = canvas.Canvas(pdf_path, pagesize=A4)

    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, 800, "EcoPack AI – Sustainability Report")

    c.setFont("Helvetica", 12)
    c.drawString(50, 765, f"CO2 Reduction: {co2_reduction_pct}%")
    c.drawString(50, 745, f"Cost Savings: Rs {cost_savings}")

    # Table header
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, 710, "Material")
    c.drawString(250, 710, "CO2")
    c.drawString(350, 710, "Cost (Rs)")

    c.setFont("Helvetica", 10)
    y = 690

    for _, row in df.iterrows():
        c.drawString(50, y, str(row["material"]))
        c.drawString(250, y, f"{row['co2']:.2f}")
        c.drawString(350, y, f"{row['cost']:.2f}")
        y -= 16

        if y < 60:
            c.showPage()
            c.setFont("Helvetica", 10)
            y = 780

    c.save()
    print("PDF report generated:", pdf_path)

    return co2_reduction_pct, cost_savings


# Allow standalone execution
if __name__ == "__main__":
    run_bi_pipeline()
