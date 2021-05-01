import sys
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QPushButton,QLabel,QBoxLayout,QFormLayout,QGroupBox
from PySide6.QtCore import *
from PySide6.QtGui import QPixmap
from UI.profile import Ui_Form
from RecipeInProfWidget import RecipeInProfile


class Profile(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.ui = Ui_Form()
        
        self.ui.setupUi(self)
        self.ui.piclabel.setPixmap(QPixmap("app/UI/recipe-book.png"))
        self.ui.piclabel.setScaledContents(True)

        self.widget =QWidget()
        formlayout =QFormLayout()
        self.blayout = QHBoxLayout()
        self.vlayout = QVBoxLayout()
        self.glayout =[]
        self.groupBox =QGroupBox() 
        self.recipeWidget = RecipeInProfile()
        self.viewButton =[]
        self.editButton=[]
        for i in range(20):


            self.recipeLabel =QLabel()
            self.recipeLabel.setPixmap(QPixmap("app/UI/recipe-book.png"))
            self.recipeLabel.setScaledContents(True)
            self.recipeLabel.setFixedSize(120,120)


            self.levelLabel =QLabel("Level:  Easy") 
            self.levelLabel.setFixedSize(120,120)
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


            self.blayout.addWidget(self.recipeLabel)
            self.glayout.append(QGridLayout())
            self.blayout.addWidget(self.levelLabel)
            self.glayout[i].addWidget(self.viewButton[i],0,0)
            self.glayout[i].addWidget(self.editButton[i],1,0)
            self.blayout.addLayout(self.glayout[i])
            
        self.groupBox.setLayout(self.blayout)
        self.ui.recipeScrollArea.setWidget(self.groupBox)
        self.ui.recipeScrollArea.setStyleSheet("border-radius: 5px")
        self.ui.recipeScrollArea.setWidgetResizable(True)
   
        


# ตรงนี้กูพยายาม import file มา ของ test_recipeแต่ทำไม่ได้ เพื่อมึงอยากเปลี่ยน อิอิ
"""
        self.blayout = QHBoxLayout()
        self.vlayout =QVBoxLayout()
        self.groupBox =QGroupBox() 
        self.recipeWidget =[]
        self.frame=QFrame()
        self.blayout2 =QHBoxLayout()
        self.t =test_recipe.Register()
        self.formlayout =QFormLayout()
        for i in range(10):
            self.t =test_recipe.Register()
            self.blayout.addWidget(self.t)     
        self.groupBox.setLayout(self.blayout)
        self.ui.recipeScrollArea.setWidget(self.t)
        self.ui.recipeScrollArea.setWidgetResizable(True)
"""  




        

    
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Profile()
    w.setFixedSize(557,457)
    w.show()
    sys.exit(app.exec_())
