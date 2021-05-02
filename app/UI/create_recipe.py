# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_recipe.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import pic_create_recipe_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(544, 471)
        Form.setStyleSheet(u"background-color: rgb(254, 173, 129);\n"
" border-radius:10px;")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 60, 58, 16))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(260, 90, 51, 16))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 200, 81, 16))
        self.ingSearch_lineEdit = QLineEdit(Form)
        self.ingSearch_lineEdit.setObjectName(u"ingSearch_lineEdit")
        self.ingSearch_lineEdit.setGeometry(QRect(120, 200, 151, 21))
        self.ingSearch_lineEdit.setStyleSheet(u"background-color: rgb(255, 223, 202);")
        self.search_pushButton = QPushButton(Form)
        self.search_pushButton.setObjectName(u"search_pushButton")
        self.search_pushButton.setGeometry(QRect(270, 200, 21, 21))
        self.search_pushButton.setStyleSheet(u"image: url(:/newPrefix/searchicon.png);\n"
"background-color: rgb(255, 255, 255);")
        self.pic_pushButton = QPushButton(Form)
        self.pic_pushButton.setObjectName(u"pic_pushButton")
        self.pic_pushButton.setGeometry(QRect(40, 60, 191, 111))
        self.pic_pushButton.setStyleSheet(u"background-color: rgb(251, 124, 0);")
        self.name_lineEdit = QLineEdit(Form)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setGeometry(QRect(320, 60, 113, 21))
        self.name_lineEdit.setStyleSheet(u"background-color: rgb(255, 223, 202);")
        self.level_comboBox = QComboBox(Form)
        self.level_comboBox.setObjectName(u"level_comboBox")
        self.level_comboBox.setGeometry(QRect(320, 90, 111, 21))
        self.level_comboBox.setStyleSheet(u"background-color: rgb(255, 223, 202);")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(310, 200, 58, 16))
        self.amount_lineEdit = QLineEdit(Form)
        self.amount_lineEdit.setObjectName(u"amount_lineEdit")
        self.amount_lineEdit.setGeometry(QRect(370, 200, 41, 21))
        self.amount_lineEdit.setStyleSheet(u"background-color: rgb(255, 223, 202);")
        self.add_pushButton = QPushButton(Form)
        self.add_pushButton.setObjectName(u"add_pushButton")
        self.add_pushButton.setGeometry(QRect(430, 200, 51, 21))
        self.add_pushButton.setStyleSheet(u"background-color: rgb(252, 123, 0);")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 240, 81, 16))
        self.instruction_textEdit = QTextEdit(Form)
        self.instruction_textEdit.setObjectName(u"instruction_textEdit")
        self.instruction_textEdit.setGeometry(QRect(120, 250, 361, 141))
        self.instruction_textEdit.setStyleSheet(u"background-color: rgb(255, 223, 202);")
        self.save_pushButton = QPushButton(Form)
        self.save_pushButton.setObjectName(u"save_pushButton")
        self.save_pushButton.setGeometry(QRect(180, 410, 81, 31))
        self.save_pushButton.setStyleSheet(u"background-color: rgb(250, 125, 0);")
        self.cancel_pushButton = QPushButton(Form)
        self.cancel_pushButton.setObjectName(u"cancel_pushButton")
        self.cancel_pushButton.setGeometry(QRect(290, 410, 81, 31))
        self.cancel_pushButton.setStyleSheet(u"background-color: rgb(250, 125, 0);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Create Recipe", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt; color:#edecee;\">Name :</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Level :", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Ingredients:", None))
        self.search_pushButton.setText("")
        self.pic_pushButton.setText(QCoreApplication.translate("Form", u"Browser", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Amount :", None))
        self.add_pushButton.setText(QCoreApplication.translate("Form", u"Add", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Intruction :", None))
        self.save_pushButton.setText(QCoreApplication.translate("Form", u"Save", None))
        self.cancel_pushButton.setText(QCoreApplication.translate("Form", u"Cancel", None))
    # retranslateUi

