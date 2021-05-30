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
        self.login.ui.signButton.clicked.connect( self.login_signupButton )
        self.login.ui.logButton.clicked.connect( self.login_loginButton )
        self.register = Register()
        self.createRecipe = None
        self.current_user = None
        self.setCentralWidget( self.login )


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
                self.setFixedSize(557,790)
                self.mainmenu = Mainmenu( self.current_user )
                self.mainmenu.ui.clickprofileButton.clicked.connect( self.main_profileButton)
                self.mainmenu.ui.clickcreateButton.clicked.connect( self.main_createButton)
                self.setStyleSheet("background-color:rgb(255, 187, 178);")
                self.setCentralWidget( self.mainmenu )
            else:
                message.setText( "Wrong password!")
                self.login.clearPassword()
                message.exec_()

    def main_profileButton( self ):
        self.profile = Profile()
        self.profile.ui.backButton.clicked.connect( self.prof_backButton )
        # self.profile.show()
        self.setFixedSize(710,465)
        self.profile.updateProfile( self.current_user )
        self.profile.ui.refreshButton.clicked.connect( self.profile.refresh )

        # self.setStyleSheet("background-color:rgb(255, 187, 178);")
        self.setCentralWidget( self.profile )

    def main_createButton( self ):
        self.createRecipe = CreateRecipe(self.current_user.getUsername())
        self.createRecipe.show()

    def prof_backButton( self ):
        self.mainmenu = Mainmenu(self.current_user)
        self.mainmenu.ui.clickprofileButton.clicked.connect( self.main_profileButton)
        self.mainmenu.ui.clickcreateButton.clicked.connect( self.main_createButton)
        self.setFixedSize(557,790)
        self.setCentralWidget( self.mainmenu )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Mainmenu()
    w.setStyleSheet( "background-color:rgb(255, 187, 178)")
    w.show()
    sys.exit(app.exec_())
