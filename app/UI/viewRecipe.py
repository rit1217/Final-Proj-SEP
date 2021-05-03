# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recipe1.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# import gade_project_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(647, 545)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"background-color: rgb(255, 172, 129);\n"
"")
        self.picture_label = QLabel(Form)
        self.picture_label.setObjectName(u"picture_label")
        self.picture_label.setGeometry(QRect(30, 50, 201, 241))
        self.picture_label.setAutoFillBackground(False)
        self.picture_label.setStyleSheet(u"background-color: rgb(255, 223, 202);\n"
"border-radius: 15px;")
        self.picture_label.setPixmap(QPixmap(u"app/UI/food1.png"))
        self.picture_label.setAlignment(Qt.AlignCenter)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(260, 40, 361, 481))
        self.widget.setStyleSheet(u"background-color: rgb(255, 223, 202);\n"
"border-radius: 15px;")
        self.cal_label = QLabel(self.widget)
        self.cal_label.setObjectName(u"cal_label")
        self.cal_label.setGeometry(QRect(90, 110, 31, 20))
        font = QFont()
        font.setPointSize(14)
        self.cal_label.setFont(font)
        self.cal_label.setLayoutDirection(Qt.LeftToRight)
        self.cal_label.setStyleSheet(u"background-color: rgb(255, 223, 202);")
        self.cal_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(130, 110, 81, 16))
        self.label_3.setFont(font)
        self.name_label = QLabel(self.widget)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(120, 20, 141, 41))
        font1 = QFont()
        font1.setPointSize(24)
        self.name_label.setFont(font1)
        self.name_label.setLayoutDirection(Qt.LeftToRight)
        self.name_label.setStyleSheet(u"background-color: rgb(255, 125, 33);")
        self.name_label.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 140, 71, 20))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"background-color: rgb(255, 223, 202);")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.level_label = QLabel(self.widget)
        self.level_label.setObjectName(u"level_label")
        self.level_label.setGeometry(QRect(90, 80, 91, 16))
        self.level_label.setFont(font)
        self.level_label.setStyleSheet(u"background-color: rgb(255, 223, 202);")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 80, 61, 20))
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(255, 223, 202);")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 110, 61, 20))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: rgb(255, 223, 202);")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(90, 140, 261, 101))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 246, 109))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ingredients_label = QLabel(self.scrollAreaWidgetContents)
        self.ingredients_label.setObjectName(u"ingredients_label")
        self.ingredients_label.setMinimumSize(QSize(0, 85))
        self.ingredients_label.setMaximumSize(QSize(215, 16777215))
        self.ingredients_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.ingredients_label)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 260, 81, 20))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"background-color: rgb(255, 223, 202);")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.scrollArea_2 = QScrollArea(self.widget)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(90, 260, 261, 201))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 246, 219))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.recipe_label = QLabel(self.scrollAreaWidgetContents_2)
        self.recipe_label.setObjectName(u"recipe_label")
        self.recipe_label.setMinimumSize(QSize(0, 195))
        self.recipe_label.setMaximumSize(QSize(225, 16777215))

        self.verticalLayout_2.addWidget(self.recipe_label)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 310, 71, 21))
        self.label_6.setStyleSheet(u"background-color: rgb(255, 223, 202);\n"
"border-radius: 15px;")
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(110, 310, 101, 21))
        self.label_7.setStyleSheet(u"background-color: rgb(255, 223, 202);")
        self.rate_spinBox = QSpinBox(Form)
        self.rate_spinBox.setObjectName(u"rate_spinBox")
        self.rate_spinBox.setGeometry(QRect(150, 350, 51, 31))
        self.rate_spinBox.setStyleSheet(u"background-color: rgb(255, 223, 202);")
        self.rate_spinBox.setRange(1,5)
        self.widget.raise_()
        self.picture_label.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.rate_spinBox.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Recipe", None))
        self.picture_label.setText("")
        self.cal_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ff9300;\">000</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ff9300;\">Kilocalories</span></p></body></html>", None))
        self.name_label.setText(QCoreApplication.translate("Form", u"Name", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ff9300;\">Ingredient :</span></p></body></html>", None))
        self.level_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ff9300;\">easy</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ff9300;\">Level :</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ff9300;\">Calories :</span></p></body></html>", None))
        self.ingredients_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ff9300;\">TextLabel</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ff9300;\">Instruction :</span></p></body></html>", None))
        self.recipe_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ff9300;\">TextLabel</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt; color:#ff9300;\">Create by : </span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt; color:#ff9300;\"> Username</span></p></body></html>", None))
    # retranslateUi

