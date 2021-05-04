import sys
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QPushButton,QLabel,QBoxLayout,QFormLayout,QGroupBox
from PySide6.QtCore import *
from PySide6.QtGui import QPixmap
from UI.mainmenu import Ui_Form
from RecipeInMenuWidget import RecipeInMenu
from databasemodel.RecipeModel import *

class Mainmenu(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.searchButton.setIcon(QPixmap("app/UI/search.png"))
        self.ui.recipepicLabel.setPixmap(QPixmap("app/UI/recipe-book.png"))
        self.ui.recipepicLabel.setScaledContents(True)
        self.ui.refreshButton.clicked.connect( self.refresh )
        
        formlayout =QFormLayout()
        self.blayout = QHBoxLayout()
        self.vlayout = QVBoxLayout()
        self.glayout =[]
        self.groupBox =QGroupBox()         
        self.viewButton =[]
        self.editButton=[]
        self.recipes = []
        recipes_info = RECIPE_MODEL.getAllRecipe()
        for i in reversed(range( self.blayout.count())):
            self.blayout.itemAt(i).widget().setParent(None)


        for i in range(len(recipes_info)):
            self.recipes.append( RecipeInMenu( recipes_info[i] ) )
            self.blayout.addWidget(self.recipes[i])
            # self.glayout.append(QGridLayout())
            # self.glayout[i].addWidget(self.levelLabel,0,0)
            # self.glayout[i].addWidget(self.viewButton[i],1,0)
            # self.blayout.addLayout(self.glayout[i])
            
        self.groupBox.setLayout(self.blayout)
        self.ui.recipemainScrollArea.setWidget(self.groupBox)
        self.ui.recipemainScrollArea.setStyleSheet("border-radius: 5px")
        self.ui.recipemainScrollArea.setWidgetResizable(True)
   
    def refresh( self ):
        self.recipes = []
        recipes_info = RECIPE_MODEL.getAllRecipe()
        for i in reversed(range( self.blayout.count())):
            self.blayout.itemAt(i).widget().setParent(None)

        for i in range(len(recipes_info)):
            self.recipes.append( RecipeInMenu( recipes_info[i] ) )
            self.blayout.addWidget(self.recipes[i])
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Mainmenu()
    w.setFixedSize(557,457)
    w.show()
    sys.exit(app.exec_())