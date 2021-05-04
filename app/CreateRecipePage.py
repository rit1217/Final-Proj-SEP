import sys
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QPushButton,QLabel,QBoxLayout,QFormLayout,QGroupBox
from PySide6.QtCore import *
from PySide6.QtGui import QPixmap
from UI.createRecipe import Ui_Form
from databasemodel.IngredientModel import *
from databasemodel.Ingredient import Ingredient

class CreateRecipe(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.cancel_pushButton.clicked.connect( self.cancel )
        self.ui.search_pushButton.clicked.connect( self.search )
        self.ui.add_pushButton.clicked.connect( self.addIngredient )
        self.ui.remove_pushButton.clicked.connect( self.removeIngredient)
        self.setFixedSize( 660, 660)
        # self.ui.recipeLabel.setPixmap(QPixmap("app/UI/recipe-book.png"))
        # self.ui.recipeLabel.setScaledContents(True)
    def cancel(self):
        self.close()

    def search( self ):
        keyword = self.ui.ingSearch_lineEdit.text()
        self.ui.searchResult_listWidget.clear()
        self.ui.searchResult_listWidget.addItems( INGREDIENT_MODEL.searchIngredient( keyword ))

    def addIngredient( self ):
        self.ui.ingredient_listWidget.addItem( self.ui.searchResult_listWidget.currentItem().text()  )

    def removeIngredient( self ):
        self.ui.ingredient_listWidget.takeItem( self.ui.ingredient_listWidget.currentRow())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = CreateRecipe()
    w.show()
    sys.exit(app.exec_())
    