#!/usr/bin/python
import mariadb

# Connect to MariaDB
try:
    conn = mariadb.connect(
        user="root",
        password="gengar",
        host="deep-blue",
        database="satellite_data")
    cur = conn.cursor()

    # Insert into obc
    try:
        cur.execute("insert into obc (id, start_time, duration, power, priority_t, priority_e) values (?, ?, ?, ?, ?, ?)",
                    (1, "2024-04-19 08:00:00", 120, 50.5, 1.0, 0.5))
    except mariadb.Error as e:
        print(f"Error inserting into obc: {e}")

    # Commit changes
    conn.commit()
    print(f"Last Inserted ID for employees: {cur.lastrowid}")

except mariadb.Error as e:
    print(f"Error connecting to MariaDB: {e}")

finally:
    if conn:
        conn.close()

