# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(428, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(4, -1, 431, 761))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setGeometry(QtCore.QRect(340, 200, 80, 80))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 200, 80, 80))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(160, 190, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 200, 80, 80))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 200, 80, 80))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalSlider = QtWidgets.QSlider(self.tab)
        self.horizontalSlider.setGeometry(QtCore.QRect(3, 110, 415, 22))
        self.horizontalSlider.setSizeIncrement(QtCore.QSize(10, 10))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.timeEdit = QtWidgets.QTimeEdit(self.tab)
        self.timeEdit.setGeometry(QtCore.QRect(0, 150, 70, 22))
        self.timeEdit.setWrapping(False)
        self.timeEdit.setFrame(False)
        self.timeEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.timeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.timeEdit.setObjectName("timeEdit")
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.tab)
        self.timeEdit_2.setGeometry(QtCore.QRect(80, 150, 70, 22))
        self.timeEdit_2.setWrapping(False)
        self.timeEdit_2.setFrame(False)
        self.timeEdit_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(65, 140, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.listView = QtWidgets.QListView(self.tab)
        self.listView.setGeometry(QtCore.QRect(0, 300, 420, 371))
        self.listView.setObjectName("listView")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.tab)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(255, 150, 160, 22))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 670, 60, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab)
        self.pushButton_7.setGeometry(QtCore.QRect(60, 670, 60, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_16 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_16.setGeometry(QtCore.QRect(10, 350, 150, 55))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_15 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_15.setGeometry(QtCore.QRect(10, 405, 150, 55))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.verticalSlider_3 = QtWidgets.QSlider(self.tab_2)
        self.verticalSlider_3.setGeometry(QtCore.QRect(10, 90, 20, 200))
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.verticalSlider_4 = QtWidgets.QSlider(self.tab_2)
        self.verticalSlider_4.setGeometry(QtCore.QRect(50, 90, 20, 200))
        self.verticalSlider_4.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_4.setObjectName("verticalSlider_4")
        self.verticalSlider_5 = QtWidgets.QSlider(self.tab_2)
        self.verticalSlider_5.setGeometry(QtCore.QRect(90, 90, 20, 200))
        self.verticalSlider_5.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_5.setObjectName("verticalSlider_5")
        self.verticalSlider_6 = QtWidgets.QSlider(self.tab_2)
        self.verticalSlider_6.setGeometry(QtCore.QRect(130, 90, 20, 200))
        self.verticalSlider_6.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_6.setObjectName("verticalSlider_6")
        self.verticalSlider_7 = QtWidgets.QSlider(self.tab_2)
        self.verticalSlider_7.setGeometry(QtCore.QRect(170, 90, 20, 200))
        self.verticalSlider_7.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_7.setObjectName("verticalSlider_7")
        self.verticalSlider_8 = QtWidgets.QSlider(self.tab_2)
        self.verticalSlider_8.setGeometry(QtCore.QRect(210, 90, 20, 200))
        self.verticalSlider_8.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_8.setObjectName("verticalSlider_8")
        self.verticalSlider_9 = QtWidgets.QSlider(self.tab_2)
        self.verticalSlider_9.setGeometry(QtCore.QRect(250, 90, 20, 200))
        self.verticalSlider_9.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_9.setObjectName("verticalSlider_9")
        self.verticalSlider_10 = QtWidgets.QSlider(self.tab_2)
        self.verticalSlider_10.setGeometry(QtCore.QRect(290, 90, 20, 200))
        self.verticalSlider_10.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_10.setObjectName("verticalSlider_10")
        self.verticalSlider_11 = QtWidgets.QSlider(self.tab_2)
        self.verticalSlider_11.setGeometry(QtCore.QRect(330, 90, 20, 200))
        self.verticalSlider_11.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_11.setObjectName("verticalSlider_11")
        self.verticalSlider_12 = QtWidgets.QSlider(self.tab_2)
        self.verticalSlider_12.setGeometry(QtCore.QRect(370, 90, 20, 200))
        self.verticalSlider_12.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_12.setObjectName("verticalSlider_12")
        self.lcdNumber = QtWidgets.QLCDNumber(self.tab_2)
        self.lcdNumber.setGeometry(QtCore.QRect(280, 350, 110, 110))
        self.lcdNumber.setObjectName("lcdNumber")
        self.dial = QtWidgets.QDial(self.tab_2)
        self.dial.setGeometry(QtCore.QRect(160, 350, 110, 110))
        self.dial.setMinimum(-20)
        self.dial.setMaximum(20)
        self.dial.setObjectName("dial")
        self.comboBox = QtWidgets.QComboBox(self.tab_2)
        self.comboBox.setGeometry(QtCore.QRect(272, 60, 121, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 428, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_5.setText(_translate("MainWindow", "⏭️"))
        self.pushButton_2.setText(_translate("MainWindow", "⏪"))
        self.pushButton.setText(_translate("MainWindow", "⏸️"))
        self.pushButton_3.setText(_translate("MainWindow", "⏩"))
        self.pushButton_4.setText(_translate("MainWindow", "⏮️"))
        self.label.setText(_translate("MainWindow", "/"))
        self.pushButton_6.setText(_translate("MainWindow", "🔁"))
        self.pushButton_7.setText(_translate("MainWindow", "🔀"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.pushButton_16.setText(_translate("MainWindow", "⚪Mono"))
        self.pushButton_15.setText(_translate("MainWindow", "♾Stereo"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Default"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())