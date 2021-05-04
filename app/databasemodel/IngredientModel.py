import requests
import json
from databasemodel.Ingredient import Ingredient
from databasemodel.modelConstant import *

class IngredientModel:
    def __init__( self ):
        pass

    def searchIngredient( self, keyword):
        keyword = keyword.replace( " ", "%20")
        api_req = "https://api.nal.usda.gov/fdc/v1/foods/search?api_key=GmPnMrQu4R4kUg62HbOHUY2Xah3EvkV8Py3J3c24&query=%s"%(keyword)
        print( api_req)
        response = requests.get(api_req)
        # print( json.dumps(response.json()["foods"], indent = 4)) 
        result = {"Text":[], "Info":[]}
        for i in response.json()["foods"]:
            try:
                temp = i["description"] + " (" + i["brandOwner"] + ") : "
            except KeyError as k:
                temp = i["description"] + " : "
            name = temp
            for j in i["foodNutrients"]:
                if j["nutrientName"] == "Energy":
                    if (j["unitName"] == "kJ"):
                        temp = temp + "%.2f KCAL/100g" %( j["value"] * 0.239)
                        energy = j["value"] * 0.239
                    else:
                        temp = temp + "%d %s/100g" %(j["value"], j["unitName"])
                        energy = j["value"]
                    break
            result["Text"].append( temp )
            result["Info"].append( {"FdcId": i["fdcId"], "Name":name, "Energy":energy})
            print( temp )
        return result

    def insertIngredientInRec( self, ingredient ):
        info = ingredient.getIngredientInfo()
        CURSOR.execute( "INSERT INTO Ingredient_Recipe(fdc_id, INGREDIENT_NAME, RECIPE_ID, QTY, UNIT_NAME, CALORIES) VALUES(?,?,?,?,?,?)",
        (info))
        CONNECTION.commit()
    
    def deleteIngredientInRec( self, recipe_id ):
        CURSOR.execute( "DELETE FROM Ingredient_Recipe WHERE RECIPE_ID = %d" %(recipe_id))
        CONNECTION.commit()

    def getIngredient( self, recipe_id ):
        CURSOR.execute( "SELECT * FROM Ingredient_Recipe WHERE RECIPE_ID = %d"%(recipe_id))
        ingredients = CURSOR.fetchall()
        res = []
        CONNECTION.commit()
        for i in range(len(ingredients)):
            res.append(Ingredient( ingredients[i][0], ingredients[i][1], ingredients[i][3], ingredients[i][4], ingredients[i][5] ))
            res[i].setRecipe(  ingredients[i][2])
        print( res )
        return res

INGREDIENT_MODEL = IngredientModel()

if __name__ == "__main__":
    INGREDIENT_MODEL.searchIngredient( "milk" )