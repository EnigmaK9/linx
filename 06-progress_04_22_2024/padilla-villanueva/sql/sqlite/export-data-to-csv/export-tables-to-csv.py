import sqlite3
import csv

# Path to the SQLite database file
database_path = 'nanoswai.db'
# List of table names to extract
tables = ['camera_computer', 'sipm', 'comms_437_mhz_rx', 'comms_437_mhz_tx', 'obc']

# Function to extract data from a table and write it to a CSV file
def extract_data_to_csv(connection, table_name):
    cursor = connection.cursor()
    # Select all data from the table
    cursor.execute(f"SELECT id, start_time, end_time, duration, power, voltage, priority_t, priority_e FROM {table_name}")
    rows = cursor.fetchall()

    # CSV output file path
    output_csv_path = f'{table_name}.csv'

    # Write the data to a CSV file
    with open(output_csv_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(['id', 'start_time', 'end_time', 'duration', 'power', 'voltage', 'priority_t', 'priority_e'])
        # Write all the data rows
        writer.writerows(rows)

    print(f"Data from table '{table_name}' has been written to '{output_csv_path}'.")

# Connect to the database and extract data for all specified tables
conn = sqlite3.connect(database_path)
try:
    for table in tables:
        extract_data_to_csv(conn, table)
finally:
    conn.close()

