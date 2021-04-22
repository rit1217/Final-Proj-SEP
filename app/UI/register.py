# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Register.ui'
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
        Form.resize(455, 284)
        Form.setStyleSheet(u"background-color: rgb(255, 136, 38)")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 30, 369, 238))
        self.widget.setStyleSheet(u"border-radius:10px;\n"
"background-color:rgb(255, 187, 178);\n"
"")
        self.signupButton = QPushButton(self.widget)
        self.signupButton.setObjectName(u"signupButton")
        self.signupButton.setGeometry(QRect(100, 210, 151, 22))
        self.signupButton.setStyleSheet(u"QPushButton{background-color:rgb(255, 127, 86);\n"
"border:none;\n"
"padding-top: 6px;\n"
"color:black;\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(255, 99, 0)\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(255, 43, 14)\n"
"}")
        self.surnameLabel = QLabel(self.widget)
        self.surnameLabel.setObjectName(u"surnameLabel")
        self.surnameLabel.setGeometry(QRect(12, 108, 55, 16))
        self.surnameLabel.setStyleSheet(u"color:black")
        self.nameLabel = QLabel(self.widget)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setGeometry(QRect(12, 76, 36, 16))
        self.nameLabel.setStyleSheet(u"color:black")
        self.nameLineEdit = QLineEdit(self.widget)
        self.nameLineEdit.setObjectName(u"nameLineEdit")
        self.nameLineEdit.setGeometry(QRect(88, 76, 261, 22))
        self.nameLineEdit.setStyleSheet(u"QLineEdit{\n"
"border:2px solid rgb(255, 201, 195);\n"
"color:black;\n"
"border-radius:10px;\n"
"background-color: rgb(255, 187, 178);\n"
"}\n"
"QLineEdit:hover{\n"
"  border:2px solid  rgb(255, 169, 93)\n"
"}\n"
"QLineEdit:focus{\n"
"  border:2px solid  rgb(255, 169, 93)\n"
"}")
        self.sexLabel = QLabel(self.widget)
        self.sexLabel.setObjectName(u"sexLabel")
        self.sexLabel.setGeometry(QRect(12, 172, 23, 16))
        self.sexLabel.setStyleSheet(u"color:black")
        self.birthLabel = QLabel(self.widget)
        self.birthLabel.setObjectName(u"birthLabel")
        self.birthLabel.setGeometry(QRect(12, 140, 30, 16))
        self.birthLabel.setStyleSheet(u"color:black")
        self.passwordLabel = QLabel(self.widget)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setGeometry(QRect(12, 44, 60, 16))
        self.passwordLabel.setStyleSheet(u"color:black")
        self.birthLineEdit = QLineEdit(self.widget)
        self.birthLineEdit.setObjectName(u"birthLineEdit")
        self.birthLineEdit.setGeometry(QRect(88, 140, 91, 22))
        self.birthLineEdit.setStyleSheet(u"QLineEdit{\n"
"border:2px solid rgb(255, 201, 195);\n"
"color:black;\n"
"border-radius:10px;\n"
"background-color: rgb(255, 187, 178);\n"
"padding-left:40px;\n"
"}\n"
"QLineEdit:hover{\n"
"  border:2px solid  rgb(255, 169, 93)\n"
"}\n"
"QLineEdit:focus{\n"
"  border:2px solid  rgb(255, 169, 93)\n"
"}")
        self.usernameLabel = QLabel(self.widget)
        self.usernameLabel.setObjectName(u"usernameLabel")
        self.usernameLabel.setGeometry(QRect(12, 12, 62, 16))
        self.usernameLabel.setStyleSheet(u"color:black")
        self.passwordLineEdit = QLineEdit(self.widget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setGeometry(QRect(88, 44, 261, 22))
        self.passwordLineEdit.setStyleSheet(u"QLineEdit{\n"
"border:2px solid rgb(255, 201, 195);\n"
"color:black;\n"
"border-radius:10px;\n"
"background-color: rgb(255, 187, 178);\n"
"}\n"
"QLineEdit:hover{\n"
"  border:2px solid  rgb(255, 169, 93)\n"
"}\n"
"QLineEdit:focus{\n"
"  border:2px solid  rgb(255, 169, 93)\n"
"}")
        self.usernameLineEdit = QLineEdit(self.widget)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")
        self.usernameLineEdit.setGeometry(QRect(88, 12, 261, 22))
        self.usernameLineEdit.setStyleSheet(u"QLineEdit{\n"
"border:2px solid rgb(255, 201, 195);\n"
"color:black;\n"
"border-radius:10px;\n"
"background-color: rgb(255, 187, 178);\n"
"}\n"
"QLineEdit:hover{\n"
"  border:2px solid  rgb(255, 169, 93)\n"
"}\n"
"QLineEdit:focus{\n"
"  border:2px solid  rgb(255, 169, 93)\n"
"}")
        self.surnameLineEdit = QLineEdit(self.widget)
        self.surnameLineEdit.setObjectName(u"surnameLineEdit")
        self.surnameLineEdit.setGeometry(QRect(88, 108, 261, 22))
        self.surnameLineEdit.setStyleSheet(u"QLineEdit{\n"
"border:2px solid rgb(255, 201, 195);\n"
"color:black;\n"
"border-radius:10px;\n"
"background-color: rgb(255, 187, 178);\n"
"}\n"
"QLineEdit:hover{\n"
"  border:2px solid  rgb(255, 169, 93)\n"
"}\n"
"QLineEdit:focus{\n"
"  border:2px solid  rgb(255, 169, 93)\n"
"}")
        self.sexCmboBox = QComboBox(self.widget)
        self.sexCmboBox.addItem("")
        self.sexCmboBox.addItem("")
        self.sexCmboBox.addItem("")
        self.sexCmboBox.setObjectName(u"sexCmboBox")
        self.sexCmboBox.setGeometry(QRect(88, 172, 91, 18))
        self.sexCmboBox.setStyleSheet(u"\n"
"color:black;\n"
"border-radius: 10px;")
        self.layoutWidget = QWidget(self.widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(190, 140, 161, 48))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.weightLabel = QLabel(self.layoutWidget)
        self.weightLabel.setObjectName(u"weightLabel")
        self.weightLabel.setStyleSheet(u"color:black")

        self.gridLayout.addWidget(self.weightLabel, 0, 0, 1, 1)

        self.weightComboBox = QComboBox(self.layoutWidget)
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.addItem("")
        self.weightComboBox.setObjectName(u"weightComboBox")
        self.weightComboBox.setStyleSheet(u"color:black;\n"
"")

        self.gridLayout.addWidget(self.weightComboBox, 0, 1, 1, 1)

        self.heightLabel = QLabel(self.layoutWidget)
        self.heightLabel.setObjectName(u"heightLabel")
        self.heightLabel.setStyleSheet(u"color:black")

        self.gridLayout.addWidget(self.heightLabel, 1, 0, 1, 1)

        self.heightComboBox = QComboBox(self.layoutWidget)
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.addItem("")
        self.heightComboBox.setObjectName(u"heightComboBox")
        self.heightComboBox.setStyleSheet(u"color:black\n"
"\n"
"")

        self.gridLayout.addWidget(self.heightComboBox, 1, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.signupButton.setText(QCoreApplication.translate("Form", u"Sign up", None))
        self.surnameLabel.setText(QCoreApplication.translate("Form", u"Surname", None))
        self.nameLabel.setText(QCoreApplication.translate("Form", u"Name", None))
        self.sexLabel.setText(QCoreApplication.translate("Form", u"Sex", None))
        self.birthLabel.setText(QCoreApplication.translate("Form", u"Birth", None))
        self.passwordLabel.setText(QCoreApplication.translate("Form", u"Password", None))
        self.usernameLabel.setText(QCoreApplication.translate("Form", u"Username", None))
        self.sexCmboBox.setItemText(0, QCoreApplication.translate("Form", u"Male", None))
        self.sexCmboBox.setItemText(1, QCoreApplication.translate("Form", u"Female", None))
        self.sexCmboBox.setItemText(2, QCoreApplication.translate("Form", u"Other", None))

        self.weightLabel.setText(QCoreApplication.translate("Form", u"Weight", None))
        self.weightComboBox.setItemText(0, QCoreApplication.translate("Form", u"30", None))
        self.weightComboBox.setItemText(1, QCoreApplication.translate("Form", u"31", None))
        self.weightComboBox.setItemText(2, QCoreApplication.translate("Form", u"32", None))
        self.weightComboBox.setItemText(3, QCoreApplication.translate("Form", u"33", None))
        self.weightComboBox.setItemText(4, QCoreApplication.translate("Form", u"34", None))
        self.weightComboBox.setItemText(5, QCoreApplication.translate("Form", u"35", None))
        self.weightComboBox.setItemText(6, QCoreApplication.translate("Form", u"36", None))
        self.weightComboBox.setItemText(7, QCoreApplication.translate("Form", u"37", None))
        self.weightComboBox.setItemText(8, QCoreApplication.translate("Form", u"38", None))
        self.weightComboBox.setItemText(9, QCoreApplication.translate("Form", u"39", None))
        self.weightComboBox.setItemText(10, QCoreApplication.translate("Form", u"40", None))
        self.weightComboBox.setItemText(11, QCoreApplication.translate("Form", u"41", None))
        self.weightComboBox.setItemText(12, QCoreApplication.translate("Form", u"42", None))
        self.weightComboBox.setItemText(13, QCoreApplication.translate("Form", u"43", None))
        self.weightComboBox.setItemText(14, QCoreApplication.translate("Form", u"44", None))
        self.weightComboBox.setItemText(15, QCoreApplication.translate("Form", u"45", None))
        self.weightComboBox.setItemText(16, QCoreApplication.translate("Form", u"46", None))
        self.weightComboBox.setItemText(17, QCoreApplication.translate("Form", u"47", None))
        self.weightComboBox.setItemText(18, QCoreApplication.translate("Form", u"48", None))
        self.weightComboBox.setItemText(19, QCoreApplication.translate("Form", u"49", None))
        self.weightComboBox.setItemText(20, QCoreApplication.translate("Form", u"50", None))
        self.weightComboBox.setItemText(21, QCoreApplication.translate("Form", u"51", None))
        self.weightComboBox.setItemText(22, QCoreApplication.translate("Form", u"52", None))
        self.weightComboBox.setItemText(23, QCoreApplication.translate("Form", u"53", None))
        self.weightComboBox.setItemText(24, QCoreApplication.translate("Form", u"54", None))
        self.weightComboBox.setItemText(25, QCoreApplication.translate("Form", u"55", None))
        self.weightComboBox.setItemText(26, QCoreApplication.translate("Form", u"56", None))
        self.weightComboBox.setItemText(27, QCoreApplication.translate("Form", u"57", None))
        self.weightComboBox.setItemText(28, QCoreApplication.translate("Form", u"58", None))
        self.weightComboBox.setItemText(29, QCoreApplication.translate("Form", u"59", None))
        self.weightComboBox.setItemText(30, QCoreApplication.translate("Form", u"60", None))
        self.weightComboBox.setItemText(31, QCoreApplication.translate("Form", u"61", None))
        self.weightComboBox.setItemText(32, QCoreApplication.translate("Form", u"62", None))
        self.weightComboBox.setItemText(33, QCoreApplication.translate("Form", u"63", None))
        self.weightComboBox.setItemText(34, QCoreApplication.translate("Form", u"64", None))
        self.weightComboBox.setItemText(35, QCoreApplication.translate("Form", u"65", None))
        self.weightComboBox.setItemText(36, QCoreApplication.translate("Form", u"66", None))
        self.weightComboBox.setItemText(37, QCoreApplication.translate("Form", u"67", None))
        self.weightComboBox.setItemText(38, QCoreApplication.translate("Form", u"68", None))
        self.weightComboBox.setItemText(39, QCoreApplication.translate("Form", u"69", None))
        self.weightComboBox.setItemText(40, QCoreApplication.translate("Form", u"70", None))
        self.weightComboBox.setItemText(41, QCoreApplication.translate("Form", u"71", None))
        self.weightComboBox.setItemText(42, QCoreApplication.translate("Form", u"72", None))
        self.weightComboBox.setItemText(43, QCoreApplication.translate("Form", u"73", None))
        self.weightComboBox.setItemText(44, QCoreApplication.translate("Form", u"74", None))
        self.weightComboBox.setItemText(45, QCoreApplication.translate("Form", u"75", None))
        self.weightComboBox.setItemText(46, QCoreApplication.translate("Form", u"76", None))
        self.weightComboBox.setItemText(47, QCoreApplication.translate("Form", u"77", None))
        self.weightComboBox.setItemText(48, QCoreApplication.translate("Form", u"78", None))
        self.weightComboBox.setItemText(49, QCoreApplication.translate("Form", u"79", None))
        self.weightComboBox.setItemText(50, QCoreApplication.translate("Form", u"80", None))
        self.weightComboBox.setItemText(51, QCoreApplication.translate("Form", u"81", None))
        self.weightComboBox.setItemText(52, QCoreApplication.translate("Form", u"82", None))
        self.weightComboBox.setItemText(53, QCoreApplication.translate("Form", u"83", None))
        self.weightComboBox.setItemText(54, QCoreApplication.translate("Form", u"84", None))
        self.weightComboBox.setItemText(55, QCoreApplication.translate("Form", u"85", None))
        self.weightComboBox.setItemText(56, QCoreApplication.translate("Form", u"86", None))
        self.weightComboBox.setItemText(57, QCoreApplication.translate("Form", u"87", None))
        self.weightComboBox.setItemText(58, QCoreApplication.translate("Form", u"88", None))
        self.weightComboBox.setItemText(59, QCoreApplication.translate("Form", u"89", None))
        self.weightComboBox.setItemText(60, QCoreApplication.translate("Form", u"90", None))
        self.weightComboBox.setItemText(61, QCoreApplication.translate("Form", u"91", None))
        self.weightComboBox.setItemText(62, QCoreApplication.translate("Form", u"92", None))
        self.weightComboBox.setItemText(63, QCoreApplication.translate("Form", u"93", None))
        self.weightComboBox.setItemText(64, QCoreApplication.translate("Form", u"94", None))
        self.weightComboBox.setItemText(65, QCoreApplication.translate("Form", u"95", None))
        self.weightComboBox.setItemText(66, QCoreApplication.translate("Form", u"96", None))
        self.weightComboBox.setItemText(67, QCoreApplication.translate("Form", u"97", None))
        self.weightComboBox.setItemText(68, QCoreApplication.translate("Form", u"98", None))
        self.weightComboBox.setItemText(69, QCoreApplication.translate("Form", u"99", None))
        self.weightComboBox.setItemText(70, QCoreApplication.translate("Form", u"100", None))
        self.weightComboBox.setItemText(71, QCoreApplication.translate("Form", u"101", None))
        self.weightComboBox.setItemText(72, QCoreApplication.translate("Form", u"102", None))
        self.weightComboBox.setItemText(73, QCoreApplication.translate("Form", u"103", None))
        self.weightComboBox.setItemText(74, QCoreApplication.translate("Form", u"104", None))
        self.weightComboBox.setItemText(75, QCoreApplication.translate("Form", u"105", None))
        self.weightComboBox.setItemText(76, QCoreApplication.translate("Form", u"106", None))
        self.weightComboBox.setItemText(77, QCoreApplication.translate("Form", u"107", None))
        self.weightComboBox.setItemText(78, QCoreApplication.translate("Form", u"108", None))
        self.weightComboBox.setItemText(79, QCoreApplication.translate("Form", u"109", None))
        self.weightComboBox.setItemText(80, QCoreApplication.translate("Form", u"110", None))
        self.weightComboBox.setItemText(81, QCoreApplication.translate("Form", u"111", None))
        self.weightComboBox.setItemText(82, QCoreApplication.translate("Form", u"112", None))
        self.weightComboBox.setItemText(83, QCoreApplication.translate("Form", u"113", None))
        self.weightComboBox.setItemText(84, QCoreApplication.translate("Form", u"114", None))
        self.weightComboBox.setItemText(85, QCoreApplication.translate("Form", u"115", None))
        self.weightComboBox.setItemText(86, QCoreApplication.translate("Form", u"116", None))
        self.weightComboBox.setItemText(87, QCoreApplication.translate("Form", u"117", None))
        self.weightComboBox.setItemText(88, QCoreApplication.translate("Form", u"118", None))
        self.weightComboBox.setItemText(89, QCoreApplication.translate("Form", u"119", None))
        self.weightComboBox.setItemText(90, QCoreApplication.translate("Form", u"120", None))

        self.heightLabel.setText(QCoreApplication.translate("Form", u"Height", None))
        self.heightComboBox.setItemText(0, QCoreApplication.translate("Form", u"130", None))
        self.heightComboBox.setItemText(1, QCoreApplication.translate("Form", u"131", None))
        self.heightComboBox.setItemText(2, QCoreApplication.translate("Form", u"132", None))
        self.heightComboBox.setItemText(3, QCoreApplication.translate("Form", u"133", None))
        self.heightComboBox.setItemText(4, QCoreApplication.translate("Form", u"134", None))
        self.heightComboBox.setItemText(5, QCoreApplication.translate("Form", u"135", None))
        self.heightComboBox.setItemText(6, QCoreApplication.translate("Form", u"136", None))
        self.heightComboBox.setItemText(7, QCoreApplication.translate("Form", u"137", None))
        self.heightComboBox.setItemText(8, QCoreApplication.translate("Form", u"138", None))
        self.heightComboBox.setItemText(9, QCoreApplication.translate("Form", u"139", None))
        self.heightComboBox.setItemText(10, QCoreApplication.translate("Form", u"140", None))
        self.heightComboBox.setItemText(11, QCoreApplication.translate("Form", u"141", None))
        self.heightComboBox.setItemText(12, QCoreApplication.translate("Form", u"142", None))
        self.heightComboBox.setItemText(13, QCoreApplication.translate("Form", u"143", None))
        self.heightComboBox.setItemText(14, QCoreApplication.translate("Form", u"144", None))
        self.heightComboBox.setItemText(15, QCoreApplication.translate("Form", u"145", None))
        self.heightComboBox.setItemText(16, QCoreApplication.translate("Form", u"146", None))
        self.heightComboBox.setItemText(17, QCoreApplication.translate("Form", u"147", None))
        self.heightComboBox.setItemText(18, QCoreApplication.translate("Form", u"148", None))
        self.heightComboBox.setItemText(19, QCoreApplication.translate("Form", u"149", None))
        self.heightComboBox.setItemText(20, QCoreApplication.translate("Form", u"150", None))
        self.heightComboBox.setItemText(21, QCoreApplication.translate("Form", u"151", None))
        self.heightComboBox.setItemText(22, QCoreApplication.translate("Form", u"152", None))
        self.heightComboBox.setItemText(23, QCoreApplication.translate("Form", u"153", None))
        self.heightComboBox.setItemText(24, QCoreApplication.translate("Form", u"154", None))
        self.heightComboBox.setItemText(25, QCoreApplication.translate("Form", u"155", None))
        self.heightComboBox.setItemText(26, QCoreApplication.translate("Form", u"156", None))
        self.heightComboBox.setItemText(27, QCoreApplication.translate("Form", u"157", None))
        self.heightComboBox.setItemText(28, QCoreApplication.translate("Form", u"158", None))
        self.heightComboBox.setItemText(29, QCoreApplication.translate("Form", u"159", None))
        self.heightComboBox.setItemText(30, QCoreApplication.translate("Form", u"160", None))
        self.heightComboBox.setItemText(31, QCoreApplication.translate("Form", u"161", None))
        self.heightComboBox.setItemText(32, QCoreApplication.translate("Form", u"162", None))
        self.heightComboBox.setItemText(33, QCoreApplication.translate("Form", u"163", None))
        self.heightComboBox.setItemText(34, QCoreApplication.translate("Form", u"164", None))
        self.heightComboBox.setItemText(35, QCoreApplication.translate("Form", u"165", None))
        self.heightComboBox.setItemText(36, QCoreApplication.translate("Form", u"166", None))
        self.heightComboBox.setItemText(37, QCoreApplication.translate("Form", u"167", None))
        self.heightComboBox.setItemText(38, QCoreApplication.translate("Form", u"168", None))
        self.heightComboBox.setItemText(39, QCoreApplication.translate("Form", u"169", None))
        self.heightComboBox.setItemText(40, QCoreApplication.translate("Form", u"170", None))
        self.heightComboBox.setItemText(41, QCoreApplication.translate("Form", u"171", None))
        self.heightComboBox.setItemText(42, QCoreApplication.translate("Form", u"172", None))
        self.heightComboBox.setItemText(43, QCoreApplication.translate("Form", u"173", None))
        self.heightComboBox.setItemText(44, QCoreApplication.translate("Form", u"174", None))
        self.heightComboBox.setItemText(45, QCoreApplication.translate("Form", u"175", None))
        self.heightComboBox.setItemText(46, QCoreApplication.translate("Form", u"176", None))
        self.heightComboBox.setItemText(47, QCoreApplication.translate("Form", u"177", None))
        self.heightComboBox.setItemText(48, QCoreApplication.translate("Form", u"178", None))
        self.heightComboBox.setItemText(49, QCoreApplication.translate("Form", u"179", None))
        self.heightComboBox.setItemText(50, QCoreApplication.translate("Form", u"180", None))
        self.heightComboBox.setItemText(51, QCoreApplication.translate("Form", u"181", None))
        self.heightComboBox.setItemText(52, QCoreApplication.translate("Form", u"182", None))
        self.heightComboBox.setItemText(53, QCoreApplication.translate("Form", u"183", None))
        self.heightComboBox.setItemText(54, QCoreApplication.translate("Form", u"184", None))
        self.heightComboBox.setItemText(55, QCoreApplication.translate("Form", u"185", None))
        self.heightComboBox.setItemText(56, QCoreApplication.translate("Form", u"186", None))
        self.heightComboBox.setItemText(57, QCoreApplication.translate("Form", u"187", None))
        self.heightComboBox.setItemText(58, QCoreApplication.translate("Form", u"188", None))
        self.heightComboBox.setItemText(59, QCoreApplication.translate("Form", u"189", None))
        self.heightComboBox.setItemText(60, QCoreApplication.translate("Form", u"190", None))
        self.heightComboBox.setItemText(61, QCoreApplication.translate("Form", u"191", None))
        self.heightComboBox.setItemText(62, QCoreApplication.translate("Form", u"192", None))
        self.heightComboBox.setItemText(63, QCoreApplication.translate("Form", u"193", None))
        self.heightComboBox.setItemText(64, QCoreApplication.translate("Form", u"194", None))
        self.heightComboBox.setItemText(65, QCoreApplication.translate("Form", u"195", None))
        self.heightComboBox.setItemText(66, QCoreApplication.translate("Form", u"196", None))
        self.heightComboBox.setItemText(67, QCoreApplication.translate("Form", u"197", None))
        self.heightComboBox.setItemText(68, QCoreApplication.translate("Form", u"198", None))
        self.heightComboBox.setItemText(69, QCoreApplication.translate("Form", u"199", None))
        self.heightComboBox.setItemText(70, QCoreApplication.translate("Form", u"200", None))

    # retranslateUi

