import sys
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QPushButton,QLabel,QBoxLayout,QFormLayout,QGroupBox
from PySide6.QtCore import *
from PySide6.QtGui import QPixmap
from UI.profile import Ui_Form
from RecipeInProfWidget import RecipeInProfile
from Constant import *

class Profile(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.ui = Ui_Form()
        self.setFixedSize( 557,465)
        self.ui.setupUi(self)
        self.ui.piclabel.setPixmap(QPixmap("app/UI/recipe-book.png"))
        self.ui.piclabel.setScaledContents(True)

        self.widget =QWidget()
        formlayout =QFormLayout()
        self.blayout = QHBoxLayout()
        self.vlayout = QVBoxLayout()
        self.groupBox =QGroupBox() 
        self.recipes = []
        for i in range(20):
            self.recipes.append( RecipeInProfile())

            self.blayout.addWidget(self.recipes[i])
          #  self.glayout.append(QGridLayout())
            #self.blayout.addWidget(self.levelLabel)
          #  self.glayout[i].addWidget(self.viewButton[i],0,0)
          #  self.glayout[i].addWidget(self.editButton[i],1,0)
         #   self.blayout.addLayout(self.glayout[i])
            
        self.groupBox.setLayout(self.blayout)
        self.ui.recipeScrollArea.setWidget(self.groupBox)
        #self.ui.recipeScrollArea.setStyleSheet("border-radius: 5px")
        self.ui.recipeScrollArea.setStyleSheet("background-color:rgb(255, 187, 178)\n")
        self.ui.recipeScrollArea.setWidgetResizable(True)

    def updateProfile( self, cur_user ):
        self.ui.usernameLabel.setText(cur_user.getUsername())
        self.ui.nameLabel_2.setText(cur_user.getFirstName())
        self.ui.lastnameLabel_2.setText(cur_user.getLastName())
        self.ui.dateLabel_2.setText(cur_user.getBirthDate())
        self.ui.genderLabel_2.setText(cur_user.getGender())
        self.ui.heightLabel_2.setText(str(cur_user.getHeight()))
        self.ui.weightLabel_2.setText(str(cur_user.getWeight()))
   
        


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
    w.setFixedSize(557,465)
    w.setStyleSheet( "background-color:rgb(255, 187, 178)")
    w.show()
    sys.exit(app.exec_())
