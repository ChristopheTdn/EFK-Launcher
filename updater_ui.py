# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'updater.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QWidget)
import ressources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 140)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(400, 140))
        MainWindow.setMaximumSize(QSize(400, 140))
        MainWindow.setBaseSize(QSize(400, 140))
        icon = QIcon()
        icon.addFile(u":/gfx/gfx/tt.jpeg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.label = QLabel(self.centralWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 111, 106))
        self.label.setPixmap(QPixmap(u":/gfx/gfx/EFK.png"))
        self.label.setScaledContents(True)
        self.label_titre = QLabel(self.centralWidget)
        self.label_titre.setObjectName(u"label_titre")
        self.label_titre.setGeometry(QRect(140, 10, 221, 36))
        font = QFont()
        font.setPointSize(16)
        self.label_titre.setFont(font)
        self.pushButton_ok = QPushButton(self.centralWidget)
        self.pushButton_ok.setObjectName(u"pushButton_ok")
        self.pushButton_ok.setGeometry(QRect(199, 102, 86, 26))
        font1 = QFont()
        font1.setPointSize(11)
        self.pushButton_ok.setFont(font1)
        self.progressBar = QProgressBar(self.centralWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(135, 50, 231, 16))
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)
        self.label_feedback = QLabel(self.centralWidget)
        self.label_feedback.setObjectName(u"label_feedback")
        self.label_feedback.setGeometry(QRect(135, 70, 226, 31))
        self.label_feedback.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"EFK Launcher Updater", None))
        self.label.setText("")
        self.label_titre.setText(QCoreApplication.translate("MainWindow", u"EFK Launcher Updater", None))
        self.pushButton_ok.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_feedback.setText("")
    # retranslateUi

