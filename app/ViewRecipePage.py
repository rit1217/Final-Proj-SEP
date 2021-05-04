import sys
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QPushButton,QLabel,QBoxLayout,QFormLayout,QGroupBox
from PySide6.QtCore import *
from PySide6.QtGui import QPixmap
from UI.viewRecipe import Ui_Form

class ViewRecipe(QWidget):
    def __init__(self, recipe):
        QWidget.__init__(self,None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.recipe = recipe
        self.ui.creator_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt; color:#ff9300;\">Create by : %s</span></p></body></html>" %self.recipe.getCreator().getUsername()))
        self.ui.inCal_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#000000;\">%s KCAL</span></p></body></html>"%str(self.recipe.getCalories())))
        self.ui.inLevel_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#000000;\">%s</span></p></body></html>"%self.recipe.getDifficulty()))
        self.ui.name_label.setText(self.recipe.getName())
        self.ui.recipe_label.setText( self.recipe.getCookingStep() )
        self.ui.recipe_label.setStyleSheet( u"color: black;")
        # self.ui.recipeLabel.setPixmap(QPixmap("app/UI/recipe-book.png"))
        # self.ui.recipeLabel.setScaledContents(True)
        
    def setRecipe(self, recipe):
        pass
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ViewRecipe("")
    w.setFixedSize(647,545)
    w.show()
    sys.exit(app.exec_())
    