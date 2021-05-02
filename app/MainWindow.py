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
from Constant import *
from ProfilePage import Profile
from CreateRecipePage import CreateRecipe

class MainWindow( QMainWindow ):
    def __init__( self ):
        QMainWindow.__init__( self, None )
        self.setFixedSize( 455, 305)
        self.setStyleSheet("background-color: rgb(255, 136, 38)")
        self.login = Login()
        self.register = Register()
        self.mainmenu = Mainmenu()
        self.profile = Profile()
        self.createRecipe = CreateRecipe()
        self.current_user = None
        self.setup_buttons()
        self.setCentralWidget( self.login )

    def setup_buttons( self ):
        self.login.ui.signButton.clicked.connect( self.login_signupButton )
        self.login.ui.logButton.clicked.connect( self.login_loginButton )
        self.mainmenu.ui.clickprofileButton.clicked.connect( self.main_profileButton)
        self.mainmenu.ui.clickcreateButton.clicked.connect( self.main_createButton)
        self.createRecipe.ui.cancel_pushButton.clicked.connect( self.create_cancelButton )

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
                self.current_user = user_info
                self.setFixedSize(557,457)
                self.setStyleSheet("background-color:rgb(255, 187, 178);")
                self.setCentralWidget( self.mainmenu )
            else:
                message.setText( "Wrong password!")
                self.login.clearPassword()
                message.exec_()

    def main_profileButton( self ):
        self.profile.setFixedSize( 557, 457)
        # self.profile.show()
        self.setFixedSize(557,457)
        self.profile.updateProfile( self.current_user )
        # self.setStyleSheet("background-color:rgb(255, 187, 178);")
        self.setCentralWidget( self.profile )

    def main_createButton( self ):
        self.createRecipe.show()
    
    def create_cancelButton( self ):
        self.createRecipe.close()
        self.createRecipe = CreateRecipe()
        self.createRecipe.ui.cancel_pushButton.clicked.connect( self.create_cancelButton )
