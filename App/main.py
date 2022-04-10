from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from loading import Ui_LoadingScreen
from image_classifier import Ui_ImagecClassifieRScreen
from capture import Ui_HomeScreen, load_models

# --------- Globals
counter = 0

# ************** Image screen *******************
class ImageClassifier(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ImagecClassifieRScreen()
        self.ui.setupUi(self)
        self.center()
        self.show()
        self.ui.back_btn.clicked.connect(self.back)
        
    def back(self):
        self.ui = MainWindow()
        self.ui.show()
        self.close()
    
    #show screen in the center 
    def center(self):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())
    
# ************** Home screen *******************
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_HomeScreen()
        self.ui.setupUi(self)
        self.center()
        self.show()
        self.ui.classsifyImage_btn.clicked.connect(self.to_image_screen)
        
    def to_image_screen(self):
        self.ui.camera.stop()
        self.ui = ImageClassifier()
        self.ui.show()
        self.close()
    
    #show screen in the center 
    def center(self):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())


# ******************* Loading screen *******************
class LoadingScreen(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoadingScreen()
        self.ui.setupUi(self)
        self.center()
        
        # remove title bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # start timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(50)
        self.show()
        
    
    def progress(self):
        global counter
        
        self.ui.progressBar.setValue(counter)
        
        if counter>=100:
            self.timer.stop()
            
            self.ui = MainWindow()
            self.ui.show()
            #close loadind windiw
            self.close()
            
        counter += 1
     
    # ----- center the window   
    def center(self):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())


if __name__=='__main__':
    import sys
    app = QApplication(sys.argv)
    window = LoadingScreen()
    sys.exit(app.exec_())