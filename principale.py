# -*- coding: utf-8 -*-

"""
Module implementing Fenetre_Principale.
"""

from PyQt6.QtCore import pyqtSlot, QTranslator
from PyQt6.QtWidgets import QMainWindow
from PyQt6 import QtGui
from Ui_principale import Ui_Fenetre_Principale
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
    
    @pyqtSlot()
    def on_pushButton_SetExePZ_clicked(self):  
        """
        Evenement appelé lors du clique sur le bouton pour choisir
        l'exe PZ
        """
        # TODO: not implemented yet     
        EFK.disk.get_ExePZ(self)
    
    @pyqtSlot()
    def on_pushButton_RunPZ_clicked(self):
        """
        Lance l'executable PZ dans un Process.
        """
        # TODO: not implemented yet
        EFK.core.runPz(self)
        
    @pyqtSlot()
    def on_pushButton_SetRepertoireSaveGame_clicked(self):  
        """
        Evenement appelé lors du clique sur le bouton pour choisir
        le repertoire de sauvegarde
        """
        # TODO: not implemented yet     
        EFK.disk.get_saveGameDir(self)


    @pyqtSlot()
    def on_pushButton_WIPE_clicked(self) -> None:
        """
        Lance le WIPE MAP
        """
        # TODO: not implemented yet     
        EFK.disk.delFile(self)

    @pyqtSlot()
    def on_radioButton_France_clicked(self) -> None:
        """
        Valide la langue Francaise et modifie l'interface a la volée
        """
        # TODO: not implemented yet
        EFK.core.changeLangue(self, 'fr-FR')
        EFK.disk.configSave(self, 'Langue', 'fr-FR')

    @pyqtSlot()
    def on_radioButton_English_clicked(self) -> None:
        """
        Valide la langue Francaise et modifie l'interface a la volée
        """
        # TODO: not implemented yet
        EFK.core.changeLangue(self, 'en-GB')
        EFK.disk.configSave(self, 'Langue', 'en-GB')

    @pyqtSlot()
    def on_commandLinkButton_Twitch_clicked(self):  
        """
        Ouvre le lien internet TWITCH TANCRED TERROR
        """
        # TODO: not implemented yet     
        webbrowser.open("https://www.twitch.tv/tancredterror")
    
    @pyqtSlot()
    def on_commandLinkButton_Youtube_clicked(self):  
        """
        Ouvre le lien internet YOUTUBE TANCRED TERROR
        """
        # TODO: not implemented yet     
        webbrowser.open("https://www.youtube.com/@TancredTerror")
    
    @pyqtSlot()
    def on_commandLinkButton_Discord_clicked(self):  
        """
        Ouvre le lien internet DISCORD TANCRED TERROR
        """
        # TODO: not implemented yet     
        webbrowser.open("https://discord.gg/rbd36ERXyu")
        
    @pyqtSlot()
    def on_commandLinkButton_STEAM_clicked(self):  
        """
        Ouvre le lien internet TWITCH TANCRED TERROR
        """
        # TODO: not implemented yet     
        webbrowser.open("https://steamcommunity.com/workshop/filedetails/?id=3048855836")
        
    def on_checkBox_DebugMode_toggled(self, checked):
        """
        Slot documentation goes here.

        @param checked DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        EFK.disk.configSave(self, 'DebugMode', checked)
        
    @pyqtSlot()
    def on_radioButton_EFKEnhanced_clicked(self) -> None:
        """
        Determine la selections des Mods pour EFK Enhanced
        """
        # TODO: not implemented yet
        EFK.disk.install_EFKEnhanced(self)
        EFK.disk.configSave(self, 'Performance', "Enhanced")

    @pyqtSlot()    
    def on_radioButton_EFKStandard_clicked(self) -> None:
        """
        Determine la selections des Mods pour EFK Standard
        """
        # TODO: not implemented yet
        EFK.disk.install_EFKStandard(self)
        EFK.disk.configSave(self, 'Performance', "Standard")
        
    @pyqtSlot()    
    def on_radioButton_EFKNoModif_clicked(self) -> None:
        """
        Determine la selections des Mods pour EFK Standard
        """
        # TODO: not implemented yet
        self.label_alert.setVisible(True)
        self.label_SignAlert.setVisible(True)
        EFK.disk.configSave(self, 'Performance', "")

    @pyqtSlot()
    def on_radioButton_EFKNoModif(self) -> None:
        """
        Valide la langue Francaise et modifie l'interface a la volée
        """
        # Ne modifie plsu la selection des Mods
        EFK.disk.configSave(self, 'Standard', "")

    @pyqtSlot()
    def on_pushButton_MajEFK_clicked(self) -> None:
        """
        Lance la mise a jour de EFK Launcher
        """
        # TODO: not implemented yet
        EFK.core.launch_EFK_launcher_updater(self)
        
    @pyqtSlot()
    def on_pushButton_UninstallEFK_clicked(self) -> None:
        """
        Supprime les scripts et les configs de EFK
        en vue d'une desinstallations 
        """
        # TODO: not implemented yet
        EFK.core.uninstall_EFK_launcher(self)