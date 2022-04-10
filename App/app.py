# importing required libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model, model_from_json


emotion_classes = ["Angry", "Disgust", "Fear", "Happy", "Neutral","Sad","Surprised"]
gender_classes = ['Female','Male']

def load_models():
    ''' load emotion model (jsn format) and gender model(h5 format) '''
    json_file = open("/home/abdelghafour/Desktop/PFE/project/model.json", 'r')
    model = json_file.read()
    json_file.close()
    emotion_model = model_from_json(model)
    emotion_model.load_weights("/home/abdelghafour/Desktop/PFE/project/model_weights.h5")
    
    gender_model = load_model("/home/abdelghafour/Desktop/PFE/project/gender_model.h5")

    return emotion_model, gender_model


def make_predictions(model, image):
    ''' make predictions from model and return his % '''
    predictions = model.predict(image)
    index = np.argmax(predictions)
    percent = predictions.max()*100
    percent = "({:.2f})".format(percent)
    
    return predictions, index, percent
    

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.VBL = QVBoxLayout()
        
        self.FeedLabel = QLabel()
        self.VBL.addWidget(self.FeedLabel)
        
        self.CancelBTN = QPushButton('Stop')
        self.CancelBTN.clicked.connect(self.CancelFeed)
        self.VBL.addWidget(self.CancelBTN)
        
        self.CaptureBTN = QPushButton('Capture')
        self.CaptureBTN.clicked.connect(self.CaptureFeed)
        self.VBL.addWidget(self.CaptureBTN)
        
        self.Worker1 = Worker1()
        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        
        self.setLayout(self.VBL)

    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))
        
    def CancelFeed(self):
        self.Worker1.stop()
        
    def CaptureFeed(self):
        self.Worker1.start()
        

class Worker1(QThread):

    ImageUpdate = pyqtSignal(QImage)
    
    def run(self):   
        
        self.ThreadActive = True
        # Load the cascade
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        # To capture video from webcam. 
        capture = cv2.VideoCapture(0)       
        # To use a video file as input 
        # capture = cv2.VideoCapture('./capture.mp4')
        while self.ThreadActive :
            #read the frame
            ret,frame = capture.read()
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
                    gray_scale = gray[y:y+h, x:x+h]
                    
                    # for predict emotions
                    gray_48 = cv2.resize(gray_scale, (48,48))
                    emotion_pixels = image.img_to_array(gray_48)
                    emotion_pixels = np.expand_dims(emotion_pixels, axis=0)
                    
                    emotion_predictions, emotion_index, emotion_percent = make_predictions(emotion_model, emotion_pixels)
                    emotion_label = emotion_classes[emotion_index]
                    #write the prediction
                    cv2.putText(frame, emotion_label, (x,y-40) ,cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255,250,50), 2)
                    cv2.putText(frame, emotion_percent, (x+150,y-40) ,cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,250,100), 1)
                    
                    # for predict gender
                    gray_64 = cv2.resize(gray_scale, (64,64))
                    gender_pixels = image.img_to_array(gray_64)
                    gender_pixels = np.expand_dims(gender_pixels, axis=0)
                    
                    gender_predictions, gender_index, gender_percent = make_predictions(gender_model, gender_pixels)        
                    gender_label = gender_classes[gender_index]
                    #write the prediction
                    cv2.putText(frame, gender_label, (x,y-10) ,cv2.FONT_HERSHEY_SIMPLEX, 0.65, (25,250,50), 2)
                    cv2.putText(frame, gender_percent, (x+150,y-10) ,cv2.FONT_HERSHEY_SIMPLEX, 0.4, (25,250,150), 1)
        
                    #show emotions plots
                    # print(emotion_predictions)
                    for i,p in enumerate(emotion_predictions[0]):
                        cv2.putText(frame, emotion_classes[i], (10, (i+1)*15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (250,80,120), 1)
                        cv2.rectangle(frame, (80, (i+1)*15), (80+round(p*100), (i+1)*15+5), (250,200,200), -1)
                     
                    #show gender plots
                    # print(gender_predictions)
                    for i,p in enumerate(gender_predictions[0]):
                        cv2.putText(frame, gender_classes[i], (450, (i+1)*15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (20,250,10), 1)
                        cv2.rectangle(frame, (500, (i+1)*15), (500+round(p*100), (i+1)*15+5), (10,205,50), -1)
                     
                # show the frame in the window after format it
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                #FlippedImage = cv2.flip(FlippedImage,1)
                toQtFormat = QImage(Image.data, Image.shape[1], Image.shape[0], QImage.Format_RGB888)
                pic = toQtFormat.scaled(720,480, Qt.KeepAspectRatio)
                # pic = toQtFormat.scaled(1000,590)
                self.ImageUpdate.emit(pic)
                
                         
    def stop(self):
        self.ThreadActive = False
        self.quit()                    



if __name__ == "__main__" :
   	#load saved models
    emotion_model, gender_model = load_models()
    # create pyqt5 app
    App = QApplication(sys.argv)
    # create the instance of our Window
    window = MainWindow()
    # start the app
    window.show()
    
    sys.exit(App.exec())
