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
# Module Interface
# Class LaunchSteam >> launch steam process
"""

from PySide6 import QtCore


class LaunchSteam(QtCore.QObject):
    """Genere un process pour lancer l application
        externe steam

    Args:
        QtCore (_type_): process QT parent pour
            permettre un lancement asynchrone
    """    
    def __init__(self, Ui, executable, argument=[]):
        super(LaunchSteam, self).__init__()
        self.commande = executable
        self.Ui = Ui
        self.argument = argument
        self.process = None
        self.initClass()

    def initClass(self):
        self.output = self.Ui.textEdit_Log
        self.process = QtCore.QProcess(self)

    def parseArguments(self):
        if self.Ui.checkBox_DebugMode.isChecked():
            self.argument.append("steam://run/108600//-debug/")
        else:
            self.argument.append("steam://run/108600/")

    def start(self):
        if self.argument is not []:
            self.parseArguments()
        self.process.start(self.commande, self.argument)
