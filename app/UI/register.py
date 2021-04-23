# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Register.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(455, 284)
        Form.setStyleSheet(u"background-color: rgb(255, 136, 38)")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 30, 369, 238))
        self.widget.setStyleSheet(u"border-radius:10px;\n"
"background-color:rgb(255, 187, 178);\n"
"")
        self.signupButton = QPushButton(self.widget)
        self.signupButton.setObjectName(u"signupButton")
        self.signupButton.setGeometry(QRect(100, 210, 151, 22))
        self.signupButton.setStyleSheet(u"QPushButton{background-color:rgb(255, 127, 86);\n"
"border:none;\n"
"padding-top: 6px;\n"
"color:black;\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(255, 99, 0)\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(255, 43, 14)\n"
"}")
        self.surnameLabel = QLabel(self.widget)
        self.surnameLabel.setObjectName(u"surnameLabel")
        self.surnameLabel.setGeometry(QRect(12, 108, 55, 16))
        self.surnameLabel.setStyleSheet(u"color:black")
        self.nameLabel = QLabel(self.widget)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setGeometry(QRect(12, 76, 36, 16))
        self.nameLabel.setStyleSheet(u"color:black")
        self.nameLineEdit = QLineEdit(self.widget)
        self.nameLineEdit.setObjectName(u"nameLineEdit")
        self.nameLineEdit.setGeometry(QRect(88, 76, 261, 22))
        self.nameLineEdit.setStyleSheet(u"QLineEdit{\n"
"border:2px solid rgb(255, 201, 195);\n"
"color:black;\n"
"border-radius:10px;\n"
"background-color: rgb(255, 187, 178);\n"
"}\n"
"QLineEdit:hover{\n"
"  border:2px solid  rgb(255, 169, 93)\n"
"}\n"
"QLineEdit:focus{\n"
"  border:2px solid  rgb(255, 169, 93)\n"
"}")
        self.sexLabel = QLabel(self.widget)
        self.sexLabel.setObjectName(u"sexLabel")
        self.sexLabel.setGeometry(QRect(20, 170, 23, 16))
        self.sexLabel.setStyleSheet(u"color:black")
        self.birthLabel = QLabel(self.widget)
        self.birthLabel.setObjectName(u"birthLabel")
        self.birthLabel.setGeometry(QRect(20, 140, 30, 16))
        self.birthLabel.setStyleSheet(u"color:black")
        self.passwordLabel = QLabel(self.widget)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setGeometry(QRect(12, 44, 60, 16))
        self.passwordLabel.setStyleSheet(u"color:black")
        self.usernameLabel = QLabel(self.widget)
        self.usernameLabel.setObjectName(u"usernameLabel")
        self.usernameLabel.setGeometry(QRect(12, 12, 62, 16))
        self.usernameLabel.setStyleSheet(u"color:black")
        self.passwordLineEdit = QLineEdit(self.widget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setGeometry(QRect(88, 44, 261, 22))
        self.passwordLineEdit.setStyleSheet(u"QLineEdit{\n"
"border:2px solid rgb(255, 201, 195);\n"
"color:black;\n"
"border-radius:10px;\n"
"background-color: rgb(255, 187, 178);\n"
"}\n"
"QLineEdit:hover{\n"
"  border:2px solid  rgb(255, 169, 93)\n"
"}\n"
"QLineEdit:focus{\n"
"  border:2px solid  rgb(255, 169, 93)\n"
"}")
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)
        self.usernameLineEdit = QLineEdit(self.widget)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")
        self.usernameLineEdit.setGeometry(QRect(88, 12, 261, 22))
        self.usernameLineEdit.setStyleSheet(u"QLineEdit{\n"
"border:2px solid rgb(255, 201, 195);\n"
"color:black;\n"
"border-radius:10px;\n"
"background-color: rgb(255, 187, 178);\n"
"}\n"
"QLineEdit:hover{\n"
"  border:2px solid  rgb(255, 169, 93)\n"
"}\n"
"QLineEdit:focus{\n"
"  border:2px solid  rgb(255, 169, 93)\n"
"}")
        self.surnameLineEdit = QLineEdit(self.widget)
        self.surnameLineEdit.setObjectName(u"surnameLineEdit")
        self.surnameLineEdit.setGeometry(QRect(88, 108, 261, 22))
        self.surnameLineEdit.setStyleSheet(u"QLineEdit{\n"
"border:2px solid rgb(255, 201, 195);\n"
"color:black;\n"
"border-radius:10px;\n"
"background-color: rgb(255, 187, 178);\n"
"}\n"
"QLineEdit:hover{\n"
"  border:2px solid  rgb(255, 169, 93)\n"
"}\n"
"QLineEdit:focus{\n"
"  border:2px solid  rgb(255, 169, 93)\n"
"}")
        self.sexComboBox = QComboBox(self.widget)
        self.sexComboBox.addItem("")
        self.sexComboBox.addItem("")
        self.sexComboBox.setObjectName(u"sexComboBox")
        self.sexComboBox.setGeometry(QRect(60, 170, 121, 20))
        self.sexComboBox.setStyleSheet(u"\n"
"color:black;\n"
"border-radius: 10px;")
        self.layoutWidget = QWidget(self.widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(190, 140, 161, 51))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.weightLabel = QLabel(self.layoutWidget)
        self.weightLabel.setObjectName(u"weightLabel")
        self.weightLabel.setStyleSheet(u"color:black")

        self.gridLayout.addWidget(self.weightLabel, 0, 0, 1, 1)

        self.heightLabel = QLabel(self.layoutWidget)
        self.heightLabel.setObjectName(u"heightLabel")
        self.heightLabel.setStyleSheet(u"color:black")

        self.gridLayout.addWidget(self.heightLabel, 1, 0, 1, 1)

        self.weightLineEdit = QLineEdit(self.layoutWidget)
        self.weightLineEdit.setObjectName(u"weightLineEdit")
        self.weightLineEdit.setStyleSheet(u"QLineEdit{\n"
"border:2px solid rgb(255, 201, 195);\n"
"color:black;\n"
"border-radius:10px;\n"
"background-color: rgb(255, 187, 178);\n"
"}\n"
"QLineEdit:hover{\n"
"  border:2px solid  rgb(255, 169, 93)\n"
"}\n"
"QLineEdit:focus{\n"
"  border:2px solid  rgb(255, 169, 93)\n"
"}")

        self.gridLayout.addWidget(self.weightLineEdit, 0, 1, 1, 1)

        self.heightLineEdit = QLineEdit(self.layoutWidget)
        self.heightLineEdit.setObjectName(u"heightLineEdit")
        self.heightLineEdit.setStyleSheet(u"QLineEdit{\n"
"border:2px solid rgb(255, 201, 195);\n"
"color:black;\n"
"border-radius:10px;\n"
"background-color: rgb(255, 187, 178);\n"
"}\n"
"QLineEdit:hover{\n"
"  border:2px solid  rgb(255, 169, 93)\n"
"}\n"
"QLineEdit:focus{\n"
"  border:2px solid  rgb(255, 169, 93)\n"
"}")

        self.gridLayout.addWidget(self.heightLineEdit, 1, 1, 1, 1)

        self.dateEdit = QDateEdit(self.widget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(80, 140, 101, 22))
        currentDate = QDate.currentDate()
        self.dateEdit.setDateRange( QDate( currentDate.year() - 120, currentDate.month(), currentDate.day() ), currentDate)
        self.dateEdit.setStyleSheet(u"color:black;\n"
"\n"
"")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.signupButton.setText(QCoreApplication.translate("Form", u"Sign up", None))
        self.surnameLabel.setText(QCoreApplication.translate("Form", u"Surname", None))
        self.nameLabel.setText(QCoreApplication.translate("Form", u"Name", None))
        self.sexLabel.setText(QCoreApplication.translate("Form", u"Sex", None))
        self.birthLabel.setText(QCoreApplication.translate("Form", u"Birth", None))
        self.passwordLabel.setText(QCoreApplication.translate("Form", u"Password", None))
        self.usernameLabel.setText(QCoreApplication.translate("Form", u"Username", None))
        self.sexComboBox.setItemText(0, QCoreApplication.translate("Form", u"Male", None))
        self.sexComboBox.setItemText(1, QCoreApplication.translate("Form", u"Female", None))

        self.weightLabel.setText(QCoreApplication.translate("Form", u"Weight", None))
        self.heightLabel.setText(QCoreApplication.translate("Form", u"Height", None))
    # retranslateUi

