import sqlite3
from passlib.hash import pbkdf2_sha256


class UserModel:
    def __init__(self):
        try:
            conn = sqlite3.connect("app/databasemodel/main_data.db")
        except:
            print ("Cannot connect to the database.")
        self.cursor = conn.cursor()
        self.cursor.execute( "SELECT USERNAME FROM Recipe")
        print( "\n", c.fetchall() )
        conn.commit()
        conn.close()

    @staticmethod
    def insertUser( self, newUser ):
        username = newUser.getUsername()
        password = pbkdf2_sha256.hash( newUser.getPassword())
        firstName = newUser.getFirstName()
        lastName = newUser.getLastName()
        height = newUser.getHeight()
        weight = newUser.getWeight()
        birthDate = newUser.getBirthDate()
        gender = newUser.getGender()
        self.cursor.execute( "INSERT INTO User(USERNAME, PASSWORD, FIRST_NAME, LAST_NAME, HEIGHT, WEIGHT, BIRTHDATE, GENDER) VALUE(?,?,?,?,?,?,?,?)",
        (username, password, firstName, lastName, height, weight, birthDate, gender))

if __name__ == "__main__":
    temp = pbkdf2_sha256.hash( "eiei")
    print( pbkdf2_sha256.verify( "eiei", temp ) )