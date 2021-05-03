import sys
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QPushButton,QLabel,QBoxLayout,QFormLayout,QGroupBox
from PySide6.QtCore import *
from PySide6.QtGui import QPixmap
from UI.createRecipe import Ui_Form

class CreateRecipe(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.cancel_pushButton.clicked.connect( self.cancel )
        # self.ui.recipeLabel.setPixmap(QPixmap("app/UI/recipe-book.png"))
        # self.ui.recipeLabel.setScaledContents(True)
        
    def cancel(self):
        self.close()
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = CreateRecipe()
    w.setFixedSize(544,471)
    w.show()
    sys.exit(app.exec_())
    