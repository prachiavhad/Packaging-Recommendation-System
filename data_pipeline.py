import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import psycopg2

DB_NAME = "postgres"  
DB_USER = "postgres"
DB_PASSWORD = "pracHi"
DB_HOST = "localhost"
DB_PORT = "5433" 

def run_data_pipeline():
    conn = None
    try:
      
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
        )
       
        df = pd.read_sql("SELECT * FROM materials", conn)
        print(f"-Data loaded successfully from 'materials' table. {len(df)} rows found. --")
        
       
        numerical_cols = [
            'strength', 'weight_capacity', 'co2_emission_score', 
            'recyclability_pct', 'unit_cost', 'biodegradability_score'
        ]
        for col in numerical_cols:
            
            df[col] = pd.to_numeric(df[col], errors='coerce') 
            df[col] = df[col].fillna(df[col].median())
        
      
        scaler = MinMaxScaler()
        

        df['co2_norm'] = scaler.fit_transform(df[['co2_emission_score']])
        df['cost_norm'] = scaler.fit_transform(df[['unit_cost']])
        df['strength_norm'] = scaler.fit_transform(df[['strength']])
        
        df['recyclability_norm'] = scaler.fit_transform(df[['recyclability_pct']])

 
        df['CO2_Impact_Index'] = (df['co2_norm'] * 0.7) + ((1 - df['recyclability_norm']) * 0.3)
        
       
        df['Cost_Efficiency_Index'] = (df['cost_norm'] * 0.6) - (df['strength_norm'] * 0.4) 
        
        
        df['Material_Suitability_Score'] = (
            (df['biodegradability_score'] / df['biodegradability_score'].max()) * 0.4 
            - df['CO2_Impact_Index'] * 0.3 
            - df['Cost_Efficiency_Index'] * 0.3 
            + df['strength_norm'] * 0.2
        )


        df.drop(columns=['co2_norm', 'cost_norm', 'strength_norm', 'recyclability_norm'], inplace=True)

        df.to_csv("prepared_materials_data.csv", index=False)
        print("Pipeline complete. Cleaned and engineered data saved to 'prepared_materials_data.csv'.")
        
        print("\n--- Top 5 Ranked Materials (by Suitability Score) ---")
        print(df[['material_type', 'material_name', 'Material_Suitability_Score']].sort_values(by='Material_Suitability_Score', ascending=False).head())

    except (Exception, psycopg2.Error) as error:
        print(f"Error during data pipeline execution: {error}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    run_data_pipeline()
