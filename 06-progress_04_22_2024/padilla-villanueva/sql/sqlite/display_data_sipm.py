import sqlite3
from datetime import datetime

def fetch_and_display_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('nanoswai.db')
    cursor = conn.cursor()

    # Execute SQL query to select all records from the sipm table, limited to the first 100 records
    cursor.execute('select * from sipm limit 100')

    # Fetch and display the results
    results = cursor.fetchall()

    # Format and display data in a readable table format
    print("ID  | Start Time (UTC)    | End Time (UTC)      | Duration (s) | Power (W) |Voltage (V)| Priority T | Priority E")
    print("-" * 124)  # Print a divider line for clarity to accommodate the new column

    for row in results:
        start_time_formatted = datetime.utcfromtimestamp(row[1]).strftime('%Y-%m-%d %H:%M:%S')
        end_time_formatted = datetime.utcfromtimestamp(row[2]).strftime('%Y-%m-%d %H:%M:%S')
        print(f"{row[0]:<3} | {start_time_formatted} | {end_time_formatted} | {row[3]:<12} | {row[4]:<9.2f} | {row[5]:<9.2f} | {row[6]:<10.2f} | {row[7]:<10.2f}")

    # Close the database connection
    conn.close()

# Call the function to display the data
fetch_and_display_data()

