# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profileEdit.ui'
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
        Form.resize(400, 295)
        Form.setStyleSheet(u"background-color: rgb(255, 223, 202);")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 30, 311, 191))
        self.widget.setStyleSheet(u"background-color: rgb(235, 155, 122);")
        self.firstname_label = QLabel(self.widget)
        self.firstname_label.setObjectName(u"firstname_label")
        self.firstname_label.setGeometry(QRect(20, 30, 71, 16))
        self.firstname_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lastname_label = QLabel(self.widget)
        self.lastname_label.setObjectName(u"lastname_label")
        self.lastname_label.setGeometry(QRect(20, 60, 71, 16))
        self.lastname_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gender_label = QLabel(self.widget)
        self.gender_label.setObjectName(u"gender_label")
        self.gender_label.setGeometry(QRect(20, 90, 71, 16))
        self.gender_label.setLayoutDirection(Qt.RightToLeft)
        self.gender_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.height_label = QLabel(self.widget)
        self.height_label.setObjectName(u"height_label")
        self.height_label.setGeometry(QRect(30, 120, 58, 16))
        self.height_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.weight_label = QLabel(self.widget)
        self.weight_label.setObjectName(u"weight_label")
        self.weight_label.setGeometry(QRect(30, 150, 58, 16))
        self.weight_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.firstname_lineEdit = QLineEdit(self.widget)
        self.firstname_lineEdit.setObjectName(u"firstname_lineEdit")
        self.firstname_lineEdit.setGeometry(QRect(110, 30, 151, 21))
        self.firstname_lineEdit.setStyleSheet(u"background-color: rgb(255, 223, 202);")
        self.lastname_lineEdit = QLineEdit(self.widget)
        self.lastname_lineEdit.setObjectName(u"lastname_lineEdit")
        self.lastname_lineEdit.setGeometry(QRect(110, 60, 151, 21))
        self.lastname_lineEdit.setStyleSheet(u"background-color: rgb(255, 223, 202);")

        self.gender_comboBox = QComboBox(self.widget)
        self.gender_comboBox.setObjectName(u"gender_comboBox")
        self.gender_comboBox.setGeometry(QRect(110, 90, 71, 21))
        self.gender_comboBox.setStyleSheet(u"background-color: rgb(255, 223, 202);")
        self.gender_comboBox.addItems(["Female", "Male"])

        self.height_lineEdit = QLineEdit(self.widget)
        self.height_lineEdit.setObjectName(u"height_spinBox")
        self.height_lineEdit.setGeometry(QRect(110, 120, 71, 22))
        self.height_lineEdit.setStyleSheet(u"background-color: rgb(255, 223, 202);\n"
"")
        self.weight_lineEdit = QLineEdit(self.widget)
        self.weight_lineEdit.setObjectName(u"weight_lineEdit")
        self.weight_lineEdit.setGeometry(QRect(110, 150, 71, 22))
        self.weight_lineEdit.setStyleSheet(u"background-color: rgb(255, 223, 202);\n"
"")

        self.cm_label = QLabel(self.widget)
        self.cm_label.setObjectName(u"cm_label")
        self.cm_label.setGeometry(QRect(190, 120, 41, 21))
        self.kg_label = QLabel(self.widget)
        self.kg_label.setObjectName(u"kg_label")
        self.kg_label.setGeometry(QRect(190, 150, 51, 21))
        self.ok_pushButton = QPushButton(Form)
        self.ok_pushButton.setObjectName(u"ok_pushButton")
        self.ok_pushButton.setGeometry(QRect(110, 240, 71, 31))
        self.ok_pushButton.setStyleSheet(u"background-color: rgb(215, 143, 112);")
        self.cancel_pushButton = QPushButton(Form)
        self.cancel_pushButton.setObjectName(u"cancel_pushButton")
        self.cancel_pushButton.setGeometry(QRect(200, 240, 71, 31))
        self.cancel_pushButton.setStyleSheet(u"background-color: rgb(215, 143, 112);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.firstname_label.setText(QCoreApplication.translate("Form", u"Firstname :", None))
        self.lastname_label.setText(QCoreApplication.translate("Form", u"Lastname :", None))
        self.gender_label.setText(QCoreApplication.translate("Form", u"Gender :", None))
        self.height_label.setText(QCoreApplication.translate("Form", u"Height :", None))
        self.weight_label.setText(QCoreApplication.translate("Form", u"Weight :", None))
        self.cm_label.setText(QCoreApplication.translate("Form", u"cm.", None))
        self.kg_label.setText(QCoreApplication.translate("Form", u"kg.", None))
        self.ok_pushButton.setText(QCoreApplication.translate("Form", u"Ok", None))
        self.cancel_pushButton.setText(QCoreApplication.translate("Form", u"Cancel", None))
    # retranslateUi

