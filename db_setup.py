import psycopg2

DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "pracHi"
DB_HOST = "localhost"
DB_PORT = "5433" 

SQL_CREATE_MATERIALS_TABLE = """
    CREATE TABLE IF NOT EXISTS materials (
        material_id SERIAL PRIMARY KEY,
        material_name VARCHAR(50),
        material_type VARCHAR(50) NOT NULL,
        strength NUMERIC,
        weight_capacity NUMERIC,
        biodegradability_score INTEGER,
        co2_emission_score NUMERIC,
        recyclability_pct NUMERIC,
        unit_cost NUMBERIC
    );
"""

SQL_CREATE_PRODUCTS_TABLE = """
    CREATE TABLE IF NOT EXISTS products (
        product_id SERIAL PRIMARY KEY,
        product_name VARCHAR(50),
        industry VARCHAR(50),
        weight_grams NUMERIC,
        fragility_level VARCHAR(50),
        shipping_category VARCHAR(50)
    );
"""

def create_tables():
    conn = None
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, 
            user=DB_USER, 
            password=DB_PASSWORD, 
            host=DB_HOST, 
            port=DB_PORT
        )
        cur = conn.cursor()

        cur.execute(SQL_CREATE_MATERIALS_TABLE)
        cur.execute(SQL_CREATE_PRODUCTS_TABLE)

        conn.commit()
        print("Database tables and initial product categories created successfully.")

    except (Exception, psycopg2.Error) as error:
        print(f"Error while connecting to PostgreSQL or creating tables. Check your credentials and database name: {error}")
    finally:
        if conn:
            cur.close()
            conn.close()
            print("PostgreSQL connection closed.")

if __name__ == "__main__":
    create_tables()
