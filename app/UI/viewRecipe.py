 

################################################################################
## Form generated from reading UI file 'recipe1.ui'
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
        Form.resize(690, 545)
        font = QFont()
        font.setPointSize(14)
        Form.setFont(font)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"background-color: rgb(255, 172, 129);\n"
"")
        self.picture_label = QLabel(Form)
        self.picture_label.setObjectName(u"picture_label")
        self.picture_label.setGeometry(QRect(30, 70, 201, 241))
        self.picture_label.setAutoFillBackground(False)
        self.picture_label.setStyleSheet(u"background-color: rgb(255, 223, 202);\n"
"border-radius: 15px;")
        self.picture_label.setPixmap(QPixmap(u"app/UI/food1.png"))
        self.picture_label.setAlignment(Qt.AlignCenter)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(260, 40, 420, 481))
        self.widget.setStyleSheet(u"background-color: rgb(255, 223, 202);\n"
"border-radius: 15px;")
        self.inCal_label = QLabel(self.widget)
        self.inCal_label.setObjectName(u"inCal_label")
        self.inCal_label.setGeometry(QRect(90, 110, 100, 20))
        self.inCal_label.setFont(font)
        self.inCal_label.setLayoutDirection(Qt.LeftToRight)
        self.inCal_label.setStyleSheet(u"background-color: rgb(255, 223, 202);")
        self.inCal_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.name_label = QLabel(self.widget)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(20, 20, 340, 41))
        font1 = QFont()
        font1.setPointSize(24)
        self.name_label.setFont(font1)
        self.name_label.setLayoutDirection(Qt.LeftToRight)
        self.name_label.setStyleSheet(u"background-color: rgb(255, 125, 33);")
        self.name_label.setAlignment(Qt.AlignCenter)
        self.ingredient_label = QLabel(self.widget)
        self.ingredient_label.setObjectName(u"ingredient_label")
        self.ingredient_label.setGeometry(QRect(10, 140, 71, 20))
        self.ingredient_label.setFont(font)
        self.ingredient_label.setStyleSheet(u"background-color: rgb(255, 223, 202);")
        self.ingredient_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.inLevel_label = QLabel(self.widget)
        self.inLevel_label.setObjectName(u"inLevel_label")
        self.inLevel_label.setGeometry(QRect(90, 80, 120, 16))
        self.inLevel_label.setFont(font)
        self.inLevel_label.setStyleSheet(u"background-color: rgb(255, 223, 202);")
        self.level_label = QLabel(self.widget)
        self.level_label.setObjectName(u"level_label")
        self.level_label.setGeometry(QRect(20, 80, 61, 20))
        self.level_label.setFont(font)
        self.level_label.setStyleSheet(u"background-color: rgb(255, 223, 202);")
        self.level_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.cal_label = QLabel(self.widget)
        self.cal_label.setObjectName(u"cal_label")
        self.cal_label.setGeometry(QRect(20, 110, 61, 20))
        self.cal_label.setFont(font)
        self.cal_label.setStyleSheet(u"background-color: rgb(255, 223, 202);")
        self.cal_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(90, 140, 310, 110))
        self.scrollArea.setWidgetResizable(True)
        # self.scrollAreaWidgetContents = QWidget()
        # self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        # self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 360, 109))
        # self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        # self.verticalLayout.setObjectName(u"verticalLayout")
        self.ingredients_listWidget = QListWidget(self.scrollArea)
        self.ingredients_listWidget.setObjectName(u"ingredients_listWidget")
        self.ingredients_listWidget.setGeometry(QRect(0, 0, 310, 109))
        self.ingredients_listWidget.setStyleSheet(u"background-color: rgb(255, 223, 202);\n"
        "color: black;")
        # self.ingredients_label = QLabel(self.scrollAreaWidgetContents)
        # self.ingredients_label.setObjectName(u"ingredients_label")
        # self.ingredients_label.setMinimumSize(QSize(0, 85))
        # self.ingredients_label.setMaximumSize(QSize(315, 16777215))
        # self.ingredients_label.setWordWrap(True)
        # self.verticalLayout.addWidget(self.ingredients_label)

        # self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.instruction_label = QLabel(self.widget)
        self.instruction_label.setObjectName(u"instruction_label")
        self.instruction_label.setGeometry(QRect(0, 260, 81, 20))
        self.instruction_label.setFont(font)
        self.instruction_label.setStyleSheet(u"background-color: rgb(255, 223, 202);")
        self.instruction_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.scrollArea_2 = QScrollArea(self.widget)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(90, 260, 310, 201))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 310, 219))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.recipe_label = QLabel(self.scrollAreaWidgetContents_2)
        self.recipe_label.setObjectName(u"recipe_label")
        self.recipe_label.setMinimumSize(QSize(0,100))
        self.recipe_label.setMaximumSize(QSize(225, 16777215))
        self.recipe_label.setStyleSheet("color: #ff9300")
        self.verticalLayout_2.addWidget(self.recipe_label)
        

        
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.creator_label = QLabel(Form)
        self.creator_label.setObjectName(u"creator_label")
        self.creator_label.setGeometry(QRect(20, 340, 220, 25))
        self.creator_label.setAlignment( Qt.AlignCenter )
        self.creator_label.setStyleSheet(u"background-color: rgb(255, 223, 202);\n"
"border-radius: 15px;")
#         self.rate_spinBox = QSpinBox(Form)
#         self.rate_spinBox.setObjectName(u"rate_spinBox")
#         self.rate_spinBox.setGeometry(QRect(160, 380, 51, 21))
#         self.rate_spinBox.setFont(font)
#         self.rate_spinBox.setStyleSheet(u"background-color: rgb(255, 223, 202);")
#         self.rate_spinBox.setMinimum(1)
#         self.rate_spinBox.setMaximum(5)
#         self.rating_label = QLabel(Form)
#         self.rating_label.setObjectName(u"rating_label")
#         self.rating_label.setGeometry(QRect(40, 380, 111, 21))
#         self.rating_label.setStyleSheet(u"background-color: rgb(255, 223, 202);\n"
# "border-radius: 15px;")
        self.comment_label = QLabel(Form)
        self.comment_label.setObjectName(u"comment_label")
        self.comment_label.setGeometry(QRect(20, 380, 81, 21))
        self.comment_label.setStyleSheet(u"background-color: rgb(255, 223, 202);")
        self.comment_lineEdit = QLineEdit(Form)
        self.comment_lineEdit.setObjectName(u"commet_lineEdit")
        self.comment_lineEdit.setGeometry(QRect(20, 417, 220,80))
        self.comment_lineEdit.setStyleSheet(u"background-color: rgb(255, 223, 202);")
        self.viewcomment = QPushButton(Form)
        self.viewcomment.setObjectName(u"viewcommnet")
        self.viewcomment.setGeometry(QRect(130,507, 111, 31))
        self.viewcomment.setStyleSheet(u"QPushButton{background-color:rgb(255, 127, 86);\n"
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
        self.sendButton = QPushButton(Form)
        self.sendButton.setObjectName(u"sendButton")
        self.sendButton.setGeometry(QRect(20,507, 91, 31))
        self.sendButton.setStyleSheet(u"QPushButton{background-color:rgb(255, 127, 86);\n"
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
        self.widget.raise_()
        self.picture_label.raise_()
        self.creator_label.raise_()
        # self.rate_spinBox.raise_()
        # self.rating_label.raise_()
        self.comment_label.raise_()
        self.comment_lineEdit.raise_()
        self.viewcomment.raise_()
        self.sendButton.raise_()
        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Recipe", None))
        self.picture_label.setText("")
        self.inCal_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ff9300;\">000</span></p></body></html>", None))
        self.name_label.setText(QCoreApplication.translate("Form", u"Name", None))
        self.ingredient_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ff9300;\">Ingredient :</span></p></body></html>", None))
        self.inLevel_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ff9300;\">easy</span></p></body></html>", None))
        self.level_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ff9300;\">Level :</span></p></body></html>", None))
        self.cal_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ff9300;\">Calories :</span></p></body></html>", None))
        # self.ingredients_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ff9300;\"></span></p></body></html>", None))
        self.instruction_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ff9300;\">Instruction :</span></p></body></html>", None))
        self.recipe_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ff9300;\">TextLabel</span></p></body></html>", None))
        self.creator_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt; color:#ff9300;\">Create by : </span></p></body></html>", None))
        # self.rating_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt; color:#ff9300;\">Rate this recipe :</span></p></body></html>", None))
        self.comment_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt; color:#ff9300;\">Comment :</span></p></body></html>", None))
        self.viewcomment.setText(QCoreApplication.translate("Form", u"view comment", None))
        self.sendButton.setText(QCoreApplication.translate("Form", u"send", None))
    # retranslateUi
