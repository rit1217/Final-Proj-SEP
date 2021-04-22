import sqlite3

try:
    CONNECTION = sqlite3.connect("app/databasemodel/main_data.db")
except:
    print ("Cannot connect to the database.")
CURSOR = CONNECTION.cursor()
