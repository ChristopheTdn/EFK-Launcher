# Form implementation generated from reading ui file 'd:\Christophe\Documents\GitHub\EFK\principale.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Fenetre_Principale(object):
    def setupUi(self, Fenetre_Principale):
        Fenetre_Principale.setObjectName("Fenetre_Principale")
        Fenetre_Principale.resize(605, 760)
        Fenetre_Principale.setMinimumSize(QtCore.QSize(605, 760))
        Fenetre_Principale.setMaximumSize(QtCore.QSize(605, 760))
        Fenetre_Principale.setBaseSize(QtCore.QSize(605, 760))
        font = QtGui.QFont()
        font.setPointSize(10)
        Fenetre_Principale.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/gfx/gfx/tt.jpeg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Fenetre_Principale.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(parent=Fenetre_Principale)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget_FenetrePrincipale = QtWidgets.QTabWidget(parent=self.centralWidget)
        self.tabWidget_FenetrePrincipale.setGeometry(QtCore.QRect(5, 385, 581, 266))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget_FenetrePrincipale.setFont(font)
        self.tabWidget_FenetrePrincipale.setToolTip("")
        self.tabWidget_FenetrePrincipale.setObjectName("tabWidget_FenetrePrincipale")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox_ModList = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox_ModList.setGeometry(QtCore.QRect(15, 10, 551, 81))
        self.groupBox_ModList.setObjectName("groupBox_ModList")
        self.label_IconStatus_MODManager = QtWidgets.QLabel(parent=self.groupBox_ModList)
        self.label_IconStatus_MODManager.setGeometry(QtCore.QRect(95, 25, 31, 31))
        self.label_IconStatus_MODManager.setText("")
        self.label_IconStatus_MODManager.setPixmap(QtGui.QPixmap(":/gfx/gfx/supprimer.png"))
        self.label_IconStatus_MODManager.setScaledContents(True)
        self.label_IconStatus_MODManager.setObjectName("label_IconStatus_MODManager")
        self.label = QtWidgets.QLabel(parent=self.groupBox_ModList)
        self.label.setGeometry(QtCore.QRect(130, 25, 371, 26))
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(15, 95, 551, 91))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_difficultEASY = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_difficultEASY.setGeometry(QtCore.QRect(70, 25, 111, 16))
        self.label_difficultEASY.setObjectName("label_difficultEASY")
        self.label_difficultSTD = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_difficultSTD.setGeometry(QtCore.QRect(225, 25, 126, 16))
        self.label_difficultSTD.setObjectName("label_difficultSTD")
        self.label_difficultHARD = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_difficultHARD.setGeometry(QtCore.QRect(400, 25, 121, 16))
        self.label_difficultHARD.setObjectName("label_difficultHARD")
        self.label_IconStatus_difficultEASY = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_IconStatus_difficultEASY.setGeometry(QtCore.QRect(90, 45, 31, 31))
        self.label_IconStatus_difficultEASY.setText("")
        self.label_IconStatus_difficultEASY.setPixmap(QtGui.QPixmap(":/gfx/gfx/supprimer.png"))
        self.label_IconStatus_difficultEASY.setScaledContents(True)
        self.label_IconStatus_difficultEASY.setObjectName("label_IconStatus_difficultEASY")
        self.label_IconStatus_difficultSTD = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_IconStatus_difficultSTD.setGeometry(QtCore.QRect(260, 45, 31, 31))
        self.label_IconStatus_difficultSTD.setText("")
        self.label_IconStatus_difficultSTD.setPixmap(QtGui.QPixmap(":/gfx/gfx/supprimer.png"))
        self.label_IconStatus_difficultSTD.setScaledContents(True)
        self.label_IconStatus_difficultSTD.setObjectName("label_IconStatus_difficultSTD")
        self.label_IconStatus_difficultHARD = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_IconStatus_difficultHARD.setGeometry(QtCore.QRect(435, 40, 31, 31))
        self.label_IconStatus_difficultHARD.setText("")
        self.label_IconStatus_difficultHARD.setPixmap(QtGui.QPixmap(":/gfx/gfx/supprimer.png"))
        self.label_IconStatus_difficultHARD.setScaledContents(True)
        self.label_IconStatus_difficultHARD.setObjectName("label_IconStatus_difficultHARD")
        self.tabWidget_FenetrePrincipale.addTab(self.tab, "")
        self.tab_Log = QtWidgets.QWidget()
        self.tab_Log.setObjectName("tab_Log")
        self.textEdit_Log = QtWidgets.QTextEdit(parent=self.tab_Log)
        self.textEdit_Log.setGeometry(QtCore.QRect(10, 10, 556, 181))
        self.textEdit_Log.setObjectName("textEdit_Log")
        self.checkBox_LOGWarn = QtWidgets.QCheckBox(parent=self.tab_Log)
        self.checkBox_LOGWarn.setGeometry(QtCore.QRect(115, 195, 61, 20))
        self.checkBox_LOGWarn.setObjectName("checkBox_LOGWarn")
        self.checkBox_LOGDebug = QtWidgets.QCheckBox(parent=self.tab_Log)
        self.checkBox_LOGDebug.setGeometry(QtCore.QRect(255, 195, 61, 20))
        self.checkBox_LOGDebug.setObjectName("checkBox_LOGDebug")
        self.checkBox_LOG = QtWidgets.QCheckBox(parent=self.tab_Log)
        self.checkBox_LOG.setGeometry(QtCore.QRect(395, 195, 61, 20))
        self.checkBox_LOG.setObjectName("checkBox_LOG")
        self.tabWidget_FenetrePrincipale.addTab(self.tab_Log, "")
        self.tab_Options = QtWidgets.QWidget()
        self.tab_Options.setObjectName("tab_Options")
        self.groupBox_maj = QtWidgets.QGroupBox(parent=self.tab_Options)
        self.groupBox_maj.setGeometry(QtCore.QRect(10, 5, 241, 216))
        self.groupBox_maj.setObjectName("groupBox_maj")
        self.pushButton_MajEFK = QtWidgets.QPushButton(parent=self.groupBox_maj)
        self.pushButton_MajEFK.setEnabled(True)
        self.pushButton_MajEFK.setGeometry(QtCore.QRect(15, 135, 216, 51))
        font = QtGui.QFont()
        font.setFamily("Bender")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_MajEFK.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/gfx/gfx/update.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_MajEFK.setIcon(icon1)
        self.pushButton_MajEFK.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_MajEFK.setObjectName("pushButton_MajEFK")
        self.label_MajEFKLauncherTexte = QtWidgets.QLabel(parent=self.groupBox_maj)
        self.label_MajEFKLauncherTexte.setGeometry(QtCore.QRect(20, 35, 206, 81))
        self.label_MajEFKLauncherTexte.setObjectName("label_MajEFKLauncherTexte")
        self.label_noConnexion = QtWidgets.QLabel(parent=self.groupBox_maj)
        self.label_noConnexion.setGeometry(QtCore.QRect(15, 190, 211, 21))
        self.label_noConnexion.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_noConnexion.setObjectName("label_noConnexion")
        self.label_UpdateAvailable = QtWidgets.QLabel(parent=self.groupBox_maj)
        self.label_UpdateAvailable.setGeometry(QtCore.QRect(20, 105, 206, 21))
        self.label_UpdateAvailable.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.label_UpdateAvailable.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_UpdateAvailable.setObjectName("label_UpdateAvailable")
        self.groupBox_UninstallEFK = QtWidgets.QGroupBox(parent=self.tab_Options)
        self.groupBox_UninstallEFK.setGeometry(QtCore.QRect(265, 5, 296, 216))
        self.groupBox_UninstallEFK.setObjectName("groupBox_UninstallEFK")
        self.pushButton_UninstallEFK = QtWidgets.QPushButton(parent=self.groupBox_UninstallEFK)
        self.pushButton_UninstallEFK.setEnabled(True)
        self.pushButton_UninstallEFK.setGeometry(QtCore.QRect(10, 135, 266, 51))
        font = QtGui.QFont()
        font.setFamily("Bender")
        font.setPointSize(18)
        font.setBold(True)
        self.pushButton_UninstallEFK.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/gfx/gfx/skull.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_UninstallEFK.setIcon(icon2)
        self.pushButton_UninstallEFK.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_UninstallEFK.setObjectName("pushButton_UninstallEFK")
        self.label_UninstallEFK = QtWidgets.QLabel(parent=self.groupBox_UninstallEFK)
        self.label_UninstallEFK.setGeometry(QtCore.QRect(15, 25, 266, 116))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_UninstallEFK.setFont(font)
        self.label_UninstallEFK.setObjectName("label_UninstallEFK")
        self.tabWidget_FenetrePrincipale.addTab(self.tab_Options, "")
        self.groupBox_UserDir = QtWidgets.QGroupBox(parent=self.centralWidget)
        self.groupBox_UserDir.setGeometry(QtCore.QRect(15, 175, 576, 116))
        self.groupBox_UserDir.setObjectName("groupBox_UserDir")
        self.lineEdit_ProfilPZ = QtWidgets.QLineEdit(parent=self.groupBox_UserDir)
        self.lineEdit_ProfilPZ.setGeometry(QtCore.QRect(95, 55, 351, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setKerning(True)
        self.lineEdit_ProfilPZ.setFont(font)
        self.lineEdit_ProfilPZ.setReadOnly(True)
        self.lineEdit_ProfilPZ.setObjectName("lineEdit_ProfilPZ")
        self.label_IconStatus_RepertoireSaveGame = QtWidgets.QLabel(parent=self.groupBox_UserDir)
        self.label_IconStatus_RepertoireSaveGame.setGeometry(QtCore.QRect(455, 75, 31, 31))
        self.label_IconStatus_RepertoireSaveGame.setText("")
        self.label_IconStatus_RepertoireSaveGame.setPixmap(QtGui.QPixmap(":/gfx/gfx/supprimer.png"))
        self.label_IconStatus_RepertoireSaveGame.setScaledContents(True)
        self.label_IconStatus_RepertoireSaveGame.setObjectName("label_IconStatus_RepertoireSaveGame")
        self.lineEdit_RepertoireSaveGame = QtWidgets.QLineEdit(parent=self.groupBox_UserDir)
        self.lineEdit_RepertoireSaveGame.setGeometry(QtCore.QRect(95, 80, 351, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setKerning(True)
        self.lineEdit_RepertoireSaveGame.setFont(font)
        self.lineEdit_RepertoireSaveGame.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_RepertoireSaveGame.setReadOnly(True)
        self.lineEdit_RepertoireSaveGame.setObjectName("lineEdit_RepertoireSaveGame")
        self.label_IconStatus_ProfilPZ = QtWidgets.QLabel(parent=self.groupBox_UserDir)
        self.label_IconStatus_ProfilPZ.setGeometry(QtCore.QRect(455, 50, 31, 31))
        self.label_IconStatus_ProfilPZ.setText("")
        self.label_IconStatus_ProfilPZ.setPixmap(QtGui.QPixmap(":/gfx/gfx/supprimer.png"))
        self.label_IconStatus_ProfilPZ.setScaledContents(True)
        self.label_IconStatus_ProfilPZ.setObjectName("label_IconStatus_ProfilPZ")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_UserDir)
        self.label_4.setGeometry(QtCore.QRect(10, 55, 81, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_UserDir)
        self.label_5.setGeometry(QtCore.QRect(10, 80, 81, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.pushButton_SetRepertoireSaveGame = QtWidgets.QPushButton(parent=self.groupBox_UserDir)
        self.pushButton_SetRepertoireSaveGame.setGeometry(QtCore.QRect(495, 80, 71, 24))
        self.pushButton_SetRepertoireSaveGame.setObjectName("pushButton_SetRepertoireSaveGame")
        self.lineEdit_ExePZ = QtWidgets.QLineEdit(parent=self.groupBox_UserDir)
        self.lineEdit_ExePZ.setGeometry(QtCore.QRect(95, 30, 351, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setKerning(True)
        self.lineEdit_ExePZ.setFont(font)
        self.lineEdit_ExePZ.setReadOnly(True)
        self.lineEdit_ExePZ.setObjectName("lineEdit_ExePZ")
        self.label_IconStatus_ExePZ = QtWidgets.QLabel(parent=self.groupBox_UserDir)
        self.label_IconStatus_ExePZ.setGeometry(QtCore.QRect(455, 25, 31, 31))
        self.label_IconStatus_ExePZ.setText("")
        self.label_IconStatus_ExePZ.setPixmap(QtGui.QPixmap(":/gfx/gfx/supprimer.png"))
        self.label_IconStatus_ExePZ.setScaledContents(True)
        self.label_IconStatus_ExePZ.setObjectName("label_IconStatus_ExePZ")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_UserDir)
        self.label_6.setGeometry(QtCore.QRect(10, 30, 81, 20))
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.pushButton_SetExePZ = QtWidgets.QPushButton(parent=self.groupBox_UserDir)
        self.pushButton_SetExePZ.setGeometry(QtCore.QRect(495, 30, 71, 24))
        self.pushButton_SetExePZ.setObjectName("pushButton_SetExePZ")
        self.label_Titre = QtWidgets.QLabel(parent=self.centralWidget)
        self.label_Titre.setGeometry(QtCore.QRect(105, 10, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Bender")
        font.setPointSize(36)
        font.setBold(False)
        self.label_Titre.setFont(font)
        self.label_Titre.setObjectName("label_Titre")
        self.label_2 = QtWidgets.QLabel(parent=self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(5, 10, 91, 91))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("d:\\Christophe\\Documents\\GitHub\\EFK\\gfx/EFK.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_Danger = QtWidgets.QLabel(parent=self.centralWidget)
        self.label_Danger.setGeometry(QtCore.QRect(320, 675, 51, 46))
        self.label_Danger.setText("")
        self.label_Danger.setPixmap(QtGui.QPixmap(":/gfx/gfx/danger.png"))
        self.label_Danger.setScaledContents(True)
        self.label_Danger.setObjectName("label_Danger")
        self.pushButton_WIPE = QtWidgets.QPushButton(parent=self.centralWidget)
        self.pushButton_WIPE.setGeometry(QtCore.QRect(95, 670, 166, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_WIPE.setFont(font)
        self.pushButton_WIPE.setObjectName("pushButton_WIPE")
        self.label_Titre_2 = QtWidgets.QLabel(parent=self.centralWidget)
        self.label_Titre_2.setGeometry(QtCore.QRect(380, 660, 196, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        self.label_Titre_2.setFont(font)
        self.label_Titre_2.setObjectName("label_Titre_2")
        self.commandLinkButton_Twitch = QtWidgets.QCommandLinkButton(parent=self.centralWidget)
        self.commandLinkButton_Twitch.setGeometry(QtCore.QRect(95, 70, 36, 36))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.commandLinkButton_Twitch.setFont(font)
        self.commandLinkButton_Twitch.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/gfx/gfx/Twitch-logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.commandLinkButton_Twitch.setIcon(icon3)
        self.commandLinkButton_Twitch.setObjectName("commandLinkButton_Twitch")
        self.commandLinkButton_Youtube = QtWidgets.QCommandLinkButton(parent=self.centralWidget)
        self.commandLinkButton_Youtube.setGeometry(QtCore.QRect(125, 70, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.commandLinkButton_Youtube.setFont(font)
        self.commandLinkButton_Youtube.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/gfx/gfx/youtube.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.commandLinkButton_Youtube.setIcon(icon4)
        self.commandLinkButton_Youtube.setIconSize(QtCore.QSize(30, 30))
        self.commandLinkButton_Youtube.setObjectName("commandLinkButton_Youtube")
        self.commandLinkButton_Discord = QtWidgets.QCommandLinkButton(parent=self.centralWidget)
        self.commandLinkButton_Discord.setGeometry(QtCore.QRect(165, 70, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.commandLinkButton_Discord.setFont(font)
        self.commandLinkButton_Discord.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/gfx/gfx/discord.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.commandLinkButton_Discord.setIcon(icon5)
        self.commandLinkButton_Discord.setIconSize(QtCore.QSize(30, 30))
        self.commandLinkButton_Discord.setObjectName("commandLinkButton_Discord")
        self.label_IconStatus_WIPEMAP = QtWidgets.QLabel(parent=self.centralWidget)
        self.label_IconStatus_WIPEMAP.setGeometry(QtCore.QRect(35, 670, 51, 46))
        self.label_IconStatus_WIPEMAP.setText("")
        self.label_IconStatus_WIPEMAP.setPixmap(QtGui.QPixmap(":/gfx/gfx/supprimer.png"))
        self.label_IconStatus_WIPEMAP.setScaledContents(True)
        self.label_IconStatus_WIPEMAP.setObjectName("label_IconStatus_WIPEMAP")
        self.commandLinkButton_STEAM = QtWidgets.QCommandLinkButton(parent=self.centralWidget)
        self.commandLinkButton_STEAM.setGeometry(QtCore.QRect(15, 105, 581, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setKerning(False)
        self.commandLinkButton_STEAM.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/gfx/gfx/Steam_Icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.commandLinkButton_STEAM.setIcon(icon6)
        self.commandLinkButton_STEAM.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton_STEAM.setCheckable(False)
        self.commandLinkButton_STEAM.setObjectName("commandLinkButton_STEAM")
        self.pushButton_RunPZ = QtWidgets.QPushButton(parent=self.centralWidget)
        self.pushButton_RunPZ.setGeometry(QtCore.QRect(445, 20, 141, 46))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_RunPZ.setFont(font)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/gfx/gfx/pz.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_RunPZ.setIcon(icon7)
        self.pushButton_RunPZ.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_RunPZ.setObjectName("pushButton_RunPZ")
        self.checkBox_DebugMode = QtWidgets.QCheckBox(parent=self.centralWidget)
        self.checkBox_DebugMode.setGeometry(QtCore.QRect(465, 65, 101, 20))
        self.checkBox_DebugMode.setObjectName("checkBox_DebugMode")
        self.groupBox_EFKEnhanced = QtWidgets.QGroupBox(parent=self.centralWidget)
        self.groupBox_EFKEnhanced.setGeometry(QtCore.QRect(15, 290, 576, 86))
        self.groupBox_EFKEnhanced.setObjectName("groupBox_EFKEnhanced")
        self.radioButton_EFKStandard = QtWidgets.QRadioButton(parent=self.groupBox_EFKEnhanced)
        self.radioButton_EFKStandard.setGeometry(QtCore.QRect(115, 40, 216, 20))
        self.radioButton_EFKStandard.setObjectName("radioButton_EFKStandard")
        self.radioButton_EFKEnhanced = QtWidgets.QRadioButton(parent=self.groupBox_EFKEnhanced)
        self.radioButton_EFKEnhanced.setGeometry(QtCore.QRect(115, 20, 216, 20))
        self.radioButton_EFKEnhanced.setChecked(True)
        self.radioButton_EFKEnhanced.setObjectName("radioButton_EFKEnhanced")
        self.label_CPULogo = QtWidgets.QLabel(parent=self.groupBox_EFKEnhanced)
        self.label_CPULogo.setGeometry(QtCore.QRect(30, 20, 51, 51))
        self.label_CPULogo.setText("")
        self.label_CPULogo.setPixmap(QtGui.QPixmap(":/gfx/gfx/performance.png"))
        self.label_CPULogo.setScaledContents(True)
        self.label_CPULogo.setObjectName("label_CPULogo")
        self.radioButton_EFKNoModif = QtWidgets.QRadioButton(parent=self.groupBox_EFKEnhanced)
        self.radioButton_EFKNoModif.setGeometry(QtCore.QRect(115, 60, 216, 20))
        self.radioButton_EFKNoModif.setObjectName("radioButton_EFKNoModif")
        self.label_alert = QtWidgets.QLabel(parent=self.groupBox_EFKEnhanced)
        self.label_alert.setGeometry(QtCore.QRect(350, 10, 206, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        self.label_alert.setFont(font)
        self.label_alert.setObjectName("label_alert")
        self.label_SignAlert = QtWidgets.QLabel(parent=self.groupBox_EFKEnhanced)
        self.label_SignAlert.setGeometry(QtCore.QRect(325, 25, 21, 51))
        self.label_SignAlert.setText("")
        self.label_SignAlert.setPixmap(QtGui.QPixmap(":/gfx/gfx/accolade.png"))
        self.label_SignAlert.setScaledContents(True)
        self.label_SignAlert.setObjectName("label_SignAlert")
        self.label_UpdateAvailable_2 = QtWidgets.QLabel(parent=self.centralWidget)
        self.label_UpdateAvailable_2.setGeometry(QtCore.QRect(165, 375, 146, 21))
        self.label_UpdateAvailable_2.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.label_UpdateAvailable_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_UpdateAvailable_2.setObjectName("label_UpdateAvailable_2")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(335, 5, 96, 111))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.radioButton_France = QtWidgets.QRadioButton(parent=self.groupBox)
        self.radioButton_France.setGeometry(QtCore.QRect(20, 10, 56, 26))
        self.radioButton_France.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/gfx/gfx/france.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.radioButton_France.setIcon(icon8)
        self.radioButton_France.setIconSize(QtCore.QSize(32, 32))
        self.radioButton_France.setCheckable(True)
        self.radioButton_France.setChecked(False)
        self.radioButton_France.setObjectName("radioButton_France")
        self.radioButton_English = QtWidgets.QRadioButton(parent=self.groupBox)
        self.radioButton_English.setGeometry(QtCore.QRect(20, 45, 56, 26))
        self.radioButton_English.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/gfx/gfx/royaumeunis.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.radioButton_English.setIcon(icon9)
        self.radioButton_English.setIconSize(QtCore.QSize(32, 32))
        self.radioButton_English.setCheckable(True)
        self.radioButton_English.setChecked(False)
        self.radioButton_English.setObjectName("radioButton_English")
        self.radioButton_Chine = QtWidgets.QRadioButton(parent=self.groupBox)
        self.radioButton_Chine.setGeometry(QtCore.QRect(20, 75, 56, 26))
        self.radioButton_Chine.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/gfx/gfx/chine.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.radioButton_Chine.setIcon(icon10)
        self.radioButton_Chine.setIconSize(QtCore.QSize(32, 32))
        self.radioButton_Chine.setCheckable(True)
        self.radioButton_Chine.setChecked(True)
        self.radioButton_Chine.setObjectName("radioButton_Chine")
        Fenetre_Principale.setCentralWidget(self.centralWidget)

        self.retranslateUi(Fenetre_Principale)
        self.tabWidget_FenetrePrincipale.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Fenetre_Principale)

    def retranslateUi(self, Fenetre_Principale):
        _translate = QtCore.QCoreApplication.translate
        Fenetre_Principale.setWindowTitle(_translate("Fenetre_Principale", "Escape From Knox County Configurator"))
        self.groupBox_ModList.setTitle(_translate("Fenetre_Principale", "MOD Manager"))
        self.label.setText(_translate("Fenetre_Principale", "<html><head/><body><p align=\"center\">Ajout Profil <span style=\" font-weight:700;\">STANDARD</span> et <span style=\" font-weight:700;\">ADVANCED</span> à <span style=\" font-weight:700; font-style:italic;\">Lua/saved_modlists.txt</span></p></body></html>"))
        self.groupBox_2.setTitle(_translate("Fenetre_Principale", "Préreglage Difficulté"))
        self.label_difficultEASY.setText(_translate("Fenetre_Principale", "Facile (EFK_Easy)"))
        self.label_difficultSTD.setText(_translate("Fenetre_Principale", "Standard (EFK_STD)"))
        self.label_difficultHARD.setText(_translate("Fenetre_Principale", "Difficile (EFK_Hard)"))
        self.tabWidget_FenetrePrincipale.setTabText(self.tabWidget_FenetrePrincipale.indexOf(self.tab), _translate("Fenetre_Principale", "Installation"))
        self.checkBox_LOGWarn.setText(_translate("Fenetre_Principale", "WARN"))
        self.checkBox_LOGDebug.setText(_translate("Fenetre_Principale", "DEBUG"))
        self.checkBox_LOG.setText(_translate("Fenetre_Principale", "LOG"))
        self.tabWidget_FenetrePrincipale.setTabText(self.tabWidget_FenetrePrincipale.indexOf(self.tab_Log), _translate("Fenetre_Principale", "Log"))
        self.groupBox_maj.setTitle(_translate("Fenetre_Principale", "Mise a Jour EFK Launcher"))
        self.pushButton_MajEFK.setText(_translate("Fenetre_Principale", "Maj EFK Launcher"))
        self.label_MajEFKLauncherTexte.setText(_translate("Fenetre_Principale", "<html><head/><body><p><span style=\" font-weight:700; text-decoration: underline;\">MaJ EFK :</span></p><p>Pour mettre a jour <span style=\" font-weight:700;\">EFK Launcher</span>,<br/>et les scripts de config EFK.<br/></p><p><br/></p></body></html>"))
        self.label_noConnexion.setText(_translate("Fenetre_Principale", "<html><head/><body><p><img src=\":/gfx/gfx/supprimer.png\" width=\"22\"/><span style=\" font-size:12pt; vertical-align:super;\">Serveur MAJ non trouvé</span></p></body></html>"))
        self.label_UpdateAvailable.setText(_translate("Fenetre_Principale", "<html><head/><body><p><img src=\":/gfx/gfx/danger.png\" width=\"20\"/><span style=\" font-size:14pt; font-weight:700; color:#ff5500; vertical-align:super;\">Mise a jour disponible</span></p></body></html>"))
        self.groupBox_UninstallEFK.setTitle(_translate("Fenetre_Principale", "Désinstaller EFK"))
        self.pushButton_UninstallEFK.setText(_translate("Fenetre_Principale", "Desinstaller EFK"))
        self.label_UninstallEFK.setText(_translate("Fenetre_Principale", "<html><head/><body><p><span style=\" font-weight:700; text-decoration: underline;\">Pour desintaller EFK :<br/></span>1 - Quitter Project Zomboid<br/>2 - Se Désabonner à la <a href=\"https://steamcommunity.com/workshop/filedetails/?id=3048855836\"><span style=\" text-decoration: underline; color:#0000ff;\">collection Steam EFK<br/></span></a>3 - Cliquer sur <span style=\" font-weight:700;\">Desinstaller EFK<br/></span>4 - Une fois le EFK Launcher Fermé<br/>Supprimer votre repertoire local du <span style=\" font-weight:700;\">EFK Launcher</span></p><p><span style=\" font-weight:700;\"><br/></span></p></body></html>"))
        self.tabWidget_FenetrePrincipale.setTabText(self.tabWidget_FenetrePrincipale.indexOf(self.tab_Options), _translate("Fenetre_Principale", "Options"))
        self.groupBox_UserDir.setTitle(_translate("Fenetre_Principale", "Repertoires Utilisateur"))
        self.label_4.setText(_translate("Fenetre_Principale", "Profil PZ :"))
        self.label_5.setText(_translate("Fenetre_Principale", "Sauvegardes :"))
        self.pushButton_SetRepertoireSaveGame.setText(_translate("Fenetre_Principale", "choisir"))
        self.label_6.setText(_translate("Fenetre_Principale", "Exe PZ :"))
        self.pushButton_SetExePZ.setText(_translate("Fenetre_Principale", "choisir"))
        self.label_Titre.setText(_translate("Fenetre_Principale", "<html><head/><body><p align=\"justify\"><span style=\" font-size:24pt; font-weight:700;\">ESCAPE FROM<br/>KNOX COUNTY</span></p></body></html>"))
        self.pushButton_WIPE.setText(_translate("Fenetre_Principale", "WIPE MAP"))
        self.label_Titre_2.setText(_translate("Fenetre_Principale", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:700; text-decoration: underline; color:#aa0000;\">IMPORTANT :</span><span style=\" font-weight:700; text-decoration: underline;\"><br/></span><span style=\" font-weight:700;\">- </span>Entre 2 raids<br/>- personnage dans la base<br/>- Quitter PZ ou au Menu principal</p></body></html>"))
        self.commandLinkButton_Twitch.setToolTip(_translate("Fenetre_Principale", "Chaine Twitch de Tancred terror"))
        self.commandLinkButton_Youtube.setToolTip(_translate("Fenetre_Principale", "Chaine YOUTUBE de Tancred terror"))
        self.commandLinkButton_Discord.setToolTip(_translate("Fenetre_Principale", "DISCORD de Tancred terror"))
        self.commandLinkButton_STEAM.setToolTip(_translate("Fenetre_Principale", "La collection de mods EFKC"))
        self.commandLinkButton_STEAM.setText(_translate("Fenetre_Principale", "Abonnements à la collection STEAM ESCAPE FROM KNOX COUNTY"))
        self.pushButton_RunPZ.setText(_translate("Fenetre_Principale", "RUN PZ"))
        self.checkBox_DebugMode.setText(_translate("Fenetre_Principale", "Mode DEBUG"))
        self.groupBox_EFKEnhanced.setTitle(_translate("Fenetre_Principale", "EFK Performances impact"))
        self.radioButton_EFKStandard.setText(_translate("Fenetre_Principale", "EFK Standard (Low CPU Power)"))
        self.radioButton_EFKEnhanced.setText(_translate("Fenetre_Principale", "EFK Enhanced (High CPU Power)"))
        self.radioButton_EFKNoModif.setText(_translate("Fenetre_Principale", "No Modif (For Modders Only)"))
        self.label_alert.setText(_translate("Fenetre_Principale", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:700; text-decoration: underline; color:#aa0000;\">IMPORTANT :</span><span style=\" font-weight:700; text-decoration: underline;\"><br/></span>If you\'re not a Modder,<br/>Please make a choice EFK Enhanced<br/>or EFK Standard <span style=\" font-weight:700; text-decoration: underline;\">Before</span> Launch PZ</p></body></html>"))
        self.label_UpdateAvailable_2.setText(_translate("Fenetre_Principale", "<html><head/><body><p><img src=\":/gfx/gfx/danger.png\" width=\"20\"/><span style=\" font-size:14pt; font-weight:700; color:#ff5500; vertical-align:super;\">Mise a jour disponible</span></p></body></html>"))
        self.radioButton_France.setToolTip(_translate("Fenetre_Principale", "French"))
        self.radioButton_English.setToolTip(_translate("Fenetre_Principale", "French"))
        self.radioButton_Chine.setToolTip(_translate("Fenetre_Principale", "French"))
