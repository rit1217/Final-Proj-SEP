# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
        Form.resize(455, 305)
        self.widget2 = QWidget(Form)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(30, 30, 401, 251))
        self.widget2.setStyleSheet(u"background-color:rgb(255, 187, 178);\n"
"border-radius:10px;\n"
"")
        self.passwordLabel = QLabel(self.widget2)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setGeometry(QRect(120, 140, 21, 21))
        self.passwordLabel.setStyleSheet(u"color:black;background-color:rgb(255, 187, 178)")
        self.passwordEdit = QLineEdit(self.widget2)
        self.passwordEdit.setObjectName(u"passwordEdit")
        self.passwordEdit.setGeometry(QRect(160, 140, 113, 21))
        self.passwordEdit.setStyleSheet(u"QLineEdit{\n"
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
        self.passwordEdit.setEchoMode(QLineEdit.Password)
        self.passwordEdit.setDragEnabled(True)
        self.passwordEdit.setReadOnly(False)
        self.userEdit = QLineEdit(self.widget2)
        self.userEdit.setObjectName(u"userEdit")
        self.userEdit.setGeometry(QRect(160, 100, 113, 21))
        font = QFont()
        font.setFamily(u".Apple Symbols Fallback")
        self.userEdit.setFont(font)
        self.userEdit.setStyleSheet(u"QLineEdit{\n"
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
        self.usernameLabel = QLabel(self.widget2)
        self.usernameLabel.setObjectName(u"usernameLabel")
        self.usernameLabel.setGeometry(QRect(120, 100, 21, 21))
        font1 = QFont()
        font1.setFamily(u"Noto Sans Kharoshthi")
        self.usernameLabel.setFont(font1)
        self.usernameLabel.setStyleSheet(u"color:black;background-color: rgb(255, 187, 178)")
        self.memberLabel = QLabel(self.widget2)
        self.memberLabel.setObjectName(u"memberLabel")
        self.memberLabel.setGeometry(QRect(120, 20, 181, 51))
        font2 = QFont()
        font2.setFamily(u".Savoye LET CC.")
        font2.setPointSize(21)
        self.memberLabel.setFont(font2)
        self.memberLabel.setStyleSheet(u"QLabel{\n"
"border:5px solid rgb(255, 127, 86);\n"
"background-color:rgb(255, 187, 178);\n"
"padding-right:10px;\n"
"padding-bottom:5px;\n"
"color:black;\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.fork = QLabel(self.widget2)
        self.fork.setObjectName(u"fork")
        self.fork.setGeometry(QRect(320, 70, 60, 91))
        self.fork.setStyleSheet(u"background-color: rgb(255, 187, 178)")
        self.logButton = QPushButton(self.widget2)
        self.logButton.setObjectName(u"logButton")
        self.logButton.setGeometry(QRect(200, 200, 113, 32))
        self.logButton.setStyleSheet(u"QPushButton{background-color:rgb(255, 127, 86);\n"
"border:none;\n"
"padding-top: 5px;\n"
"color:black;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(255, 99, 0)\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(255, 43, 14)\n"
"}\n"
"\n"
"\n"
"")
        self.signButton = QPushButton(self.widget2)
        self.signButton.setObjectName(u"signButton")
        self.signButton.setGeometry(QRect(70, 200, 113, 32))
        self.signButton.setStyleSheet(u"QPushButton{background-color:rgb(255, 127, 86);\n"
"border:none;\n"
"padding-top: 5px;\n"
"color:black;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(255, 99, 0)\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(255, 43, 14)\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.Spoon = QLabel(self.widget2)
        self.Spoon.setObjectName(u"Spoon")
        self.Spoon.setGeometry(QRect(20, 70, 71, 91))
        self.Spoon.setStyleSheet(u"background-color: rgb(255, 187, 178)")
        self.Spoon.setPixmap(QPixmap(u":/newPrefix/spoon.png"))
        self.Spoon.setScaledContents(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.passwordLabel.setText("")
        self.passwordEdit.setPlaceholderText(QCoreApplication.translate("Form", u"password", None))
        self.userEdit.setPlaceholderText(QCoreApplication.translate("Form", u"username", None))
        self.usernameLabel.setText("")
        self.memberLabel.setText(QCoreApplication.translate("Form", u"   Member Login", None))
        self.fork.setText("")
        self.logButton.setText(QCoreApplication.translate("Form", u"Log in", None))
        self.signButton.setText(QCoreApplication.translate("Form", u"Sign up", None))
        self.Spoon.setText("")
    # retranslateUi
