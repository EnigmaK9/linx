import sqlite3
import random
from datetime import datetime, timedelta

# Connect to SQLite database
conn = sqlite3.connect('adcs_data.db')
c = conn.cursor()

# Create table if not exists
c.execute('''create table if not exists adcs_data (
                data_id integer primary key,
                start_time timestamp not null,
                end_time timestamp not null,
                duration real,
                timestamp timestamp not null,
                orientation real,
                angular_velocity_x real,
                angular_velocity_y real,
                angular_velocity_z real,
                magnetorquer_x real,
                magnetorquer_y real,
                magnetorquer_z real,
                star_sensor_orientation real,
                gyroscopic_sensor_data_x real,
                gyroscopic_sensor_data_y real,
                gyroscopic_sensor_data_z real,
                solar_sensor_orientation real,
                error_correction_data text,
                power_consumption real
                )''')

# Start and end time of sampling
start_time = datetime.utcnow()
end_time = start_time + timedelta(days=1)

# Sampling cycles
sampling_interval = timedelta(minutes=1)
sampling_cycles = int((end_time - start_time) / sampling_interval)

# Insert data into the table
for i in range(sampling_cycles):
    timestamp = start_time + i * sampling_interval
    orientation = random.uniform(0, 2 * 3.1416)  # random values between 0 and 2pi
    power_consumption = random.uniform(1, 10)  # random values between 1 and 10 Watts
    # Calculate duty cycles (duty cycle = on-time duration / sampling interval)
    duty_cycle = random.uniform(0.1, 0.9)  # Percentage of time on
    duration = sampling_interval.total_seconds() * duty_cycle
    # Insert data into the table
    c.execute('''insert into adcs_data (start_time, end_time, duration, timestamp, orientation, power_consumption)
                  values (?, ?, ?, ?, ?, ?)''',
              (start_time, end_time, duration, timestamp, orientation, power_consumption))

# Commit changes and close connection
conn.commit()
conn.close()

