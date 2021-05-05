import sqlite3
from databasemodel.Recipe import Recipe
from databasemodel.modelConstant import *

class RecipeModel:
    def __init__(self):
        pass

    def convertToBinaryData( self, filename):
        # Convert digital data to binary format
        with open(filename, 'rb') as file:
            blobData = file.read()
        return blobData
        
    def insertRecipe( self, newRecipe ):
        info = newRecipe.getRecipeInfo()
        CURSOR.execute( "INSERT INTO Recipe(RECIPE_ID, NAME, CALORIES, COOKING_STEP, CREATOR, DIFFICULTY) VALUES(?,?,?,?,?,?)",
        (info))
        CONNECTION.commit()

    def updateRecipe( self, recipe ):
        info = list(recipe.getRecipeInfo()[1:])
        info.append( recipe.getId() )
        info = tuple(info)
        print( info )
        CURSOR.execute( "UPDATE Recipe SET NAME = '%s', CALORIES = %f, COOKING_STEP = '%s', CREATOR = '%s', DIFFICULTY = '%s' WHERE RECIPE_ID = %d"
        %(info))
        CONNECTION.commit()

    def getRecipeFromID( self, recipe_id ):
        statement = "SELECT * FROM Recipe WHERE RECIPE_ID = '%d'" %(recipe_id)
        CURSOR.execute( statement)
        recipes = CURSOR.fetchall()
        CONNECTION.commit()
        res = []
        for i in recipes:
            res.append(Recipe( i ))
        return res

    def getRecipeFromCreator( self, creator ):
        statement = "SELECT * FROM Recipe WHERE CREATOR = '%s'" %(creator)
        CURSOR.execute( statement)
        recipes = CURSOR.fetchall()
        CONNECTION.commit()
        res = []
        for i in recipes:
            res.append(Recipe( i ))
        return res

    def getAllRecipe( self ):
        statement = "SELECT * FROM Recipe"
        CURSOR.execute( statement)
        recipes = CURSOR.fetchall()
        CONNECTION.commit()
        res = []
        for i in recipes:
            res.append(Recipe( i ))
        return res

    def getMaxId( self ):
        statement = "SELECT MAX(RECIPE_ID) FROM Recipe"
        CURSOR.execute( statement)
        res = CURSOR.fetchone()
        CONNECTION.commit()
        return res
    
    def searchRecipeByName( self, keyword ):
        statement = "SELECT * FROM Recipe WHERE NAME LIKE '%" + keyword + "%'"
        CURSOR.execute(  statement)
        res = []
        recipes = CURSOR.fetchall()
        CONNECTION.commit()
        for i in recipes:
            res.append( Recipe(i))
        return res

    def insertImageById( self, image, recipe_id ):
        statement = "UPDATE Recipe SET IMAGE = ? WHERE RECIPE_ID = %d"%(recipe_id)
        blobImage = self.convertToBinaryData( image )
        CURSOR.execute( statement, (blobImage,))
        CONNECTION.commit()



RECIPE_MODEL = RecipeModel()

if __name__ == "__main__":
    rm = RecipeModel()
    rec = rm.getRecipeFromID( 9 )
    print ( rec )
