import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('nanoswai.db')
cursor = conn.cursor()

# Function to clean data from the obc table
def clean_obc_data():
    # SQL command to delete all records from the obc table
    cursor.execute('delete from obc')

    # Save the changes to the database
    conn.commit()
    print("Data has been cleaned from the obc table.")

# Example usage: clean the obc table
clean_obc_data()

# Close the connection to the database
conn.close()

