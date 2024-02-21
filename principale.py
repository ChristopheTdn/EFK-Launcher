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
╚═╝     ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
# Module implementing Fenetre_Principale.
"""

from PySide6.QtCore import Slot, QTranslator, QTimer
from PySide6.QtWidgets import QMainWindow
from principale_ui import Ui_Fenetre_Principale
import os
import EFK
import webbrowser
import json
# necessaire pour integrer les ressources
import ressources_rc


class Fenetre_Principale(QMainWindow, Ui_Fenetre_Principale):
    """
    Fenetre principale Interface EFK Launcher
    avec gestion des evenements et signaux
    """

    def __init__(self, parent=None):
        """
        Constructeur Fenetre Principale
        @param parent reference to the parent widget (defaults to None)
        """
        super().__init__(parent)
        timer = QTimer(self)
        timer.timeout.connect(self.TestWipeMapFile)
        timer.start(15000)  # toute les x secondes * 1000
        self.translator = QTranslator()
        self.setupUi(self)
        EFK.core.init_application(self)

    def TestWipeMapFile(self) -> None:
        """
        Test presence WIPEMAP.json
        Pour automatiser WIPEMAP
        """
        if os.path.isfile(self.lineEdit_ProfilPZ.text() + "/Sandbox Presets/WIPEMAP.json"):
            with open(self.lineEdit_ProfilPZ.text() + "/Sandbox Presets/WIPEMAP.json") as wipeMapFile:
                STATWipeMap = json.load(wipeMapFile)
            self.lineEdit_RepertoireSaveGame.setText(STATWipeMap["SaveGameDir"])
            EFK.core.writeLog(self, "AUTO-WIPEMAP", " SaveGame Directory set.")
            EFK.disk.configSave("SaveGame", STATWipeMap["SaveGameDir"])
            EFK.core.setFlags(self)
            EFK.core.writeLog(self,
                              "AUTO-WIPEMAP",
                              " Auto-Wipemap request detected.")
            EFK.disk.delFileTarget(
                self,
                self.lineEdit_ProfilPZ.text() + "/Sandbox Presets/WIPEMAP.json"
            )
            EFK.core.writeLog(self,
                              "AUTO-WIPEMAP",
                              " Auto-Wipemap file deleted.")
            print("Process AUTO WIPEMAP activate")
            EFK.disk.delFile(self)
            EFK.sounds.play(self,
                            son="qrc:/sounds/sounds/whoosh.mp3",
                            volume=0.6)

    @Slot()
    def on_pushButton_SetExePZ_clicked(self):
        """
        QT Evenement :
        Evenement appelé lors du clique sur le bouton pour Localiser
        l'éxécutable Steam
        """
        EFK.sounds.play(self)
        EFK.disk.get_ExeSteam(self)

    @Slot()
    def on_pushButton_RunPZ_clicked(self):
        """
        QT Evenement :
        Lance l'executable PZ dans un Process.
        """
        EFK.sounds.play(self)
        EFK.core.runPz(self)

    @Slot()
    def on_pushButton_SetRepertoireSaveGame_clicked(self):
        """
        QT Evenement :
        Evenement appelé lors du clique sur le bouton pour choisir
        le repertoire de sauvegarde
        """
        EFK.sounds.play(self)
        EFK.disk.get_saveGameDir(self)

    @Slot()
    def on_pushButton_WIPE_clicked(self) -> None:
        """
        QT Evenement :
        Lance le WIPE MAP
        """
        EFK.disk.delFile(self)
        self.checkBox_unlock.setChecked(False)
        EFK.sounds.play(self,
                        son="qrc:/sounds/sounds/whoosh.mp3",
                        volume=0.6)

    @Slot()
    def on_comboBox_Translate_currentIndexChanged(self):
        langage = "en-EN"
        if self.comboBox_Translate.currentIndex() == 0:
            langage = 'fr-FR'
        elif self.comboBox_Translate.currentIndex() == 1:
            langage = 'zh-CN'
        elif self.comboBox_Translate.currentIndex() == 2:
            langage = 'en-GB'
        elif self.comboBox_Translate.currentIndex() == 3:
            langage = 'ko-KR'
        elif self.comboBox_Translate.currentIndex() == 4:
            langage = 'ru-RU'
        elif self.comboBox_Translate.currentIndex() == 5:
            langage = 'es-ES'
        EFK.sounds.play(self)
        EFK.core.changeLangue(self, langage)
        EFK.disk.configSave("Langue", langage)

    @Slot()
    def on_commandLinkButton_Twitch_clicked(self):
        """
        QT Evenement :
        Ouvre le lien internet TWITCH TANCRED TERROR
        """
        EFK.sounds.play(self)
        webbrowser.open("https://www.twitch.tv/tancredterror")

    @Slot()
    def on_commandLinkButton_Youtube_clicked(self):
        """
        QT Evenement :
        Ouvre le lien internet YOUTUBE TANCRED TERROR
        """
        EFK.sounds.play(self)
        webbrowser.open("https://www.youtube.com/@TancredTerror")

    @Slot()
    def on_commandLinkButton_Discord_clicked(self):
        """
        QT Evenement :
        Ouvre le lien internet DISCORD TANCRED TERROR
        """
        EFK.sounds.play(self)
        webbrowser.open("https://discord.gg/rbd36ERXyu")

    @Slot()
    def on_commandLinkButton_STEAM_clicked(self):
        """
        QT Evenement :
        Ouvre le lien internet TWITCH TANCRED TERROR
        """
        EFK.sounds.play(self)
        EFK.core.openEFKCollection(self)

    @Slot()
    def on_checkBox_unlock_stateChanged(self):
        """
        QT Evenement :
        Slot documentation goes here.
        @param checked DESCRIPTION
        @type bool
        """
        EFK.sounds.play(self)
        buttonState = self.checkBox_unlock.isChecked()
        self.label_Titre_2.setVisible(buttonState)
        self.label_Danger.setVisible(buttonState)
        self.pushButton_WIPE.setEnabled(buttonState)

    @Slot()
    def on_checkBox_DebugMode_stateChanged(self):
        """
        QT Evenement :
        Active le Debug Mode lors du Lancement de PZ.

        @param checked : Sauvegarde l'etat dans le fichier Config si True
        @type bool
        """
        EFK.sounds.play(self)
        EFK.disk.configSave("DebugMode", self.checkBox_DebugMode.isChecked())

    @Slot()
    def on_radioButton_EFKEnhanced_clicked(self) -> None:
        """
        QT Evenement :
        Determine la selections des Mods pour EFK Enhanced
        """
        EFK.sounds.play(self)
        EFK.disk.install_EFKEnhanced(self)
        EFK.disk.configSave("Performance", "Enhanced")

    @Slot()
    def on_radioButton_EFKNoModif_clicked(self):
        """
        QT Evenement :
        Determine la selections des Mods pour EFK Standard
        """
        EFK.sounds.play(self)
        self.label_alert.setVisible(True)
        self.label_SignAlert.setVisible(True)
        EFK.disk.configSave("Performance", "")

    @Slot()
    def on_radioButton_EFKStandard_clicked(self) -> None:
        """
        QT Evenement :
        Determine la selections des Mods pour EFK Standard
        """
        EFK.sounds.play(self)
        EFK.disk.install_EFKStandard(self)
        EFK.disk.configSave("Performance", "Standard")

    @Slot()
    def on_pushButton_MajEFK_clicked(self) -> None:
        """
        QT Evenement :
        Lance la mise a jour de EFK Launcher
        """
        EFK.sounds.play(self)
        EFK.core.launch_EFK_launcher_updater(self)

    @Slot()
    def on_pushButton_UninstallEFK_clicked(self) -> None:
        """
        QT Evenement :
        Supprime les scripts et les configs de EFK
        en vue d'une desinstallations
        """
        EFK.sounds.play(self)
        EFK.core.uninstall_EFK_launcher(self)
