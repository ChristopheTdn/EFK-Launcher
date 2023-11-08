#! /usr/bin/python3
#-*- coding: utf-8 -*-
#
# Module Interface DISK
# Gestion des acces disk et des liens

import os
import json
from PyQt6 import QtWidgets
from PyQt6 import QtGui
from pathlib import Path
from . import disk

def get_userPZDir(self):
    repertoire = str((Path.home()).joinpath("zomboid")).replace("\\","/")
    
    self.lineEdit_ProfilPZ.setText(repertoire)
    disk.verif_lien(self,
                    directory=repertoire,
                    icon=self.label_IconStatus_ProfilPZ
                    )
    disk.configSave(self, "Profil", repertoire)


def get_saveGameDir(self):
    """
    Determine Le dossier de sauvegarde de PZ
    """
    repertoire = QtWidgets.QFileDialog.getExistingDirectory(
        parent=self,
        caption="Select directory",
        directory=self.lineEdit_ProfilPZ.text()+"/Saves/Sandbox",
        options=QtWidgets.QFileDialog.Option.DontUseNativeDialog,
        )
    self.lineEdit_RepertoireSaveGame.setText(repertoire)
    disk.verif_lien(self,
                    directory=repertoire,
                    icon=self.label_IconStatus_RepertoireSaveGame)
    disk.configSave(self,"SaveGame",repertoire)
    
def get_ExePZ(self):
    """
    Determine L executable PZ 
    """
    fichier = QtWidgets.QFileDialog.getOpenFileName(
        parent=self,
        caption="trouve l'executable PZ",
        directory="c:",
        filter = "ProjectZomboid64.bat",
        options=QtWidgets.QFileDialog.Option.DontUseNativeDialog,
        )
    if fichier[0] != "" :
        self.lineEdit_ExePZ.setText(fichier[0])
        disk.verif_lien(self,
                        file=fichier[0],
                        icon=self.label_IconStatus_ExePZ)
        disk.configSave(self,"ExePZ",fichier[0])
    
def get_MODManager(self):
    """
    Determine la présence du fichier de base MODManager et le complete au besoin 
    """
    if not os.path.isfile(self.lineEdit_ProfilPZ.text()+"/Lua/saved_modlists.txt"):
        with open(self.lineEdit_ProfilPZ.text()+"/Lua/saved_modlists.txt", "w") as file:
            file.write("VERSION=2\n")
            file.write("mmFavorites:\n")
        
    disk.verif_lien(self,
                    file=self.lineEdit_ProfilPZ.text()+"/Lua/saved_modlists.txt",
                    icon=self.label_IconStatus_MODManager)
    # determine la presence des profil Standard et Advanced
    with open(self.lineEdit_ProfilPZ.text()+"/Lua/saved_modlists.txt", "r") as file:
            df = file.read()
    
    if "Escape From Knox Project STD:" in df:
        self.checkBox_ProfileEFKStandard.setChecked(True) 
    if "Escape From Knox Project ADV:" in df:
        self.checkBox_ProfileEFKAdvanced.setChecked(True) 

def test_MODManager_STD(self,checked):
    with open("config/modmanager/EFK_STD.txt", "r") as file:
        EFK_STD = file.read()
    with open(self.lineEdit_ProfilPZ.text()+"/Lua/saved_modlists.txt", "r") as file:
        df = file.read()
    if EFK_STD in df and not checked:
        df = df.replace(EFK_STD+"\n","")
    elif EFK_STD not in df and checked :
        df += EFK_STD+"\n"

    with open(self.lineEdit_ProfilPZ.text()+"/Lua/saved_modlists.txt", "w") as file:
        file.write(df)
        
def test_MODManager_ADV(self, checked):
    with open("config/modmanager/EFK_ADV.txt", "r") as file:
        EFK_ADV = file.read()
    with open(self.lineEdit_ProfilPZ.text()+"/Lua/saved_modlists.txt", "r") as file:
        df = file.read()
    if EFK_ADV in df and not checked:
        df = df.replace(EFK_ADV+"\n","")
    elif EFK_ADV not in df and checked :
        df += EFK_ADV+"\n"

    with open(self.lineEdit_ProfilPZ.text()+"/Lua/saved_modlists.txt", "w") as file:
        file.write(df)

def verif_lien(self,
               directory="",
               file="",
               icon=None):
    if directory != "":
        if os.path.isdir(directory):
            icon.setPixmap(QtGui.QPixmap(":/gfx/gfx/valide.png"))
        else:
            icon.setPixmap(QtGui.QPixmap(":/gfx/gfx/supprimer.png"))
    if file != "":
        if os.path.isfile(file):
            icon.setPixmap(QtGui.QPixmap(":/gfx/gfx/valide.png"))
        else:
            icon.setPixmap(QtGui.QPixmap(":/gfx/gfx/supprimer.png"))


def configSave(self, key, valeur):
    with open('config/EFKLauncher/config.json', 'r+') as fichier:
        config = json.load(fichier)
        config[key] = valeur
        fichier.seek(0)
        json.dump(config, fichier, indent=4)
        fichier.truncate()


def delFile(self):
    """_summary_
    """    
    listeProtect =["delfile.exe",
               "delfile.py",
               "fichiers.txt"]
    try :
        with open('config/delfile/fichiers.txt', 'r') as f:
            for line in f:
                listeProtect.append(line.strip())
    except :
        print('ERROR : Impossible de trouver le fichier "fichiers.txt" dans le repertoire.')

    files = os.listdir(self.lineEdit_RepertoireSaveGame.text())
    # pour chaque fichier, test si les fichiers sont dans la liste de fichier à conserver sinon, efface
    for file in files:
        if file not in listeProtect and file[0] != ".":
            os.remove(os.path.join(self.lineEdit_RepertoireSaveGame.text(), file))
            print(f"{file} effacé...")
