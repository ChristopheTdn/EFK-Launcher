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
Module implementing Mw_updater.
"""
from PySide6 import QtWidgets
from PySide6.QtCore import Slot
from PySide6.QtCore import QCoreApplication
from PySide6 import QtWidgets
from updater_ui import Ui_Updater_MainWindow
import EFK
import ressources_rc  # necessaire pour integrer les ressources

class Mw_updater(QtWidgets.QMainWindow, Ui_Updater_MainWindow):
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
        if EFK.core.sysInfo() == "linux":
            if not EFK.reseau.is_website_online("Updater_MainWindow",
                                                "https://su66.fr/ftp/efklauncher/nux/EFKLauncher.zip"):
                EFK.reseau.message(self,
                                   QCoreApplication.translate("Updater_MainWindow",
                                                                    "ERROR_Server_Offline"))
                self.pushButton_ok.setEnabled(False)
        else :
            if not EFK.reseau.is_website_online("Updater_MainWindow",
                                                "https://su66.fr/ftp/efklauncher/EFKLauncher.zip"):
                EFK.reseau.message(self,
                                   QCoreApplication.translate("Updater_MainWindow",
                                                              "ERROR_Server_Offline",
                                                              None))
                self.pushButton_ok.setEnabled(False)
        
    @Slot()
    def on_pushButton_ok_clicked(self):
        """
        Valide le debut de la procedure d'update
        """
        if EFK.core.sysInfo() == "linux":
            EFK.reseau.init_maj_process_nux(self, "http://www.su66.fr/ftp/efklauncher/nux/EFKLauncher.zip", "tmp", "EFKLauncher.zip")
        else:
            EFK.reseau.init_maj_process_win(self, "http://www.su66.fr/ftp/efklauncher/EFKLauncher.zip", "tmp", "EFKLauncher.zip")
