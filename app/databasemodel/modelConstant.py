import sqlite3
import re

try:
    CONNECTION = sqlite3.connect("app/databasemodel/main_data.db", timeout=10)
except:
    print ("Cannot connect to the database.")
CURSOR = CONNECTION.cursor()

if __name__ == "__main__":
    r = [re.search("[a-z,A-Z,0-9,_]", i )for i in "ASinlke934_"]
    print( r )
        