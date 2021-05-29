import sys
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QPushButton,QLabel,QBoxLayout,QFormLayout,QGroupBox
from PySide6.QtCore import *
from PySide6.QtGui import QPixmap
from UI.viewRecipe import Ui_Form
from ViewCommentPage import ViewComment
from databasemodel.IngredientModel import *
from databasemodel.RecipeModel import *
from databasemodel.CommentModel import *
from databasemodel.RatingModel import *

class ViewRecipe(QWidget):
    def __init__(self, recipe, currentUser):
        QWidget.__init__(self,None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.recipe = recipe
        self.current_user = currentUser
        self.viewCommentPage = ViewComment( self.recipe )
        self.ui.creator_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt; color:#ff9300;\">Create by : %s</span></p></body></html>" %self.recipe.getCreator().getUsername()))
        self.ui.inCal_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#000000;\">%s KCAL</span></p></body></html>"%str(self.recipe.getCalories())))
        self.ui.inLevel_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#000000;\">%s</span></p></body></html>"%self.recipe.getDifficulty()))
        self.ui.name_label.setText(self.recipe.getName())
        self.ui.recipe_label.setText( self.recipe.getCookingStep() )
        self.ui.recipe_label.setStyleSheet( u"color: black;")
        # self.ui.ingredients_label.setStyleSheet( u"color: black;")
        self.picture = RECIPE_MODEL.getImageById( self.recipe.getId() )
        if self.picture is not None:
            pix = QPixmap()
            pix.loadFromData( self.picture[0] )
            self.ui.picture_label.setScaledContents( True )
            self.ui.picture_label.setPixmap( pix )

        self.ingredients = INGREDIENT_MODEL.getIngredient( self.recipe.getId() )
        print( self.ingredients )
        for i in self.ingredients:
            ing =  "%s  %.2f  %s  : %.2f KCAL" %(i.getName(), i.getQty(), i.getUnit(), i.getCalories())
            self.ui.ingredients_listWidget.addItem( ing)
        # self.ui.recipeLabel.setPixmap(QPixmap("app/UI/recipe-book.png"))
        # self.ui.recipeLabel.setScaledContents(True)
        if self.current_user.getUsername() == self.recipe.getCreator().getUsername():
            self.ui.rateButton.close()
            self.ui.rate_spinBox.close()
            self.ui.rating_label.close()
            self.ui.comment_lineEdit.close()
            self.ui.comment_label.close()
            self.ui.sendButton.close()
            self.ui.viewcomment.setGeometry( QRect(10,400, 240, 31))
            self.ui.viewcomment.clicked.connect( self.viewComment )

        else:
            self.ui.sendButton.clicked.connect( self.sendComment)
            self.ui.viewcomment.clicked.connect( self.viewComment )
            current_rating = RATING_MODEL.getRating( self.current_user.getUsername(), self.recipe.getId() )
            print ("\n\n" , current_rating, "\n\n")
            if current_rating is not None:
                self.ui.rateButton.clicked.connect( self.updateRate )
                self.ui.rate_spinBox.setValue( current_rating )
            else:
                self.ui.rateButton.clicked.connect( self.rate )
            
    def sendComment(self):
        comment = self.ui.comment_lineEdit.text()
        COMMENT_MODEL.insertComment( self.current_user.getUsername(), self.recipe.getId(), comment )
        self.ui.comment_lineEdit.setText("")
        message = QMessageBox( None )
        message.setText( "Comment sent!")
        message.exec_()
    
    def viewComment( self ):
        self.viewCommentPage.show()
    
    def rate( self ):
        RATING_MODEL.insertRating( self.current_user.getUsername(), self.recipe.getId(), self.ui.rate_spinBox.value())
        self.ui.rateButton.clicked.disconnect()
        self.ui.rateButton.clicked.connect( self.updateRate )
        message = QMessageBox( None )
        message.setText( "Recipe Rated!")
        message.exec_()

    def updateRate( self ):
        confirm = QMessageBox( None)
        answer = confirm.question( None, "Rating Confirmation", "Do you want to rate this recipe again?", confirm.No | confirm.Yes )
        if answer == confirm.Yes:
            RATING_MODEL.updateRating( self.current_user.getUsername(), self.recipe.getId(), self.ui.rate_spinBox.value())
            message = QMessageBox( None )
            message.setText( "Recipe Rated!")
            message.exec_()
        else:
            confirm.close()
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ViewRecipe("")
    w.setFixedSize(647,545)
    w.show()
    sys.exit(app.exec_())
    