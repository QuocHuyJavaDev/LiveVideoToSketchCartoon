import sys
import platform

import cv2
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from main_ui import *
from filter_func import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ######################### SKETCH #########################
        # Divide
        self.ui.btnDivide.clicked.connect(self.divide_sketch_flag)

        # Laplacian
        self.ui.btnLaplacian.clicked.connect(self.laplacian_sketch_flag)


        ######################## CARTOON ##################################
        # Thresholding
        self.ui.btnThreshold.clicked.connect(self.thresholding_cartoon_flag)

        # K-Means
        self.ui.btnKMeans.clicked.connect(self.kmeans_cartoon_flag)

        # Mean Shift
        self.ui.btnMeanShift.clicked.connect(self.mean_shift_cartoon_flag)

        self.video_capture = cv2.VideoCapture(0)
        self.video_capture.set(cv2.CAP_PROP_BUFFERSIZE, 2)

        # Create a timer for updating the video display
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_video)
        self.timer.start(30)


        ## SHOW ==> MAIN WINDOW
        self.show()

    def update_video(self):
        # Read the next frame from the video capture
        ret, frame = self.video_capture.read()
        if ret:
            # Convert the frame to RGB format
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Create QImage from the frame
            image = QImage(frame_rgb.data, frame_rgb.shape[1], frame_rgb.shape[0], QImage.Format_RGB888)
            # Create QPixmap from the QImage
            pixmap = QPixmap.fromImage(image)
            # Scale the QPixmap to fit the labels' size
            scaled_pixmap = pixmap.scaled(self.ui.lblOrVideo.size(), Qt.KeepAspectRatio)
            # Set the QPixmap on the label
            self.ui.lblOrVideo.setPixmap(scaled_pixmap)


    def divide_sketch_flag(self):
        self.timer.timeout.connect(self.divide_sketch)
        self.timer.start(30)

    def divide_sketch(self):
        ret, frame = self.video_capture.read()
        if ret:
            divide_sketch_result = FilterFunction.divide_sketch_Filter(self,frame)

    def laplacian_sketch_flag(self):
        self.timer.timeout.connect(self.laplacian_sketch)
        self.timer.start(30)

    def laplacian_sketch(self):
        ret, frame = self.video_capture.read()
        if ret:
            laplacian_sketch_result = FilterFunction.laplacian_sketch_Filter(self, frame)



    def thresholding_cartoon_flag(self):
        self.timer.timeout.connect(self.thresholding_cartoon)
        self.timer.start(30)

    def thresholding_cartoon(self):
        # Read the current frame from the video capture
        ret, frame = self.video_capture.read()
        if ret:
            thresholding_cartoon_result = FilterFunction.thresholding_cartoon_Filter(self, frame)


    def kmeans_cartoon_flag(self):
        self.timer.timeout.connect(self.kmeans_cartoon)
        self.timer.start(30)

    def kmeans_cartoon(self):
        # Read the current frame from the video capture
        ret, frame = self.video_capture.read()
        if ret:
            cartoon2 =FilterFunction.kmeans_cartoon_Filter(self, frame)

    def mean_shift_cartoon_flag(self):
        self.timer.timeout.connect(self.mean_shift_cartoon)
        self.timer.start(30)

    def mean_shift_cartoon(self):
        # Read the current frame from the video capture
        ret, frame = self.video_capture.read()
        if ret:
            cartoon2 =FilterFunction.mean_shift_cartoon_Filter(self, frame)



    def closeEvent(self, event):
        # Release the video capture and stop the timer
        self.video_capture.release()
        self.timer.stop()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())