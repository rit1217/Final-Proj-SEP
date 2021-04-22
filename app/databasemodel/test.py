import sqlite3
from passlib.hash import pbkdf2_sha256
from User import User

class UserModel:
    def __init__(self):
        try:
            self.conn = sqlite3.connect("app/databasemodel/main_data.db")
        except:
            print ("Cannot connect to the database.")
        self.cursor = self.conn.cursor()
        
    def insertUser( self, newUser ):
        info = newUser.getUserInfo()
        self.cursor.execute( "INSERT INTO User(USERNAME, PASSWORD, FIRST_NAME, LAST_NAME, HEIGHT, WEIGHT, BIRTHDATE, GENDER) VALUES(?,?,?,?,?,?,?,?)",
        (info))
        self.conn.commit()

    def getUser( self, username ):
        statement = "SELECT * FROM User WHERE USERNAME = '%s'" %(username)
        self.cursor.execute( statement)
        user_info = self.cursor.fetchone()
        self.conn.commit()
        return User( user_info )
        
    def closeConnection( self ):
        self.conn.close()

if __name__ == "__main__":
    u = User(("rit", "pwd", "Phurit", "Warapattnapong", 181, 73, "11/7/2001", "Male"))
    um = UserModel()
    userfromdb = um.getUser( "rit" )
    print( userfromdb )
    um.closeConnection()
    print( pbkdf2_sha256.verify( u.getPassword(), userfromdb.getPassword() ) )