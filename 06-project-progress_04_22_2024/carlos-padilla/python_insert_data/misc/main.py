import pymysql
import random
from datetime import datetime, timedelta
import camera_mantis_data_generator
import obc_data_generator

# Parameters for database connection
db_params = {
    'host': 'deep-blue',
    'user': 'root',
    'password': 'gengar',
    'db': 'satellite_data',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

# Establish a database connection
connection = pymysql.connect(**db_params)

# Function to insert data into camera_mantis table
def insert_camera_mantis_data(connection):
    # Generate synthetic data for camera_mantis
    data = camera_mantis_data_generator.generate_data_for_camera_mantis()

    # SQL statement for inserting data
    insert_query = """
    insert into camera_mantis (timestamp, image_url, description, status)
    values (%s, %s, %s, %s)
    """

    try:
        # Execute the SQL statement
        with connection.cursor() as cursor:
            cursor.executemany(insert_query, data)
        connection.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        connection.close()

# Call the function to insert data
insert_camera_mantis_data(connection)

