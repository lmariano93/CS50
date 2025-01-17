import sqlite3

# Connect to the source and destination databases
conn_source = sqlite3.connect('imdb_titles.db')  # Source database
conn_dest = sqlite3.connect('data.db')  # Destination database

cursor_source = conn_source.cursor()
cursor_dest = conn_dest.cursor()

# Table name
table_name = "titles"

# Copy data from the source table to the destination database
cursor_source.execute(f"SELECT * FROM {table_name}")
rows = cursor_source.fetchall()

# Insert the data into the destination database table
for row in rows:
    placeholders = ', '.join(['?'] * len(row))  # Create the correct number of placeholders
    cursor_dest.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", row)

# Commit the changes and close the connections
conn_dest.commit()
conn_source.close()
conn_dest.close()

print(f"Data from the table {table_name} successfully copied to the destination database.")
