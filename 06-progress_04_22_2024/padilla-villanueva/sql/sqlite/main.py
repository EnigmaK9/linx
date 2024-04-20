import sqlite3
from generate_camera_computer_data import insert_camera_computer_data

# Connect to the SQLite database
conn = sqlite3.connect('nanoswai.db')
cursor = conn.cursor()

# List of script files
script_files = [
    '01-acds_control.sql',
    '02-acds_sense_magnetorque.sql',
    '03-acds_reaction_wheel.sql',
    '04-comms_437_mhz_rx.sql',
    '05-comms_437_mhz_tx.sql',
    '06-comms_2408_mhz_tx.sql',
    '07-camera_computer.sql',
    '08-sipm.sql',
    '09-sp_cam.sql',
    '10-tuna_cam.sql',
    '11-obc.sql',
    '12-eps.sql',
    '13-deployment_panels_antennas.sql'
]

# Execute each script
for script in script_files:
    with open(script, 'r') as file:
        sql_script = file.read()
    cursor.executescript(sql_script)
    print(f"Executed {script}")

# Generate and insert data for camera_computer
    insert_camera_computer_data(conn)

# Commit changes and close connection
conn.commit()
conn.close()

