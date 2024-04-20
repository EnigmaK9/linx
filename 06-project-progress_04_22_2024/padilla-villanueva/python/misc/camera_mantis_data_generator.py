from datetime import datetime, timedelta
import random

def generate_data_for_camera_mantis():
    # List to store synthetic data
    data_list = []

    # Define the start date and time for data generation
    start_datetime = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

    # Generate data for one day
    for _ in range(24 * 60):  # Assuming we generate one record per minute
        timestamp = start_datetime.strftime('%Y-%m-%d %H:%M:%S')
        image_url = f"http://example.com/image_{random.randint(1, 100)}.jpg"
        description = "Synthetic image description"
        status = random.choice(['active', 'inactive'])

        data_list.append((timestamp, image_url, description, status))

        # Increment time by one minute
        start_datetime += timedelta(minutes=1)

    # Return the generated data
    return data_list

