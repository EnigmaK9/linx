import sqlite3
from datetime import datetime, timedelta
import random

def insert_camera_computer_data(db_connection):
    cursor = db_connection.cursor()
    start_time = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)  # Start at midnight

    # Generate data for 24 hours, assuming operation every 10 minutes on average
    while start_time < datetime.now().replace(hour=23, minute=50, second=0, microsecond=0):
        duration = random.randint(1, 10)  # Duration in minutes, less than 10 minutes
        capture_time = start_time
        power = 4.5  # Power used in Watts
        priority_t = random.uniform(0.1, 1.0)  # Task priority between 0.1 and 1.0
        priority_e = random.uniform(0.1, 1.0)  # Execution priority between 0.1 and 1.0

        cursor.execute('''
            insert into camera_computer (start_time, duration, power, priority_t, priority_e)
            values (?, ?, ?, ?, ?)
        ''', (capture_time.strftime('%Y-%m-%d %H:%M:%S'), duration, power, priority_t, priority_e))

        # Increment the start time by the operation duration to simulate continuous data generation
        start_time += timedelta(minutes=duration)

    db_connection.commit()
    print("Camera computer data generated and inserted for the entire day.")

