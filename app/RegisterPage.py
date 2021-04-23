import sys
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QPushButton,QLabel,QBoxLayout,QFormLayout,QGroupBox
from PySide6.QtCore import *
from UI.register import Ui_Form
from databasemodel.UserModel import *
from databasemodel.User import User
from passlib.hash import pbkdf2_sha256
class Register(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setFixedSize( 455, 305 )
        self.setStyleSheet("background-color: rgb(255, 136, 38)")
        self.ui.signupButton.clicked.connect( self.registerConfirm )

    def clearUI(self):
        self.ui.usernameLineEdit.setText("")
        self.ui.passwordLineEdit.setText("")
        self.ui.sexComboBox.setCurrentIndex(0)
        self.ui.dateEdit.setDate( QDate.currentDate() )
        self.ui.heightLineEdit.setText("")        
        self.ui.weightLineEdit.setText("")
        self.ui.nameLineEdit.setText("")
        self.ui.surnameLineEdit.setText("")

    def registerConfirm( self ):
        info = []
        info.append(self.ui.usernameLineEdit.text())
        info.append(pbkdf2_sha256.hash(self.ui.passwordLineEdit.text()))
        info.append(self.ui.nameLineEdit.text())
        info.append(self.ui.surnameLineEdit.text())
        info.append(int(self.ui.heightLineEdit.text()))
        info.append(int(self.ui.weightLineEdit.text()))
        info.append(self.ui.dateEdit.date().toString("dd/MM/yyyy"))
        info.append(self.ui.sexComboBox.currentText())
        info = tuple( info )
        USER_MODEL.insertUser( User(info) )
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Register()
    w.setFixedSize(455,305)
    w.show()
    print( QDate( 2021, 2, 10).toString("dd/MM/yyyy") )
    sys.exit(app.exec_())

''' username : rrrit
pwd : pass '''