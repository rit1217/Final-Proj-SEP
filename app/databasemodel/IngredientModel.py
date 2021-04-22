import requests
import json
from Ingredient import Ingredient
from modelConstant import *

class IngredientModel:
    def __init__( self ):
        pass

    def searchIngredient( self, keyword):
        keyword = keyword.replace( " ", "%20")
        api_req = "https://api.nal.usda.gov/fdc/v1/foods/search?api_key=GmPnMrQu4R4kUg62HbOHUY2Xah3EvkV8Py3J3c24&query=%s"%(keyword)
        print( api_req)
        response = requests.get(api_req)
        # print( json.dumps(response.json()["foods"], indent = 4)) 
        for i in response.json()["foods"]:
            print( i["description"] + " " + i["brandOwner"] + " : ", end = "" )
            for j in i["foodNutrients"]:
                if j["nutrientName"] == "Energy":
                    if (j["unitName"] == "kJ"):
                        print(j["value"] * 0.239, "KCAL")
                    else:
                        print( j["value"], j["unitName"])
                    break

INGREDIENT_MODEL = IngredientModel()

if __name__ == "__main__":
    INGREDIENT_MODEL.searchIngredient( "milk" )