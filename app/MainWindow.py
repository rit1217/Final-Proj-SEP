import sys
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QPushButton,QLabel,QBoxLayout,QFormLayout,QGroupBox
from PySide6.QtCore import *
from PySide6.QtGui import QPixmap
from LoginPage import Login
from RegisterPage import Register
from MainMenuPage import Mainmenu
from databasemodel.UserModel import *
from passlib.hash import pbkdf2_sha256

class MainWindow( QMainWindow ):
    def __init__( self ):
        QMainWindow.__init__( self, None )
        self.setFixedSize( 455, 305)
        self.setStyleSheet("background-color: rgb(255, 136, 38)")
        self.login = Login()
        self.register = Register()
        self.mainmenu = Mainmenu()
        self.setup_buttons()
        self.setCentralWidget( self.login )

    def setup_buttons( self ):
        self.login.ui.signButton.clicked.connect( self.login_signupButton )
        self.login.ui.logButton.clicked.connect( self.login_loginButton )

    def login_signupButton( self ):
        self.register.clearUI()
        self.register.show()

    def login_loginButton( self ):
        usr_ent_username = self.login.getUserEnter()["username"]
        usr_ent_password = self.login.getUserEnter()["password"]
        user_info = USER_MODEL.getUser( usr_ent_username )
        message = QMessageBox( None)

        if user_info == None :
            message.setText( "Wrong username!")
            message.exec_()
        else:
            if pbkdf2_sha256.verify( usr_ent_password, user_info.getPassword() ):
                self.setFixedSize(557,453)
                self.setStyleSheet("background-color:rgb(255, 187, 178);")
                self.setCentralWidget( self.mainmenu )
            else:
                message.setText( "Wrong password!")
                self.login.clearPassword()
                message.exec_()
