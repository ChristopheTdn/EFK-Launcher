import sys
from PyQt6 import QtWidgets, QtCore
from principale import Fenetre_Principale
import shutil

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
else:
    # Efface toute trace des operations d'Update
    shutil.rmtree("tmp", True)
    #Install Traduction
    TRANSLATOR = QtCore.QTranslator()
    TRANSLATOR.load(":/translation/translations/en-GB.qm")
    #Creation de l application
    app.installTranslator(TRANSLATOR)
    FORM = Fenetre_Principale()
    FORM.show()
    sys.exit(app.exec())
