import sys
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QPushButton,QLabel,QBoxLayout,QFormLayout,QGroupBox
from PySide6.QtCore import *
from PySide6.QtGui import QPixmap
from UI.viewComment import Ui_Form
from databasemodel.CommentModel import *

class ViewComment(QWidget):
    def __init__(self, recipe):
        QWidget.__init__(self,None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.recipe = recipe
        self.ui.pushButton.clicked.connect( self.close )
        self.ui.inRecipe_label.setText( self.recipe.getName())
        self.ui.inCreator_label.setText( self.recipe.getCreator().getUsername())
        self.updateComment()

    def updateComment( self ):
        allComment = COMMENT_MODEL.getCommentByRecipe( self.recipe.getId())
        self.ui.comment_listWidget.clear()
        for i in allComment:
            self.ui.comment_listWidget.addItem( " @%s:\n%s\n" %(i[0], i[1]))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ViewComment()
    w.setFixedSize(643,420)
    w.show()
    sys.exit(app.exec_())
    