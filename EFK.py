"""
███████╗███████╗██╗  ██╗    ██╗      █████╗ ██╗   ██╗███╗   ██╗ ██████╗██╗  ██╗███████╗██████╗     
██╔════╝██╔════╝██║ ██╔╝    ██║     ██╔══██╗██║   ██║████╗  ██║██╔════╝██║  ██║██╔════╝██╔══██╗    
█████╗  █████╗  █████╔╝     ██║     ███████║██║   ██║██╔██╗ ██║██║     ███████║█████╗  ██████╔╝    
██╔══╝  ██╔══╝  ██╔═██╗     ██║     ██╔══██║██║   ██║██║╚██╗██║██║     ██╔══██║██╔══╝  ██╔══██╗    
███████╗██║     ██║  ██╗    ███████╗██║  ██║╚██████╔╝██║ ╚████║╚██████╗██║  ██║███████╗██║  ██║    
╚══════╝╚═╝     ╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

Un utilitaire pour permettre de configurer facilement
et lancer le MOD EFK par TancredTerror sur Project Zomboid

source : https://github.com/ChristopheTdn/EFK-Launcher
Idea : Tancred Terror
code : MrGToF
Traduction : MrGToF (fr,en), Screamff (cn)
             ElPacsWTF (es)
Discord : https://discord.com/invite/rbd36ERXyu
"""

import sys
from PySide6 import QtWidgets, QtCore
from principale import Fenetre_Principale
import shutil
import EFK

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
    # creation fichier config si rien n existe
    EFK.core.create_config()
    # Installe Traduction
    TRANSLATOR = QtCore.QTranslator()
    TRANSLATOR.load(":/translation/translations/en-GB.qm")
    # Creation de l application
    app.installTranslator(TRANSLATOR)
    FORM = Fenetre_Principale()
    FORM.show()
    sys.exit(app.exec())
