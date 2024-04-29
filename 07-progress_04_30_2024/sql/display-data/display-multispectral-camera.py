import sqlite3

def display_data(cursor, table_name, limit=10):
    # Execute SQL query to retrieve a limited number of rows
    cursor.execute(f"SELECT * FROM {table_name} LIMIT ?", (limit,))
    rows = cursor.fetchall()

    # Get column information
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = [column[1] for column in cursor.fetchall()]

    # Calculate column widths based on the maximum length of the data in each column
    column_widths = [len(max([str(row[i]) for row in rows] + [col], key=len)) for i, col in enumerate(columns)]

    # Print table name and header
    print(f"\nTable: {table_name}")
    header = " | ".join(col.ljust(column_widths[i]) for i, col in enumerate(columns))
    print(header)
    print("-" * len(header))

    # Print rows with data aligned
    for row in rows:
        formatted_row = " | ".join(str(col).ljust(column_widths[i]) for i, col in enumerate(row))
        print(formatted_row)

# Connect to the SQLite database
conn = sqlite3.connect('../nanoswai.db')
cursor = conn.cursor()

# Display first 10 records from operation_periods table
display_data(cursor, "operation_periods")

# Display first 10 records from multispectral_camera table
display_data(cursor, "multispectral_camera")

# Close the connection to the database
conn.close()
