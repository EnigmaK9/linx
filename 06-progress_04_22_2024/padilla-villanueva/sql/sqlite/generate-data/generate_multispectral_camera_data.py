import sqlite3
import random
from datetime import datetime, timedelta

# Connect to the SQLite database
conn = sqlite3.connect('../nanoswai.db')
cursor = conn.cursor()

# Function to generate data
def generate_data(num_days):
    base_date = datetime(2024, 6, 1)  # Starting date set to June 1, 2024
    voltage = 5  # Operational voltage is constant at 5V
    for day in range(num_days):
        orbit_number = random.randint(1, 15)  # Random orbit number between 1 and 15
        for _ in range(random.randint(1, 1)):  # Assuming between 1 and 1 captures per day
            start_minute = random.uniform(30, 50)  # Simulate the orbit passing over Mexico
            start_time = base_date + timedelta(days=day, minutes=start_minute)
            end_time = start_time + timedelta(minutes=random.uniform(5, 10))  # End time after random duration

            # Calculate the activity duration based on the timestamp difference
            activity_duration = (end_time - start_time).total_seconds() / 60  # Convert seconds to minutes

            power_imaging = random.uniform(2.0, 5.9)  # Power in imaging mode
            priority_t = random.uniform(0.1, 1.0)  # Transmission priority
            priority_e = random.uniform(0.1, 1.0)  # Execution priority

            try:
                cursor.execute('''
                insert into multispectral_camera (start_time, end_time, power, voltage, orbit, activity_duration, priority_t, priority_e)
                values (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (int(start_time.timestamp()), int(end_time.timestamp()), power_imaging, voltage, orbit_number, activity_duration, priority_t, priority_e))
            except sqlite3.Error as e:
                print(f"An error occurred: {e}")
    # Save the changes to the database
    conn.commit()

# Example usage: generate data for one year (365 days)
generate_data(365)

# Close the connection to the database
conn.close()
