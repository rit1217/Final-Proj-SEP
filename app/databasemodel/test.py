import sqlite3

conn = sqlite3.connect("app/databasemodel/main_data.db")
c = conn.cursor()
c.execute( "SELECT USERNAME FROM Recipe")
print( "\n", c.fetchall() )
conn.commit()
conn.close()