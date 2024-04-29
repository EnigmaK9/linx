import sqlite3

# Conexión a la base de datos o creación si no existe
conn = sqlite3.connect('nanoswai.db')
cursor = conn.cursor()

# Ejecución del script SQL
with open('nanoswai.sql', 'r') as sql_file:
    sql_script = sql_file.read()
    cursor.executescript(sql_script)

# Confirmar cambios y cerrar la conexión
conn.commit()
conn.close()

print("Base de datos 'nanoswai.db' creada exitosamente.")
