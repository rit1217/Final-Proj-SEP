import sqlite3
from databasemodel.Recipe import Recipe
from databasemodel.modelConstant import *

class RecipeModel:
    def __init__(self):
        pass
        
    def insertRecipe( self, newRecipe ):
        info = newRecipe.getUserInfo()
        CURSOR.execute( "INSERT INTO Recipe(RECIPE_ID, NAME, CALORIES, COOKING_STEP, CREATOR, IMAGE) VALUES(?,?,?,?,?,?)",
        (info))
        CONNECTION.commit()

    def getRecipeFromID( self, recipe_id ):
        statement = "SELECT * FROM Recipe WHERE RECIPE_ID = '%d'" %(recipe_id)
        CURSOR.execute( statement)
        recipes = CURSOR.fetchall()
        CONNECTION.commit()
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

RECIPE_MODEL = RecipeModel()

if __name__ == "__main__":
    rm = RecipeModel()
    rec = rm.getRecipeFromCreator( 'rrrit1' )
    print ( rec )
