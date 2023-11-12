from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtWidgets import QWidget
import interface
import os
class Player(QtWidgets.QMainWindow, interface.Ui_MainWindow):
    def __init__(self):
        super(Player, self).__init__()
        self.setupUi(self)
        self.actionAdd_folder.triggered.connect(self.load_folder)
        self.pushButton_pause.clicked.connect(self.play)
        self.setFixedSize(self.size())
        self.mediaPlayer = QtMultimedia.QMediaPlayer()
        self.mediaPlayer.setVolume(self.volume_Slider.value())
        self.volume_Slider.valueChanged.connect(self.volume_change)
        self.pushButton_next.clicked.connect(self.next_song)
        self.listWidget.itemSelectionChanged.connect(self.select_item)
        self.dir = ""
        self.item = ""
        self.content = ""
        self.played = False
        # код слайдера отслеживания таймингов
        self.music_Slider.setTracking(True)  # Включение отслеживание перемещения ползунка (перемещение по песне)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_slider)
        self.timer.start(1000)  # Обновление ползунка каждые * миллисекунд
        self.music_Slider.sliderReleased.connect(
        self.set_media_position)  # Обновление позиции медиаплеера при отпускании ползунка
        #
        #⏸️▶️

    def load_folder(self):
        self.listWidget.clear()
        dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Select directory")

        if dir:
            for file_name in os.listdir(dir):
                if file_name.endswith(".mp3"):
                    self.listWidget.addItem(os.path.join(dir, file_name))
                self.dir = dir

    def play(self):
        played = self.played
        if self.item:
            if not played:
                self.pushButton_pause.setText("⏸")
                self.played = True
                self.mediaPlayer.play()
            else:
                self.mediaPlayer.pause()
                self.pushButton_pause.setText("▶")
                self.played = False

    def volume_change(self):
        self.mediaPlayer.setVolume(self.volume_Slider.value())

    def next_song(self):
        pass

    def update_slider(self):
        if self.played:
            position = self.mediaPlayer.position()
            duration = self.mediaPlayer.duration()
            #
            self.music_Slider.setMaximum(duration)
            self.music_Slider.setValue(position)
            #
            position_time = QTime(0, 0)
            position_time = position_time.addMSecs(position * 60)
            duration_time = QTime(0, 0)
            duration_time = duration_time.addMSecs(duration * 60)
            #
            self.timeEdit_1.setTime(position_time)
            self.timeEdit_2.setTime(duration_time)

    def set_media_position(self):
        position = self.music_Slider.value()
        self.mediaPlayer.setPosition(position)



    def select_item(self):
        self.item = self.listWidget.currentItem()
        file_name = os.path.join(self.item.text())
        self.content = QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(file_name))
        self.mediaPlayer.setMedia(self.content)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    player = Player()
    player.show()
    app.exec()
