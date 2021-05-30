import sys
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QPushButton,QLabel,QBoxLayout,QFormLayout,QGroupBox
from PySide6.QtCore import *
from PySide6.QtGui import QPixmap
from UI.mainmenu import Ui_Form
from RecipeInMenuWidget import RecipeInMenu
from databasemodel.RecipeModel import *

class Mainmenu(QWidget):
    def __init__(self, currentUser):
        QWidget.__init__(self,None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.current_user = currentUser
        self.ui.searchButton.setIcon(QPixmap("app/UI/search.png"))
        self.ui.recipepicLabel.setPixmap(QPixmap("app/UI/recipe-book.png"))
        self.ui.recipepicLabel.setScaledContents(True)
        self.ui.refreshButton.clicked.connect( self.refresh )
        self.ui.searchButton.clicked.connect( self.search )
        self.ui.nameRadioButton.setChecked( True )
        formlayout =QFormLayout()
        self.blayout = QHBoxLayout()
        self.vlayout = QVBoxLayout()
        self.glayout =[]
        self.groupBox =QGroupBox()         
        self.viewButton =[]
        self.editButton=[]
        self.recipes = []
        recipes_info = RECIPE_MODEL.getAllRecipe()
        for i in reversed(range( self.vlayout.count())):
            self.vlayout.itemAt(i).widget().setParent(None)


        for i in range(len(recipes_info)):
            self.recipes.append( RecipeInMenu( recipes_info[i], self.current_user ) )
            self.vlayout.addWidget(self.recipes[i])
            # self.glayout.append(QGridLayout())
            # self.glayout[i].addWidget(self.levelLabel,0,0)
            # self.glayout[i].addWidget(self.viewButton[i],1,0)
            # self.blayout.addLayout(self.glayout[i])
            
        self.groupBox.setLayout(self.vlayout)
        self.ui.recipemainScrollArea.setWidget(self.groupBox)
        self.ui.recipemainScrollArea.setStyleSheet("border-radius: 5px")
        self.ui.recipemainScrollArea.setWidgetResizable(True)
   
    def refresh( self ):
        self.recipes = []
        recipes_info = RECIPE_MODEL.getAllRecipe()
        for i in reversed(range( self.vlayout.count())):
            self.vlayout.itemAt(i).widget().setParent(None)

        for i in range(len(recipes_info)):
            self.recipes.append( RecipeInMenu( recipes_info[i], self.current_user ) )
            self.vlayout.addWidget(self.recipes[i])
    
    def search( self ):
        print( "\n%s\n" %(self.ui.searchEdit.text()))
        self.recipes = []
        search_text = self.ui.searchEdit.text()
        if self.ui.nameRadioButton.isChecked():
            recipes_info = RECIPE_MODEL.searchRecipeByName( search_text )
        else:
            try:
                search_text = float( search_text )
            except:
                message = QMessageBox()
                message.setText( "Calories must be real number!")
                message.exec_()
                return
            if self.ui.maximumRadioButton.isChecked():
                recipes_info = RECIPE_MODEL.searchRecipeByMaxCal( float(search_text ))
            else:
                recipes_info = RECIPE_MODEL.searchRecipeByMinCal( float(search_text ))

        for i in reversed(range( self.blayout.count())):
            self.blayout.itemAt(i).widget().setParent(None)

        for i in range(len(recipes_info)):
            self.recipes.append( RecipeInMenu( recipes_info[i], self.current_user ) )
            self.blayout.addWidget(self.recipes[i])
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Mainmenu()
    w.setFixedSize(557,457)
    w.show()
    sys.exit(app.exec_())