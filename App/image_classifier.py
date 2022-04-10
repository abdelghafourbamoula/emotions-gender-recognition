from PyQt5 import QtCore, QtGui, QtWidgets
import tensorflow as tf
import numpy as np
import cv2
from utils import load_models, make_predictions
from utils import emotion_classes, gender_classes
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import seaborn as sns
import matplotlib.pyplot as plt


class Ui_ImagecClassifieRScreen(object):
    def setupUi(self, ImagecClassifieRScreen):
        ImagecClassifieRScreen.setObjectName("ImagecClassifieRScreen")
        ImagecClassifieRScreen.resize(920, 600)
        ImagecClassifieRScreen.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(ImagecClassifieRScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header_frame = QtWidgets.QFrame(self.centralwidget)
        self.header_frame.setMaximumSize(QtCore.QSize(16777215, 60))
        self.header_frame.setStyleSheet("QFrame{\n"
"border-radius: 5px;\n"
"border: 1px solid rgb(200, 200, 200);\n"
"}")
        self.header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_frame.setObjectName("header_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setContentsMargins(20, 5, 20, 5)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.choseImage_btn = QtWidgets.QPushButton(self.header_frame)
        self.choseImage_btn.setMinimumSize(QtCore.QSize(135, 0))
        self.choseImage_btn.setStyleSheet("QPushButton{\n"
"background-color: rgb(158, 158, 158);\n"
"border-style: none;\n"
"padding: 2px;\n"
"color: rgb(253, 253, 253);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(188, 188, 190);\n"
"padding: 3px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(88, 148, 150);\n"
"padding: 2px;\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/photo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.choseImage_btn.setIcon(icon)
        self.choseImage_btn.setIconSize(QtCore.QSize(32, 26))
        self.choseImage_btn.setAutoDefault(True)
        self.choseImage_btn.setDefault(False)
        self.choseImage_btn.setObjectName("choseImage_btn")
        self.horizontalLayout_2.addWidget(self.choseImage_btn)
        self.imagePath_field = QtWidgets.QLineEdit(self.header_frame)
        self.imagePath_field.setMinimumSize(QtCore.QSize(480, 28))
        self.imagePath_field.setStyleSheet("border-color: rgb(143, 143, 143);\n"
"color: rgb(117, 117, 117);\n"
"paddding: 3px;")
        self.imagePath_field.setObjectName("imagePath_field")
        self.horizontalLayout_2.addWidget(self.imagePath_field)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.predict_btn = QtWidgets.QPushButton(self.header_frame)
        self.predict_btn.setMinimumSize(QtCore.QSize(175, 0))
        self.predict_btn.setStyleSheet("QPushButton{\n"
"background-color: rgb(8, 177, 129);\n"
"border-style: none;\n"
"padding: 4px;\n"
"color: rgb(253, 253, 253);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(28, 197, 139);\n"
"padding: 3px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(18, 137, 109);\n"
"padding: 2px;\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/work-done.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.predict_btn.setIcon(icon1)
        self.predict_btn.setIconSize(QtCore.QSize(26, 26))
        self.predict_btn.setObjectName("predict_btn")
        self.horizontalLayout_2.addWidget(self.predict_btn)
        self.verticalLayout.addWidget(self.header_frame)
        self.center_frame = QtWidgets.QFrame(self.centralwidget)
        self.center_frame.setStyleSheet("border-style: none;")
        self.center_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.center_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.center_frame.setObjectName("center_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.center_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.images_frame = QtWidgets.QFrame(self.center_frame)
        self.images_frame.setMinimumSize(QtCore.QSize(400, 0))
        self.images_frame.setMaximumSize(QtCore.QSize(500, 16777215))
        self.images_frame.setStyleSheet("QFrame{\n"
"border-radius: 5px;\n"
"border: 1px solid rgb(200, 200, 200);\n"
"}")
        self.images_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.images_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.images_frame.setObjectName("images_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.images_frame)
        self.verticalLayout_2.setContentsMargins(15, 5, 15, 5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.detectedFaces_label = QtWidgets.QLabel(self.images_frame)
        self.detectedFaces_label.setMinimumSize(QtCore.QSize(0, 30))
        self.detectedFaces_label.setMaximumSize(QtCore.QSize(500, 25))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(12)
        self.detectedFaces_label.setFont(font)
        self.detectedFaces_label.setStyleSheet("color: rgb(101, 101, 101);")
        self.detectedFaces_label.setText("")
        self.detectedFaces_label.setAlignment(QtCore.Qt.AlignCenter)
        self.detectedFaces_label.setObjectName("detectedFaces_label")
        self.verticalLayout_2.addWidget(self.detectedFaces_label)
        self.loadedimage_label = QtWidgets.QLabel(self.images_frame)
        self.loadedimage_label.setMinimumSize(QtCore.QSize(250, 200))
        self.loadedimage_label.setMaximumSize(QtCore.QSize(500, 400))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.loadedimage_label.setFont(font)
        self.loadedimage_label.setText("")
        self.loadedimage_label.setPixmap(QtGui.QPixmap("../../../.designer/project/test_images/1_HEoLBLidT2u4mhJ0oiDgig.png"))
        self.loadedimage_label.setScaledContents(True)
        self.loadedimage_label.setObjectName("loadedimage_label")
        self.verticalLayout_2.addWidget(self.loadedimage_label)
        self.horizontalLayout.addWidget(self.images_frame)
        self.detectedfaces = QtWidgets.QFrame(self.center_frame)
        self.detectedfaces.setMinimumSize(QtCore.QSize(600, 0))
        self.detectedfaces.setStyleSheet("QFrame{\n"
"border-radius: 5px;\n"
"border: 1px solid rgb(200, 200, 200);\n"
"}")
        self.detectedfaces.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.detectedfaces.setFrameShadow(QtWidgets.QFrame.Raised)
        self.detectedfaces.setObjectName("detectedfaces")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.detectedfaces)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.predictions_label = QtWidgets.QLabel(self.detectedfaces)
        self.predictions_label.setMaximumSize(QtCore.QSize(16777215, 150))
        self.predictions_label.setText("")
        self.predictions_label.setPixmap(QtGui.QPixmap("../../../Screenshot_select-area_20220328235007.png"))
        self.predictions_label.setScaledContents(True)
        self.predictions_label.setObjectName("predictions_label")
        self.verticalLayout_3.addWidget(self.predictions_label)
        self.plots_frame = QtWidgets.QFrame(self.detectedfaces)
        self.plots_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.plots_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.plots_frame.setObjectName("plots_frame")
        self.plots_frame.setStyleSheet('padding:10px;')
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.plots_frame)
        self.plot_label = QtWidgets.QLabel(self.plots_frame)
        self.plot_label.setText("")
        self.plot_label.setScaledContents(True)
        self.plot_label.setObjectName("plot_label")
        self.verticalLayout_3.addWidget(self.predictions_label)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.addWidget(self.plot_label)
        self.verticalLayout_3.addWidget(self.plots_frame)
        self.horizontalLayout.addWidget(self.detectedfaces)
        self.verticalLayout.addWidget(self.center_frame)
        self.footer_frame = QtWidgets.QFrame(self.centralwidget)
        self.footer_frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.footer_frame.setStyleSheet("border-style: none;")
        self.footer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer_frame.setObjectName("footer_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.footer_frame)
        self.horizontalLayout_3.setContentsMargins(7, 2, 7, 2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.back_btn = QtWidgets.QPushButton(self.footer_frame)
        self.back_btn.setMinimumSize(QtCore.QSize(50, 0))
        self.back_btn.setStyleSheet("QPushButton{\n"
"background-color: rgb(85, 85, 245);\n"
"border-style: none;\n"
"padding:5px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(105, 105, 255);\n"
"padding: 3px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(70, 70, 205);\n"
"padding: 6px;\n"
"}\n"
"")
        self.back_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/images/left-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_btn.setIcon(icon2)
        self.back_btn.setIconSize(QtCore.QSize(32, 20))
        self.back_btn.setObjectName("back_btn")
        self.horizontalLayout_3.addWidget(self.back_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.exit_btn = QtWidgets.QPushButton(self.footer_frame)
        self.exit_btn.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.exit_btn.setFont(font)
        self.exit_btn.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.exit_btn.setStyleSheet("QPushButton{\n"
"background-color: rgb(230, 60, 75);\n"
"\n"
"border-style: none;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(245, 70, 70);\n"
"padding: 3px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(225, 60, 60);\n"
"padding: 6px;\n"
"}\n"
"")
        self.exit_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn.setIcon(icon3)
        self.exit_btn.setIconSize(QtCore.QSize(26, 26))
        self.exit_btn.setAutoDefault(True)
        self.exit_btn.setDefault(False)
        self.exit_btn.setFlat(False)
        self.exit_btn.setObjectName("exit_btn")
        self.horizontalLayout_3.addWidget(self.exit_btn)
        self.verticalLayout.addWidget(self.footer_frame)
        ImagecClassifieRScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(ImagecClassifieRScreen)
        QtCore.QMetaObject.connectSlotsByName(ImagecClassifieRScreen)

        #  browse images
        self.choseImage_btn.clicked.connect(self.browse_images)
        # predict image
        self.predict_btn.clicked.connect(self.predict)
        # exit window
        self.exit_btn.clicked.connect(self.exit)
        
    def browse_images(self):
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(
                parent=None, 
                caption="Open files", 
                directory="/home/abdelghafour/Desktop/PFE/project/test_images", 
                filter="Images (*.png *.jpg *.jpeg)", 
                options=QtWidgets.QFileDialog.DontUseNativeDialog
        )
        self.imagePath_field.setText(file_name)
        # print(file_name)
        
    def predict(self):
        img_path = self.imagePath_field.text()
        # Load the cascade
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        # Read the input image
        img = cv2.imread(img_path)
        # Convert into grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect faces
        faces = face_cascade.detectMultiScale(
                                        gray,
                                        scaleFactor = 1.1,
                                        minNeighbors = 5,
                                        minSize = (30, 30)
                                )
        #--- add pixmap image
        self.detectedFaces_label.setText(f"Detected Faces: {len(faces)}")
        emotion_model, gender_model = load_models()
        pred_txt = ''
        i=0
        for (x, y, w, h) in faces:                
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
                gray_scale = gray[y:y+h, x:x+w]            
                gray_48 = cv2.resize(gray_scale, (48,48))
                emotion_predictions, em_index, em_percent = make_predictions(emotion_model, gray_48)        
                emotion_label = emotion_classes[em_index]
                cv2.putText(img, emotion_label, (x,y-30) ,cv2.FONT_HERSHEY_SIMPLEX, 0.85, (255,250,50), 2)
                cv2.putText(img, em_percent, (x+x//2,y-30) ,cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,250,100), 1)
                
                gray_64 = cv2.resize(gray_scale, (64,64))                
                gender_predictions, gender_index, gender_percent = make_predictions(gender_model, gray_64)        
                gender_label = gender_classes[gender_index]
                #write the prediction
                cv2.putText(img, gender_label, (x,y-10) ,cv2.FONT_HERSHEY_SIMPLEX, 0.45, (25,250,50), 2)
                cv2.putText(img, gender_percent, (x+x//2,y-10) ,cv2.FONT_HERSHEY_SIMPLEX, 0.4, (25,250,150), 1)

                plt.figure()
                # sns.set_theme()
                sns.set_style("white")
                plt.subplot(1,2,1)
                sns.barplot(x=np.arange(7), y=emotion_predictions[0])
                # plt.xticks(np.arange(7), ['angry','disgust','fear','happy','sad','surprise','neutral'])
                plt.title('emotions predictions')
                plt.xlabel('emotions')
                plt.ylabel('percent')
                plt.subplot(1,2,2)
                # sns.set()
                plt.pie(gender_predictions[0], labels=['female', 'male'], autopct = '%0.0f%%')
                plt.legend()
                plt.title('gender predictions')
                
                plt.savefig('/home/abdelghafour/Desktop/PFE/App/images/plot.png')
                self.plot_label.setPixmap(QtGui.QPixmap("/home/abdelghafour/Desktop/PFE/App/images/plot.png"))
                
       
                pred_txt += f"- face {i+1}: {emotion_label} {gender_label}\n"
                i+=1
                
        self.predictions_label.setText(pred_txt)
        
        # show image
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        image = QtGui.QImage(img, img.shape[1], img.shape[0], img.strides[0], QtGui.QImage.Format_RGB888)
        pixMapImage = QtGui.QPixmap.fromImage(image)
        self.loadedimage_label.setPixmap(pixMapImage)     
                   
                        
    def exit(self):
        sys.exit(app.exec_())
        
 
    def retranslateUi(self, ImagecClassifieRScreen):
        _translate = QtCore.QCoreApplication.translate
        ImagecClassifieRScreen.setWindowTitle(_translate("ImagecClassifieRScreen", "MainWindow"))
        self.choseImage_btn.setText(_translate("ImagecClassifieRScreen", "chose image"))
        self.predict_btn.setText(_translate("ImagecClassifieRScreen", "Make Predictions"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ImagecClassifieRScreen = QtWidgets.QMainWindow()
    ui = Ui_ImagecClassifieRScreen()
    ui.setupUi(ImagecClassifieRScreen)
    ImagecClassifieRScreen.show()
    sys.exit(app.exec_())

