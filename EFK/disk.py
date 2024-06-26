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
# Module Interface DISK
# Gestion des acces disk et des liens
"""

import os
import json
from PySide6 import QtWidgets
from PySide6 import QtGui
from pathlib import Path
import shutil
from . import disk
from . import core


def get_userPZDir(self: QtWidgets) -> None:
    repertoire = str((Path.home()).joinpath("Zomboid")).replace("\\", "/")

    self.lineEdit_ProfilPZ.setText(repertoire)
    if disk.verif_lien(self, directory=repertoire,
                       icon=self.label_IconStatus_ProfilPZ):
        disk.configSave("Profil", repertoire)


def get_saveGameDir(self: QtWidgets) -> None:
    """
    Determine Le dossier de sauvegarde de PZ
    """

    repertoire = QtWidgets.QFileDialog.getExistingDirectory(
        parent=self,
        caption="Select directory",
        dir=self.lineEdit_ProfilPZ.text() + "/Saves/Sandbox",
        options=QtWidgets.QFileDialog.Option.DontUseNativeDialog,
    )
    name = os.path.basename(repertoire)
    self.lineEdit_RepertoireSaveGame.setText(name)
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
            disk.configSave("SaveGame", name)
            self.label_IconStatus_RepertoireSaveGame.setPixmap(
                QtGui.QPixmap(":/gfx/gfx/valide.png")
            )


def get_ExeSteam(self: QtWidgets) -> None:
    """
    Determine L executable STEAM pour lancer PZ
    """
    exeSteam = ""
    platform = core.sysInfo()
    if platform == "Linux":
        exeSteam = "steam"
    elif platform == "win32":
        exeSteam = "steam.exe"
    elif platform == "mac":
        # TODO: determine l executable steam sous mac
        pass

    fichier = QtWidgets.QFileDialog.getOpenFileName(
        parent=self,
        caption="trouve l'executable Steam",
        filter=exeSteam,
        options=QtWidgets.QFileDialog.Option.DontUseNativeDialog,
    )
    if fichier[0] != "":
        self.lineEdit_ExePZ.setText(fichier[0])
        if disk.verif_lien(self, file=fichier[0],
                           icon=self.label_IconStatus_ExePZ):
            disk.configSave("ExePZ", fichier[0])


def get_MODManager(self: QtWidgets) -> None:
    """
    Determine la présence du fichier de base MODManager
    et le complete au besoin
    """
    if not os.path.isfile(self.lineEdit_ProfilPZ.text() + "/Lua/saved_modlists.txt"):
        with open(
            self.lineEdit_ProfilPZ.text() + "/Lua/saved_modlists.txt",
            "w"
        ) as file:
            file.write("VERSION=2\n")
            file.write("mmFavorites:\n")


def effaceModManagerProfil(self):
    with open(
        self.lineEdit_ProfilPZ.text() + "/Lua/saved_modlists.txt",
        "r",
        encoding="utf-8"
    ) as file:
        df = file.readlines()

    finaltext = ""

    for ligne in df:
        if (
            "Escape From Knox Project ADV:" not in ligne
            and "Escape From Knox Project STD:" not in ligne
        ):
            finaltext += ligne

    with open(
        self.lineEdit_ProfilPZ.text() + "/Lua/saved_modlists.txt",
        "w",
        encoding="utf-8"
    ) as file:
        file.write(finaltext)


def install_EFKMods(self: QtWidgets) -> None:
    filePath = shutil.copy(
        "config/EFK/default.txt",
        self.lineEdit_ProfilPZ.text() + "/mods/default.txt",
    )
    core.writeLog(
        self,
        "EFK Mods",
        f" Pré install EFK Mods ({filePath})"
    )
    filePath = shutil.copy(
        "config/EFK/SurvivorOptions.lua",
        self.lineEdit_ProfilPZ.text() + "/Lua/SurvivorOptions.lua",
    )
    core.writeLog(
        self,
        "EFK Mods",
        f" Pré install EFK Mods ({filePath})"
    )


def verif_lien(self: QtWidgets, directory="", file="", icon=None) -> None:
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
    if file != "" and icon is not None:
        if os.path.isfile(file):
            icon.setPixmap(QtGui.QPixmap(":/gfx/gfx/valide.png"))
            return True
        else:
            icon.setPixmap(QtGui.QPixmap(":/gfx/gfx/supprimer.png"))
            return False


def configSave(key, valeur):
    with open("config/EFKLauncher/config.json", "r+") as fichier:
        config = json.load(fichier)
        config[key] = valeur
        fichier.seek(0)
        json.dump(config, fichier, indent=4)
        fichier.truncate()


def delFileTarget(self, fichier: str):
    """efface le fichier passé en parametre
    Args:
        fichier (str): chemin du fichier à effacer
    """
    if os.path.isfile(fichier):
        lien = Path(fichier)
        lien.unlink()
    core.writeLog(self, "delfile", f"{fichier} deleted")


def delFile(self: QtWidgets) -> None:
    """Efface une liste de fichier dans un repertoire hormis ceux
    present dans la liste du fichiers.txt"""

    core.writeLog(self, "DelFile", " Process WIPE MAP Start...")
    listeProtect = ["delfile.exe", "delfile.py", "fichiers.txt"]

    if not (
        self.lineEdit_RepertoireSaveGame.text() != ""
    ):
        core.writeLog(
            self,
            "DelFile",
            " ERROR > Save Dir is not validate for WIPE MAP process."
        )
        return

    try:
        with open("config/delfile/fichiers.txt", "r") as f:
            for line in f:
                listeProtect.append(line.strip())
    except:
        core.writeLog(
            "DelFile",
            " ERROR > fichiers.txt missing in EFK Launcher config dir."
        )
        self.tabWidget_FenetrePrincipale.setCurrentIndex(1)
    log = ""
    nbrFile = 0
    if self.lineEdit_RepertoireSaveGame.text() != "":
        repertoire = os.path.join(
            self.lineEdit_ProfilPZ.text() + "/Saves/Sandbox/",
            self.lineEdit_RepertoireSaveGame.text(),
        )
        files = os.listdir(repertoire)
        # pour chaque fichier, test si les fichiers sont dans la liste
        # de fichier à conserver sinon, efface
        for file in files:
            if file not in listeProtect and file[0] != ".":
                try:
                    fichier = os.path.normpath(repertoire + os.path.sep + file)
                    if os.path.isfile(fichier):
                        lien = Path(fichier)
                        lien.unlink()
                        nbrFile += 1    
                    else:
                        core.writeLog(
                            self,
                            "Delfile",
                            f"INFO > {file} not found. no deletion"
                        )

                except:
                    core.writeLog(
                        self,
                        "Delfile",
                        f"ERROR > Fail to delete {file}. You need to start again the WIPE MAP on main Menu or Quit PZ.",
                    )
                    self.tabWidget_FenetrePrincipale.setCurrentIndex(1)
    else:
        core.writeLog(
            self,
            "DelFile",
            " ERROR > Save Dir is not validate for WIPE MAP process."
        )
    log += f"<strong>Delfile</strong> : {nbrFile} deleted<br>"
    core.writeLog(self, "Delfile", log)
    core.writeLog(self, "DelFile", "Process WIPE MAP ending...")
