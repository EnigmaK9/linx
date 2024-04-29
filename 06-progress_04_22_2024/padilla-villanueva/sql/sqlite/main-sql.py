import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('nanoswai.db')
cursor = conn.cursor()

# List of script files and associated table names
script_files = [
    ('01-acds_control.sql', ['acds_control', 'acds_control_magnetorque']),
    ('02-acds_sense_magnetorque.sql', ['acds_sense_magnetorque']),
    ('03-acds_reaction_wheel.sql', ['acds_reaction_wheel']),
    ('04-comms_437_mhz_rx.sql', ['comms_437_mhz_rx']),
    ('05-comms_437_mhz_tx.sql', ['comms_437_mhz_tx']),
    ('06-comms_2408_mhz_tx.sql', ['comms_2408_mhz_tx']),
    ('07-camera_computer.sql', ['camera_computer']),
    ('08-sipm.sql', ['sipm']),
    ('09-sp_cam.sql', ['sp_cam']),
    ('10-tuna_cam.sql', ['tuna_cam']),
    ('11-obc.sql', ['obc']),
    ('12-eps.sql', ['eps']),
    ('13-deployment_panels_antennas.sql', ['deployment_panels_antennas'])
]

# Function to check if tables exist
def tables_exist(tables):
    for table_name in tables:
        cursor.execute(''' select count(name) from sqlite_master where type='table' and name=? ''', (table_name,))
        if cursor.fetchone()[0] == 0:
            return False
    return True

# Execute each script
for script, tables in script_files:
    if not tables_exist(tables):
        try:
            with open(script, 'r') as file:
                sql_script = file.read()
            cursor.executescript(sql_script.lower())  # Convert script to lowercase before executing
            print(f"Executed {script}")
        except sqlite3.OperationalError as e:
            print(f"Operational error occurred while executing {script}: {e}")
    else:
        print(f"Skipped {script} because tables {', '.join(tables)} already exist")

# Commit changes and close connection
conn.commit()
conn.close()

