import requests
import json
response = requests.get("https://api.nal.usda.gov/fdc/v1/foods/search?api_key=GmPnMrQu4R4kUg62HbOHUY2Xah3EvkV8Py3J3c24&query=Beef%20fat")
# print( json.dumps(response.json()["foods"], indent = 4)) 
for i in response.json()["foods"]:
    print( i["description"] + " : ", end = "" )
    for j in i["foodNutrients"]:
        if j["nutrientName"] == "Energy":
            if (j["unitName"] == "kJ"):
                print(j["value"] * 0.239, "KCAL")
            else:
                print( j["value"], j["unitName"])
            break