# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'YtDownloader.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import filedialog
from pytube import YouTube
import os

yt= YouTube


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800,600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_down = QtWidgets.QPushButton(self.centralwidget)
        self.btn_down.setGeometry(QtCore.QRect(350, 220, 320, 90))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.btn_down.setFont(font)
        self.btn_down.setObjectName("btn_down")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 170, 501, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 30, 471, 51))
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QtCore.QRect(70, 120, 570, 51))
        self.rb_video = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_video.setGeometry(QtCore.QRect(70, 200, 150, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.rb_video.setFont(font)
        self.rb_video.setObjectName("rb_video")
        self.rd_audio = QtWidgets.QRadioButton(self.centralwidget)
        self.rd_audio.setGeometry(QtCore.QRect(70, 250, 120, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        
        self.rd_audio.setFont(font)
        self.rd_audio.setObjectName("rd_audio")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(70, 350, 471, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YTDownloader"))
        self.btn_down.setText(_translate("MainWindow", "Download"))
        self.label_2.setText(_translate("MainWindow", "YoutubeDownloader"))
        self.label_3.setText(_translate("MainWindow", "cole a url do video aqui"))
        self.rb_video.setText(_translate("MainWindow", "Video"))
        self.rd_audio.setText(_translate("MainWindow", "Audio"))

         #acao do botao
        self.btn_down.clicked.connect(self.download)
    
    



    def download(self):
        if self.rb_video.isChecked()==True:
            url = self.lineEdit.text()
            yt = YouTube(url)
            video = yt.streams.get_highest_resolution()
            save_path=filedialog.askdirectory()
            video.download(save_path)
        elif self.rd_audio.isChecked() == True:
            try:
                url= self.lineEdit.text()
                yt = YouTube(url)
                audio = yt.streams.filter(only_audio=True).first()
                save_path=filedialog.askdirectory()
                out_file=audio.download(save_path)
                base,ext = os.path.splitext(out_file)
                new_file=base+ '.mp3'
                os.rename(out_file,new_file)
                    
            except Exception as e:
                   self.label.config(text=f"Erro : {str(e)}")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
