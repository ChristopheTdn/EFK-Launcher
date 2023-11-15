# -*- coding: utf-8 -*-

"""
Module implementing Mw_updater.
"""

from PyQt6.QtCore import pyqtSlot
from PyQt6 import QtWidgets
from Ui_updater import Ui_MainWindow
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
        if not EFK.reseau.is_website_online(self, "https://su66.fr/ftp/efklauncher/EFKLauncher.zip"):
            EFK.reseau.message(self, "ECHEC : le serveur ne repond pas.")
            self.pushButton_ok.setEnabled(False)

    @pyqtSlot()
    def on_pushButton_ok_clicked(self):
        """
        Valide le debut de la procedure d'update
        """
        EFK.reseau.init_maj_process(self, "http://www.su66.fr/ftp/efklauncher/EFKLauncher.zip", "tmp", "EFKLauncher.zip")

