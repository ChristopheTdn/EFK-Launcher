import sys
from PyQt6 import QtWidgets, QtCore
from principale import Fenetre_Principale

app = QtWidgets.QApplication(sys.argv)
TRANSLATOR = QtCore.QTranslator()
TRANSLATOR.load(":/translation/translations/en-GB.qm")
app.installTranslator(TRANSLATOR)
FORM = Fenetre_Principale()
FORM.show()
sys.exit(app.exec())
