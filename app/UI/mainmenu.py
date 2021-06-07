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
        Form.resize(557, 790)
        Form.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 10, 291, 150))
        self.widget.setStyleSheet(u"background-color:rgb(255, 186, 141);\n"
"border-radius:20px")
        self.searchButton = QPushButton(self.widget)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(20, 10, 31, 31))
        self.searchButton.setStyleSheet(u"QPushButton{background-color:rgb(255, 127, 86);\n"
"border:none;\n"
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
        self.searchEdit.setGeometry(QRect(90, 10, 131, 31))
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
        self.serchbyLabel = QLabel(self.widget)
        self.serchbyLabel.setObjectName(u"serchbyLabel")
        self.serchbyLabel.setGeometry(QRect(10, 50, 71, 21))
        self.serchbyLabel.setStyleSheet(u"color:black")
        self.widget1 = QWidget(self.widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(90, 50, 134, 88))
        self.verticalLayout =QVBoxLayout(self.widget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.nameRadioButton = QRadioButton(self.widget1)
        self.nameRadioButton.setObjectName(u"nameRadioButton")
        self.nameRadioButton.setStyleSheet(u"color:black")

        self.verticalLayout.addWidget(self.nameRadioButton)

        self.maximumRadioButton = QRadioButton(self.widget1)
        self.maximumRadioButton.setObjectName(u"maximumRadioButton")
        self.maximumRadioButton.setStyleSheet(u"color:black")

        self.verticalLayout.addWidget(self.maximumRadioButton)

        self.minimumRadioButton = QRadioButton(self.widget1)
        self.minimumRadioButton.setObjectName(u"minimumRadioButton")
        self.minimumRadioButton.setStyleSheet(u"color:black")

        self.verticalLayout.addWidget(self.minimumRadioButton)

        self.creatorRadioButton = QRadioButton(self.widget1)
        self.creatorRadioButton.setObjectName(u"creatorRadioButton")
        self.creatorRadioButton.setStyleSheet(u"color:black")

        self.verticalLayout.addWidget(self.creatorRadioButton)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(30, 170, 490, 480))
        self.widget_2.setStyleSheet(u"background-color:rgb(255, 127, 86);\n"
"border-radius:20px")
        self.recipemainScrollArea = QScrollArea(self.widget_2)
        self.recipemainScrollArea.setObjectName(u"recipemainScrollArea")
        self.recipemainScrollArea.setGeometry(QRect(10, 20, 470, 440))
        self.recipemainScrollArea.setStyleSheet(u"background-color:rgb(255, 186, 141);\n"
"border-radius:20px;")
        self.recipemainScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 451, 150))
        self.recipemainScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.recipepicLabel = QLabel(Form)
        self.recipepicLabel.setObjectName(u"recipepicLabel")
        self.recipepicLabel.setGeometry(QRect(50, 650, 141, 131))
        self.clickcreateButton = QPushButton(Form)
        self.clickcreateButton.setObjectName(u"clickcreateButton")
        self.clickcreateButton.setGeometry(QRect(260, 730, 113, 32))
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

        self.refreshButton = QPushButton(Form)
        self.refreshButton.setObjectName(u"refreshButton")
        self.refreshButton.setGeometry(QRect(400, 730, 113, 32))
        self.refreshButton.setStyleSheet(u"QPushButton{background-color:rgb(255, 127, 86);\n"
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
        self.createLabel.setGeometry(QRect(300, 670, 181, 41))
        self.createLabel.setStyleSheet(u"background-color:rgb(255, 127, 86);\n"
"border-radius:20px;\n"
"color:black;")
        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(350, 40, 151, 51))
        self.widget_3.setStyleSheet(u"background-color:rgb(255, 186, 141);\n"
"border-radius:20px")
        #self.profileLabel = QLabel(self.widget_3)
        #self.profileLabel.setObjectName(u"profileLabel")
        #self.profileLabel.setGeometry(QRect(20, 20, 60, 16))
        #self.profileLabel.setStyleSheet(u"color:black")
        self.clickprofileButton = QPushButton(self.widget_3)
        self.clickprofileButton.setObjectName(u"clickprofileButton")
        self.clickprofileButton.setGeometry(QRect(30, 11, 91, 31))
        self.clickprofileButton.setStyleSheet(u"QPushButton{background-color:rgb(255, 127, 86);\n"
"border:none;\n"
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
        self.serchbyLabel.setText(QCoreApplication.translate("Form", u"Search by:", None))
        self.nameRadioButton.setText(QCoreApplication.translate("Form", u"Name", None))
        self.maximumRadioButton.setText(QCoreApplication.translate("Form", u"Maximum Calories", None))
        self.minimumRadioButton.setText(QCoreApplication.translate("Form", u"Minimum Calories", None))
        self.creatorRadioButton.setText(QCoreApplication.translate("Form", u"Creator    ", None))
        self.recipepicLabel.setText(QCoreApplication.translate("Form", u"         TextLabel", None))
        self.clickcreateButton.setText(QCoreApplication.translate("Form", u"Create", None))
        self.createLabel.setText(QCoreApplication.translate("Form", u"     Create your own recipe", None))
        #self.profileLabel.setText(QCoreApplication.translate("Form", u"Profile:", None))
        self.clickprofileButton.setText(QCoreApplication.translate("Form", u"Profile", None))
        self.refreshButton.setText(QCoreApplication.translate("Form", u"Refresh", None))

    # retranslateUi


