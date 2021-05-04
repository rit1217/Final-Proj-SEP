import sys
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QPushButton,QLabel,QBoxLayout,QFormLayout,QGroupBox
from PySide6.QtCore import *
from PySide6.QtGui import QPixmap
from UI.recipeInProfile import Ui_Form
from ViewRecipePage import ViewRecipe
from CreateRecipePage import CreateRecipe

class RecipeInProfile(QWidget):
    def __init__(self, recipe ):
        QWidget.__init__(self,None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.recipeLabel.setPixmap(QPixmap("app/UI/recipe-book.png"))
        self.ui.recipeLabel.setScaledContents(True)
        self.ui.previewButton.clicked.connect( self.viewButtonClick )
        self.ui.editButton.clicked.connect( self.editButtonClick )
        self.setFixedSize( 445, 150)
        self.recipe = recipe
        self.view = ViewRecipe( self.recipe )
        self.createRecipe = CreateRecipe( self.recipe.getCreator().getUsername())
        self.createRecipe.setRecipe( recipe )
        self.ui.recipenameLabel.setText("Recipe: %s"%(self.recipe.getName()))
        self.ui.levelLabel.setText( "Difficulty: %s" %(self.recipe.getDifficulty()))


    def viewButtonClick(self):
        
        self.view.show()
    
    def editButtonClick( self ):
        self.createRecipe.show()
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = RecipeInProfile()
    w.setFixedSize(445,162)
    w.show()
    sys.exit(app.exec_())
    