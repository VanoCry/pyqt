from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
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
        self.dir = ""
        self.played = False
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
        item = self.listWidget.currentItem()
        played = self.played
        if item:
            if not played:
                file_name = os.path.join(item.text())
                content = QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(file_name))
                self.mediaPlayer.setMedia(content)
                self.pushButton_pause.setText("⏸")
                self.played = True
                self.mediaPlayer.play()
            else:
                self.mediaPlayer.stop()
                self.pushButton_pause.setText("▶")
                self.played = False

    def volume_change(self):
        self.mediaPlayer.setVolume(self.volume_Slider.value())

    def next_song(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    player = Player()
    player.show()
    app.exec()
