import sys
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QPushButton,QLabel,QBoxLayout,QFormLayout,QGroupBox
from PySide6.QtCore import *
from PySide6.QtGui import QPixmap
from UI.login import Ui_Form
from databasemodel.UserModel import *

class Login(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.Spoon.setPixmap(QPixmap("app/UI/spoon.png"))
        self.ui.Spoon.setScaledContents(True)
        self.ui.fork.setPixmap(QPixmap("app/UI/fork.png"))
        self.ui.fork.setScaledContents(True)
        self.ui.usernameLabel.setPixmap(QPixmap("app/UI/id-card.png"))
        self.ui.usernameLabel.setScaledContents(True)
        self.ui.passwordLabel.setPixmap(QPixmap("app/UI/padlock.png"))
        self.ui.passwordLabel.setScaledContents(True)
        # self.ui.logButton.clicked connect( self.login )
        self.setFixedSize( 455, 305 )

    def getUserEnter( self ):
        return { "username" : self.ui.userEdit.text(), "password" : self.ui.passwordEdit.text() }
    
    def clearPassword( self ):
        self.ui.passwordEdit.setText( "")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Login()
    w.setFixedSize(455,305)
    w.setStyleSheet("background-color: rgb(255, 136, 38)")
    w.show()
    sys.exit(app.exec_())
