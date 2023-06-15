# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainxufYze.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1000)
        MainWindow.setStyleSheet(u"background-color: rgb(25, 25, 25);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lblOrVideo = QLabel(self.centralwidget)
        self.lblOrVideo.setObjectName(u"lblOrVideo")
        self.lblOrVideo.setGeometry(QRect(10, 70, 940, 902))
        self.lblOrVideo.setStyleSheet(u"background-color: rgb(49, 49, 49);\n"
"border-radius: 25px;")
        self.lblEditVideo = QLabel(self.centralwidget)
        self.lblEditVideo.setObjectName(u"lblEditVideo")
        self.lblEditVideo.setGeometry(QRect(970, 70, 940, 902))
        self.lblEditVideo.setStyleSheet(u"background-color: rgb(49, 49, 49);\n"
"border-radius: 25px;")
        self.btnDivide = QPushButton(self.centralwidget)
        self.btnDivide.setObjectName(u"btnDivide")
        self.btnDivide.setGeometry(QRect(100, 20, 111, 41))
        font = QFont()
        font.setFamily(u"Arial Narrow")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnDivide.setFont(font)
        self.btnDivide.setStyleSheet(u"background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.btnLaplacian = QPushButton(self.centralwidget)
        self.btnLaplacian.setObjectName(u"btnLaplacian")
        self.btnLaplacian.setGeometry(QRect(230, 20, 111, 41))
        font1 = QFont()
        font1.setFamily(u"Arial Narrow")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.btnLaplacian.setFont(font1)
        self.btnLaplacian.setStyleSheet(u"background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.lblSketch = QLabel(self.centralwidget)
        self.lblSketch.setObjectName(u"lblSketch")
        self.lblSketch.setGeometry(QRect(14, 5, 941, 61))
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        self.lblSketch.setFont(font2)
        self.lblSketch.setStyleSheet(u"color: rgb(203, 203, 203);\n"
"padding-left: 15px;")
        self.lblSketch.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lblCartoon = QLabel(self.centralwidget)
        self.lblCartoon.setObjectName(u"lblCartoon")
        self.lblCartoon.setGeometry(QRect(959, 5, 941, 61))
        self.lblCartoon.setFont(font2)
        self.lblCartoon.setStyleSheet(u"color: rgb(203, 203, 203);\n"
"padding-left: 25px;\n"
"border-left: 2px solid #a1a1a1;")
        self.lblCartoon.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.btnThreshold = QPushButton(self.centralwidget)
        self.btnThreshold.setObjectName(u"btnThreshold")
        self.btnThreshold.setGeometry(QRect(1070, 20, 111, 41))
        self.btnThreshold.setFont(font1)
        self.btnThreshold.setStyleSheet(u"background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.btnKMeans = QPushButton(self.centralwidget)
        self.btnKMeans.setObjectName(u"btnKMeans")
        self.btnKMeans.setGeometry(QRect(1200, 20, 111, 41))
        self.btnKMeans.setFont(font)
        self.btnKMeans.setStyleSheet(u"background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.btnSave = QPushButton(self.centralwidget)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setGeometry(QRect(1820, 10, 81, 51))
        font3 = QFont()
        font3.setFamily(u"Arial Narrow")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.btnSave.setFont(font3)
        self.btnSave.setStyleSheet(u"background-color: #F2DD6C;\n"
"color: rgb(0,0,0);\n"
"border-radius: 20px;")
        self.btnRecord = QPushButton(self.centralwidget)
        self.btnRecord.setObjectName(u"btnRecord")
        self.btnRecord.setGeometry(QRect(1720, 10, 81, 51))
        self.btnRecord.setFont(font3)
        self.btnRecord.setStyleSheet(u"background-color: #F2DD6C;\n"
"color: rgb(0,0,0);\n"
"border-radius: 20px;")
        self.btnMeanShift = QPushButton(self.centralwidget)
        self.btnMeanShift.setObjectName(u"btnMeanShift")
        self.btnMeanShift.setGeometry(QRect(1330, 20, 111, 41))
        self.btnMeanShift.setFont(font)
        self.btnMeanShift.setStyleSheet(u"background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.lblSketch.raise_()
        self.lblOrVideo.raise_()
        self.lblEditVideo.raise_()
        self.btnDivide.raise_()
        self.btnLaplacian.raise_()
        self.lblCartoon.raise_()
        self.btnThreshold.raise_()
        self.btnKMeans.raise_()
        self.btnSave.raise_()
        self.btnRecord.raise_()
        self.btnMeanShift.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lblOrVideo.setText("")
        self.lblEditVideo.setText("")
        self.btnDivide.setText(QCoreApplication.translate("MainWindow", u"Divide", None))
        self.btnLaplacian.setText(QCoreApplication.translate("MainWindow", u"Laplacian", None))
        self.lblSketch.setText(QCoreApplication.translate("MainWindow", u"SKETCH", None))
        self.lblCartoon.setText(QCoreApplication.translate("MainWindow", u"CARTOON", None))
        self.btnThreshold.setText(QCoreApplication.translate("MainWindow", u"Threshold", None))
        self.btnKMeans.setText(QCoreApplication.translate("MainWindow", u"K-Means", None))
        self.btnSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btnRecord.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.btnMeanShift.setText(QCoreApplication.translate("MainWindow", u"Mean Shift", None))
    # retranslateUi

