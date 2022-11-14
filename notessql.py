
import sqlite3

# open a SQLite connection
# a database file called data.db will be created,
# if it does not exist
connection = sqlite3.connect('new.db')

# create a database cursor
cur = connection.cursor()


# create the database table if it doesn't exist
table_schema = """
CREATE TABLE IF NOT EXISTS notes (
   id  INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT
);
"""
cur.execute(table_schema)



#
# Inserting to the database
for i in range(0,5):
    id = input('ID:')
    name = input('Note name: ')
    desc = input('Note description: ')

    # insert some hard-coded data
    insert_query = """
    INSERT INTO notes (id, name, description)
    VALUES (?, ?, ?);
    """
    cur.execute(insert_query, (id, name, desc))

    # save it in the database file
    connection.commit()


#
# Querying the database
#

# query the database for ALL data in the notes table
cur.execute('SELECT * FROM notes;')

# print the result
print('\nNotes:')
for row in cur.fetchall():
    display_name = row[1]
    display_desc = row[2]

    print(f'Note name: {display_name}\nNote description: {display_desc}\n')





# query the database for ALL data in the notes table
cur.execute('SELECT * FROM notes;')

# print the result
result = cur.fetchall()
print(result)

# close the cursor
cur.close()

# close the connection
connection.close()