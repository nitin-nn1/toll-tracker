import sqlite3

def initialize_database():
    # 1. Connect to the database (this creates the file if it doesn't exist)
    conn = sqlite3.connect('tolls.db')
    cursor = conn.cursor()

    print("Building the database...")

    # 2. Create a table for the static NTTA routes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ntta_rates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            highway_name TEXT NOT NULL,
            toll_tag_rate REAL NOT NULL,
            zip_cash_rate REAL NOT NULL
        )
    ''')

    # 3. Clear any old test data to avoid duplicates if you run this twice
    cursor.execute('DELETE FROM ntta_rates')

    # 4. Insert the flat rates for a standard 2-axle vehicle
    rates_data = [
        ('DNT', 1.94, 3.88),  # Example segment on the Dallas North Tollway
        ('PGBT', 2.35, 4.70), # Example segment on the Pres. George Bush Turnpike
        ('SRT', 3.10, 6.20)   # Example segment on the Sam Rayburn Tollway
    ]

    cursor.executemany('''
        INSERT INTO ntta_rates (highway_name, toll_tag_rate, zip_cash_rate)
        VALUES (?, ?, ?)
    ''', rates_data)

    # 5. Save the changes and close the connection
    conn.commit()
    conn.close()
    
    print("Success! Database 'tolls.db' created and populated.")

# Run the function
if __name__ == "__main__":
    initialize_database()