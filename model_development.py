# model_development.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

def develop_model():
    try:
        df = pd.read_csv('prepared_materials_data.csv')
        
        features_to_drop = ['material_id', 'material_name', 'Material_Suitability_Score']
        
        X = df.drop(columns=features_to_drop)
        y = df['Material_Suitability_Score']
        
        X = pd.get_dummies(X, columns=['material_type'], drop_first=True)
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        y_pred = model.predict(X_test)
        
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        print("\n--- Model Training & Evaluation Complete ---")
        print(f"Random Forest Regressor (Target: Material_Suitability_Score)")
        print(f"Mean Absolute Error (MAE): {mae:.4f}")
        print(f"R-squared (R²): {r2:.4f}")
        
        model_filename = 'rf_suitability_model.joblib'
        joblib.dump(model, model_filename)
        
        feature_list_filename = 'model_features.joblib'
        joblib.dump(X.columns.tolist(), feature_list_filename)
        
        print(f"\nModel saved as '{model_filename}'")
        print(f"Feature list saved as '{feature_list_filename}'")

    except FileNotFoundError:
        print("ERROR: 'prepared_materials_data.csv' not found. Ensure you ran data_pipeline.py successfully.")
    except Exception as e:
        print(f"An error occurred during model development: {e}")

if __name__ == "__main__":
    develop_model()
