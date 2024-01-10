import time
import wave
#####
## Тварь номер 1
import simpleaudio
## Тварь номер 2 (звук винды)
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
##
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
    audio = None
    player = None
    is_playing = False
    item = []
    dir = ""
    paths = []
    names = []
    volume = None  # Изменил имя переменной
    def __init__(self):
        super(Player, self).__init__()
        self.playback_direction = 1
        self.setupUi(self)
        self.setFixedSize(self.size())
        ## Звук винды
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        self.volume = cast(interface, POINTER(IAudioEndpointVolume))  # Сохраняем интерфейс в переменной
        ##
        #
        self.pushButton_play.clicked.connect(self.play)
        #
        self.action_OpenFolder.triggered.connect(self.load_folder)
        #
        self.listWidget.itemSelectionChanged.connect(self.select_item)
        #
        self.horizontalSlider_volume.valueChanged.connect(self.update_volume)
        #
        self.pushButton_next.clicked.connect(self.next_song)
        #
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
        if self.is_playing:
            self.player.stop()
            self.is_playing = False
            self.pushButton_play.setText('▶️')

        if self.listWidget.count() != 0:
            current_row = self.listWidget.currentRow()

            if self.playback_direction == 1:
                next_row = current_row + 1
            else:
                next_row = current_row - 1

            if next_row < 0:
                next_row = self.listWidget.count() - 1
            elif next_row >= self.listWidget.count():
                next_row = 0

            next_item = self.listWidget.item(next_row)
            self.listWidget.setCurrentItem(next_item)
            self.select_item()

            if self.audio and not self.is_playing:
                self.player = simpleaudio.play_buffer(
                    self.audio.raw_data,
                    self.audio.channels,
                    self.audio.sample_width,
                    self.audio.frame_rate
                )
                self.is_playing = True
                self.pushButton_play.setText('⏸')


    def prev_song(self):
        pass


    def running_label(self):
        pass
    def check_playback_state(self):
        pass

    def select_item(self):
        self.item = self.listWidget.currentItem()
        index = self.listWidget.currentRow()
        self.file_path = self.paths[index]
        self.audio = AudioSegment.from_file(self.file_path, format="mp3")
        self.label_track.setText(self.item.text()[:-4])

    def play(self):
        if self.audio and not self.is_playing:
            self.player = simpleaudio.play_buffer(
                self.audio.raw_data,
                self.audio.channels,
                self.audio.sample_width,
                self.audio.frame_rate
            )
            self.is_playing = True
            self.pushButton_play.setText('⏸')
        elif self.is_playing:
            self.player.stop()
            self.is_playing = False
            self.pushButton_play.setText('▶️')

###### pip install simpleaudio ############
        # Кровь и пот 3 часов дэбага, хотя нет подожди, уже sка 4 часа дэбага
        # всё работает и славно 11.01.2024 1:57
    def update_volume(self):
        volume = self.horizontalSlider_volume.value()
        self.volume.SetMasterVolumeLevelScalar(volume / 100, None)
        if self.horizontalSlider_volume.value() == 0:
            self.pushButton_mute.setText("🔇")
        elif self.horizontalSlider_volume.value() > 0 and self.horizontalSlider_volume.value() <= 10:
            self.pushButton_mute.setText("🔈")
        elif self.horizontalSlider_volume.value() > 10 and self.horizontalSlider_volume.value() < 20:
            self.pushButton_mute.setText("🔉")
        elif self.horizontalSlider_volume.value() >= 20 and self.horizontalSlider_volume.value() <= 25:
            self.pushButton_mute.setText("🔊")
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
