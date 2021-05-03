import sys
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QPushButton,QLabel,QBoxLayout,QFormLayout,QGroupBox
from PySide6.QtCore import *
from PySide6.QtGui import QPixmap
from UI.recipeInMenu import Ui_Form
from ViewRecipePage import ViewRecipe

class RecipeInMenu(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.recipeLabel.setPixmap(QPixmap("app/UI/fast-food.png"))
        self.ui.recipeLabel.setScaledContents(True)
        self.setFixedSize( 364, 130)
        self.ui.previewButton.clicked.connect( self.viewButtonClick )
        self.view = ViewRecipe()

    def viewButtonClick(self):
        self.view.show()
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Register()
    w.setFixedSize(364,130)
    w.show()
    sys.exit(app.exec_())
    