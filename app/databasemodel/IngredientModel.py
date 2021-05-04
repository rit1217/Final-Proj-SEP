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
        result = []
        for i in response.json()["foods"]:
            try:
                temp = i["description"] + " (" + i["brandOwner"] + ") : "
            except KeyError as k:
                temp = i["description"] + " : "
            for j in i["foodNutrients"]:
                if j["nutrientName"] == "Energy":
                    if (j["unitName"] == "kJ"):
                        temp = temp + "%.2f KCAL" %( j["value"] * 0.239)
                    else:
                        temp = temp + "%d %s" %(j["value"], j["unitName"])
                    break
            result.append( temp )
            print( temp )
        return result

    def insertIngredientInRec( self, ingredients ):
        for i in ingredients:
            info = i.getIngredientInfo()
            CURSOR.execute( "INSERT INTO Ingredient_Recipe(fdc_id, INGREDIENT_NAME, RECIPE_ID, QTY, UNIT_NAME, CALORIES) VALUES(?,?,?,?,?,?)",
            (info))
            CONNECTION.commit()

INGREDIENT_MODEL = IngredientModel()

if __name__ == "__main__":
    INGREDIENT_MODEL.searchIngredient( "milk" )