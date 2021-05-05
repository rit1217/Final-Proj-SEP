import sys
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QPushButton,QLabel,QBoxLayout,QFormLayout,QGroupBox
from PySide6.QtCore import *
from PySide6.QtGui import QPixmap
from UI.createRecipe import Ui_Form
from databasemodel.IngredientModel import *
from databasemodel.Ingredient import Ingredient
from databasemodel.RecipeModel import *

class CreateRecipe(QWidget):
    def __init__(self, current_user ):
        QWidget.__init__(self,None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.cancel_pushButton.clicked.connect( self.cancel )
        self.ui.save_pushButton.clicked.connect( self.save )
        self.ui.search_pushButton.clicked.connect( self.search )
        self.ui.add_pushButton.clicked.connect( self.addIngredient )
        self.ui.remove_pushButton.clicked.connect( self.removeIngredient)
        self.ui.pic_pushButton.clicked.connect( self.browse )
        self.setFixedSize( 660, 660)
        self.unitMultiplier = [1, 1, 220, 4.5, 14, 28]
        self.ingredients = []
        self.current_user = current_user
        self.recipe = None
        self.picture = None
        # self.ui.recipeLabel.setPixmap(QPixmap("app/UI/recipe-book.png"))
        # self.ui.recipeLabel.setScaledContents(True)
    def cancel(self):
        self.close()

    def browse( self ):
        self.picture = QFileDialog.getOpenFileName(None, "Open a file", ":","Images (*.png *.xpm *.jpg)")[0]
        
    def search( self ):
        keyword = self.ui.ingSearch_lineEdit.text()
        self.ui.searchResult_listWidget.clear()
        self.search_result = INGREDIENT_MODEL.searchIngredient( keyword )
        self.ui.searchResult_listWidget.addItems( self.search_result["Text"])


    def addIngredient( self ):
        amount = self.ui.amount_lineEdit.text()

        if float(amount) > 0 :
            selectedIndex = self.ui.searchResult_listWidget.currentRow()
            selectedItem = self.search_result["Info"][selectedIndex]
            unit = self.ui.unit_comboBox.currentText()
            print( self.unitMultiplier[self.ui.unit_comboBox.currentIndex()] )
            energy = selectedItem["Energy"] * float(amount) * self.unitMultiplier[self.ui.unit_comboBox.currentIndex()] / 100
            duplicate = False
            for i in range( len( self.ingredients )):
                if self.ingredients[i].getName() == selectedItem["Name"][:-3]:
                    self.ingredients[i].addEnergy( energy )
                    items = [self.ui.unit_comboBox.itemText(i) for i in range(self.ui.unit_comboBox.count())]
                    self.ingredients[i].addQty( float(amount) * self.unitMultiplier[self.ui.unit_comboBox.currentIndex()] / self.unitMultiplier[items.index(self.ingredients[i].getUnit())])
                    duplicate = True
            if duplicate:
                self.ui.ingredient_listWidget.clear()
                for i in self.ingredients:
                    self.ui.ingredient_listWidget.addItem( i.getName() + "  " + str(i.getQty()) + "  " + i.getUnit() + "  : " + "%.2f KCAL"%i.getCalories())
            else:
                self.ingredients.append( Ingredient( selectedItem["FdcId"], selectedItem["Name"][:-3], float(amount), unit, energy) )
                self.ui.ingredient_listWidget.addItem( selectedItem["Name"][:-3] + "  " + amount + "  " + unit + "  : " + str(energy) + " KCAL" )
        print( self.ingredients)

    def removeIngredient( self ):
        selectedIndex = self.ui.ingredient_listWidget.currentRow()
        self.ingredients.pop(selectedIndex)
        self.ui.ingredient_listWidget.takeItem( selectedIndex )
    
    def save( self ):
        message = QMessageBox( None )
        if len(self.ui.name_lineEdit.text()) > 0:
            if len(self.ingredients) > 0:
                if len(self.ui.instruction_textEdit.toPlainText()) > 0:
                    recipe_id = RECIPE_MODEL.getMaxId()[0] + 1
                    total_cal = 0
                    for i in range( len(self.ingredients)):
                        self.ingredients[i].setRecipe( recipe_id )
                        INGREDIENT_MODEL.insertIngredientInRec( self.ingredients[i])
                        total_cal += self.ingredients[i].getCalories()
                    recipe_info = (recipe_id, self.ui.name_lineEdit.text(), total_cal, self.ui.instruction_textEdit.toPlainText(), 
                    self.current_user, self.ui.level_comboBox.currentText())
                    RECIPE_MODEL.insertRecipe( Recipe(recipe_info) )
                    if self.picture is not None:
                        RECIPE_MODEL.insertImageById( self.picture, recipe_id )
                    message.setText("Recipe saved!")
                    self.close()
                else:
                    message.setText( "Please insert cooking instruction.")
            else:
                message.setText( "Please insert ingredient.")
        else:
            message.setText("Please insert recipe name.")

        message.exec_()
    
    def setRecipe( self, recipe ):
        self.recipe = recipe
        self.ui.save_pushButton.clicked.disconnect()
        self.ui.save_pushButton.clicked.connect( self.update )
        self.ui.name_lineEdit.setText( self.recipe.getName() )
        self.ui.level_comboBox.setCurrentIndex( int(self.recipe.getDifficulty()[0] )-1)
        self.ui.instruction_textEdit.setText( self.recipe.getCookingStep() )
        self.ingredients = INGREDIENT_MODEL.getIngredient( self.recipe.getId() )
        for i in self.ingredients:
            self.ui.ingredient_listWidget.addItem( "%s  %.2f  %s  : %.2f KCAL" %(i.getName(), i.getQty(), i.getUnit(), i.getCalories()))

    def update( self ):
        message = QMessageBox( None )
        if len(self.ui.name_lineEdit.text()) > 0:
            if len(self.ingredients) > 0:
                if len(self.ui.instruction_textEdit.toPlainText()) > 0:
                    total_cal = 0
                    INGREDIENT_MODEL.deleteIngredientInRec( self.recipe.getId())
                    for i in range( len(self.ingredients)):
                        self.ingredients[i].setRecipe( self.recipe.getId() )
                        INGREDIENT_MODEL.insertIngredientInRec( self.ingredients[i])
                        total_cal += self.ingredients[i].getCalories()
                    recipe_info = (self.recipe.getId(), self.ui.name_lineEdit.text(), total_cal, self.ui.instruction_textEdit.toPlainText(), 
                    self.current_user, self.ui.level_comboBox.currentText())
                    print( "recipe info : ", recipe_info)
                    RECIPE_MODEL.updateRecipe( Recipe(recipe_info) )
                    if self.picture is not None:
                        RECIPE_MODEL.insertImageById( self.picture, self.recipe.getId() )
                    message.setText("Recipe saved!")
                    self.close()
                else:
                    message.setText( "Please insert cooking instruction.")
            else:
                message.setText( "Please insert ingredient.")
        else:
            message.setText("Please insert recipe name.")

        message.exec_()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = CreateRecipe( "rrrit1")
    w.show()
    sys.exit(app.exec_())
    