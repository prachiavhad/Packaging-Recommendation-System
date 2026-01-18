import sqlite3

def setup_logs():
    conn = sqlite3.connect('materials.db')
    cursor = conn.cursor()
    
    # Create the table to track user clicks/selections
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS selection_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            material_name TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    conn.commit()
    conn.close()
    print("✅ selection_logs table created successfully in materials.db")

if __name__ == "__main__":
    setup_logs()