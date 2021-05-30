import sys
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QPushButton,QLabel,QBoxLayout,QFormLayout,QGroupBox
from PySide6.QtCore import *
from PySide6.QtGui import QPixmap
from UI.recipeInProfile import Ui_Form
from ViewRecipePage import ViewRecipe
from CreateRecipePage import CreateRecipe
from databasemodel.RecipeModel import *
from databasemodel.RatingModel import *
from databasemodel.CommentModel import *
from databasemodel.IngredientModel import *

class RecipeInProfile(QWidget):
    def __init__(self, recipe, currentUser, profilePage ):
        QWidget.__init__(self,None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.current_user = currentUser
        self.profile_page = profilePage
        self.ui.recipeLabel.setPixmap(QPixmap("app/UI/recipe-book.png"))
        self.ui.recipeLabel.setScaledContents(True)
        self.ui.previewButton.clicked.connect( self.viewButtonClick )
        self.ui.editButton.clicked.connect( self.editButtonClick )
        self.setFixedSize( 500, 150)
        self.recipe = recipe
        self.view = ViewRecipe( self.recipe, self.current_user )
        self.createRecipe = CreateRecipe( self.recipe.getCreator().getUsername())
        self.createRecipe.setRecipe( recipe )
        self.ui.recipenameLabel.setText("Recipe: %s"%(self.recipe.getName()))
        self.ui.ratingLabel.setText("Rating: %.1f" %(RATING_MODEL.getAverageRating( self.recipe.getId())))
        self.ui.levelLabel.setText( "Difficulty: %s" %(self.recipe.getDifficulty()))
        self.picture = RECIPE_MODEL.getImageById( self.recipe.getId() )
        if self.picture is not None:
            pix = QPixmap()
            pix.loadFromData( self.picture[0] )
            self.ui.recipeLabel.setScaledContents( True )
            self.ui.recipeLabel.setPixmap( pix )
        self.ui.deleteButton.clicked.connect( self.deleteButtonClick )

    def viewButtonClick(self):
        
        self.view.show()
    
    def editButtonClick( self ):
        self.createRecipe.show()

    def deleteButtonClick( self ):
        confirm = QMessageBox( None)
        answer = confirm.question( None, "Delete Confirmation", "Do you want to delete this recipe?", confirm.No | confirm.Yes )
        if answer == confirm.Yes:
            self.profile_page.recipes.remove( self )
            RECIPE_MODEL.deleteById( self.recipe.getId() )
            COMMENT_MODEL.deleteByRecipe( self.recipe.getId())
            RATING_MODEL.deleteByRecipe( self.recipe.getId())
            INGREDIENT_MODEL.deleteIngredientInRec( self.recipe.getId() )
            self.profile_page.refresh()
        else:
            confirm.close()
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = RecipeInProfile()
    w.setFixedSize(445,162)
    w.show()
    sys.exit(app.exec_())
    