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
        for _ in range(random.randint(1, 4)):  # Assuming between 1 and 4 captures per day
            start_hour = random.randint(6, 18)  # Capture photos only between 6 AM and 6 PM
            start_time = base_date + timedelta(days=day, hours=start_hour, minutes=random.randint(0, 59))
            duration = random.randint(120, 600)  # Duration between 2 minutes and 10 minutes
            end_time = start_time + timedelta(seconds=duration)

            # Assuming 70% of time in imaging mode and 30% in readout mode
            imaging_duration = duration * 0.7
            readout_duration = duration - imaging_duration
            power_imaging = random.uniform(2.0, 2.6)  # Realistic power consumption in imaging mode
            power_readout = random.uniform(3.5, 4.6)  # Realistic power consumption in readout mode
            voltage = random.uniform(5.0, 5.5)  # Operating voltage in volts
            # Calculate weighted average of power consumption
            average_power = (power_imaging * imaging_duration + power_readout * readout_duration) / duration

            priority_t = random.uniform(0.1, 1.0)  # Transmission priority
            priority_e = random.uniform(0.1, 1.0)  # Execution priority

            cursor.execute('''
            insert into camera_computer (start_time, end_time, duration, power, voltage, priority_t, priority_e)
            values (?, ?, ?, ?, ?, ?, ?)
            ''', (int(start_time.timestamp()), int(end_time.timestamp()), duration, average_power, voltage, priority_t, priority_e))

    # Save the changes to the database
    conn.commit()

# Example usage: generate data for one year (365 days)
generate_data(365)

# Close the connection to the database
conn.close()

