from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoadingScreen(object):
    def setupUi(self, LoadingScreen):
        LoadingScreen.setObjectName("LoadingScreen")
        LoadingScreen.resize(800, 493)
        self.centralwidget = QtWidgets.QWidget(LoadingScreen)
        font = QtGui.QFont()
        font.setFamily("Serif")
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("QWidget{\n"
"background-color: rgb(26, 164, 255);\n"
"border-radius: 10px;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(60, 60, 60, 20)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 95))
        font = QtGui.QFont()
        font.setFamily("Fredoka One")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-top: 2px solid rgb(255, 255, 255);\n"
"border-radius: 0;\n"
"padding-top: 12px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Fredoka One")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setFamily("Fredoka One")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("border-bottom: 2px solid rgb(255, 255, 255);\n"
"border-radius: 0;\n"
"padding-bottom: 12px;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/emotions.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setStyleSheet("QProgressBar{\n"
"color: rgb(255, 255, 255);\n"
"text-align:center;\n"
"}\n"
"QProgressBar:chunk{\n"
"background-color: rgb(255, 241, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.483, x2:1, y2:0.5, stop:0 rgba(255, 243, 75, 255), stop:1 rgba(255, 202, 79, 255));\n"
"border-radius:10px;\n"
"}\n"
"\n"
"")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(250, 250, 250);")
        self.label_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        LoadingScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoadingScreen)
        QtCore.QMetaObject.connectSlotsByName(LoadingScreen)

    def retranslateUi(self, LoadingScreen):
        _translate = QtCore.QCoreApplication.translate
        LoadingScreen.setWindowTitle(_translate("LoadingScreen", "MainWindow"))
        self.label_2.setText(_translate("LoadingScreen", "Face Emotion Detection "))
        self.label_3.setText(_translate("LoadingScreen", "&"))
        self.label_4.setText(_translate("LoadingScreen", "Gender Detection "))
        self.label_6.setText(_translate("LoadingScreen", "By Abelghafour Bamoula & Soukaina Ougouammou"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoadingScreen = QtWidgets.QMainWindow()
    ui = Ui_LoadingScreen()
    ui.setupUi(LoadingScreen)
    LoadingScreen.show()
    sys.exit(app.exec_())

