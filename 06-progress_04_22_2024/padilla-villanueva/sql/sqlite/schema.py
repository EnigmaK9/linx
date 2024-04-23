import sqlite3
import os
from PIL import Image, ImageDraw, ImageFont

def print_and_save_database_schema():
    # Get the current working directory and the path to the database
    database_path = os.path.join(os.getcwd(), 'nanoswai.db')

    # Connect to the SQLite database
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # Retrieve and display the CREATE statements for all tables and views
    cursor.execute("select type, name, sql from sqlite_master where type='table' or type='view'")
    schema = cursor.fetchall()

    # Prepare text to be written to image
    schema_text = ""
    for item in schema:
        schema_text += f"Type: {item[0]}\nName: {item[1]}\nSQL:\n{item[2]}\n" + "-" * 40 + "\n"

    # Close the database connection
    conn.close()

    # Determine the size of image needed
    width, height = 800, len(schema_text.split('\n')) * 15 + 50

    # Create an image with white background
    img = Image.new('RGB', (width, height), color = (255, 255, 255))
    d = ImageDraw.Draw(img)

    # Load the DejaVu Sans font
    font_path = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'  # Path to DejaVu Sans font
    font_size = 14
    font = ImageFont.truetype(font_path, font_size)

    # Drawing text on the image
    d.text((10, 10), schema_text, font=font, fill=(0, 0, 0))

    # Save the image
    img.save('database_schema.png')

# Call the function to print and save the schema
print_and_save_database_schema()

