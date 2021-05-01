# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainmenu.ui'
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
        Form.resize(557, 453)
        Form.setStyleSheet(u"background-color:rgb(255, 187, 178)")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 40, 201, 51))
        self.widget.setStyleSheet(u"background-color:rgb(255, 186, 141);\n"
"border-radius:20px")
        self.searchButton = QPushButton(self.widget)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(20, 10, 31, 31))
        self.searchButton.setStyleSheet(u"QPushButton{background-color:rgb(255, 127, 86);\n"
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
"}")
        self.searchEdit = QLineEdit(self.widget)
        self.searchEdit.setObjectName(u"searchEdit")
        self.searchEdit.setGeometry(QRect(60, 10, 131, 31))
        self.searchEdit.setStyleSheet(u"QLineEdit{\n"
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
        self.searchEdit.setEchoMode(QLineEdit.Normal)
        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(30, 110, 491, 171))
        self.widget_2.setStyleSheet(u"background-color:rgb(255, 127, 86);\n"
"border-radius:20px")
        self.recipemainScrollArea = QScrollArea(self.widget_2)
        self.recipemainScrollArea.setObjectName(u"recipemainScrollArea")
        self.recipemainScrollArea.setGeometry(QRect(20, 20, 451, 151))
        self.recipemainScrollArea.setStyleSheet(u"background-color:rgb(255, 186, 141);\n"
"border-radius:20px;")
        self.recipemainScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 451, 151))
        self.recipemainScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.recipepicLabel = QLabel(Form)
        self.recipepicLabel.setObjectName(u"recipepicLabel")
        self.recipepicLabel.setGeometry(QRect(50, 300, 141, 131))
        self.clickcreateButton = QPushButton(Form)
        self.clickcreateButton.setObjectName(u"clickcreateButton")
        self.clickcreateButton.setGeometry(QRect(260, 370, 113, 32))
        self.clickcreateButton.setStyleSheet(u"QPushButton{background-color:rgb(255, 127, 86);\n"
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
"}")
        self.createLabel = QLabel(Form)
        self.createLabel.setObjectName(u"createLabel")
        self.createLabel.setGeometry(QRect(230, 310, 181, 41))
        self.createLabel.setStyleSheet(u"background-color:rgb(255, 127, 86);\n"
"border-radius:20px;\n"
"color:black;")
        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(310, 40, 201, 51))
        self.widget_3.setStyleSheet(u"background-color:rgb(255, 186, 141);\n"
"border-radius:20px")
        self.profileLabel = QLabel(self.widget_3)
        self.profileLabel.setObjectName(u"profileLabel")
        self.profileLabel.setGeometry(QRect(20, 20, 60, 16))
        self.profileLabel.setStyleSheet(u"color:black")
        self.clickprofileButton = QPushButton(self.widget_3)
        self.clickprofileButton.setObjectName(u"clickprofileButton")
        self.clickprofileButton.setGeometry(QRect(80, 11, 91, 31))
        self.clickprofileButton.setStyleSheet(u"QPushButton{background-color:rgb(255, 127, 86);\n"
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
"}")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.searchButton.setText("")
        self.searchEdit.setInputMask("")
        self.searchEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Search?", None))
        self.recipepicLabel.setText(QCoreApplication.translate("Form", u"         TextLabel", None))
        self.clickcreateButton.setText(QCoreApplication.translate("Form", u"Create", None))
        self.createLabel.setText(QCoreApplication.translate("Form", u"     Create your own recipe", None))
        self.profileLabel.setText(QCoreApplication.translate("Form", u"Profile:", None))
        self.clickprofileButton.setText(QCoreApplication.translate("Form", u"Click", None))
    # retranslateUi

