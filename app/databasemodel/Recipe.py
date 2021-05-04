from databasemodel.UserModel import *

class Recipe:
    def __init__( self, recipe_info ):
        self.id = recipe_info[0]
        self.name = recipe_info[1]
        self.calories = recipe_info[2]
        self.cooking_step = recipe_info[3]
        print (recipe_info[4] )
        user_info = USER_MODEL.getUser( recipe_info[4] )
        print (user_info)
        self.creator = user_info
        self.info = recipe_info
        self.difficulty = recipe_info[5]
        self.ingredients = []
        
    def __str__( self ):
        return "%08d %s\n%d KCAL\n%s\nCreated By : %s" %(self.id, self.name, self.calories, self.cooking_step, self.creator)

    def getId( self ):
        return self.id

    def getName( self ):
        return self.name

    def getCalories( self ):
        return self.calories

    def getCookingStep( self):
        return self.cooking_step

    def getCreator( self ):
        return self.creator

    def getDifficulty( self ):
        return self.difficulty

    def getIngredients( self ):
        #@TODO
        pass



