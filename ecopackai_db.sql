# db_setup.py

import psycopg2

# IMPORTANT: Replace these with your actual PostgreSQL credentials
DB_NAME = "ecopackai_db"
DB_USER = "postgres"
DB_PASSWORD = "pracHI"
DB_HOST = "localhost" # or the host if you use a cloud instance
DB_PORT = "5433"

# SQL to create the Materials table
# SERIAL PRIMARY KEY: Auto-increments, unique ID for each material
SQL_CREATE_MATERIALS_TABLE = """
CREATE TABLE IF NOT EXISTS materials (
    material_name SERIAL PRIMARY KEY,
    material_type VARCHAR(50) NOT NULL,
    strength NUMERIC,
    weight_capacity NUMERIC,
    biodegradability_score INTEGER,
    co2_emission_score NUMERIC,
    recyclability_pct NUMERIC,
);
"""

# SQL to create the Product Categories table
SQL_CREATE_PRODUCTS_TABLE = """
CREATE TABLE IF NOT EXISTS products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(50),
	industry VARCHAR(50),
	weight_grams NUMERIC,
	fragility_level VARCHAR(50),
	shipping_category
);
"""

def create_tables():
    conn = None
    try:
        # Establish connection
        conn = psycopg2.connect(
            dbname=ecopackai_db, user=postgres, password=pracHi, host=localhost, port=5433
        )
        cur = conn.cursor()

        # Execute table creation commands
        cur.execute(SQL_CREATE_MATERIALS_TABLE)
        cur.execute(SQL_CREATE_PRODUCTS_TABLE)

        # Insert sample product categories (optional, you can do this later)
        cur.execute("INSERT INTO products (category_name, protection_level, is_perishable) VALUES ('Electronics', 5, FALSE) ON CONFLICT (category_name) DO NOTHING;")
        cur.execute("INSERT INTO products (category_name, protection_level, is_perishable) VALUES ('Food/Perishables', 3, TRUE) ON CONFLICT (category_name) DO NOTHING;")

        # Commit changes
        conn.commit()
        print("Database tables and initial product categories created successfully.")

    except (Exception, psycopg2.Error) as error:
        print(f"Error while connecting to PostgreSQL or creating tables: {error}")
    finally:
        if conn:
            cur.close()
            conn.close()
            print("PostgreSQL connection closed.")

if __name__ == "__main__":
    create_tables()