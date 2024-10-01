from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QGridLayout, QWidget, QMessageBox, QMainWindow, QApplication
from PyQt5.QtCore import QCoreApplication, QSettings, QUrl
from info_micro import list_microphones
from os import path
from window1 import Ui_MainWindow
from info_micro import list_microphones
from win_main2 import Window2
from time import sleep
import webbrowser
import toml
import asyncio
import llama

press_btn = False
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        
        #Наследование
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        #Импорт иконок:
        #TitleWin
        
        icon = QtGui.QIcon()
        parent_dir = path.dirname(path.abspath(__file__))
        icon.addPixmap(QtGui.QPixmap(path.join(parent_dir,"texture","icontitle.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        
        #Кнопка запуска ассистента
        
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(path.join(parent_dir,"texture","icon_play1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.btn_play.setIcon(icon1)
        self.ui.btn_play.setFlat(True)
        self.ui.btn_play.clicked.connect(self.start_ass)
        
        #Кнопка настроек
        
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(path.join(parent_dir,"texture","icon_settings.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.btn_settings.setIcon(icon2)
        self.ui.btn_settings.setFlat(True)
        
        #buttons_settings
        
        self.ui.btn_settings.clicked.connect(self.new_window_event)
        
        self.wn2 = Window2(self)
        
        
        #Галвный текст
        
        self.ui.title_text.linkActivated.connect(self.open_url)
        self.ui.title_text.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        #Обработка ответа на promt
        #global promt
        #promt = asyncio.run(llama.chat('Привет'))
        
        
    def open_url(self):
        webbrowser.open_new('http:/vaskill.rf.gd')
        
    def new_window_event(self): 
        self.wn2.show()
        #self.hide()
        
    def start_ass(self):
        parent_dir = path.dirname(path.abspath(__file__))
        global press_btn
        if press_btn == False:
            icon_play = QtGui.QIcon()
            icon_play.addPixmap(QtGui.QPixmap(path.join(parent_dir, 'texture', 'icon_stop.png')))
            self.ui.btn_play.setIcon(icon_play)
            press_btn = True
            print(press_btn)
            #self.ui.label_4.setText(promt)
        elif press_btn == True:
            icon_play1 = QtGui.QIcon()
            icon_play1.addPixmap(QtGui.QPixmap(path.join(parent_dir, 'texture', 'icon_play1.png')))
            self.ui.btn_play.setIcon(icon_play1)
            press_btn = False
            print(press_btn)
            
        
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
        
        