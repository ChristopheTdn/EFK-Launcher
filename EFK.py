"""  EFK LAUNCHER 

Un utilitaire pour permettre de configurer facilement
et lancer le MOD EFK par TancredTerror sur Project Zomboid

"""

import sys
from PyQt6 import QtWidgets, QtCore
from principale import Fenetre_Principale
import shutil

app = QtWidgets.QApplication(sys.argv)

# Determine si le Launcher est lancé avec l arguments
# -updater ou -u
updater = False
for arg in sys.argv:
    if arg.lower() == "-updater" or arg == "-u":
        updater = True

if updater:
    # Dirige le Launcher vers l interface de mise a jour
    from updater import Mw_updater
    MAINFORM = Mw_updater()
    MAINFORM.show()
    sys.exit(app.exec())
else:
    # Efface toute trace des operations d'Update
    shutil.rmtree("tmp", True)
    # Installe Traduction
    TRANSLATOR = QtCore.QTranslator()
    TRANSLATOR.load(":/translation/translations/en-GB.qm")
    # Creation de l application
    app.installTranslator(TRANSLATOR)
    FORM = Fenetre_Principale()
    FORM.show()
    sys.exit(app.exec())
