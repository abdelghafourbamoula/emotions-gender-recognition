from PyQt5 import QtCore, QtGui, QtWidgets

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model, model_from_json
from utils import load_models, make_predictions
from utils import emotion_classes, gender_classes
from image_classifier import Ui_ImagecClassifieRScreen

#------------------------- Home Window -------------------------------
class Ui_HomeScreen(object):
    def setupUi(self, HomeScreen):
        HomeScreen.setObjectName("HomeScreen")
        HomeScreen.resize(802, 512)
        HomeScreen.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(HomeScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 3)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.side_bar = QtWidgets.QFrame(self.centralwidget)
        self.side_bar.setMinimumSize(QtCore.QSize(175, 0))
        self.side_bar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.side_bar.setStyleSheet("background-color: rgb(26, 164, 255);\n"
"border-radius:10px;")
        self.side_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.side_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_bar.setObjectName("side_bar")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.side_bar)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 15)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title_label = QtWidgets.QLabel(self.side_bar)
        self.title_label.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Unifont Upper")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("color: rgb(225, 255, 255);")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.verticalLayout_2.addWidget(self.title_label)
        self.label = QtWidgets.QLabel(self.side_bar)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/face.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 85, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.classsifyImage_btn = QtWidgets.QPushButton(self.side_bar)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.classsifyImage_btn.setFont(font)
        self.classsifyImage_btn.setStyleSheet("QPushButton{\n"
"color: rgb(67, 172, 102);\n"
"    background-color: qlineargradient(spread:pad, x1:0.016, y1:0.0909091, x2:1, y2:0.648, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(207, 235, 235, 255));\n"
"text-align:left;\n"
"padding:10px;\n"
"}\n"
"\n"
"\n"
"QPushButton::hover{\n"
"color: rgb(0, 141, 202);\n"
"background-color: rgb(206, 237, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"color: rgb(10, 171, 192);\n"
"    background-color: rgb(245, 253, 255);\n"
"border: 1px solid rgb(190,190,190);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.classsifyImage_btn.setIcon(icon)
        self.classsifyImage_btn.setIconSize(QtCore.QSize(36, 36))
        self.classsifyImage_btn.setAutoDefault(False)
        self.classsifyImage_btn.setDefault(False)
        self.classsifyImage_btn.setFlat(False)
        self.classsifyImage_btn.setObjectName("classsifyImage_btn")
        self.verticalLayout_2.addWidget(self.classsifyImage_btn)
        self.exit_btn = QtWidgets.QPushButton(self.side_bar)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.exit_btn.setFont(font)
        self.exit_btn.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.exit_btn.setStyleSheet("QPushButton{\n"
"color:rgb(232, 87, 90);\n"
"    background-color: qlineargradient(spread:pad, x1:0.016, y1:0.0909091, x2:1, y2:0.648, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(207, 235, 235, 255));\n"
"text-align:left;\n"
"padding:10px;\n"
"}\n"
"\n"
"\n"
"QPushButton::hover{\n"
"color: rgb(0, 141, 202);\n"
"background-color: rgb(206, 237, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"color: rgb(10, 171, 192);\n"
"    background-color: rgb(245, 253, 255);\n"
"border: 1px solid rgb(190,190,190);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn.setIcon(icon2)
        self.exit_btn.setIconSize(QtCore.QSize(36, 36))
        self.exit_btn.setAutoDefault(True)
        self.exit_btn.setDefault(False)
        self.exit_btn.setFlat(False)
        self.exit_btn.setObjectName("exit_btn")
        self.verticalLayout_2.addWidget(self.exit_btn)
        self.horizontalLayout.addWidget(self.side_bar)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("border-radius: 10px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setContentsMargins(2, 2, 2, 0)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.camera_label = QtWidgets.QLabel(self.frame_2)
        self.camera_label.setStyleSheet("border-radius:10px;")
        self.camera_label.setText("")
        self.camera_label.setObjectName("camera_label")
        self.verticalLayout.addWidget(self.camera_label)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_3.setStyleSheet("border-radius: 10px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 0)
        self.horizontalLayout_2.setSpacing(45)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.capture_btn = QtWidgets.QPushButton(self.frame_3)
        self.capture_btn.setMinimumSize(QtCore.QSize(95, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.capture_btn.setFont(font)
        self.capture_btn.setStyleSheet("QPushButton{\n"
"background-color: rgb(39, 188, 69);\n"
"border-style: none;\n"
"border-radius: 15px;\n"
"color: rgb(255, 255, 255);\n"
"padding: 3px 6px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(22, 231, 36);\n"
"padding: 2px 3px;\n"
"font-size: 10px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(22, 241, 46);\n"
"font-size: 12px;\n"
"}\n"
"\n"
"\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/capture.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.capture_btn.setIcon(icon3)
        self.capture_btn.setIconSize(QtCore.QSize(30, 30))
        self.capture_btn.setFlat(False)
        self.capture_btn.setObjectName("capture_btn")
        self.horizontalLayout_2.addWidget(self.capture_btn)
        self.stop_btn = QtWidgets.QPushButton(self.frame_3)
        self.stop_btn.setMinimumSize(QtCore.QSize(95, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.stop_btn.setFont(font)
        self.stop_btn.setStyleSheet("QPushButton{\n"
"background-color: rgb(249, 37, 37);\n"
"border-style: none;\n"
"border-radius: 15px;\n"
"color: rgb(255, 255, 255);\n"
"padding: 4px 6px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(247, 16, 16);\n"
"padding: 2px 3px;\n"
"font-size: 10px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(255, 30, 33);\n"
"font-size: 12px;\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop_btn.setIcon(icon4)
        self.stop_btn.setIconSize(QtCore.QSize(27, 27))
        self.stop_btn.setFlat(False)
        self.stop_btn.setObjectName("stop_btn")
        self.horizontalLayout_2.addWidget(self.stop_btn)
        self.save_btn = QtWidgets.QPushButton(self.frame_3)
        self.save_btn.setMinimumSize(QtCore.QSize(95, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.save_btn.setFont(font)
        self.save_btn.setStyleSheet("QPushButton{\n"
"background-color: rgb(206, 229, 239);\n"
"border-style: none;\n"
"border-radius: 15px;\n"
"color: rgb(30, 30, 50);\n"
"padding: 5px 6px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(231, 246, 255);\n"
"padding: 2px 3px;\n"
"font-size: 10px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(179, 218, 235);\n"
"font-size: 12px;\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/bookmark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_btn.setIcon(icon5)
        self.save_btn.setIconSize(QtCore.QSize(24, 24))
        self.save_btn.setFlat(False)
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout_2.addWidget(self.save_btn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 1)
        self.verticalLayout.addWidget(self.frame_3)
        self.horizontalLayout.addWidget(self.frame_2)
        HomeScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(HomeScreen)
        QtCore.QMetaObject.connectSlotsByName(HomeScreen)
        
        #---------- add video camera capture
        self.camera = CameraCapture()
        self.camera.start()
        self.camera.ImageUpdate.connect(self.image_update)
        self.capture_btn.clicked.connect(self.capture)
        self.stop_btn.clicked.connect(self.stop)
        self.save_btn.clicked.connect(self.save)
                
    def image_update(self, Image):
        self.camera_label.setPixmap(QtGui.QPixmap.fromImage(Image))
        
    def stop(self):
        self.camera.stop()
        
    def capture(self):
        self.camera.start()
        
    def save(self):
        cap = self.camera.capture
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        writer= cv2.VideoWriter('video.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 20, (width,height))
        
        while self.camera.ThreadActive:
            ret,frame= cap.read()
            writer.write(frame)
           
                
    def retranslateUi(self, HomeScreen):
        _translate = QtCore.QCoreApplication.translate
        HomeScreen.setWindowTitle(_translate("HomeScreen", "MainWindow"))
        self.title_label.setText(_translate("HomeScreen", "Real Time Detection"))
        self.classsifyImage_btn.setText(_translate("HomeScreen", " By Images"))
        self.exit_btn.setText(_translate("HomeScreen", " Exit"))
        self.capture_btn.setText(_translate("HomeScreen", "Capture"))
        self.stop_btn.setText(_translate("HomeScreen", "Stop"))
        self.save_btn.setText(_translate("HomeScreen", "Save"))

#------------- opnencv camrera capture -------------------
class CameraCapture(QtCore.QThread):

    ImageUpdate = QtCore.pyqtSignal(QtGui.QImage)
    
    def run(self):           
        self.ThreadActive = True
        # Load the cascade
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        #load saved models
        emotion_model, gender_model = load_models()
        # To capture video from webcam. 
        try:
            self.capture = cv2.VideoCapture(0) 
        except:
            print('===> Filed to connect the webcam ...')      
        # To use a video file as input 
        # capture = cv2.VideoCapture('./capture.mp4')
        while self.ThreadActive :
            #read the frame
            ret,frame = self.capture.read()
            frame = cv2.flip(frame,1)
            if ret:
                #convert to grayscale
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                #detect the faces
                faces = face_cascade.detectMultiScale(gray, 1.1, 1)
                print(len(faces), 'faces detected ...')
                
                for (x,y,w,h) in faces:
                    # face retangle
                    cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)        
                    gray_scale = gray[y:y+h, x:x+w]
                    
                    # for predict emotions
                    gray_48 = cv2.resize(gray_scale, (48,48))                    
                    emotion_predictions, emotion_index, emotion_percent = make_predictions(emotion_model, gray_48)
                    emotion_label = emotion_classes[emotion_index]
                    # write the prediction
                    cv2.putText(frame, emotion_label, (x,y-40) ,cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255,250,50), 2)
                    cv2.putText(frame, emotion_percent, (x+x//2,y-40) ,cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,250,100), 1)
                    
                    # for predict gender
                    gray_64 = cv2.resize(gray_scale, (64,64))
                    gender_predictions, gender_index, gender_percent = make_predictions(gender_model, gray_64)        
                    gender_label = gender_classes[gender_index]
                    #write the prediction
                    cv2.putText(frame, gender_label, (x,y-10) ,cv2.FONT_HERSHEY_SIMPLEX, 0.45, (25,250,50), 2)
                    cv2.putText(frame, gender_percent, (x+x//2,y-10) ,cv2.FONT_HERSHEY_SIMPLEX, 0.4, (25,250,150), 1)
        
                    #show emotions plots
                    for i,p in enumerate(emotion_predictions[0]):
                        cv2.putText(frame, emotion_classes[i], (10, (i+1)*15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (250,80,20), 1)
                        cv2.rectangle(frame, (80, (i+1)*15), (80+round(p*100), (i+1)*15-5), (255,164,26), -1)
                     
                    #show gender plots
                    for i,p in enumerate(gender_predictions[0]):
                        cv2.putText(frame, gender_classes[i], (450, (i+1)*15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (5,220,20), 1)
                        cv2.rectangle(frame, (500, (i+1)*15), (500+round(p*100), (i+1)*15-5), (10,205,50), -1)
                     
                # show the frame in the window after format it
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                toQtFormat = QtGui.QImage(Image.data, Image.shape[1], Image.shape[0], QtGui.QImage.Format_RGB888)
                picture = toQtFormat.scaled(800,700, QtCore.Qt.KeepAspectRatio)
                self.ImageUpdate.emit(picture)           
                        
    def stop(self):
        self.ThreadActive = False
        #self.quit()                    
 

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HomeScreen = QtWidgets.QMainWindow()
    ui = Ui_HomeScreen()
    ui.setupUi(HomeScreen)
    HomeScreen.show()
    sys.exit(app.exec_())

