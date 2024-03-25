"""
███████╗███████╗██╗  ██╗██╗      █████╗ ██╗   ██╗███╗   ██╗ ██████╗██╗  ██╗███████╗██████╗
██╔════╝██╔════╝██║ ██╔╝██║     ██╔══██╗██║   ██║████╗  ██║██╔════╝██║  ██║██╔════╝██╔══██╗
█████╗  █████╗  █████╔╝ ██║     ███████║██║   ██║██╔██╗ ██║██║     ███████║█████╗  ██████╔╝
██╔══╝  ██╔══╝  ██╔═██╗ ██║     ██╔══██║██║   ██║██║╚██╗██║██║     ██╔══██║██╔══╝  ██╔══██╗
███████╗██║     ██║  ██╗███████╗██║  ██║╚██████╔╝██║ ╚████║╚██████╗██║  ██║███████╗██║  ██║
╚══════╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

███╗   ███╗ ██████╗ ██████╗ ██╗   ██╗██╗     ███████╗
████╗ ████║██╔═══██╗██╔══██╗██║   ██║██║     ██╔════╝
██╔████╔██║██║   ██║██║  ██║██║   ██║██║     █████╗
██║╚██╔╝██║██║   ██║██║  ██║██║   ██║██║     ██╔══╝
██║ ╚═╝ ██║╚██████╔╝██████╔╝╚██████╔╝███████╗███████╗
╚═╝     ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝#
# Module Interface CORE
#
"""

from PySide6 import QtWidgets
from PySide6 import QtGui, QtCore
import sys
import os
import requests
import json
import shutil
import subprocess
import EFK.launchsteam as launchsteam
import EFK.disk as disk
import EFK.reseau as reseau
from datetime import datetime


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
    if sysInfo() == "linux":
        version_url = "https://su66.fr/ftp/efklauncher/nux/version.txt"
    else:
        version_url = "https://su66.fr/ftp/efklauncher/version.txt"

    if reseau.is_website_online(self, version_url):
        versionOnline = requests.get(version_url).text.replace("\n", "")
    else:
        self.label_noConnexion.setVisible(True)
        self.pushButton_MajEFK.setEnabled(False)

    with open("config/EFKLauncher/version.txt") as fichier:
        versionExe = fichier.readline().rstrip()

    if versionOnline != "" and versionOnline != versionExe:
        self.label_UpdateAvailable.setVisible(True)
        self.label_UpdateAvailable_2.setVisible(True)

    # Affiche le numero de version
    with open("config/EFKLauncher/version.txt", "r") as fichier:
        self.label_version.setText("v " + fichier.read())


def create_config():
    if not os.path.isfile("config/EFKLauncher/config.json"):
        config = {}
        with open("config/EFKLauncher/config.json", "w") as fichier_config:
            json.dump(config, fichier_config)

    with open("config/EFKLauncher/config.json", "r") as fichier:
        CONFIG = json.load(fichier)

    if "Langue" not in CONFIG:
        disk.configSave("Langue", "en-GB")
    if "SaveGame" not in CONFIG:
        disk.configSave("SaveGame", "")
    if "Profil" not in CONFIG:
        disk.configSave("Profil", "")
    if "ExePZ" not in CONFIG:
        disk.configSave("ExePZ", "")
    if "DebugMode" not in CONFIG:
        disk.configSave("DebugMode", False)
    if "Performance" not in CONFIG:
        disk.configSave("Performance", "")

def exePZ() -> str :
    """
    Ouvre le fichier exePZ
    """
    if sysInfo() == "linux":
        return "steam"
    elif sysInfo() == "win32":
        return LocateSteam_windows()
    elif sysInfo() == "mac":
        # todo: Verifier le bon fonctionnement de cette commande sous mac
        return "/Applications/Steam.app/Contents/MacOS/steam_osx "

def loadConfig(self) -> None:
    # Recupere les configs enregistrées
    with open("config/EFKLauncher/config.json", "r") as fichier:
        CONFIG = json.load(fichier)

    self.lineEdit_RepertoireSaveGame.setText(CONFIG["SaveGame"])
    self.checkBox_DebugMode.setChecked(CONFIG["DebugMode"])

    if CONFIG["Performance"] == "NoModif":
        self.radioButton_EFKNoModif.setChecked(True)
    else:
        self.radioButton_EFKEnhanced.setChecked(True)

    if CONFIG["Langue"] == "fr-FR":
        self.comboBox_Translate.setCurrentIndex(0)
    elif CONFIG["Langue"] == "es-ES":
        self.comboBox_Translate.setCurrentIndex(5)
    elif CONFIG["Langue"] == "zh-CN":
        self.comboBox_Translate.setCurrentIndex(1)
    elif CONFIG["Langue"] == "ko-KR":
        self.comboBox_Translate.setCurrentIndex(3)
    elif CONFIG["Langue"] == "ru-RU":
        self.comboBox_Translate.setCurrentIndex(4)
    else:
        CONFIG["Langue"] == "en-GB"
        self.comboBox_Translate.setCurrentIndex(2)

    changeLangue(self, CONFIG["Langue"])
    setFlags(self)


def setFlags(self) -> None:
    """
    Verifie l'ensemble des liens pour en determiner la validité
    et modifier les icones correspondant sur l interface
    """

    disk.verif_lien(
        self,
        directory=self.lineEdit_ProfilPZ.text(),
        icon=self.label_IconStatus_ProfilPZ,
    )

    # Preset Difficulty
    shutil.copy(
        "config/difficulty/EFK Easy.cfg",
        self.lineEdit_ProfilPZ.text() + "/Sandbox Presets/",
    )
    shutil.copy(
        "config/difficulty/EFK STD.cfg",
        self.lineEdit_ProfilPZ.text() + "/Sandbox Presets/",
    )
    shutil.copy(
        "config/difficulty/EFK Hard.cfg",
        self.lineEdit_ProfilPZ.text() + "/Sandbox Presets/",
    )



def runPz(self) -> None:
    self.process = launchsteam.LaunchSteam(self, exePZ())
    self.process.start()


def openEFKCollection(self):
    self.process = launchsteam.LaunchSteam(
        self,
        exePZ(),
        argument=[
            "steam://openurl/https://steamcommunity.com/sharedfiles/filedetails/?id=3048855836"
        ],
    )
    self.process.start()


def changeLangue(self, langue):
    app = QtWidgets.QApplication.instance()
    TRANSLATOR = QtCore.QTranslator()
    TRANSLATOR.load(f":/translation/translations/{langue}.qm")
    app.installTranslator(TRANSLATOR)
    main_window = QtWidgets.QMainWindow()
    self.retranslateUi(main_window)


def init_MODManager(self):
    disk.get_MODManager(self)


def writeLog(self, title, texte):
    if title == "CLEAR":
        self.textEdit_Log.clear()
    else:
        now = datetime.now()
        gdh = now.strftime("%Y-%m-%d %H:%M:%S")
        cursor = self.textEdit_Log.textCursor()
        self.textEdit_Log.insertHtml(f"<strong>{title}</strong> : {gdh}-> {texte}<br>")
        self.textEdit_Log.ensureCursorVisible()


def sysInfo():
    from sys import platform as _platform

    if _platform == "linux" or _platform == "linux2":  # environnement Linux
        return "linux"
    elif _platform == "win32":
        return "win32"
    elif _platform == "darwin":
        return "mac"
    else:
        return "unknown system"


def launch_EFK_launcher_updater(self):
    """EFK Launcher updater
    - réalise une copie de l'executable 'goslaunchera3'' dans le repertoire 'tmp'
    - lance avec le parametre '--updater'
    - ferme l'application courante.'
    """

    platform = sysInfo()
    executable = ""
    if platform == "linux":  # environnement Linux
        executable = "EFK Launcher"
    elif platform == "win32":  # windows:
        executable = "EFK Launcher.exe"  # environnement windows
    elif platform == "mac":  # mac
        # TODO: trouver nom executable EFK Launcher sous mac
        pass

    # création repertoire tmp
    if not os.path.exists("tmp"):
        os.makedirs("tmp")

    # copie executable EFK Launcher
    shutil.copyfile(executable, "tmp/" + executable)

    # Lance EFKLauncher --updater
    if platform == "linux":
        os.system(f'chmod +x "./tmp/{executable}"')
        subprocess.Popen(f'"./tmp/{executable}" -updater', shell=True)

    elif platform == "win32":
        # Windows
        subprocess.Popen([f"tmp/{executable}", "-updater"])
    elif platform == "mac":  # mac
        # TODO: lancer executable dans le repertoire tmp sous mac...
        pass

    # quitte l'application en cours
    sys.exit()


def uninstall_EFK_launcher(self):
    """Efface l'ensemble des script de EFK"""
    liste = [
        self.lineEdit_ProfilPZ.text() + "/Sandbox Presets/EFK Easy.cfg",
        self.lineEdit_ProfilPZ.text() + "/Sandbox Presets/EFK STD.cfg",
        self.lineEdit_ProfilPZ.text() + "/Sandbox Presets/EFK Hard.cfg",
    ]
    for fichier in liste:
        disk.delFileTarget(self, fichier)
    disk.effaceModManagerProfil(self)
    sys.exit()


def LocateSteam_windows() -> str:
    import winreg

    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER, r"Software\Valve\Steam", 0, winreg.KEY_READ
    )
    (LienSteam, typevaleur) = winreg.QueryValueEx(key, "SteamExe")
    winreg.CloseKey(key)
    return LienSteam


################################################################

if __name__ == "__main__":
    # execute when run directly, but not when called as a module.
    # therefore this section allows for testing this module!

    # print "running directly, not as a module!"

    sys.exit()
