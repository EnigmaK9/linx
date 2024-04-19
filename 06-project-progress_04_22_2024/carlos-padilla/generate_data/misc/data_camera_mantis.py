import random
from datetime import datetime, timedelta

# Utility functions
def generate_power_usage(min_power, max_power):
    """Generates a random power usage value between min_power and max_power."""
    return round(random.uniform(min_power, max_power), 2)

def generate_start_times(number_of_starts, total_minutes):
    """Generates a list of random start times throughout the day."""
    return sorted(random.sample(range(total_minutes), number_of_starts))

def generate_durations(number_of_starts, max_duration):
    """Generates a list of random durations for each start time."""
    return [random.randint(1, max_duration) for _ in range(number_of_starts)]

def generate_priorities():
    """Generates random priority values for tasks."""
    return round(random.uniform(0, 1), 2)

def create_simulation_data_for_camera_mantis(day):
    """
    Generates synthetic simulation data for the camera_mantis table.
    """
    # Constants for simulation
    MIN_POWER = 0.5   # Min power usage of the camera
    MAX_POWER = 2.0   # Max power usage of the camera
    MAX_DURATION = 10 # Max duration of camera being on in minutes
    TOTAL_MINUTES = 24 * 60 # Total minutes in a day
    UTC_START_DAY = datetime.strptime(day, '%Y-%m-%d') # Start of the day in UTC

    # The camera will be on less than 10 minutes during the day
    total_on_time = 0
    start_times = []
    durations = []

    while total_on_time < 10:
        # Generate a random start time and duration
        start_time = random.randint(0, TOTAL_MINUTES - 1)
        duration = random.randint(1, MAX_DURATION)

        # Check if the total on time will exceed 10 minutes with this duration
        if total_on_time + duration > 10:
            duration = 10 - total_on_time

        # Save the start time and duration
        start_times.append(start_time)
        durations.append(duration)

        # Update the total on time
        total_on_time += duration

    # Generate synthetic data for each on-time of the camera
    data_entries = []
    for start_time, duration in zip(start_times, durations):
        power = generate_power_usage(MIN_POWER, MAX_POWER)
        priority_t = generate_priorities()
        priority_e = generate_priorities()

        # Calculate the start time as a datetime object
        start_time_datetime = (UTC_START_DAY + timedelta(minutes=start_time)).strftime('%Y-%m-%d %H:%M:%S')

        data_entry = {
            'start_time': start_time_datetime,
            'duration': duration,
            'power': power,
            'priority_t': priority_t,
            'priority_e': priority_e
        }
        data_entries.append(data_entry)

    return data_entries

def insert_data_into_camera_mantis(data_entries):
    """
    Generates SQL insert statements for the synthetic data entries for camera_mantis.
    """
    insert_statements = []

    for entry in data_entries:
        insert_statement = f"INSERT INTO camera_mantis (start_time, duration, power, priority_t, priority_e) VALUES ('{entry['start_time']}', {entry['duration']}, {entry['power']}, {entry['priority_t']}, {entry['priority_e']});"
        insert_statements.append(insert_statement)

    return insert_statements

# Module for generating data for camera_mantis
def module_camera_mantis(day):
    # Generate data for a whole day in UTC
    data_entries = create_simulation_data_for_camera_mantis(day)
    # Generate SQL insert statements for the generated data
    sql_statements = insert_data_into_camera_mantis(data_entries)
    return sql_statements

# Example use:
# Generate synthetic data SQL insert statements for the camera_mantis table for a given day
example_day = "2024-04-18"
camera_mantis_insert_statements = module_camera_mantis(example_day)

# Show the first few insert statements as an example
camera_mantis_insert_statements[:5]

