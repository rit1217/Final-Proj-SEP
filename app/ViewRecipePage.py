import sys
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QPushButton,QLabel,QBoxLayout,QFormLayout,QGroupBox
from PySide6.QtCore import *
from PySide6.QtGui import QPixmap
from UI.viewRecipe import Ui_Form

class ViewRecipe(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # self.ui.recipeLabel.setPixmap(QPixmap("app/UI/recipe-book.png"))
        # self.ui.recipeLabel.setScaledContents(True)
        
    def clickevent(self):
        self.ui.label.setText("Have click!!!!!")
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ViewRecipe()
    w.setFixedSize(647,545)
    w.show()
    sys.exit(app.exec_())
    