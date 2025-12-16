simport psycopg2
import pandas as pd
from io import StringIO

DB_NAME = "postgres"  
DB_USER = "postgres"
DB_PASSWORD = "pracHi"
DB_HOST = "localhost"
DB_PORT = "5433" 

def ingest_csv_to_db(csv_file_path, table_name, column_list):
    conn = None
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
        )
        cur = conn.cursor()

        df = pd.read_csv(csv_file_path)
        
        df = df[column_list]

        buffer = StringIO()
    
        df.to_csv(buffer, index=False, header=False) 
        buffer.seek(0)
    
        cur.copy_from(
            buffer,
            table_name,
            sep=",",
            columns=column_list
        )

        conn.commit()
        print(f"Successfully inserted {len(df)} rows into the '{table_name}' table from '{csv_file_path}'.")

    except FileNotFoundError:
        print(f"ERROR: CSV file '{csv_file_path}' not found. Make sure it's in the same folder.")
    except (Exception, psycopg2.Error) as error:
        print(f"Error during data ingestion into '{table_name}': {error}")
        if conn:
            conn.rollback() 
    finally:
        if conn:
            cur.close()
            conn.close()

if __name__ == "__main__":
    
    materials_columns = [
        'material_name', 'material_type', 'strength', 'weight_capacity', 
        'biodegradability_score', 'co2_emission_score', 'recyclability_pct', 'unit_cost'
    ]

    ingest_csv_to_db('Materials_dataset before Cleaning.csv', 'materials', materials_columns)

    products_columns = [
        'product_name', 'industry', 'weight_grams', 'fragility_level', 'shipping_category'
    ]
    
    ingest_csv_to_db('Product_dataset before Cleaning.csv', 'products', products_columns)
