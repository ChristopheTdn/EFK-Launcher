# Form implementation generated from reading ui file 'd:\Christophe\Documents\GitHub\EFK\updater.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 140)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(400, 140))
        MainWindow.setMaximumSize(QtCore.QSize(400, 140))
        MainWindow.setBaseSize(QtCore.QSize(400, 140))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/gfx/gfx/tt.jpeg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(parent=self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 111, 106))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/gfx/gfx/EFK.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_titre = QtWidgets.QLabel(parent=self.centralWidget)
        self.label_titre.setGeometry(QtCore.QRect(150, 10, 206, 36))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_titre.setFont(font)
        self.label_titre.setObjectName("label_titre")
        self.pushButton_ok = QtWidgets.QPushButton(parent=self.centralWidget)
        self.pushButton_ok.setGeometry(QtCore.QRect(199, 102, 86, 26))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_ok.setFont(font)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.progressBar = QtWidgets.QProgressBar(parent=self.centralWidget)
        self.progressBar.setGeometry(QtCore.QRect(135, 50, 231, 16))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.label_feedback = QtWidgets.QLabel(parent=self.centralWidget)
        self.label_feedback.setGeometry(QtCore.QRect(135, 70, 226, 31))
        self.label_feedback.setText("")
        self.label_feedback.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_feedback.setObjectName("label_feedback")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EFK Launcher Updater"))
        self.label_titre.setText(_translate("MainWindow", "EFK Launcher Updater"))
        self.pushButton_ok.setText(_translate("MainWindow", "Update"))