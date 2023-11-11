#! /usr/bin/python3
#-*- coding: utf-8 -*-
#
# Module Interface CORE

from PyQt6 import QtWidgets
from PyQt6 import QtGui,QtCore
import sys
import os
from . import disk
import json
import shutil


def init_application(self):
    # Définition Constantes
    # Determine repertoire Utilisateur
    disk.get_userPZDir(self)
    loadConfig(self)
    init_MODManager(self)


def loadConfig(self):
    with open("config/EFKLauncher/config.json", "r") as fichier:
        CONFIG = json.load(fichier)
    self.lineEdit_RepertoireSaveGame.setText(CONFIG["SaveGame"])
    
    if CONFIG["Langue"] == "fr-FR":
        self.radioButton_France.setChecked(True)        
    elif CONFIG["Langue"] == "en-GB":
        self.radioButton_English.setChecked(True)
    changeLangue(self,CONFIG["Langue"])

    setFlags(self)

def setFlags(self):
    """
    Verifie l'ensemble des liens pour en determiner la validité
    et modifier les icones correspondant sur l interface
    """

    disk.verif_lien(self, directory=self.lineEdit_ProfilPZ.text(), icon=self.label_IconStatus_ProfilPZ)
    if disk.verif_lien(self,
                       directory=os.path.join(self.lineEdit_ProfilPZ.text()+"/Saves/Sandbox",self.lineEdit_RepertoireSaveGame.text()),
                       icon=self.label_IconStatus_RepertoireSaveGame):
        self.pushButton_WIPE.setEnabled(True)
        self.label_IconStatus_WIPEMAP.setPixmap(QtGui.QPixmap(":/gfx/gfx/checked.png"))
    else :
        self.pushButton_WIPE.setEnabled(False)
        self.label_IconStatus_WIPEMAP.setPixmap(QtGui.QPixmap(":/gfx/gfx/supprimer.png"))
        

    # MOD Manager
    disk.verif_lien(self, file=self.lineEdit_ProfilPZ.text()+"/Lua/saved_modlists.txt", icon=self.label_IconStatus_MODManager)
    # Preset Difficulty
    if not disk.verif_lien(self, file=self.lineEdit_ProfilPZ.text()+"/Sandbox Presets/EFK Easy.cfg", icon=self.label_IconStatus_difficultEASY) :
        shutil.copy('config/difficulty/EFK Easy.cfg', self.lineEdit_ProfilPZ.text()+"/Sandbox Presets/")
        self.label_IconStatus_difficultEASY.setPixmap(QtGui.QPixmap(":/gfx/gfx/valide.png"))

    if not disk.verif_lien(self, file=self.lineEdit_ProfilPZ.text()+"/Sandbox Presets/EFK STD.cfg", icon=self.label_IconStatus_difficultSTD) :
        shutil.copy('config/difficulty/EFK STD.cfg', self.lineEdit_ProfilPZ.text()+"/Sandbox Presets/")
        self.label_IconStatus_difficultSTD.setPixmap(QtGui.QPixmap(":/gfx/gfx/valide.png"))

    if not disk.verif_lien(self, file=self.lineEdit_ProfilPZ.text()+"/Sandbox Presets/EFK Hard.cfg", icon=self.label_IconStatus_difficultHARD) :
        shutil.copy('config/difficulty/EFK Hard.cfg', self.lineEdit_ProfilPZ.text()+"/Sandbox Presets/")
        self.label_IconStatus_difficultHARD.setPixmap(QtGui.QPixmap(":/gfx/gfx/valide.png"))
        
def changeLangue(self, langue):
    app = QtWidgets.QApplication.instance()
    TRANSLATOR = QtCore.QTranslator()
    TRANSLATOR.load(f':/translation/translations/{langue}.qm')
    app.installTranslator(TRANSLATOR)
    main_window = QtWidgets.QMainWindow()
    self.retranslateUi(main_window)


def init_MODManager(self):
    disk.get_MODManager(self)

def writeLog(self,title, texte):
    cursor = self.textEdit_Log.textCursor()
    self.textEdit_Log.insertHtml(f'<strong>{title}</strong> : {texte}<br>')
    self.textEdit_Log.ensureCursorVisible()
################################################################

if __name__ == "__main__":

    # execute when run directly, but not when called as a module.
    # therefore this section allows for testing this module!

    # print "running directly, not as a module!"

    sys.exit()
