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
        Form.setStyleSheet(u"background-color:rgb(255, 187, 178);")
        self.recipeLabel = QLabel(Form)
        self.recipeLabel.setObjectName(u"recipeLabel")
        self.recipeLabel.setGeometry(QRect(10, 0, 151, 131))
        self.levelLabel = QLabel(Form)
        self.levelLabel.setObjectName(u"levelLabel")
        self.levelLabel.setGeometry(QRect(210, 60, 60, 16))
        self.levelLabel.setStyleSheet(u"color: black;")

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(170, 0, 21, 141))
        self.widget.setStyleSheet(u"background-color:rgb(255, 187, 178);")
        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(290, 0, 21, 141))
        self.widget_2.setStyleSheet(u"background-color:rgb(255, 187, 178);")
        self.previewLabel = QPushButton(Form)
        self.previewLabel.setObjectName(u"previewLabel")
        self.previewLabel.setGeometry(QRect(320, 20, 113, 32))
        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(440, 0, 3, 141))
        self.widget_3.setStyleSheet(u"background-color:rgb(255, 127, 86);")
        self.previewLabel.setStyleSheet(u"QPushButton{background-color:rgb(255, 127, 86);\n"
"border:none;\n"
"border-radius: 10px;\n"

"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(255, 99, 0)\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(255, 43, 14)\n"
"}")
        self.editLabel = QPushButton(Form)
        self.editLabel.setObjectName(u"editLabel")
        self.editLabel.setGeometry(QRect(320, 80, 113, 32))
        self.editLabel.setStyleSheet(u"QPushButton{background-color:rgb(255, 127, 86);\n"
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
        self.levelLabel.setText(QCoreApplication.translate("Form", u"Level:", None))
        self.previewLabel.setText(QCoreApplication.translate("Form", u"View recipe", None))
        self.editLabel.setText(QCoreApplication.translate("Form", u"Edit", None))
    # retranslateUi
