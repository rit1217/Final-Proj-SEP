import sys
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QPushButton,QLabel,QBoxLayout,QFormLayout,QGroupBox
from PySide6.QtCore import *
from UI.register import Ui_Form

class Register(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
       
    def clickevent(self):
        self.ui.label.setText("Have click!!!!!")
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Register()
    w.setFixedSize(455,305)
    w.show()
    print( QDate( 2021, 2, 10).toString("dd/MM/yyyy") )
    sys.exit(app.exec_())
