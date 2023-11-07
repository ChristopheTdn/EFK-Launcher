from PyQt6 import QtCore


class LaunchPz(QtCore.QObject):
    def __init__(self, Ui):
        super(LaunchPz, self).__init__()
        self.commande = r"F:\SteamLibrary\steamapps\common\ProjectZomboid\ProjectZomboid64.bat"
        self.Ui = Ui
        self.process = None
        self.argument = ""
        self.initClass()

    def initClass(self):
        self.output = self.Ui.textEdit_Log
        self.process = QtCore.QProcess(self)
        self.process.readyReadStandardOutput.connect(self.dataReady)

    def dataReady(self):
        cursor = self.output.textCursor()
        # cursor.movePosition(cursor.End)
        data = str(self.process.readAllStandardOutput())
        self.output.insertHtml(self.parserdata(data))
        self.output.ensureCursorVisible()

    def parserdata(self, data):
        """
        Parcours les données renvoyés par PZ
        """
        listinfo = data.split("\n")
        returnData = ""
        for info in listinfo:
            info = info.replace("\\n", "<br>")\
                .replace("b'", "")\
                .replace('\\r', "")\
                .replace("'", "")\
                .replace('WARN', "<strong>WARN</strong>")\
                .replace('LOG', "<strong>LOG</strong>")\
                .replace('DEBUG', "<strong>DEBUG</strong>")
            if not self.Ui.checkBox_LOGWarn.isChecked() and "<strong>WARN</strong>" in info:
                info =""
            elif not self.Ui.checkBox_LOGDebug.isChecked() and "<strong>DEBUG</strong>" in info:
                info =""
            elif not self.Ui.checkBox_LOG.isChecked() and "<strong>LOG</strong>" in info:
                info =""
            elif info != "":
                returnData += f"{info}"
        return returnData
    
    def parseArguments(self):
        arguments = []
        if self.Ui.checkBox_DebugMode.isChecked():
            arguments.append("-debug")
        return arguments
    
    def start(self):
        self.process.start(self.commande, self.parseArguments())