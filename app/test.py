import sqlite3

conn = sqlite3.connect("Food.db")
c = conn.cursor()
c.execute( "SELECT fdc_id FROM market_acquisition WHERE brand_description LIKE '%MILK%'")
print( "\n", c.fetchall() )
conn.commit()
conn.close()