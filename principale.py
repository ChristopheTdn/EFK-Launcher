# -*- coding: utf-8 -*-

"""
Module implementing Fenetre_Principale.
"""

from PySide6.QtCore import Slot, QTranslator
from PySide6.QtWidgets import QMainWindow
from PySide6 import QtGui
from principale_ui import Ui_Fenetre_Principale
import EFK
import webbrowser
import ressources_rc


class Fenetre_Principale(QMainWindow, Ui_Fenetre_Principale):
    """
    Fenetre principale Interface EFK Launcher
    avec gestion des evenements et signaux
    """
    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super().__init__(parent)
        self.translator = QTranslator()
        self.setupUi(self)
        EFK.core.init_application(self)
    
    @Slot()
    def on_pushButton_SetExePZ_clicked(self):  
        """
        Evenement appelé lors du clique sur le bouton pour choisir
        l'exe PZ
        """
        # TODO: not implemented yet     
        EFK.sounds.play(self)
        EFK.disk.get_ExePZ(self)

        
    @Slot()
    def on_pushButton_RunPZ_clicked(self):
        """
        Lance l'executable PZ dans un Process.
        """
        # TODO: not implemented yet
        EFK.sounds.play(self)
        EFK.core.runPz(self)

        
    @Slot()
    def on_pushButton_SetRepertoireSaveGame_clicked(self):  
        """
        Evenement appelé lors du clique sur le bouton pour choisir
        le repertoire de sauvegarde
        """
        # TODO: not implemented yet     
        EFK.sounds.play(self)
        EFK.disk.get_saveGameDir(self)


    @Slot()
    def on_pushButton_WIPE_clicked(self) -> None:
        """
        Lance le WIPE MAP
        """
        # TODO: not implemented yet     
        EFK.sounds.play(self)
        EFK.disk.delFile(self)


    @Slot()
    def on_radioButton_France_clicked(self) -> None:
        """
        Valide la langue Francaise et modifie l'interface a la volée
        """
        # TODO: not implemented yet
        EFK.sounds.play(self)
        EFK.core.changeLangue(self, 'fr-FR')
        EFK.disk.configSave('Langue', 'fr-FR')

        
    @Slot()
    def on_radioButton_English_clicked(self) -> None:
        """
        Valide la langue Francaise et modifie l'interface a la volée
        """
        # TODO: not implemented yet
        EFK.sounds.play(self)
        EFK.core.changeLangue(self, 'en-GB')
        EFK.disk.configSave('Langue', 'en-GB')

        
    @Slot()
    def on_radioButton_Chine_clicked(self) -> None:
        """
        Valide la langue Chinoise et modifie l'interface a la volée
        """
        # TODO: not implemented yet
        EFK.sounds.play(self)
        EFK.core.changeLangue(self, 'zh-CN')
        EFK.disk.configSave( 'Langue', 'zh-CN')


    @Slot()
    def on_commandLinkButton_Twitch_clicked(self):  
        """
        Ouvre le lien internet TWITCH TANCRED TERROR
        """
        # TODO: not implemented yet     
        EFK.sounds.play(self)
        webbrowser.open("https://www.twitch.tv/tancredterror")
    
    @Slot()
    def on_commandLinkButton_Youtube_clicked(self):  
        """
        Ouvre le lien internet YOUTUBE TANCRED TERROR
        """
        # TODO: not implemented yet     
        EFK.sounds.play(self)
        webbrowser.open("https://www.youtube.com/@TancredTerror")
        
    @Slot()
    def on_commandLinkButton_Discord_clicked(self):  
        """
        Ouvre le lien internet DISCORD TANCRED TERROR
        """
        # TODO: not implemented yet     
        EFK.sounds.play(self)
        webbrowser.open("https://discord.gg/rbd36ERXyu")

        
    @Slot()
    def on_commandLinkButton_STEAM_clicked(self):  
        """
        Ouvre le lien internet TWITCH TANCRED TERROR
        """
        # TODO: not implemented yet
        EFK.sounds.play(self)
        webbrowser.open("https://steamcommunity.com/workshop/filedetails/?id=3048855836")
        
    @Slot()
    def on_checkBox_unlock_stateChanged(self):
        """
        Slot documentation goes here.

        @param checked DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        EFK.sounds.play(self)
        buttonState = self.checkBox_unlock.isChecked()
        self.pushButton_WIPE.setEnabled(buttonState)
        
     
    @Slot()
    def on_checkBox_DebugMode_stateChanged(self):
        """
        Slot documentation goes here.

        @param checked DESCRIPTION
        @type bool
        """
        EFK.sounds.play(self)
        EFK.disk.configSave('DebugMode', self.checkBox_DebugMode.isChecked())
     
        
    @Slot()
    def on_radioButton_EFKEnhanced_clicked(self) -> None:
        """
        Determine la selections des Mods pour EFK Enhanced
        """
        # TODO: not implemented yet
        EFK.sounds.play(self)
        EFK.disk.install_EFKEnhanced(self)
        EFK.disk.configSave( 'Performance', "Enhanced")
        
    @Slot()
    def on_radioButton_EFKNoModif_clicked(self):
        """
        Determine la selections des Mods pour EFK Standard
        """
        # TODO: not implemented yet
        EFK.sounds.play(self)
        self.label_alert.setVisible(True)
        self.label_SignAlert.setVisible(True)
        EFK.disk.configSave('Performance', "")

    @Slot()
    def on_radioButton_EFKStandard_clicked(self) -> None:
        """
        Determine la selections des Mods pour EFK Standard
        """
        # TODO: not implemented yet
        EFK.sounds.play(self)
        EFK.disk.install_EFKStandard(self)
        EFK.disk.configSave( 'Performance', "Standard")


        
    @Slot()
    def on_radioButton_EFKNoModif(self) -> None:
        """
        Valide la langue Francaise et modifie l'interface a la volée
        """
        # Ne modifie plsu la selection des Mods
        EFK.sounds.play(self)
        EFK.disk.configSave( 'Standard', "")

        
    @Slot()
    def on_pushButton_MajEFK_clicked(self) -> None:
        """
        Lance la mise a jour de EFK Launcher
        """
        # TODO: not implemented yet
        EFK.sounds.play(self)
        EFK.core.launch_EFK_launcher_updater(self)

        
    @Slot()
    def on_pushButton_UninstallEFK_clicked(self) -> None:
        """
        Supprime les scripts et les configs de EFK
        en vue d'une desinstallations 
        """
        # TODO: not implemented yet
        EFK.sounds.play(self)
        EFK.core.uninstall_EFK_launcher(self)
