import sqlite3
import random
from datetime import datetime, timedelta

# Connect to the SQLite database
conn = sqlite3.connect('nanoswai.db')
cursor = conn.cursor()

# Function to generate data
def generate_data(num_days):
    base_date = datetime.utcnow()
    for day in range(num_days):
        for _ in range(random.randint(1, 3)):  # Assuming between 1 and 3 tasks per day for OBC
            start_time = base_date + timedelta(days=day, hours=random.randint(0, 23), minutes=random.randint(0, 59))
            duration = random.randint(60, 3600)  # Duration between 1 minute and 1 hour
            end_time = start_time + timedelta(seconds=duration)

            # Power consumption assumptions for OBC: idle, normal and high workloads
            if duration < 600:  # Short tasks, likely idle or light processing
                power = random.uniform(0.5, 1.0)
            elif duration < 1800:  # Moderate duration, normal workload
                power = random.uniform(1.0, 1.5)
            else:  # Long tasks, high processing demand
                power = random.uniform(1.5, 2.5)

            priority_d = random.uniform(0.1, 1.0)  # Priority for download tasks
            priority_e = random.uniform(0.1, 1.0)  # Execution priority

            cursor.execute('''
            insert into obc (start_time, end_time, duration, power, priority_d, priority_e)
            values (?, ?, ?, ?, ?, ?)
            ''', (int(start_time.timestamp()), int(end_time.timestamp()), duration, power, priority_d, priority_e))

    # Save the changes to the database
    conn.commit()

# Example usage: generate data for one year (365 days)
generate_data(365)

# Close the connection to the database
conn.close()

