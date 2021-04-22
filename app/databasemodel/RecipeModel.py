import sqlite3
from Recipe import Recipe
from modelConstant import *

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
        recipe_info = CURSOR.fetchone()
        print (recipe_info)
        CONNECTION.commit()
        rec = Recipe( recipe_info )
        print ( rec )

if __name__ == "__main__":
    rm = RecipeModel()
    rec = rm.getRecipeFromID( 1 )
    print ( rec )
