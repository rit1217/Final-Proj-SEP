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
        CURSOR.execute( "SELECT AVG(RATING) FROM Rating WHERE RECIPE_ID = %d" %(recipe_id))
        avg = CURSOR.fetchone()
        CONNECTION.commit()
        print( "\n\n", avg, "\n\n")
        if avg[0] is None:
            avg = 0.0
        else:
            avg = avg[0]
        return avg
    
    def getRating( self, username, recipe_id ):
        CURSOR.execute( "SELECT RATING FROM Rating WHERE RECIPE_ID = %d AND USERNAME = '%s'" %(recipe_id, username))
        rating = CURSOR.fetchone()
        CONNECTION.commit()
        if rating is not None:
            return rating[0]
        else:
            return rating
    
    def deleteByRecipe( self, recipe_id ):
        statement = "DELETE FROM Rating WHERE RECIPE_ID = %d" %(recipe_id)
        CURSOR.execute( statement )
        CONNECTION.commit()
        
RATING_MODEL = RatingModel()