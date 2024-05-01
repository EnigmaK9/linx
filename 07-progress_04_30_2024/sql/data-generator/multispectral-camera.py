import sqlite3
import random
from datetime import datetime, timedelta

# Connect to the SQLite database
conn = sqlite3.connect('../nanoswai.db')
cursor = conn.cursor()

# Function to generate data
def generate_data(num_days):
    base_date = datetime(2024, 6, 1, 8, 0, 0)  # Starting date set to June 1, 2024, at 8:00 AM
    orbit_duration = timedelta(minutes=94.6)  # Duration of each orbit is 94.6 minutes

    for day in range(num_days):
        for orbit in range(14):  # 14 orbits in a day
            start_time = base_date + timedelta(days=day) + (orbit * orbit_duration)
            end_time = start_time + timedelta(minutes=10)  # Each operation lasts 10 minutes

            # Select power usage mode
            if random.choice(['imaging', 'readout']) == 'imaging':
                power = random.uniform(3.0, 5.9)  # Power usage for imaging mode is less than 6 watts
                subsystem_type = 'Multispectral Camera'
            else:
                power = random.uniform(1.0, 3.9)  # Power usage for readout mode is less than 4 watts
                subsystem_type = 'Multispectral Camera'

            voltage = 5  # Operational voltage is constant at 5V
            execution_priority = round(random.uniform(0, 1), 6)  # Execution priority with 6 decimal places
            transmission_priority = round(random.uniform(0, 1), 6)  # Transmission priority with 6 decimal places

            # Insert data into operation_periods table including the subsystem type
            cursor.execute('''
            insert into operation_periods (start_time, end_time, power, voltage, orbit, execution_priority,
            transmission_priority, subsystem_type)
            values (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (start_time.strftime('%Y-%m-%d %H:%M:%S'), end_time.strftime('%Y-%m-%d %H:%M:%S'), power, voltage,
                  orbit + 1, execution_priority, transmission_priority, subsystem_type))

            period_id = cursor.lastrowid  # Get the last inserted ID

            # Generate multispectral camera data linked to the operation period
            operational_status = random.choice(['active', 'inactive', 'maintenance'])
            last_updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Insert data into multispectral_camera table
            cursor.execute('''
            insert into multispectral_camera (period_id, operational_status, last_updated)
            values (?, ?, ?)
            ''', (period_id, operational_status, last_updated))

    # Commit the changes to the database
    conn.commit()

# Example usage: generate data for 365 days
generate_data(365)

# Close the connection to the database
conn.close()
