class User:
    def __init__( self, user_info ):
        print (user_info)
        self.username = user_info[0]
        self.password = user_info[1]
        self.firstName = user_info[2]
        self.lastName = user_info[3]
        self.height = user_info[4]
        self.weight = user_info[5]
        self.birthDate = user_info[6]
        self.gender = user_info[7]
        self.info = user_info

    def __str__( self ):
        return "Username : %s\nPassword(Encrypted) : %s\nName : %s %s\nHeight : %d cm\nWeight : %d kg\nBirth Date : %s\nGender : %s\n" %(self.username,
        self.password, self.firstName, self.lastName, self.height, self.weight, self.birthDate, self.gender)

    def getUsername(  self ):
        return self.username
    
    def getPassword( self ):
        return self.password
    
    def getFirstName( self ):
        return self.firstName

    def getLastName( self ):
        return self.lastName
    
    def getHeight( self ):
        return self.height
    
    def getWeight( self ):
        return self.weight
    
    def getBirthDate( self ):
        return self.birthDate

    def getGender( self ):
        return self.gender

    def getUserInfo( self ):
        return self.info

