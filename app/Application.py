import sys
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QPushButton,QLabel,QBoxLayout,QFormLayout,QGroupBox
from PySide6.QtCore import *
from PySide6.QtGui import QPixmap
from LoginPage import Login
from RegisterPage import Register

class Application:
    def __init__( self ):
        self.app = QApplication(sys.argv)
        self.register = Register()
        self.login = Login()

    def run( self ):
        self.login.ui.signButton.clicked.connect( self.signup)
        self.login.show()
        sys.exit(self.app.exec_())

    
    def signup( self ):
        self.register.clearUI()
        self.register.show()

app = Application()
app.run()

        