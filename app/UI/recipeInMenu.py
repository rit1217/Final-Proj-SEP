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
        Form.resize(364, 130)
        Form.setStyleSheet(u"background-color:rgb(255, 186, 141);")
        self.recipeLabel = QLabel(Form)
        self.recipeLabel.setObjectName(u"recipeLabel")
        self.recipeLabel.setGeometry(QRect(10, 10, 111, 111))
        
        self.levelLabel = QLabel(Form)
        self.levelLabel.setObjectName(u"levelLabel")
        self.levelLabel.setGeometry(QRect(170, 58, 190, 16))
        self.levelLabel.setStyleSheet(u"color:rgb(80, 80, 80);")
        
        self.creatorLabel = QLabel(Form)
        self.creatorLabel.setObjectName(u"creatorLabel")
        self.creatorLabel.setGeometry(QRect(170, 75, 190, 16))
        self.creatorLabel.setStyleSheet(u"color:rgb(80, 80, 80);")

        self.previewButton = QPushButton(Form)
        self.previewButton.setObjectName(u"previewButton")
        self.previewButton.setGeometry(QRect(170, 100, 91, 31))
        self.previewButton.setStyleSheet(u"QPushButton{background-color:rgb(255, 127, 86);\n"
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
        self.recipenameLabel = QLabel(Form)
        self.recipenameLabel.setObjectName(u"recipenameLabel")
        self.recipenameLabel.setGeometry(QRect(170, 0, 180, 41))

        self.ratingLabel = QLabel(Form)
        self.ratingLabel.setObjectName(u"recipeLabel")
        self.ratingLabel.setGeometry(QRect(170, 40, 111, 16))

        self.recipenameLabel.setStyleSheet(u"color:black;")
        self.recipeLabel.setWordWrap( True )
        self.ratingLabel.setStyleSheet( u"color:blue;")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(357, 7, 3, 120))
        self.widget.setStyleSheet(u"background-color:rgb(255, 127, 86)")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.recipeLabel.setText("")
        self.ratingLabel.setText(QCoreApplication.translate("Form", u"Rating: ", None))
        self.levelLabel.setText(QCoreApplication.translate("Form", u"Level:", None))
        self.creatorLabel.setText(QCoreApplication.translate("Form", u"Created by:", None))
        self.previewButton.setText(QCoreApplication.translate("Form", u"View ", None))
        self.recipenameLabel.setText(QCoreApplication.translate("Form", u"Recipe:Name", None))
    # retranslateUi

