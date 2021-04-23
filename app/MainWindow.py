import sys
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QPushButton,QLabel,QBoxLayout,QFormLayout,QGroupBox
from PySide6.QtCore import *
from PySide6.QtGui import QPixmap
from LoginPage import Login
from RegisterPage import Register
from databasemodel.UserModel import *

class MainWindow( QMainWindow ):
    def __init__( self ):
        QMainWindow.__init__( self, None )
        self.setFixedSize( 455, 305)
        self.setStyleSheet("background-color: rgb(255, 136, 38)")
        self.login = Login()
        self.login.ui.signButton.clicked.connect( self.login_signupButton )
        self.login.ui.logButton.clicked.connect( self.login_loginButton )
        self.register = Register()
        self.setCentralWidget( self.login )

    def login_signupButton( self ):
        self.register.clearUI()
        self.register.show()

    def login_loginButton( self ):
        usr_ent_username = self.login.getUserEnter()["username"]
        usr_ent_password = self.login.getUserEnter()["password"]
        user_info = USER_MODEL.getUser( usr_ent_username )
        if user_info == None :
            message = QMessageBox( None)
            message.setText( "Wrong username!")
            message.exec_()