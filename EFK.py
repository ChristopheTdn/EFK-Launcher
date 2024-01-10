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
from updater import Mw_updater
import shutil
import json
import EFK


app = QtWidgets.QApplication(sys.argv)
# Installe Traduction
TRANSLATOR = QtCore.QTranslator(app)
app.installTranslator(TRANSLATOR)

# Determine si le Launcher est lancé avec l arguments
# -updater ou -u
updater = False
for arg in sys.argv:
    if arg.lower() == "-updater" or arg == "-u":
        updater = True
        
# creation fichier config si rien n existe
EFK.core.create_config()
with open("config/EFKLauncher/config.json", "r") as fichier:
    CONFIG = json.load(fichier)
    
TRANSLATOR.load(f":/translation/translations/{CONFIG['Langue']}.qm")

if updater :
    # Dirige le Launcher vers l interface de mise a jour
    UPDATER_APPS = Mw_updater()
    # affiche le formulaire
    UPDATER_APPS.show()
    # affiche l'Updater dans la langue du config
    EFK.core.changeLangue(UPDATER_APPS, CONFIG["Langue"])
    sys.exit(app.exec())

else:
    # Efface toute trace des operations d'Update
    shutil.rmtree("tmp", True)
    # Creation de l application
    FORM = Fenetre_Principale()
    # affiche le formulaire
    FORM.show()
    sys.exit(app.exec())
