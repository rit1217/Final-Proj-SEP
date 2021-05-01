import sys
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QPushButton,QLabel,QBoxLayout,QFormLayout,QGroupBox
from PySide6.QtCore import *
from PySide6.QtGui import QPixmap
from UI.recipeInProfile import Ui_Form

class RecipeInProfile(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.recipeLabel.setPixmap(QPixmap("app/UI/recipe-book.png"))
        self.ui.recipeLabel.setScaledContents(True)
        
    def clickevent(self):
        self.ui.label.setText("Have click!!!!!")
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Register()
    w.setFixedSize(440,162)
    w.show()
    sys.exit(app.exec_())
    