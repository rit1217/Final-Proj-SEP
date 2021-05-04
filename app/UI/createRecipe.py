# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Create_recipe.ui'
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
        Form.resize(548, 659)
        Form.setStyleSheet(u"background-color: rgb(254, 173, 129);\n"
" border-radius:10px;")
        self.name_label = QLabel(Form)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(260, 60, 58, 16))
        self.level_label = QLabel(Form)
        self.level_label.setObjectName(u"level_label")
        self.level_label.setGeometry(QRect(260, 90, 51, 16))
        self.ingSearch_label = QLabel(Form)
        self.ingSearch_label.setObjectName(u"ingSearch_label")
        self.ingSearch_label.setGeometry(QRect(40, 140, 81, 16))
        self.ingSearch_lineEdit = QLineEdit(Form)
        self.ingSearch_lineEdit.setObjectName(u"ingSearch_lineEdit")
        self.ingSearch_lineEdit.setGeometry(QRect(120, 140, 151, 21))
        self.ingSearch_lineEdit.setStyleSheet(u"background-color: rgb(255, 223, 202);\n"
        "color: black;")
        self.search_pushButton = QPushButton(Form)
        self.search_pushButton.setObjectName(u"search_pushButton")
        self.search_pushButton.setGeometry(QRect(270, 140, 21, 21))
        self.search_pushButton.setStyleSheet(u"image: url(app/UI/searchicon.png);\n"
"background-color: rgb(255, 255, 255);")
        self.pic_pushButton = QPushButton(Form)
        self.pic_pushButton.setObjectName(u"pic_pushButton")
        self.pic_pushButton.setGeometry(QRect(70, 90, 101, 21))
        self.pic_pushButton.setStyleSheet(u"QPushButton{background-color:rgb(250, 125, 0);\n"
"border:none;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(255, 99, 0)\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(255, 43, 14)\n"
"}")
        self.name_lineEdit = QLineEdit(Form)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setGeometry(QRect(320, 60, 113, 21))
        self.name_lineEdit.setStyleSheet(u"background-color: rgb(255, 223, 202);\n"
        "color: black;")
        self.level_comboBox = QComboBox(Form)
        self.level_comboBox.setObjectName(u"level_comboBox")
        self.level_comboBox.setGeometry(QRect(320, 90, 111, 21))
        self.level_comboBox.setStyleSheet(u"background-color: rgb(255, 223, 202);")
        self.amount_label = QLabel(Form)
        self.amount_label.setObjectName(u"amount_label")
        self.amount_label.setGeometry(QRect(310, 140, 58, 16))
        self.amount_lineEdit = QLineEdit(Form)
        self.amount_lineEdit.setObjectName(u"amount_lineEdit")
        self.amount_lineEdit.setGeometry(QRect(370, 140, 41, 21))
        self.amount_lineEdit.setStyleSheet(u"background-color: rgb(255, 223, 202);\n"
        "color: black;")
        self.add_pushButton = QPushButton(Form)
        self.add_pushButton.setObjectName(u"add_pushButton")
        self.add_pushButton.setGeometry(QRect(430, 140, 51, 21))
        self.add_pushButton.setStyleSheet(u"QPushButton{background-color:rgb(250, 125, 0);\n"
"border:none;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(255, 99, 0)\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(255, 43, 14)\n"
"}")
        self.instruction_label = QLabel(Form)
        self.instruction_label.setObjectName(u"instruction_label")
        self.instruction_label.setGeometry(QRect(40, 440, 81, 16))
        self.instruction_textEdit = QTextEdit(Form)
        self.instruction_textEdit.setObjectName(u"instruction_textEdit")
        self.instruction_textEdit.setGeometry(QRect(120, 440, 361, 141))
        self.instruction_textEdit.setStyleSheet(u"background-color: rgb(255, 223, 202);\n"
        "color: black;")
        self.save_pushButton = QPushButton(Form)
        self.save_pushButton.setObjectName(u"save_pushButton")
        self.save_pushButton.setGeometry(QRect(180, 600, 81, 31))
        self.save_pushButton.setStyleSheet(u"QPushButton{background-color:rgb(250, 125, 0);\n"
"border:none;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(255, 99, 0)\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(255, 43, 14)\n"
"}")
        self.cancel_pushButton = QPushButton(Form)
        self.cancel_pushButton.setObjectName(u"cancel_pushButton")
        self.cancel_pushButton.setGeometry(QRect(290, 600, 81, 31))
        self.cancel_pushButton.setStyleSheet(u"QPushButton{background-color:rgb(250, 125, 0);\n"
"border:none;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(255, 99, 0)\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(255, 43, 14)\n"
"}")
        self.image_label = QLabel(Form)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setGeometry(QRect(80, 60, 81, 16))
        self.searchResult_listWidget = QListWidget(Form)
        self.searchResult_listWidget.setObjectName(u"searchResult_listWidget")
        self.searchResult_listWidget.setGeometry(QRect(120, 170, 361, 115))
        self.searchResult_listWidget.setStyleSheet(u"background-color: rgb(255, 223, 202);\n"
        "color: black;")
        self.ingredient_label = QLabel(Form)
        self.ingredient_label.setObjectName(u"ingredient_label")
        self.ingredient_label.setGeometry(QRect(40, 300, 81, 16))
        self.ingredient_textBrowser = QTextBrowser(Form)
        self.ingredient_textBrowser.setObjectName(u"ingredient_textBrowser")
        self.ingredient_textBrowser.setGeometry(QRect(120, 295, 361, 130))
        self.ingredient_textBrowser.setStyleSheet(u"background-color: rgb(255, 223, 202);\n"
        "color: black;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Create Recipe", None))
        self.name_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt; color:#edecee;\">Name :</span></p></body></html>", None))
        self.level_label.setText(QCoreApplication.translate("Form", u"Level :", None))
        self.ingSearch_label.setText(QCoreApplication.translate("Form", u"Ingredients:", None))
        self.search_pushButton.setText("")
        self.pic_pushButton.setText(QCoreApplication.translate("Form", u"Browser", None))
        self.amount_label.setText(QCoreApplication.translate("Form", u"Amount :", None))
        self.add_pushButton.setText(QCoreApplication.translate("Form", u"Add", None))
        self.instruction_label.setText(QCoreApplication.translate("Form", u"Intruction :", None))
        self.save_pushButton.setText(QCoreApplication.translate("Form", u"Save", None))
        self.cancel_pushButton.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.image_label.setText(QCoreApplication.translate("Form", u"Insert image", None))
        self.ingredient_label.setText(QCoreApplication.translate("Form", u"Ingredients:", None))
    # retranslateUi

