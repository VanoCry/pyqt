import time
import wave
#####
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QCursor, QPixmap
####
import inter2
import os
from random import shuffle
###
from pydub import AudioSegment
from pydub.playback import play
##

#
class Player(QtWidgets.QMainWindow, inter2.Ui_MainWindow):
    def __init__(self):
        self.is_playing = False
        self.item = []
        self.dir = ""
        self.paths = []
        self.names = []
        self.file_path = None
        super(Player, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        #
        self.action_OpenFolder.triggered.connect(self.load_folder)
        #
        self.listWidget.itemSelectionChanged.connect(self.select_item)
        ###

        ###
    def load_folder(self):
        self.listWidget.clear()
        self.dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Select directory")
        if self.dir:
            self.paths = []
            self.names = []
            for file_name in os.listdir(self.dir):
                if file_name.endswith(".mp3"):
                    full_path = os.path.join(self.dir, file_name)
                    song_name = os.path.basename(file_name)

                    self.paths.append(full_path)  # Сохраните полный путь
                    self.names.append(song_name)  # Сохраните название файла

                    self.listWidget.addItem(song_name)  # Отображайте название в listWidget
            self.dir = dir

    def shuffle_tracks(self):
        pass

    def next_song(self):
        pass

    def prev_song(self):
        pass

    def select_item(self):
        self.item = self.listWidget.currentItem()
        index = self.listWidget.currentRow()  # Получите индекс выбранной песни
        self.file_path = self.paths[index]  # Используйте индекс для получения полного пути к файлу
        ## прописать плеер селект
        self.label_track.setText(self.item.text()[:-4])


class Interface:
    def running_label(self):
        pass


class Sound:
    def check_playback_state(self):
        pass

    def play(self):
        if not Player.is_playing:
            Player.pushButton_play.setText('⏸')
            self.play_audio()
        else:
            Player.pushButton_play.setText('▶️')
            self.stop_audio()

    def play_audio(self):
        if Player.file_path != None:
            self.audio = AudioSegment.from_mp3(Player.file_path)
            self.audio_thread = AudioThread(self.audio)################################################
            self.audio_thread.start()

    def stop_audio(self):

    def volume_change(self):
        pass

    def update_slider(self):
        pass

    def set_media_position(self):
        pass

    def select_item(self):
        pass




if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    player = Player()
    player.show()
    app.exec()
