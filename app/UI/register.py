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
        Form.resize(454, 305)
        Form.setStyleSheet(u"background-color: rgb(255, 136, 38)")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 10, 391, 281))
        self.widget.setStyleSheet(u"border-radius:10px;\n"
"background-color:rgb(255, 187, 178);\n"
"")
        self.signupButton = QPushButton(self.widget)
        self.signupButton.setObjectName(u"signupButton")
        self.signupButton.setGeometry(QRect(110, 250, 151, 22))
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
        self.layoutWidget = QWidget(self.widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(210, 175, 161, 56))
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

        self.widget1 = QWidget(self.widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(30, 10, 341, 152))
        self.gridLayout_2 = QGridLayout(self.widget1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.usernameLabel = QLabel(self.widget1)
        self.usernameLabel.setObjectName(u"usernameLabel")
        self.usernameLabel.setStyleSheet(u"color:black")

        self.gridLayout_2.addWidget(self.usernameLabel, 0, 0, 1, 1)

        self.passwordLabel = QLabel(self.widget1)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setStyleSheet(u"color:black")

        self.gridLayout_2.addWidget(self.passwordLabel, 1, 0, 1, 1)

        self.comfirmLabel = QLabel(self.widget1)
        self.comfirmLabel.setObjectName(u"comfirmLabel")
        self.comfirmLabel.setStyleSheet(u"color:black;")

        self.gridLayout_2.addWidget(self.comfirmLabel, 2, 0, 1, 2)

        self.comfirmLineEdit = QLineEdit(self.widget1)
        self.comfirmLineEdit.setObjectName(u"comfirmLineEdit")
        self.comfirmLineEdit.setStyleSheet(u"QLineEdit{\n"
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
        self.comfirmLineEdit.setEchoMode(QLineEdit.Password)

        self.gridLayout_2.addWidget(self.comfirmLineEdit, 2, 2, 1, 1)

        self.nameLabel = QLabel(self.widget1)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setStyleSheet(u"color:black")

        self.gridLayout_2.addWidget(self.nameLabel, 3, 0, 1, 1)

        self.surnameLabel = QLabel(self.widget1)
        self.surnameLabel.setObjectName(u"surnameLabel")
        self.surnameLabel.setStyleSheet(u"color:black")

        self.gridLayout_2.addWidget(self.surnameLabel, 4, 0, 1, 1)

        self.surnameLineEdit = QLineEdit(self.widget1)
        self.surnameLineEdit.setObjectName(u"surnameLineEdit")
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

        self.gridLayout_2.addWidget(self.surnameLineEdit, 4, 2, 1, 1)

        self.nameLineEdit = QLineEdit(self.widget1)
        self.nameLineEdit.setObjectName(u"nameLineEdit")
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

        self.gridLayout_2.addWidget(self.nameLineEdit, 3, 2, 1, 1)

        self.passwordLineEdit = QLineEdit(self.widget1)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
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

        self.gridLayout_2.addWidget(self.passwordLineEdit, 1, 2, 1, 1)

        self.usernameLineEdit = QLineEdit(self.widget1)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")
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

        self.gridLayout_2.addWidget(self.usernameLineEdit, 0, 2, 1, 1)

        self.widget2 = QWidget(self.widget)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(30, 180, 171, 48))
        self.gridLayout_3 = QGridLayout(self.widget2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.birthLabel = QLabel(self.widget2)
        self.birthLabel.setObjectName(u"birthLabel")
        self.birthLabel.setStyleSheet(u"color:black")

        self.gridLayout_3.addWidget(self.birthLabel, 0, 0, 1, 1)

        self.dateEdit = QDateEdit(self.widget2)
        self.dateEdit.setObjectName(u"dateEdit")
        currentDate = QDate.currentDate()
        self.dateEdit.setDateRange( QDate( currentDate.year() - 120, currentDate.month(), currentDate.day() ), currentDate)
        self.dateEdit.setStyleSheet(u"color:black;\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.dateEdit, 0, 1, 1, 1)

        self.sexLabel = QLabel(self.widget2)
        self.sexLabel.setObjectName(u"sexLabel")
        self.sexLabel.setStyleSheet(u"color:black")

        self.gridLayout_3.addWidget(self.sexLabel, 1, 0, 1, 1)

        self.sexComboBox = QComboBox(self.widget2)
        self.sexComboBox.addItem("")
        self.sexComboBox.addItem("")
        self.sexComboBox.setObjectName(u"sexComboBox")
        self.sexComboBox.setStyleSheet(u"\n"
"color:black;\n"
"border-radius: 10px;")

        self.gridLayout_3.addWidget(self.sexComboBox, 1, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.signupButton.setText(QCoreApplication.translate("Form", u"Sign up", None))
        self.weightLabel.setText(QCoreApplication.translate("Form", u"Weight:", None))
        self.heightLabel.setText(QCoreApplication.translate("Form", u"Height:", None))
        self.usernameLabel.setText(QCoreApplication.translate("Form", u"Username:", None))
        self.passwordLabel.setText(QCoreApplication.translate("Form", u"Password:", None))
        self.comfirmLabel.setText(QCoreApplication.translate("Form", u"Comfirm Password:", None))
        self.nameLabel.setText(QCoreApplication.translate("Form", u"First Name:", None))
        self.surnameLabel.setText(QCoreApplication.translate("Form", u"Last Name:", None))
        self.birthLabel.setText(QCoreApplication.translate("Form", u"Birth:", None))
        self.sexLabel.setText(QCoreApplication.translate("Form", u"Gender:", None))
        self.sexComboBox.setItemText(0, QCoreApplication.translate("Form", u"Male", None))
        self.sexComboBox.setItemText(1, QCoreApplication.translate("Form", u"Female", None))

    # retranslateUi

