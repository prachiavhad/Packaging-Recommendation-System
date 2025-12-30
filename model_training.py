import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor # Excellent alternative to XGBoost
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib


df = pd.read_csv('prepared_materials_data.csv')


features = ['strength', 'biodegradability_score', 'recyclability_pct', 'material_type']
X = df[features].copy()


y_cost = df['unit_cost']
y_co2 = df['co2_emission_score']


le = LabelEncoder()
X['material_type'] = le.fit_transform(X['material_type'])


X_train, X_test, y_cost_train, y_cost_test = train_test_split(X, y_cost, test_size=0.2, random_state=42)
_, _, y_co2_train, y_co2_test = train_test_split(X, y_co2, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


print("Training Models...")


rf_cost_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_cost_model.fit(X_train_scaled, y_cost_train)


gb_co2_model = GradientBoostingRegressor(n_estimators=100, random_state=42)
gb_co2_model.fit(X_train_scaled, y_co2_train)


def evaluate_model(model, X_t, y_t, target_name):
    predictions = model.predict(X_t)
    rmse = np.sqrt(mean_squared_error(y_t, predictions))
    mae = mean_absolute_error(y_t, predictions)
    r2 = r2_score(y_t, predictions)
    print(f"\nMetrics for {target_name}:")
    print(f" - RMSE: {rmse:.4f}")
    print(f" - MAE:  {mae:.4f}")
    print(f" - R2 Score: {r2:.4f}")

evaluate_model(rf_cost_model, X_test_scaled, y_cost_test, "Cost Prediction")
evaluate_model(gb_co2_model, X_test_scaled, y_co2_test, "CO2 Prediction")


X_all_scaled = scaler.transform(X)
df['predicted_cost'] = rf_cost_model.predict(X_all_scaled)
df['predicted_co2'] = gb_co2_model.predict(X_all_scaled)


df['ai_rank_score'] = (df['predicted_cost'].rank()) * 0.4 + (df['predicted_co2'].rank()) * 0.6
ranked_materials = df.sort_values('ai_rank_score')


joblib.dump(rf_cost_model, 'rf_cost_model.joblib')
joblib.dump(gb_co2_model, 'gb_co2_model.joblib')
joblib.dump(scaler, 'scaler.joblib')
joblib.dump(le, 'encoder.joblib')

print("\nTop 3 AI Recommended Materials:")
print(ranked_materials[['material_name', 'predicted_cost', 'predicted_co2']].head(3))
