# -*- coding: utf-8 -*-

"""
Module implementing Mw_updater.
"""

from PySide6.QtCore import Slot
from PySide6 import QtWidgets
from updater_ui import Ui_MainWindow
import EFK


class Mw_updater(QtWidgets.QMainWindow, Ui_MainWindow):
    """
    Interface QT pour réaliser l'Update du EFK Launcher
    """
    def __init__(self, parent=None):
        """
        Constructeur

        @param : parent reference to the parent widget
        @type QWidget
        """
        super().__init__(parent)
        self.setupUi(self)

        # Si le site n est pas consultable, bloque la possibilité d'Update
        if EFK.core.sysInfo()=="linux":
            if not EFK.reseau.is_website_online(self, "https://su66.fr/ftp/efklauncher/nux/EFKLauncher.zip"):
                EFK.reseau.message(self, "ECHEC : server is offline.")
                self.pushButton_ok.setEnabled(False)
        else : 
            if not EFK.reseau.is_website_online(self, "https://su66.fr/ftp/efklauncher/EFKLauncher.zip"):
                EFK.reseau.message(self, "ECHEC : server is offline.")
                self.pushButton_ok.setEnabled(False)

    @Slot()
    def on_pushButton_ok_clicked(self):
        """
        Valide le debut de la procedure d'update
        """
        if EFK.core.sysInfo()=="linux":
            EFK.reseau.init_maj_process_nux(self, "http://www.su66.fr/ftp/efklauncher/nux/EFKLauncher.zip", "tmp", "EFKLauncher.zip")
        else :
            EFK.reseau.init_maj_process_win(self, "http://www.su66.fr/ftp/efklauncher/EFKLauncher.zip", "tmp", "EFKLauncher.zip")

