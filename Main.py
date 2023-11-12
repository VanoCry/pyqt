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
        self.pushButton_prev.clicked.connect(self.prev_song)
        self.listWidget.itemSelectionChanged.connect(self.select_item)
        self.dir = ""
        self.item = ""
        self.content = ""
        self.playback_direction = 1  # 1 для воспроизведения вперед, -1 для воспроизведения назад
        #
        self.play_check_timer = QTimer(self)
        self.play_check_timer.timeout.connect(self.check_playback_state)
        self.play_check_timer.start(1000)  # Проверка каждую секунду
        # код слайдера отслеживания таймингов
        self.music_Slider.setTracking(True)  # Включение отслеживание перемещения ползунка (перемещение по песне)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_slider)
        self.timer.start(1000)  # Обновление ползунка каждые * миллисекунд
        self.music_Slider.sliderReleased.connect(
            self.set_media_position)  # Обновление позиции медиаплеера при отпускании ползунка

    def check_playback_state(self):
        if self.mediaPlayer.state() == QtMultimedia.QMediaPlayer.PlayingState:
            self.pushButton_pause.setText("⏸")
        else:
            self.pushButton_pause.setText("▶")

    def load_folder(self):
        self.listWidget.clear()
        dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Select directory")

        if dir:
            for file_name in os.listdir(dir):
                if file_name.endswith(".mp3"):
                    self.listWidget.addItem(os.path.join(dir, file_name))
                self.dir = dir

    def play(self):
        if self.mediaPlayer.state() == QtMultimedia.QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def volume_change(self):
        self.mediaPlayer.setVolume(self.volume_Slider.value())

    def update_slider(self):
        position = self.mediaPlayer.position()
        duration = self.mediaPlayer.duration()
        #
        self.music_Slider.setMaximum(duration)
        self.music_Slider.setValue(position)
        #
        position_time = QTime(0, 0)
        position_time = position_time.addMSecs(position)
        duration_time = QTime(0, 0)
        duration_time = duration_time.addMSecs(duration)
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

    def next_song(self):
        if self.listWidget.count() != 0:
            current_row = self.listWidget.currentRow()
            was_playing = (self.mediaPlayer.state() == QtMultimedia.QMediaPlayer.PlayingState)

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

            if was_playing:
                self.play()

    def prev_song(self):
        if self.listWidget.count() != 0:
            current_row = self.listWidget.currentRow()
            was_playing = (self.mediaPlayer.state() == QtMultimedia.QMediaPlayer.PlayingState)

            if self.playback_direction == 1:
                prev_row = current_row - 1
            else:
                prev_row = current_row + 1

            if prev_row < 0:
                prev_row = self.listWidget.count() - 1
            elif prev_row >= self.listWidget.count():
                prev_row = 0

            prev_item = self.listWidget.item(prev_row)
            self.listWidget.setCurrentItem(prev_item)
            self.select_item()

            if was_playing:
                self.play()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    player = Player()
    player.show()
    app.exec()
