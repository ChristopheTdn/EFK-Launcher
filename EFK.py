import sys
from PyQt6 import QtWidgets, QtCore
from principale import Fenetre_Principale

app = QtWidgets.QApplication(sys.argv)

updater = False
for arg in sys.argv:
    if arg.lower() == "-updater" or arg == "-u":
        updater = True

if updater:
    from updater import Mw_updater
    MAINFORM = Mw_updater()
    MAINFORM.show()
    sys.exit(app.exec())
else :
    TRANSLATOR = QtCore.QTranslator()
    TRANSLATOR.load(":/translation/translations/en-GB.qm")
    app.installTranslator(TRANSLATOR)
    FORM = Fenetre_Principale()
    FORM.show()
    sys.exit(app.exec())
