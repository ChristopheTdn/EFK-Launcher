#! /usr/bin/python3
#-*- coding: utf-8 -*-
#
# Module Interface CORE

from PyQt6 import QtWidgets
from PyQt6 import QtGui,QtCore
from . import launchpz
import sys
from . import disk
import json


def init_application(self):
    # Définition Constantes
    # Determine repertoire Utilisateur
    disk.get_userPZDir(self)
    loadConfig(self)
    init_MODManager(self)
    init_Difficulty(self)

def loadConfig(self):
    with open("config/EFKLauncher/config.json", "r") as fichier:
        CONFIG = json.load(fichier)
    self.lineEdit_ExePZ.setText(CONFIG["ExePZ"])
    self.lineEdit_RepertoireSaveGame.setText(CONFIG["SaveGame"])
    if CONFIG["Langue"] == "fr-FR":
        self.radioButton_France.setChecked(True)        
    elif CONFIG["Langue"] == "en-GB":
        self.radioButton_English.setChecked(True)
    changeLangue(self,CONFIG["Langue"])

def changeLangue(self, langue):
    app = QtWidgets.QApplication.instance()
    TRANSLATOR = QtCore.QTranslator()
    TRANSLATOR.load(f':/translation/translations/{langue}.qm')
    app.installTranslator(TRANSLATOR)
    main_window = QtWidgets.QMainWindow()
    self.retranslateUi(main_window)


def init_MODManager(self):
    disk.get_MODManager(self)

def init_Difficulty(self):
    disk.get_MODManager(self)

def runPz(self):
    self.process = launchpz.LaunchPz(self)
    self.process.start()


################################################################

if __name__ == "__main__":

    # execute when run directly, but not when called as a module.
    # therefore this section allows for testing this module!

    # print "running directly, not as a module!"

    sys.exit()
