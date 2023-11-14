# -*- coding: utf-8 -*-

"""
Module implementing Mw_updater.
"""

from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QMainWindow

from Ui_updater import Ui_MainWindow
import EFK


class Mw_updater(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super().__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_ok_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        EFK.maj.init_maj_process(self, "http://www.su66.fr/ftp/efklauncher/EFKLauncher.zip", "tmp", "EFKLauncher.zip")
