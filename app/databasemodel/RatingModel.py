from databasemodel.modelConstant import *

class RatingModel:
    def __init__( self ):
        pass

    def insertRating( self, username, recipe_id, rating ):
        CURSOR.execute( "INSERT INTO Rating(USERNAME, RECIPE_ID, RATING) VALUES(?,?,?)", (username, recipe_id, rating))
        CONNECTION.commit()

    def updateRating( self, username, recipe_id, rating ):
        CURSOR.execute( "UPDATE Rating SET RATING = %d WHERE USERNAME = '%s' AND RECIPE_ID = %d" %( rating, username, recipe_id))
        CONNECTION.commit()
    
    def getAverageRating( self, recipe_id ):
        CURSOR.execute( "SELECT AVG(RATING) FROM Rating WHERE RECIPE_ID = %d", %(recipe_id))
        avg = CURSOR.fetchone()
        CONNECTION.commit()
        return avg
    
    def getRating( self, username, recipe_id ):
        CURSOR.execute( "SELECT RATING FROM Rating WHERE RECIPE_ID = %d AND USERNAME = '%s'" %(recipe_id, username))
        rating = CURSOR.fetchone()
        CONNECTION.commit()
        return rating
        
RATING_MODEL = RatingModel()