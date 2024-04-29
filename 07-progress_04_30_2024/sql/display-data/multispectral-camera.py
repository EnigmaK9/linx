import sqlite3

def display_data(cursor, table_name, limit=10):
    cursor.execute(f"select * from {table_name} limit ?", (limit,))
    rows = cursor.fetchall()

    # Print column names
    cursor.execute(f"pragma table_info({table_name})")
    columns = [column[1] for column in cursor.fetchall()]
    print(f"\nTable: {table_name}")
    print("|".join(columns))
    print("-" * (len(columns) * 10))

    # Print table data
    for row in rows:
        print("|".join(str(col) for col in row))

# Connect to the SQLite database
conn = sqlite3.connect('../nanoswai.db')
cursor = conn.cursor()

# Display first 10 records from operation_periods table
display_data(cursor, "operation_periods")

# Display first 10 records from multispectral_camera table
display_data(cursor, "multispectral_camera")

# Close the connection to the database
conn.close()
