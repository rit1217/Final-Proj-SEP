import sqlite3
from passlib.hash import pbkdf2_sha256
from databasemodel.User import User
from databasemodel.modelConstant import *

class UserModel:
    def __init__(self):
        pass
        
    def insertUser( self, newUser ):
        info = newUser.getUserInfo()
        CURSOR.execute( "INSERT INTO User(USERNAME, PASSWORD, FIRST_NAME, LAST_NAME, HEIGHT, WEIGHT, BIRTHDATE, GENDER) VALUES(?,?,?,?,?,?,?,?)",info)
        CONNECTION.commit()

    def getUser( self, username ):
        statement = "SELECT * FROM User WHERE USERNAME = '%s'" %(username)
        CURSOR.execute( statement)
        user_info = CURSOR.fetchone()
        CONNECTION.commit()
        if user_info is None : return None
        return User( user_info )

USER_MODEL = UserModel()

if __name__ == "__main__":
    u = User(("rrrit", "pass", "Phurit", "Warapattnapong", 181, 73, "11/7/2001", "Male"))
    USER_MODEL.insertUser( u )
    print( userfromdb )
    print( pbkdf2_sha256.verify( u.getPassword(), userfromdb.getPassword()))