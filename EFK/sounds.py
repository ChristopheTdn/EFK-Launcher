from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QMediaPlayer,QAudioOutput
import ressources_rc

def play(self, son="qrc:/sounds/sounds/clic.mp3", volume=0.2):
    self.player = QMediaPlayer()
    self.audio = QAudioOutput()
    self.player.setAudioOutput(self.audio)
    self.player.setSource(QUrl(son))
    self.audio.setVolume(volume)
    self.player.play()
