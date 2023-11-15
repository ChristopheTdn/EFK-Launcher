
from PyQt6 import QtWidgets
import sys
import os,pathlib
import shutil
import zipfile
import time
import requests


def init_maj_process(self, url, dest, file):
    self.pushButton_ok.setEnabled(False)

    while "Tout se deroule bien":
        #Creer le repertoire temporaire
        message(self, "Création du repertoire de destination")
        if not os.path.exists(dest):
            os.makedirs(dest)
        #Telecharge l'archive

        message(self, "Téléchargement de l'archive")
        telecharge_fichier(self, url, dest, file)
#        except:
#            message(self, "ERREUR Téléchargement...")
#            break
#
        #Efface le "EFK Launcher" de base
        try:
            os.remove("EFK Launcher.exe")
        except:
            message(self, "ERREUR : Quitter EFK Launcher et recommencer...")
            break

        #Dezippe le EFK Launcher
        try:
            message(self, "Decompression de l'archive")
            unzip(self, url, dest, file)
        except:
            message(self, "Probleme de decompression du fichier Zip...")
            time.sleep(1)
        #Efface le repertoire temporaire
        try:
            message(self, "Nettoyage fichier temporaire")
            shutil.rmtree("tmp", True)
        except:
            message(self, "impossible d'effacer le repertoire temporaire")
            time.sleep(1)

        #Relance le EFK Launcher nouveau
        message(self, "")
        from sys import platform as _platform
        if _platform == "linux" or _platform == "linux2":
            # linux
            os.system('./efklauncher')
        elif _platform == "win32":
            # Windows
            import subprocess
            if getattr(sys, 'frozen', False):
                application_path = os.path.dirname(sys.executable)
            elif __file__:
                application_path = os.path.dirname(__file__)
            ExecNewLauncher = os.path.join(pathlib.Path(application_path).parent, "EFK Launcher.exe")
            subprocess.Popen(ExecNewLauncher)
        sys.exit()

    self.pushButton_ok.setEnabled(True) 

def telecharge_fichier(self, url, dest, file):
    import urllib.request
    from threading import Thread
    class Telecharger(object):
        def __init__(self):
            self.count = 0
            self.block_size = 0
            self.total_size = 1

        def get_file(self):
            time.sleep(0.2)
            urllib.request.urlretrieve(url, dest+'/'+file, self.reporthook)

        def reporthook(self, count, block_size, total_size):
            self.count = count
            self.block_size = block_size
            self.total_size = total_size

    Tel = Telecharger()
    t1 = Thread(target=Tel.get_file)
    t1.start()

    while (t1.is_alive()):
        time.sleep(0.1)
        val = round((Tel.count*8191.87 / Tel.total_size)*100, 0)
        self.progressBar.setValue(int(val))
        QtWidgets.QApplication.processEvents()
    time.sleep(2)

def unzip(self, url, dest, file):
    zipf = zipfile.ZipFile(dest+"/"+file, 'r')
    zipf.extractall()


def message(self, texte):
    self.label_feedback.setText(texte)
    QtWidgets.QApplication.processEvents()  # Maj affichage interface
    time.sleep(1)
    
def is_website_online(self,url: str) -> bool:
    
    try:
        response = requests.head(url)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False