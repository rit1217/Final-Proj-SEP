# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'commentPage.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
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
        Form.resize(643, 420)
        Form.setStyleSheet(u"\n"
"background-color: rgb(255, 223, 202);")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 40, 521, 291))
        self.widget.setStyleSheet(u"background-color: rgb(254, 173, 129);")
        self.relabel = QLabel(self.widget)
        self.relabel.setObjectName(u"relabel")
        self.relabel.setGeometry(QRect(40, 30, 91, 16))
        self.relabel.setStyleSheet(u"font: 13pt \".AppleSystemUIFont\";\n"
"background-color: rgb(254, 173, 129);")
        self.inRecipe_label = QLabel(self.widget)
        self.inRecipe_label.setObjectName(u"inRecipe_label")
        self.inRecipe_label.setGeometry(QRect(140, 30, 251, 16))
        self.inRecipe_label.setStyleSheet(u"background-color: rgb(254, 173, 129);")
        self.creator_label = QLabel(self.widget)
        self.creator_label.setObjectName(u"creator_label")
        self.creator_label.setGeometry(QRect(40, 60, 58, 16))
        self.creator_label.setStyleSheet(u"background-color: rgb(254, 173, 129);")
        self.inCreator_label = QLabel(self.widget)
        self.inCreator_label.setObjectName(u"inCreator_label")
        self.inCreator_label.setGeometry(QRect(110, 60, 111, 16))
        self.inCreator_label.setStyleSheet(u"background-color: rgb(254, 173, 129);")
        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(40, 90, 441, 181))
        self.scrollArea.setWidgetResizable(True)
        self.comment_listWidget = QListWidget(self.scrollArea)
        self.comment_listWidget.setObjectName(u"comment_listWidget")
        self.comment_listWidget.setGeometry(QRect(0, 0, 441, 181))
        self.comment_listWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
        "color: black;")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(470, 360, 112, 31))
        self.pushButton.setStyleSheet(u"background-color: rgb(254, 173, 129);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.relabel.setText(QCoreApplication.translate("Form", u"Recipe name :", None))
        self.inRecipe_label.setText("")
        self.creator_label.setText(QCoreApplication.translate("Form", u"Creator :", None))
        self.inCreator_label.setText("")
        self.pushButton.setText(QCoreApplication.translate("Form", u"Close", None))
    # retranslateUi

