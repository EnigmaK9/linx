import sqlite3
import csv

# Path to the SQLite database file
database_path = 'nanoswai.db'
# List of table names to query
tables = ['camera_computer', 'sipm', 'comms_437_mhz_rx', 'comms_437_mhz_tx', 'obc']
# Specific day for the query
specific_day = '2024-04-21'

# Function to generate SQL queries for power usage per day for the given tables
def generate_power_per_day_queries(specific_day):
    queries = {}
    for table in tables:
        query = f"""
        select sum(power) as total_power,
               date(start_time, 'unixepoch') as day
        from {table}
        where date(start_time, 'unixepoch') = '{specific_day}'
        group by day;
        """
        queries[table] = query
    return queries

# Function to execute the generated queries and fetch results
def fetch_power_per_day(connection, queries):
    results = {}
    cursor = connection.cursor()
    for table, query in queries.items():
        cursor.execute(query)
        result = cursor.fetchone()
        results[table] = result[0] if result else 0  # If there's no data for that day, return 0
    return results

# CSV output file path
output_csv_path = 'power_usage_results.csv'

# Connect to the database, run the queries, fetch the results, and write them to a CSV file
conn = sqlite3.connect(database_path)
try:
    queries = generate_power_per_day_queries(specific_day)
    power_usage_results = fetch_power_per_day(conn, queries)

    # Write the results to a CSV file
    with open(output_csv_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(['Table', 'Total Power (Watts)', 'Day'])
        # Write the data
        for table, power in power_usage_results.items():
            writer.writerow([table, power, specific_day])
finally:
    conn.close()

# The 'power_usage_results.csv' file will now contain the power usage results

