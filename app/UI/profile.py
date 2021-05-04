
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Profile.ui'
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
        Form.resize(557, 457)
        Form.setStyleSheet(u"background-color:rgb(255, 187, 178)")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 190, 241, 51))
        self.widget.setStyleSheet(u"background-color:rgb(255, 127, 86);\n"
"border-radius:20px")
        self.usernameLabel = QLabel(self.widget)
        self.usernameLabel.setObjectName(u"usernameLabel")
        self.usernameLabel.setAlignment( Qt.AlignCenter)
        self.usernameLabel.setGeometry(QRect(20, 20, 200, 16))
        font = QFont()
        font.setPointSize(20)
        self.usernameLabel.setFont(font)

        self.usernameLabel.setStyleSheet(u"color:black")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(270, 30, 271, 188))
        self.frame.setStyleSheet(u"background-color:rgb(255, 127, 86);\n"
"border-radius:20px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.nameLabel = QLabel(self.frame)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setStyleSheet(u"color:black")

        self.gridLayout.addWidget(self.nameLabel, 0, 0, 1, 1)

        self.lastnameLabel = QLabel(self.frame)
        self.lastnameLabel.setObjectName(u"lastnameLabel")
        self.lastnameLabel.setStyleSheet(u"color:black")

        self.gridLayout.addWidget(self.lastnameLabel, 1, 0, 1, 1)

        self.dateLabel = QLabel(self.frame)
        self.dateLabel.setObjectName(u"dateLabel")
        self.dateLabel.setStyleSheet(u"color:black")

        self.gridLayout.addWidget(self.dateLabel, 2, 0, 1, 1)

        self.genderLabel = QLabel(self.frame)
        self.genderLabel.setObjectName(u"genderLabel")
        self.genderLabel.setStyleSheet(u"color:black")

        self.gridLayout.addWidget(self.genderLabel, 3, 0, 1, 1)

        self.heightLabel = QLabel(self.frame)
        self.heightLabel.setObjectName(u"heightLabel")
        self.heightLabel.setStyleSheet(u"color:black")

        self.gridLayout.addWidget(self.heightLabel, 4, 0, 1, 1)

        self.weightLabel = QLabel(self.frame)
        self.weightLabel.setObjectName(u"weightLabel")
        self.weightLabel.setStyleSheet(u"color:black")

        self.gridLayout.addWidget(self.weightLabel, 5, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 6, 1)

        self.nameLabel_2 = QLabel(self.frame)
        self.nameLabel_2.setObjectName(u"nameLabel_2")
        self.nameLabel_2.setStyleSheet(u"color:black")

        self.gridLayout_2.addWidget(self.nameLabel_2, 0, 1, 1, 1)

        self.lastnameLabel_2 = QLabel(self.frame)
        self.lastnameLabel_2.setObjectName(u"lastnameLabel_2")
        self.lastnameLabel_2.setStyleSheet(u"color:black")

        self.gridLayout_2.addWidget(self.lastnameLabel_2, 1, 1, 1, 1)

        self.dateLabel_2 = QLabel(self.frame)
        self.dateLabel_2.setObjectName(u"dateLabel_2")
        self.dateLabel_2.setStyleSheet(u"color:black")

        self.gridLayout_2.addWidget(self.dateLabel_2, 2, 1, 1, 1)

        self.genderLabel_2 = QLabel(self.frame)
        self.genderLabel_2.setObjectName(u"genderLabel_2")
        self.genderLabel_2.setStyleSheet(u"color:black")

        self.gridLayout_2.addWidget(self.genderLabel_2, 3, 1, 1, 1)

        self.heightLabel_2 = QLabel(self.frame)
        self.heightLabel_2.setObjectName(u"heightLabel_2")
        self.heightLabel_2.setStyleSheet(u"color:black")

        self.gridLayout_2.addWidget(self.heightLabel_2, 4, 1, 1, 1)

        self.weightLabel_2 = QLabel(self.frame)
        self.weightLabel_2.setObjectName(u"weightLabel_2")
        self.weightLabel_2.setStyleSheet(u"color:black")

        self.gridLayout_2.addWidget(self.weightLabel_2, 5, 1, 1, 1)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(20, 250, 411, 210))
        self.widget_2.setStyleSheet(u"background-color:rgb(255, 127, 86);\n"
"border-radius:15px")
        self.recipeScrollArea = QScrollArea(self.widget_2)
        self.recipeScrollArea.setObjectName(u"recipeScrollArea")
        self.recipeScrollArea.setGeometry(QRect(30, 10, 361, 190))
        self.recipeScrollArea.setStyleSheet(u"background-color:rgb(255, 187, 178);\n"
"border-radius:15px;")
        self.recipeScrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 361, 150))
        self.recipeScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.piclabel = QLabel(Form)
        self.piclabel.setObjectName(u"piclabel")
        self.piclabel.setGeometry(QRect(60, 20, 151, 151))
        self.refreshButton = QPushButton(Form)
        self.refreshButton.setObjectName(u"refreshButton")
        self.refreshButton.setGeometry(QRect(450, 370, 91, 32))
        self.refreshButton.setStyleSheet(u"QPushButton{background-color:rgb(255, 127, 86);\n"
"border:none;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(255, 99, 0)\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(255, 43, 14)\n"
"}")

        self.backButton = QPushButton(Form)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(450, 410, 91, 32))
        self.backButton.setStyleSheet(u"QPushButton{background-color:rgb(255, 127, 86);\n"
"border:none;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(255, 99, 0)\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(255, 43, 14)\n"
"}")

        self.widget_2.raise_()
        self.frame.raise_()
        self.widget.raise_()
        self.piclabel.raise_()
        self.backButton.raise_()
        self.refreshButton.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.usernameLabel.setText(QCoreApplication.translate("Form", u"OOOOOOOOOOOOOO", None))
        self.nameLabel.setText(QCoreApplication.translate("Form", u"Name:", None))
        self.lastnameLabel.setText(QCoreApplication.translate("Form", u"Lastname:", None))
        self.dateLabel.setText(QCoreApplication.translate("Form", u"Date of birth:", None))
        self.genderLabel.setText(QCoreApplication.translate("Form", u"Gender:", None))
        self.heightLabel.setText(QCoreApplication.translate("Form", u"Height:", None))
        self.weightLabel.setText(QCoreApplication.translate("Form", u"Weight:", None))
        self.nameLabel_2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lastnameLabel_2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.dateLabel_2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.genderLabel_2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.heightLabel_2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.weightLabel_2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.backButton.setText(QCoreApplication.translate("Form", u"Back", None))
        self.refreshButton.setText(QCoreApplication.translate("Form", u"Refresh", None))


        self.piclabel.setText("")
    # retranslateUi

