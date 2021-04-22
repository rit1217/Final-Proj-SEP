import sqlite3
try:
    conn = sqlite3.connect("../main_data.db")
except:
    print( "Cannot connect to the database.")   
c = conn.cursor()
c.execute( "SELECT USERNAME FROM User")
print( "\n", c.fetchall() )
conn.commit()
conn.close()