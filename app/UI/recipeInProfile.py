# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recipe.ui'
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
        Form.resize(445, 330)
        Form.setStyleSheet(u"background-color:rgb(255, 186, 141);")
        self.recipeLabel = QLabel(Form)
        self.recipeLabel.setObjectName(u"recipeLabel")
        self.recipeLabel.setGeometry(QRect(0, 0, 151, 151))

        self.recipenameLabel = QLabel(Form)
        self.recipenameLabel.setObjectName(u"recipenameLabel")
        self.recipenameLabel.setGeometry(QRect(200, 5, 180, 50))
        self.recipenameLabel.setStyleSheet(u"color: black;")
        
        self.ratingLabel = QLabel(Form)
        self.ratingLabel.setObjectName(u"ratingLabel")
        self.ratingLabel.setGeometry(QRect(200, 60, 180, 20))
        self.ratingLabel.setStyleSheet(u"color: blue;")

        self.levelLabel = QLabel(Form)
        self.levelLabel.setObjectName(u"levelLabel")
        self.levelLabel.setGeometry(QRect(200, 85, 180, 20))
        self.levelLabel.setStyleSheet(u"color: black;")

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(170, 0, 21, 141))
        self.widget.setStyleSheet(u"background-color:rgb(255, 186, 141);")
        self.previewButton = QPushButton(Form)
        self.previewButton.setObjectName(u"previewButton")
        self.previewButton.setGeometry(QRect(200, 115, 90, 32))
        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(0, 160, 500, 3))
        self.widget_3.setStyleSheet(u"background-color:rgb(255, 186, 141);")
        self.previewButton.setStyleSheet(u"QPushButton{background-color:rgb(255, 127, 86);\n"
"border:none;\n"
"border-radius: 10px;\n"

"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(255, 99, 0)\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(255, 43, 14)\n"
"}")
        self.editButton = QPushButton(Form)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setGeometry(QRect(300, 115, 90, 32))
        self.editButton.setStyleSheet(u"QPushButton{background-color:rgb(255, 127, 86);\n"
"border:none;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(255, 99, 0)\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(255, 43, 14)\n"
"}")
        self.deleteButton = QPushButton(Form)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setGeometry(QRect(400, 115, 90, 32))
        self.deleteButton.setStyleSheet(u"QPushButton{background-color:rgb(255, 127, 86);\n"
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
        self.recipeLabel.setText("")
        self.recipenameLabel.setText(QCoreApplication.translate("Form", u"Recipe: Name", None))
        self.levelLabel.setText(QCoreApplication.translate("Form", u"Level:", None))
        self.previewButton.setText(QCoreApplication.translate("Form", u"View recipe", None))
        self.editButton.setText(QCoreApplication.translate("Form", u"Edit", None))
        self.deleteButton.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.ratingLabel.setText(QCoreApplication.translate("Form", u"Rating:", None))

    # retranslateUi

