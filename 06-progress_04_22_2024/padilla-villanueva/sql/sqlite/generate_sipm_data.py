import sqlite3
import random
from datetime import datetime, timedelta

# Connect to the SQLite database
conn = sqlite3.connect('nanoswai.db')
cursor = conn.cursor()

# Function to generate data for the SIPM table
def generate_data(num_days):
    base_date = datetime.utcnow()
    for day in range(num_days):
        for _ in range(random.randint(1, 4)):  # Assuming between 1 and 4 captures per day
            start_hour = random.randint(0, 23)  # Captures can occur at any hour of the day
            start_time = base_date + timedelta(days=day, hours=start_hour, minutes=random.randint(0, 59))
            duration = random.randint(1, 10)  # Duration between 1 second and 10 seconds
            end_time = start_time + timedelta(seconds=duration)

            power = random.uniform(0.5, 1.5)  # Realistic power consumption for a Cosmic Ray Detector

            priority_d = random.uniform(0.1, 1.0)
            priority_e = random.uniform(0.1, 1.0)

            cursor.execute('''
            insert into sipm (start_time, end_time, duration, power, priority_d, priority_e)
            values (?, ?, ?, ?, ?, ?)
            ''', (int(start_time.timestamp()), int(end_time.timestamp()), duration, power, priority_d, priority_e))

    # Save the changes to the database
    conn.commit()

# Example usage: generate data for one year (365 days)
generate_data(365)

# Close the connection to the database
conn.close()

