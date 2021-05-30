import sys
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QPushButton,QLabel,QBoxLayout,QFormLayout,QGroupBox
from PySide6.QtCore import *
from PySide6.QtGui import QPixmap
from UI.recipeInMenu import Ui_Form
from ViewRecipePage import ViewRecipe
from databasemodel.RecipeModel import *
from databasemodel.RatingModel import *

class RecipeInMenu(QWidget):
    def __init__(self, recipe, currentUser):
        QWidget.__init__(self,None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.current_user = currentUser
        self.ui.recipeLabel.setPixmap(QPixmap("app/UI/fast-food.png"))
        self.ui.recipeLabel.setScaledContents(True)
        self.setFixedSize( 364, 130)
        self.ui.previewButton.clicked.connect( self.viewButtonClick )
        self.recipe = recipe
        self.view = ViewRecipe( self.recipe, self.current_user )
        self.ui.recipenameLabel.setText("Recipe: %s"%(self.recipe.getName()))
        self.ui.ratingLabel.setText("Rating: %.1f" %(RATING_MODEL.getAverageRating( self.recipe.getId())))
        self.ui.levelLabel.setText( "Difficulty: %s" %(self.recipe.getDifficulty()))
        self.ui.creatorLabel.setText("Created by: %s" %(self.recipe.getCreator().getUsername()))
        self.picture = RECIPE_MODEL.getImageById( self.recipe.getId() )
        if self.picture is not None:
            pix = QPixmap()
            pix.loadFromData( self.picture[0] )
            self.ui.recipeLabel.setScaledContents( True )
            self.ui.recipeLabel.setPixmap( pix )

    def viewButtonClick(self):
        self.view.show()
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Register()
    w.setFixedSize(364,130)
    w.show()
    sys.exit(app.exec_())
    