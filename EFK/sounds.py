from PyQt6.QtCore import QUrl
from PyQt6.QtMultimedia import QMediaPlayer,QAudioOutput
import ressources_rc

def play(self, son ="qrc:/sounds/sounds/clic.mp3"):
    self.player = QMediaPlayer()
    self.audio = QAudioOutput()
    self.player.setAudioOutput(self.audio)
    self.player.setSource(QUrl(son))
    self.player.play()

