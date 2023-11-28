#
# Module Interface CORE
#

from PySide6 import QtWidgets
from PySide6 import QtGui, QtCore
import sys
import os
from . import launchpz
from . import disk
from . import reseau
import requests
import json
import shutil
import subprocess

def init_application(self):
    # Définition Constantes
    # Determine repertoire Utilisateur
    disk.get_userPZDir(self)
    loadConfig(self)
    init_MODManager(self)
    
    # determine la version en ligne
    self.label_noConnexion.setVisible(False)
    self.label_UpdateAvailable.setVisible(False)
    self.label_UpdateAvailable_2.setVisible(False)
    self.pushButton_MajEFK.setEnabled(True)
    versionOnline = ""
    if sysInfo() == "linux" :
        version_url =  "https://su66.fr/ftp/efklauncher/nux/version.txt"
    else :
        version_url =  "https://su66.fr/ftp/efklauncher/version.txt"
    
    if reseau.is_website_online(self, version_url):
        versionOnline = requests.get(version_url).text.replace('\n',"")
    else:
        self.label_noConnexion.setVisible(True)
        self.pushButton_MajEFK.setEnabled(False)

    with open("config/EFKLauncher/version.txt") as fichier:
        versionExe = fichier.readline().rstrip()

    if versionOnline != "" and versionOnline != versionExe :
        self.label_UpdateAvailable.setVisible(True)
        self.label_UpdateAvailable_2.setVisible(True)
        
    # Affiche le numero de version
    with open("config/EFKLauncher/version.txt", "r") as fichier:
        self.label_version.setText('v '+fichier.read())

def create_config():

    if not os.path.isfile("config/EFKLauncher/config.json"):
        config = {}
        with open("config/EFKLauncher/config.json", "w") as fichier_config:
            json.dump(config, fichier_config)

    with open("config/EFKLauncher/config.json", "r") as fichier:
        CONFIG = json.load(fichier)

    if 'Langue' not in CONFIG:
        disk.configSave("Langue", "en-GB")
    if 'SaveGame' not in CONFIG:
        disk.configSave("SaveGame", "")
    if 'Profil' not in CONFIG:
        disk.configSave("Profil", "")
    if 'ExePZ' not in CONFIG:
        disk.configSave("ExePZ", "")
    if 'DebugMode' not in CONFIG:
        disk.configSave("DebugMode", False)
    if "Performance" not in CONFIG:
        disk.configSave("Performance", "")

def loadConfig(self) -> None:

    # Recupere les configs enregistrées
    with open("config/EFKLauncher/config.json", "r") as fichier:
        CONFIG = json.load(fichier)
    self.lineEdit_ExePZ.setText(CONFIG["ExePZ"])
    self.lineEdit_RepertoireSaveGame.setText(CONFIG["SaveGame"])
    self.checkBox_DebugMode.setChecked(CONFIG["DebugMode"])

    self.label_alert.setVisible(False)
    self.label_SignAlert.setVisible(False)
    if CONFIG["Performance"] == "Enhanced":
        self.radioButton_EFKEnhanced.setChecked(True)
        disk.install_EFKEnhanced(self)
    elif CONFIG["Performance"] =="Standard":
        disk.install_EFKStandard(self)
        self.radioButton_EFKStandard.setChecked(True)
    else :
        self.label_alert.setVisible(True)
        self.label_SignAlert.setVisible(True)
        self.radioButton_EFKNoModif.setChecked(True)

    if CONFIG["Langue"] == "fr-FR":
        self.radioButton_France.setChecked(True)        
    elif CONFIG["Langue"] == "en-GB":
        self.radioButton_English.setChecked(True)
    changeLangue(self, CONFIG["Langue"])

    setFlags(self)


def setFlags(self) -> None:
    """
    Verifie l'ensemble des liens pour en determiner la validité
    et modifier les icones correspondant sur l interface
    """
    disk.verif_lien(self, file=self.lineEdit_ExePZ.text(), icon=self.label_IconStatus_ExePZ)

    disk.verif_lien(self, directory=self.lineEdit_ProfilPZ.text(), icon=self.label_IconStatus_ProfilPZ)
    if self.lineEdit_RepertoireSaveGame.text() != "" and \
        disk.verif_lien(self,
                       directory=os.path.join(self.lineEdit_ProfilPZ.text()+"/Saves/Sandbox",self.lineEdit_RepertoireSaveGame.text()),
                       icon=self.label_IconStatus_RepertoireSaveGame):
        self.pushButton_WIPE.setEnabled(True)
        self.label_IconStatus_WIPEMAP.setPixmap(QtGui.QPixmap(":/gfx/gfx/checked.png"))
    else :
        self.label_IconStatus_RepertoireSaveGame.setPixmap(QtGui.QPixmap(":/gfx/gfx/supprimer.png"))
        self.pushButton_WIPE.setEnabled(False)
        self.label_IconStatus_WIPEMAP.setPixmap(QtGui.QPixmap(":/gfx/gfx/supprimer.png"))

    # MOD Manager
    disk.verif_lien(self, file=self.lineEdit_ProfilPZ.text()+"/Lua/saved_modlists.txt", icon=self.label_IconStatus_MODManager)

    # Preset Difficulty
    shutil.copy('config/difficulty/EFK Easy.cfg', self.lineEdit_ProfilPZ.text()+"/Sandbox Presets/")
    disk.verif_lien(self, file=self.lineEdit_ProfilPZ.text()+"/Sandbox Presets/EFK Easy.cfg", icon=self.label_IconStatus_difficultEASY)

    shutil.copy('config/difficulty/EFK STD.cfg', self.lineEdit_ProfilPZ.text()+"/Sandbox Presets/")
    disk.verif_lien(self, file=self.lineEdit_ProfilPZ.text()+"/Sandbox Presets/EFK STD.cfg", icon=self.label_IconStatus_difficultSTD)

    shutil.copy('config/difficulty/EFK Hard.cfg', self.lineEdit_ProfilPZ.text()+"/Sandbox Presets/")
    disk.verif_lien(self, file=self.lineEdit_ProfilPZ.text()+"/Sandbox Presets/EFK Hard.cfg", icon=self.label_IconStatus_difficultHARD)

def runPz(self) -> None:
    self.process = launchpz.LaunchPz(self,
                                     self.lineEdit_ExePZ.text())
    self.process.start()

def changeLangue(self, langue):
    app = QtWidgets.QApplication.instance()
    TRANSLATOR = QtCore.QTranslator()
    TRANSLATOR.load(f':/translation/translations/{langue}.qm')
    app.installTranslator(TRANSLATOR)
    main_window = QtWidgets.QMainWindow()
    self.retranslateUi(main_window)

def init_MODManager(self):
    disk.get_MODManager(self)

def writeLog(self, title, texte):

    if title == "CLEAR":
        self.textEdit_Log.clear()
    else :
        cursor = self.textEdit_Log.textCursor()
        self.textEdit_Log.insertHtml(f'<strong>{title}</strong> : {texte}<br>')
        self.textEdit_Log.ensureCursorVisible()
def sysInfo() :
    from sys import platform as _platform
    if _platform == "linux" or _platform == "linux2": # environnement Linux
        return 'linux'
    elif _platform == "win32":
        return "windows"
    else :
        return "unknow system"

def launch_EFK_launcher_updater(self):
    ''' EFK Launcher updater
       - réalise une copie de l'executable 'goslaunchera3'' dans le repertoire 'tmp'
       - lance avec le parametre '--updater'
       - ferme l'application courante.'
           '''
    platform = sysInfo()
    if platform == "linux" or platform == "linux2": # environnement Linux
        executable="EFK Launcher"
    else : 
       executable="EFK Launcher.exe" # environnement windows
    # création repertoire tmp
    if not os.path.exists('tmp'):
        os.makedirs('tmp') 
    #copie executable EFK Launcher
    shutil.copyfile(executable, 'tmp/'+executable)
    #Lance EFKLauncher --updater
    if platform == "linux":
        os.system(f'chmod +x "./tmp/{executable}"')
        subprocess.Popen(f'"./tmp/{executable}" -updater',shell=True)
    elif platform == "win32":
        # Windows
        subprocess.Popen([f'tmp/{executable}','-updater'])
    #quitte l'application en cours
    sys.exit()

def uninstall_EFK_launcher(self) :
    """Efface l'ensemble des script de EFK
    """
    liste = [
        self.lineEdit_ProfilPZ.text()+"/Sandbox Presets/EFK Easy.cfg",
        self.lineEdit_ProfilPZ.text()+"/Sandbox Presets/EFK STD.cfg",
        self.lineEdit_ProfilPZ.text()+"/Sandbox Presets/EFK Hard.cfg"
    ]
    for fichier in liste:
        disk.delFileTarget(self, fichier)
    disk.effaceModManagerProfil(self)
    sys.exit()

################################################################

if __name__ == "__main__":

    # execute when run directly, but not when called as a module.
    # therefore this section allows for testing this module!

    # print "running directly, not as a module!"

    sys.exit()
