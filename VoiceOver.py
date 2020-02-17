import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox,QDesktopWidget,QComboBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
# from PySide import QtGui
import tkinter

from gtts import gTTS 

# This module is imported so that we can  
# play the converted audio 
import os 


 
root = tkinter.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
print(width, " x ", height)
class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Audio Download'
        self.left = 10
        self.top = 10
        self.width = 350
        self.height = 200
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(width/2, height/2, self.width, self.height)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        # Create textbox
        
        self.textbox = QLineEdit(self)
        self.textbox.setPlaceholderText("Audio Text") 
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)
        self.name = QLineEdit(self)
        self.name.setPlaceholderText("File Name (Dont use SPACE)")
        self.name.move(20, 80)
        self.name.resize(280,40)
        # Create a button in the window
        self.button = QPushButton('Download', self)
        self.button.move(20,150)
        
        self.dropDown = QComboBox('Language',self)
        for i in gtts.lang.tts_langs().len:
            self.dropDown.addItem(i)
            
        self.dropDown.move(20,200)

        # # connect button to function on_click
        # self.button.clicked.connect(self.on_click)
        # self.show()
    def SaveAudio(self):
        textboxValue = self.textbox.text()
        name =  self.name.text()
        language = 'en'
        
        # Passing the text and language to the engine,  
        # here we have marked slow=False. Which tells  
        # the module that the converted audio should  
        # have a high speed 
        # myobj = gTTS(text=textboxValue, lang=language, slow=False) 
        
        # # Saving the converted audio in a mp3 file named 
        # # welcome  
        # (firstWord, rest) = textboxValue.split(maxsplit=1)
        # myobj.save(name+".mp3") 
        
        # # Playing the converted file 
        # os.system(name + ".mp3") 
    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        self.SaveAudio()
        # QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        # self.textbox.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
