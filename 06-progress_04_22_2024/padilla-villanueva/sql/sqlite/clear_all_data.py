import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('nanoswai.db')
cursor = conn.cursor()

# Function to clean data from the obc table
def clean_obc_data():
    # SQL command to delete all records from the obc table

    cursor.execute('delete from acds_control')
    cursor.execute('delete from acds_sense_magnetorque')
    cursor.execute('delete from acds_reaction_wheel')
    cursor.execute('delete from comms_437_mhz_rx')
    cursor.execute('delete from comms_437_mhz_tx')
    cursor.execute('delete from comms_2408_mhz_tx')
    cursor.execute('delete from camera_computer')
    cursor.execute('delete from sipm')
    cursor.execute('delete from sp_cam')
    cursor.execute('delete from tuna_cam')
    cursor.execute('delete from obc')
    cursor.execute('delete from eps')
    cursor.execute('delete from deployment_panels_antennas')
    # Save the changes to the database
    conn.commit()
    print("All data has been cleaned from the database.")

# Example usage: clean all data from the database
clean_obc_data()

# Close the connection to the database
conn.close()


