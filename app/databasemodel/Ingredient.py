class Ingredient:
    def __init__( self, fdc_id, name, qty, unit, calories ):
        self.fdc_id = fdc_id
        self.name = name
        self.qty = qty
        self.unit = unit
        self.calories = calories
        self.recipe = None
        self.info = (fdc_id, name,0, qty, unit, calories)

    def getIngredientInfo( self ):
        return self.info

    def getFdcId( self ):
        return self.fdc_id

    def getName( self ):
        return self.name
    
    def getCalories( self ):
        return self.calories
    
    def getQty( self ):
        return self.qty
    
    def addQty( self, qty ):
        self.qty += qty
    
    def getUnit( self ):
        return self.unit
    
    def addEnergy ( self, energ ):
        self.calories += energ

    def setRecipe( self, recipe_id):
        self.recipe = recipe_id
        self.info = (self.fdc_id, self.name,self.recipe, self.qty, self.unit, self.calories)
    
    def getRecipe( self ):
        return self.recipe
    
    def getCalories( self ) :
         return self.calories


    def __str__( self ):
        return "%s %s %f %s %f" %( self.fdc_id, self.name, self.qty, self.unit, self.calories )