import sqlite3
import facebook


db_connection = sqlite3.connect('db.sqlite3')
cursor = db_connection.cursor()
cursor.execute('SELECT * FROM socialaccount_socialtoken;')
for socialtoken in cursor.fetchall():
    graph = facebook.GraphAPI(socialtoken[1])
    # Writes 'Hello, world' to the active user's wall.
    graph.put_object(parent_object='me', connection_name='feed',
                     message='Hello, world')
