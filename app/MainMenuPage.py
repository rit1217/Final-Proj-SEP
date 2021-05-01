import sys
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QPushButton,QLabel,QBoxLayout,QFormLayout,QGroupBox
from PySide6.QtCore import *
from PySide6.QtGui import QPixmap
from UI.mainmenu import Ui_Form

class Mainmenu(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.searchButton.setIcon(QPixmap("app/UI/search.png"))
        self.ui.recipepicLabel.setPixmap(QPixmap("app/UI/recipe-book.png"))
        self.ui.recipepicLabel.setScaledContents(True)
        
        formlayout =QFormLayout()
        self.blayout = QHBoxLayout()
        self.vlayout = QVBoxLayout()
        self.glayout =[]
        self.groupBox =QGroupBox()         
        self.viewButton =[]
        self.editButton=[]
        
        for i in range(20):


            self.foodLabel =QLabel()
            self.foodLabel.setPixmap(QPixmap("app/UI/fast-food.png"))
            self.foodLabel.setScaledContents(True)
            self.foodLabel.setFixedSize(120,110)


            self.levelLabel =QLabel("Level:  Easy") 
            self.levelLabel.setFixedSize(100,50)
            self.levelLabel.setStyleSheet("color:black")


            self.viewButton.append(QPushButton("View"))
            self.viewButton[i].setFixedSize(80,20)
            self.viewButton[i].setStyleSheet("QPushButton{background-color:rgb(255, 127, 86);\n"
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


            self.editButton.append(QPushButton("Edit"))
            self.editButton[i].setFixedSize(80,20)
            self.editButton[i].setStyleSheet("QPushButton{background-color:rgb(255, 127, 86);\n"
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


            self.blayout.addWidget(self.foodLabel)
            self.glayout.append(QGridLayout())
            self.glayout[i].addWidget(self.levelLabel,0,0)
            self.glayout[i].addWidget(self.viewButton[i],1,0)
            self.blayout.addLayout(self.glayout[i])
            
        self.groupBox.setLayout(self.blayout)
        self.ui.recipemainScrollArea.setWidget(self.groupBox)
        self.ui.recipemainScrollArea.setStyleSheet("border-radius: 5px")
        self.ui.recipemainScrollArea.setWidgetResizable(True)
   
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Mainmenu()
    w.setFixedSize(557,453)
    w.show()
    sys.exit(app.exec_())