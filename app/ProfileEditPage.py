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
    def __init__(self, user):
        QWidget.__init__(self,None)
        self.ui = Ui_Form()
        self.current_user = user
        self.ui.firstname_lineEdit.setText( self.current_user.getFirstName() )
        self.ui.lastname_lineEdit.setText( self.current_user.getLastName() )
        self.ui.height_lineEdit.setText( str(self.current_user.getHeight()))
        self.ui.weight_lineEdit.setText( str(self.current_user.getWeight()))
        index = self.ui.gender_comboBox.findData( self.current_user.getGender())
        self.ui.gender_comboBox.setCurrentIndex( index )
        self.ui.ok_pushButton.clicked.connect( self.save )
        self.ui.cancel_pushButton.clicked.connect( self.cancel )

    def cancel(self):
        self.close()

    def save( self ):
        usr_ent_username = self.ui.usernameLineEdit.text()
        username_valid = [re.search( "[a-z,A-Z,0-9,_]", i )for i in usr_ent_username]
        fname_valid = [re.search( "[a-z,A-Z]", i )for i in self.ui.nameLineEdit.text()]
        lname_valid = [re.search( "[a-z,A-Z]", i )for i in self.ui.surnameLineEdit.text()]
        usr_ent_password = self.ui.passwordLineEdit.text()
        pwd_valid = [re.search( "[a-z,A-Z,0-9,_]", i )for i in usr_ent_password]
        usr_ent_weight = self.ui.weightLineEdit.text()
        usr_ent_height = self.ui.heightLineEdit.text()
        weight_valid = [re.search( "[0-9]", i) for i in usr_ent_weight]
        height_valid = [re.search( "[0-9]", i) for i in usr_ent_height]
        
        message = QMessageBox( None )
        if len(usr_ent_password) <= 0 or len(usr_ent_username) <= 0 or len(self.ui.heightLineEdit.text()) <= 0 or len(self.ui.weightLineEdit.text()) <= 0 or len(self.ui.nameLineEdit.text()) <= 0 or len(self.ui.surnameLineEdit.text()) <= 0:
            message.setText( "Please fill in all field.")
        else:
            if None not in username_valid and len(usr_ent_username) >= 4 and len(usr_ent_username) <= 14:
                if USER_MODEL.getUser( usr_ent_username ) is None:
                    if len(usr_ent_password) >= 8 and None not in pwd_valid:
                        if usr_ent_password == self.ui.comfirmLineEdit.text():
                            if None not in fname_valid and None not in lname_valid:
                                if None not in weight_valid and None not in height_valid and int(usr_ent_weight) > 0 and int(usr_ent_height) > 0:
                                    self.registerConfirm()
                                    message.setText( "Registration complete!")
                                    self.close()
                                else:
                                    message.setText("Weight and Height must be integer.")
                            else:
                                message.setText("First name and Last name must contain only English alphabet.")

                        else:
                            message.setText( "Password are not matching.")
                        
                    else:
                        message.setText( "Password must be at least 8-14 characters long and must not contain special character.")
                else:
                    message.setText( "Username already existed.")
            else:
                message.setText( "Username must be at least 4 characters long and must not contain special character.")
        message.exec_()

    def registerConfirm( self ):
        info = []
        info.append(self.ui.usernameLineEdit.text())
        info.append(pbkdf2_sha256.hash(self.ui.passwordLineEdit.text()))
        info.append(self.ui.nameLineEdit.text()[0].upper() + self.ui.nameLineEdit.text()[1:].lower())
        info.append(self.ui.surnameLineEdit.text()[0].upper() + self.ui.surnameLineEdit.text()[1:].lower())
        info.append(int(self.ui.heightLineEdit.text()))
        info.append(int(self.ui.weightLineEdit.text()))
        info.append(self.ui.dateEdit.date().toString("dd/MM/yyyy"))
        info.append(self.ui.sexComboBox.currentText())
        info = tuple( info )
        u = User(info)
        USER_MODEL.insertUser( u )