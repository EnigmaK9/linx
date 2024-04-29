import sqlite3

# Function to clean all data from tables
def clean_database(cursor):
    # List of table names
    tables = [
        "nanosatellite",
        "acds_control",
        "sipm",
        "deployment_panels_antennas",
        "tuna_cam",
        "sp_cam",
        "electrical_power_system",
        "acds_reaction_wheel",
        "acds_sense_magnetorque",
        "comms_2408_mhz_tx",
        "comms_437_mhz_tx",
        "comms_437_mhz_rx",
        "multispectral_camera",
        "operation_periods"
    ]

    for table in tables:
        cursor.execute(f"delete from {table}")
        print(f"All data deleted from table '{table}'")

# Connect to the database
conn = sqlite3.connect('../nanoswai.db')
cursor = conn.cursor()

# Clean all data from tables
clean_database(cursor)

# Commit changes and close the connection
conn.commit()
conn.close()
