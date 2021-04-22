class Ingredient:
    def __init__( self, fdc_id, name, qty, unit, calories ):
        self.fdc_id = fdc_id
        self.name = name
        self.qty = qty
        self.unit = unit
        self.calories = calories
        self.info = (fdc_id, name, qty, unit, calories)