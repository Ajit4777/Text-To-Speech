import sys
from PyQt5.QtWidgets import QStyleFactory, QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox,QDesktopWidget,QCheckBox,QProgressBar,QLabel,QComboBox
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQT tuts!")
        self.setWindowIcon( QIcon('pythonlogo.png'))

        extractAction =  QAction("&GET TO THE CHOPPAH!!!", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
        
        self.home()

    def home(self):
        btn =  QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(0,100)

        extractAction =  QAction( QIcon('todachoppa.png'), 'Flee the Scene', self)
        extractAction.triggered.connect(self.close_application)
        
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)

        checkBox =  QCheckBox('Shrink Window', self)
        checkBox.move(100, 25)
        checkBox.stateChanged.connect(self.enlarge_window)

        self.progress =  QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)

        self.btn =  QPushButton("Download",self)
        self.btn.move(200,120)
        self.btn.clicked.connect(self.download)

        print(self.style().objectName())
        self.styleChoice =  QLabel("Windows Vista", self)

        comboBox =  QComboBox(self)
        comboBox.addItem("motif")
        comboBox.addItem("Windows")
        comboBox.addItem("cde")
        comboBox.addItem("Plastique")
        comboBox.addItem("Cleanlooks")
        comboBox.addItem("windowsvista")
        comboBox.move(50, 250)
        
        self.styleChoice.move(50,150)
        comboBox.activated[str].connect(self.style_choice)

        self.show()


    def style_choice(self, text):
        self.styleChoice.setText(text)
        QApplication.setStyle( QStyleFactory.create(text))


    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)
        
        

    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50,50, 1000, 600)
        else:
            self.setGeometry(50, 50, 500, 300)
        

    def close_application(self):
        choice =  QMessageBox.question(self, 'Extract!',
                                            "Get into the chopper?",
                                             QMessageBox.Yes |  QMessageBox.No)
        if choice ==  QMessageBox.Yes:
            print("Extracting Naaaaaaoooww!!!!")
            sys.exit()
        else:
            pass
        

    
def run():
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()