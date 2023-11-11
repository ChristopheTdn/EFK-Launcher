#! /usr/bin/python3
# -*- coding: utf-8 -*-
#
# Module Interface DISK
# Gestion des acces disk et des liens

import os
import json
from PyQt6 import QtWidgets
from PyQt6 import QtGui
from pathlib import Path
from . import disk
from . import core


def get_userPZDir(self):
    repertoire = str((Path.home()).joinpath("zomboid")).replace("\\", "/")

    self.lineEdit_ProfilPZ.setText(repertoire)
    if disk.verif_lien(self, directory=repertoire, icon=self.label_IconStatus_ProfilPZ):
        disk.configSave(self, "Profil", repertoire)


def get_saveGameDir(self):
    """
    Determine Le dossier de sauvegarde de PZ
    """
    repertoire = QtWidgets.QFileDialog.getExistingDirectory(
        parent=self,
        caption="Select directory",
        directory=self.lineEdit_ProfilPZ.text() + "/Saves/Sandbox",
        options=QtWidgets.QFileDialog.Option.DontUseNativeDialog,
    )
    name = os.path.basename(repertoire)
    self.lineEdit_RepertoireSaveGame.setText(name)
    self.pushButton_WIPE.setEnabled(False)
    self.label_IconStatus_WIPEMAP.setPixmap(QtGui.QPixmap(":/gfx/gfx/supprimer.png"))
    self.label_IconStatus_RepertoireSaveGame.setPixmap(
        QtGui.QPixmap(":/gfx/gfx/supprimer.png")
    )
    if name != "":
        if disk.verif_lien(
            self,
            directory=os.path.join(
                self.lineEdit_ProfilPZ.text() + "/Saves/Sandbox", name
            ),
            icon=self.label_IconStatus_RepertoireSaveGame,
        ):
            disk.configSave(self, "SaveGame", name)
            self.pushButton_WIPE.setEnabled(True)
            self.label_IconStatus_WIPEMAP.setPixmap(
                QtGui.QPixmap(":/gfx/gfx/valide.png")
            )
            self.label_IconStatus_RepertoireSaveGame.setPixmap(
                QtGui.QPixmap(":/gfx/gfx/valide.png")
            )


def get_MODManager(self):
    """
    Determine la présence du fichier de base MODManager et le complete au besoin
    """
    if not os.path.isfile(self.lineEdit_ProfilPZ.text() + "/Lua/saved_modlists.txt"):
        with open(
            self.lineEdit_ProfilPZ.text() + "/Lua/saved_modlists.txt", "w"
        ) as file:
            file.write("VERSION=2\n")
            file.write("mmFavorites:\n")

    disk.install_MODManager_STD(self)
    disk.install_MODManager_ADV(self)

    disk.verif_lien(
        self,
        file=self.lineEdit_ProfilPZ.text() + "/Lua/saved_modlists.txt",
        icon=self.label_IconStatus_MODManager,
    )

def install_MODManager_STD(self):
    with open("config/modmanager/EFK_STD.txt", "r") as file:
        EFK_STD = file.read()
    with open(self.lineEdit_ProfilPZ.text() + "/Lua/saved_modlists.txt", "r") as file:
        df = file.read()
    if EFK_STD not in df:
        df += EFK_STD + "\n"

    with open(self.lineEdit_ProfilPZ.text() + "/Lua/saved_modlists.txt", "w") as file:
        file.write(df)


def install_MODManager_ADV(self):
    with open("config/modmanager/EFK_ADV.txt", "r") as file:
        EFK_ADV = file.read()
    with open(self.lineEdit_ProfilPZ.text() + "/Lua/saved_modlists.txt", "r") as file:
        df = file.read()
    if EFK_ADV not in df:
        df += EFK_ADV + "\n"

    with open(self.lineEdit_ProfilPZ.text() + "/Lua/saved_modlists.txt", "w") as file:
        file.write(df)


def verif_lien(self, directory="", file="", icon=None):
    """Verification du fichier/repertoire passé en parametre

    Args:
        directory (str, optional): _description_. Defaults to "".
        file (str, optional): _description_. Defaults to "".
        icon (_type_, optional): _description_. Defaults to None.

    Returns:
        bool: True si lien/repertoire existe
    """
    if directory != "":
        if os.path.isdir(directory):
            icon.setPixmap(QtGui.QPixmap(":/gfx/gfx/valide.png"))
            return True
        else:
            icon.setPixmap(QtGui.QPixmap(":/gfx/gfx/supprimer.png"))
            return False
    if file != "":
        if os.path.isfile(file):
            icon.setPixmap(QtGui.QPixmap(":/gfx/gfx/valide.png"))
            return True
        else:
            icon.setPixmap(QtGui.QPixmap(":/gfx/gfx/supprimer.png"))
            return False


def configSave(self, key, valeur):
    with open("config/EFKLauncher/config.json", "r+") as fichier:
        config = json.load(fichier)
        config[key] = valeur
        fichier.seek(0)
        json.dump(config, fichier, indent=4)
        fichier.truncate()


def delFile(self):
    """_summary_"""
    core.writeLog(self, "DelFile", " Process WIPE MAP Start...")
    listeProtect = ["delfile.exe", "delfile.py", "fichiers.txt"]
    try:
        with open("config/delfile/fichiers.txt", "r") as f:
            for line in f:
                listeProtect.append(line.strip())
    except:
        core.writeLog(
            "DelFile", f" ERROR > fichiers.txt missing in EFK Launcher config dir."
        )
        self.tabWidget_FenetrePrincipale.setCurrentIndex(1)

    if self.lineEdit_RepertoireSaveGame.text() != "":
        repertoire = os.path.join(
            self.lineEdit_ProfilPZ.text() + "/Saves/Sandbox",
            self.lineEdit_RepertoireSaveGame.text(),
        )
        files = os.listdir(repertoire)
        # pour chaque fichier, test si les fichiers sont dans la liste de fichier à conserver sinon, efface
        for file in files:
            if file not in listeProtect and file[0] != ".":
                try:
                    os.remove(os.path.join(repertoire, file))
                    core.writeLog(self, "Delfile", f"{file} deleted")
                except:
                    core.writeLog(
                        self,
                        "Delfile",
                        f"ERROR > Fail to delete {file}. You need to star again the WIPE MAP on main Menu or Quit PZ.",
                    )
                    self.tabWidget_FenetrePrincipale.setCurrentIndex(1)
    else:
        core.writeLog(
            "DelFile", f" ERROR > Save Dir is not validate for WIPE MAP process."
        )
    core.writeLog(self, "DelFile", " Process WIPE MAP ending...")
