# ai_recommendation_model.py
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def run_module_4():
    print("--- Training AI Recommendation Models ---")
    
    try:
        # 1. Load Data
        df = pd.read_csv('prepared_materials_data.csv')
        
        # 2. Prepare Features (X) and Targets (y)
        # We drop IDs and the calculated scores to let the AI learn from raw properties
        X = df.drop(columns=['material_id', 'material_name', 'unit_cost', 
                             'co2_emission_score', 'Material_Suitability_Score', 
                             'CO2_Impact_Index', 'Cost_Efficiency_Index'])
        
        # Convert categorical 'material_type' into numbers
        X = pd.get_dummies(X, columns=['material_type'], drop_first=True)
        feature_names = X.columns.tolist()

        # --- 3. Train Cost Model (Random Forest) ---
        print("Training Cost Predictor...")
        X_train, X_test, y_train, y_test = train_test_split(X, df['unit_cost'], test_size=0.2, random_state=42)
        cost_model = RandomForestRegressor(n_estimators=100, random_state=42)
        cost_model.fit(X_train, y_train)

        # --- 4. Train CO2 Model (XGBoost) ---
        print("Training CO2 Predictor...")
        X_train, X_test, y_train, y_test = train_test_split(X, df['co2_emission_score'], test_size=0.2, random_state=42)
        co2_model = XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
        co2_model.fit(X_train, y_train)

        # 5. Save everything for the Flask App
        joblib.dump(cost_model, 'cost_predictor.joblib')
        joblib.dump(co2_model, 'co2_predictor.joblib')
        joblib.dump(feature_names, 'ml_features_v2.joblib')
        
        print("Success! Models saved as .joblib files.")
        print(f"Features trained on: {len(feature_names)}")

    except Exception as e:
        print(f"Error during training: {e}")

if __name__ == "__main__":
    run_module_4()
