import sys
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QPushButton,QLabel,QBoxLayout,QFormLayout,QGroupBox
from PySide6.QtCore import *
from PySide6.QtGui import QPixmap
from UI.profile import Ui_Form
from RecipeInProfWidget import RecipeInProfile
from RegisterPage import Register
from ProfileEditPage import ProfileEdit
from Constant import *
from databasemodel.RecipeModel import *
from datetime import date

class Profile(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.ui = Ui_Form()
        self.setFixedSize( 710,465)
        self.ui.setupUi(self)
        self.ui.piclabel.setPixmap(QPixmap("app/UI/pngegg.png"))
        self.ui.piclabel.setScaledContents(True)
        self.widget =QWidget()
        formlayout =QFormLayout()
        self.blayout = QHBoxLayout()
        self.vlayout = QVBoxLayout()
        self.groupBox =QGroupBox()
        self.ui.editButton.clicked.connect( self.editProfile )


    def refresh( self ):
        self.updateProfile( self.user )

    def updateProfile( self, cur_user ):
        self.user = cur_user
        self.ui.usernameLabel.setText(cur_user.getUsername())
        self.ui.nameLabel_2.setText(cur_user.getFirstName())
        self.ui.lastnameLabel_2.setText(cur_user.getLastName())
        self.ui.dateLabel_2.setText(cur_user.getBirthDate())
        self.ui.genderLabel_2.setText(cur_user.getGender())
        self.ui.heightLabel_2.setText(str(cur_user.getHeight()))
        age = int(date.today().strftime("%Y")) - int(cur_user.getBirthDate()[-4:])
        if cur_user.getGender() == "Male":
            bmr = 10 * cur_user.getWeight() + 6.25 * cur_user.getHeight() - 5 * age + 5
        else:
            bmr = 10 * cur_user.getWeight() + 6.25 * cur_user.getHeight() - 5 * age - 161
        cal_need = bmr * 1.375
        cal_need = int(cal_need)
        self.ui.calLabel_2.setText( str(cal_need) + " kcal")
        print( cal_need )

        self.recipes = []
        recipes_info = RECIPE_MODEL.getRecipeFromCreator( self.user.getUsername() )
        for i in reversed(range( self.vlayout.count())):
            self.vlayout.itemAt(i).widget().setParent(None)

        for i in range(len(recipes_info)):
            self.recipes.append( RecipeInProfile( recipes_info[i], self.user, self))
            self.vlayout.addWidget(self.recipes[i])

            
        self.groupBox.setLayout(self.vlayout)
        self.ui.recipeScrollArea.setWidget(self.groupBox)
        self.ui.recipeScrollArea.setStyleSheet("background-color:rgb(255, 187, 178)\n")
        self.ui.recipeScrollArea.setWidgetResizable(True)

    def editProfile( self ):
        self.editPage = ProfileEdit( self.user, self )
        self.editPage.show()

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Profile()
    w.setFixedSize(557,465)
    w.setStyleSheet( "background-color:rgb(255, 255, 255)")
    w.show()
    sys.exit(app.exec_())