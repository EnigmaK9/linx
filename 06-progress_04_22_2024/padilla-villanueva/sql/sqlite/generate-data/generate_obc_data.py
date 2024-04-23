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
        # Assuming a task every hour to simulate continuous operation
        for hour in range(24):
            start_time = base_date + timedelta(days=day, hours=hour)
            if random.random() > 0.5:  # 50% chance of having an active task
                duration = random.randint(60, 3600)  # Random duration between 1 minute and 1 hour
                end_time = start_time + timedelta(seconds=duration)

                if duration < 600:  # Short tasks, likely idle or light processing
                    power = random.uniform(0.5, 1.0)
                    voltage = random.uniform(3.3, 3.7)  # Lower voltage for light tasks
                elif duration < 1800:  # Moderate duration, normal workload
                    power = random.uniform(1.0, 1.5)
                    voltage = random.uniform(3.8, 4.2)
                else:  # Long tasks, high processing demand
                    power = random.uniform(1.5, 2.5)
                    voltage = random.uniform(4.3, 4.7)

                priority_t = random.uniform(0.1, 1.0)  # Priority for download tasks
                priority_e = random.uniform(0.1, 1.0)  # Execution priority
            else:  # Low power mode, simulating idle or maintenance tasks
                end_time = start_time + timedelta(hours=1)  # Idle for the rest of the hour
                power = random.uniform(0.1, 0.5)  # Very low power consumption
                voltage = random.uniform(3.0, 3.2)  # Even lower voltage for idle
                priority_t = 0.1  # Low priority for idle time
                priority_e = 0.1

            duration = int((end_time - start_time).total_seconds())  # Calculating duration from time difference

            cursor.execute('''
            insert into obc (start_time, end_time, duration, power, voltage, priority_t, priority_e)
            values (?, ?, ?, ?, ?, ?, ?)
            ''', (int(start_time.timestamp()), int(end_time.timestamp()), duration, power, voltage, priority_t, priority_e))

    # Save the changes to the database
    conn.commit()

# Example usage: generate data for one year (365 days)
generate_data(365)

# Close the connection to the database
conn.close()

