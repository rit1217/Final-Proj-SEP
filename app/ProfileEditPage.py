import sys
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QPushButton,QLabel,QBoxLayout,QFormLayout,QGroupBox
from PySide6.QtCore import *
from UI.profileEdit import Ui_Form
from databasemodel.UserModel import *
from databasemodel.User import User
from passlib.hash import pbkdf2_sha256
import re

class ProfileEdit(QWidget):
    def __init__(self, user, profilePage):
        QWidget.__init__(self,None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.current_user = user
        self.profile_page = profilePage
        self.ui.firstname_lineEdit.setText( self.current_user.getFirstName() )
        self.ui.lastname_lineEdit.setText( self.current_user.getLastName() )
        self.ui.height_lineEdit.setText( str(self.current_user.getHeight()))
        self.ui.weight_lineEdit.setText( str(self.current_user.getWeight()))
        self.ui.gender_comboBox.setCurrentText( self.current_user.getGender() )
        self.ui.ok_pushButton.clicked.connect( self.save )
        self.ui.cancel_pushButton.clicked.connect( self.cancel )

    def cancel(self):
        self.close()

    def save( self ):
        fname_valid = [re.search( "[a-z,A-Z]", i )for i in self.ui.firstname_lineEdit.text()]
        lname_valid = [re.search( "[a-z,A-Z]", i )for i in self.ui.lastname_lineEdit.text()]
        usr_ent_weight = self.ui.weight_lineEdit.text()
        usr_ent_height = self.ui.height_lineEdit.text()
        weight_valid = [re.search( "[0-9]", i) for i in usr_ent_weight]
        height_valid = [re.search( "[0-9]", i) for i in usr_ent_height]
        
        message = QMessageBox( None )
        if len(self.ui.height_lineEdit.text()) <= 0 or len(self.ui.weight_lineEdit.text()) <= 0 or len(self.ui.firstname_lineEdit.text()) <= 0 or len(self.ui.lastname_lineEdit.text()) <= 0:
            message.setText( "Please fill in all field.")
        else:
            if None not in fname_valid and None not in lname_valid:
                if None not in weight_valid and None not in height_valid and int(usr_ent_weight) > 0 and int(usr_ent_height) > 0:
                    self.registerConfirm()
                    message.setText( "Registration complete!")
                    self.close()
                else:
                    message.setText("Weight and Height must be integer.")
            else:
                message.setText("First name and Last name must contain only English alphabet.")
        message.exec_()

    def registerConfirm( self ):
        info = []
        info.append(self.ui.firstname_lineEdit.text()[0].upper() + self.ui.firstname_lineEdit.text()[1:].lower())
        info.append(self.ui.lastname_lineEdit.text()[0].upper() + self.ui.lastname_lineEdit.text()[1:].lower())
        info.append(int(self.ui.height_lineEdit.text()))
        info.append(int(self.ui.weight_lineEdit.text()))
        info.append(self.ui.gender_comboBox.currentText())
        info = tuple( info )
        USER_MODEL.updateUser( self.current_user.getUsername(), info )
        self.profile_page.updateProfile( USER_MODEL.getUser(self.current_user.getUsername()))

