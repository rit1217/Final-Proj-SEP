import sys
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QPushButton,QLabel,QBoxLayout,QFormLayout,QGroupBox
from PySide6.QtCore import *
from PySide6.QtGui import QPixmap
from UI.loginimport Ui_Form

class Login(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.Spoon.setPixmap(QPixmap("spoon.png"))
        self.ui.Spoon.setScaledContents(True)
        self.ui.fork.setPixmap(QPixmap("fork.png"))
        self.ui.fork.setScaledContents(True)
        self.ui.usernameLabel.setPixmap(QPixmap("id-card.png"))
        self.ui.usernameLabel.setScaledContents(True)
        self.ui.passwordLabel.setPixmap(QPixmap("padlock.png"))
        self.ui.passwordLabel.setScaledContents(True)
        
        self.ui.signButton.clicked.connect(self.clicked)
    

    def clicked(self):
        print("hi")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Login()
    w.setFixedSize(455,305)
    w.setStyleSheet("background-color: rgb(255, 136, 38)")
    w.show()
    sys.exit(app.exec_())
