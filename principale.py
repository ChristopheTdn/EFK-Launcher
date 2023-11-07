# -*- coding: utf-8 -*-

"""
Module implementing Fenetre_Principale.
"""

from PyQt6.QtCore import pyqtSlot,QTranslator
from PyQt6.QtWidgets import QMainWindow
from PyQt6 import QtGui
from Ui_principale import Ui_Fenetre_Principale
import EFK
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
    def on_pushButton_RunPZ_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        EFK.core.runPz(self)
        
    @pyqtSlot()
    def on_lineEdit_ProfilPZ_editingFinished(self):
        """
        Evenement appelé lors de la validation de la ligne de saisie
        de Ui.lineEdit_ProfilPZ
        """
        # TODO: not implemented yet
        EFK.disk.verif_lien(self,
                            directory=self.lineEdit_ProfilPZ.text(),
                            icon=self.label_IconStatus_ProfilPZ)
        

    @pyqtSlot()
    def on_lineEdit_RepertoireSaveGame_editingFinished(self):
        """
        test signal
        """
        # TODO: not implemented yet
        EFK.disk.verif_lien(self,
                            directory=self.lineEdit_RepertoireSaveGame.text(),
                            icon=self.label_IconStatus_RepertoireSaveGame)


    @pyqtSlot()
    def on_pushButton_SetRepertoireSaveGame_clicked(self):  
        """
        Evenement appelé lors du clique sur le bouton pour choisir
        le repertoire de sauvegarde
        """
        # TODO: not implemented yet     
        EFK.disk.get_saveGameDir(self)
        
    @pyqtSlot()
    def on_pushButton_SetExePZ_clicked(self):  
        """
        Evenement appelé lors du clique sur le bouton pour choisir
        l'exe PZ
        """
        # TODO: not implemented yet     
        EFK.disk.get_ExePZ(self)
     
    @pyqtSlot(bool)
    def on_checkBox_ProfileEFKStandard_toggled(self, checked):
        """
        Slot documentation goes here.

        @param checked DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        EFK.disk.test_MODManager_STD(self,checked)
        
    @pyqtSlot(bool)
    def on_checkBox_ProfileEFKAdvanced_toggled(self, checked):
        """
        Slot documentation goes here.

        @param checked DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        EFK.disk.test_MODManager_ADV(self,checked)
    
    @pyqtSlot()
    def on_radioButton_France_clicked(self):
        """
        Valide la langue Francaise et modifie l'interface a la volée
        """
        # TODO: not implemented yet
        EFK.core.changeLangue(self, 'fr-FR')
        EFK.disk.configSave(self, 'Langue', 'fr-FR')

    @pyqtSlot()
    def on_radioButton_English_clicked(self):
        """
        Valide la langue Francaise et modifie l'interface a la volée
        """
        # TODO: not implemented yet
        EFK.core.changeLangue(self, 'en-GB')
        EFK.disk.configSave(self, 'Langue', 'en-GB')