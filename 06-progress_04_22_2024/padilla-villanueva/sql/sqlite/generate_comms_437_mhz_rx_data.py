import sqlite3
import random
from datetime import datetime, timedelta

# Connect to the SQLite database
conn = sqlite3.connect('nanoswai.db')
cursor = conn.cursor()

# Function to generate data for the comms_437_mhz_rx table
def generate_data(num_days):
    base_date = datetime.utcnow()
    for day in range(num_days):
        for _ in range(random.randint(1, 3)):  # Assuming between 1 and 3 uplink sessions per day
            start_hour = random.randint(0, 23)  # Uplink sessions can occur at any hour of the day
            start_time = base_date + timedelta(days=day, hours=start_hour, minutes=random.randint(0, 59))
            duration = random.randint(30, 300)  # Duration between 30 seconds and 5 minutes
            end_time = start_time + timedelta(seconds=duration)

            power = random.uniform(5, 20)  # Power in watts, typical for a small satellite transmitter
            voltage = random.uniform(3.3, 5.0)  # Operating voltage in volts

            priority_t = random.uniform(0.1, 1.0)  # Transmission priority
            priority_e = random.uniform(0.1, 1.0)  # Execution priority

            cursor.execute('''
            insert into comms_437_mhz_rx (start_time, end_time, duration, power, voltage, priority_t, priority_e)
            values (?, ?, ?, ?, ?, ?, ?)
            ''', (int(start_time.timestamp()), int(end_time.timestamp()), duration, power, voltage, priority_t, priority_e))

    # Save the changes to the database
    conn.commit()

# Example usage: generate data for 365 days
generate_data(365)

# Close the connection to the database
conn.close()

