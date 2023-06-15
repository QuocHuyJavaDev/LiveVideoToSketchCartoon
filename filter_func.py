import cv2
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QImage)
from sklearn.cluster import MeanShift, estimate_bandwidth
import numpy as np


class FilterFunction():

    ################################# SKETCH ######################################

    # Divide
    def divide_sketch_Filter(self, frame):
        # lọc tăng sawcs nét ảnh bằng cách làm nổi bật các biên cạnh ảnh
        kernel_sharpening = np.array([[-1, -1, -1],
                                      [-1, 9, -1],
                                      [-1, -1, -1]])
        frame = cv2.filter2D(frame, -1, kernel_sharpening)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        invertImage = 255 - gray
        # Làm mờ ảnh và loại bỏ nhiễu
        blurred = cv2.GaussianBlur(invertImage, (15, 15), 0)
        invBlurred = 255 - blurred
        # chia từng pixel trong gray cho từng pixel tương ứng trong invBlurred. KQ gioi hạn 0-255
        sketch = cv2.divide(gray, invBlurred, scale=256.0)
        sketch_frame_rgb = cv2.cvtColor(sketch, cv2.COLOR_GRAY2RGB)
        # Create QImage from the sketch frame
        sketch_image = QImage(sketch_frame_rgb.data, sketch_frame_rgb.shape[1], sketch_frame_rgb.shape[0],
                              QImage.Format_RGB888)
        # Create QPixmap from the QImage
        sketch_pixmap = QPixmap.fromImage(sketch_image)
        # Scale the QPixmap to fit the sketch label's size
        scaled_sketch_pixmap = sketch_pixmap.scaled(self.ui.lblEditVideo.size(), Qt.KeepAspectRatio)
        # Set the QPixmap on the sketch label
        self.ui.lblEditVideo.setPixmap(scaled_sketch_pixmap)
        return sketch_frame_rgb

    # Laplacian
    def laplacian_sketch_Filter(self, frame):
        src = cv2.GaussianBlur(frame, (3, 3), 0)
        src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        ddepth = cv2.CV_16S
        kernel_size = 3
        dst = cv2.Laplacian(src_gray, ddepth, ksize=kernel_size)
        abs_dst = cv2.convertScaleAbs(dst)
        result = cv2.bitwise_not(abs_dst)
        frame_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
        cartoon_image = QImage(frame_rgb.data, frame_rgb.shape[1], frame_rgb.shape[0], QImage.Format_RGB888)
        # Create QPixmap from the QImage
        sketch_pixmap = QPixmap.fromImage(cartoon_image)
        # Scale the QPixmap to fit the sketch label's size
        scaled_sketch_pixmap = sketch_pixmap.scaled(self.ui.lblEditVideo.size(), Qt.KeepAspectRatio)
        # Set the QPixmap on the sketch label
        self.ui.lblEditVideo.setPixmap(scaled_sketch_pixmap)

    ##################### CARTOON ################################

    # Thresholding 
    def thresholding_cartoon_Filter(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
        color = cv2.bilateralFilter(frame, 9, 300, 300)
        cartoon = cv2.bitwise_and(color, color, mask=edges)
        frame_rgb = cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB)
        # Create QImage from the sketch frame
        sketch_image = QImage(frame_rgb.data, frame_rgb.shape[1], frame_rgb.shape[0], QImage.Format_RGB888)
        # Create QPixmap from the QImage
        sketch_pixmap = QPixmap.fromImage(sketch_image)
        # Scale the QPixmap to fit the sketch label's size
        scaled_sketch_pixmap = sketch_pixmap.scaled(self.ui.lblEditVideo.size(), Qt.KeepAspectRatio)
        # Set the QPixmap on the sketch label
        self.ui.lblEditVideo.setPixmap(scaled_sketch_pixmap)

    # K-Means
    def kmeans_cartoon_Filter(self, frame):
        frame_width = int(frame.shape[1])
        frame_height = int(frame.shape[0])
        print(frame_width)
        print(frame_height)
        framecopy = frame
        framecopy = cv2.resize(framecopy, (int(frame_width) - 380, int(frame_height) - 380))
        div = 10
        framecopy = framecopy // div * div + div // 2
        # chuyển từ dạng ma trận 2D sang dạng vector 2D có kích thước (N, 3)
        vectorized = framecopy.reshape((-1, 3))
        vectorized = np.float32(vectorized)
        # Xác định tiêu chí dừng
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        #  Số lần thử để chạy thuật toán K-means với các tâm khởi tạo khác nhau. Kết quả tốt nhất sẽ được chọn.
        attempts = 10
        # pp chọn tâm cu bằng KMEANS_PP_CENTERS
        ret, label, centers = cv2.kmeans(vectorized, 10, None, criteria, attempts, cv2.KMEANS_PP_CENTERS)
        centers = np.uint8(centers)
        res = centers[label.flatten()]
        result_image = res.reshape((framecopy.shape))
        #result_image = result_image + 10
        result_image = cv2.resize(result_image, (int(frame_width), int(frame_height)))
        frame_rgb = cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB)
        # Create QImage from the sketch frame
        sketch_image = QImage(frame_rgb.data, frame_rgb.shape[1], frame_rgb.shape[0], QImage.Format_RGB888)
        # Create QPixmap from the QImage
        sketch_pixmap = QPixmap.fromImage(sketch_image)
        # Scale the QPixmap to fit the sketch label's size
        scaled_sketch_pixmap = sketch_pixmap.scaled(self.ui.lblEditVideo.size(), Qt.KeepAspectRatio)
        # Set the QPixmap on the sketch label
        self.ui.lblEditVideo.setPixmap(scaled_sketch_pixmap)

    # Mean Shift
    def mean_shift_cartoon_Filter(self, frame):
        frame_width = int(frame.shape[1])
        frame_height = int(frame.shape[0])
        print(frame_width)
        print(frame_height)
        framecopy = frame
        framecopy = cv2.resize(framecopy, (int(frame_width) - 380, int(frame_height) - 380))
        div = 30
        framecopy = framecopy // div * div + div // 2
        vectorized = framecopy.reshape((-1, 3))
        bandwidth = estimate_bandwidth(vectorized, quantile=0.1, n_samples=100)
        ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
        #Dán nhãn cho từng cụm dữ liệu
        ms.fit(vectorized)
        # Xuất ra 1 mảng ds các label
        labels = ms.labels_
        # Mảng chứa các tâm cụm
        centers = ms.cluster_centers_
        # Chuyển các giá trị center sang so nguyên đảm bảo giá trị trong mảng centers nằm trong khoảng từ 0 đến 255
        centers = np.uint8(centers)
        # Mảng res chứa các giá trị điểm ảnh trong cụm ảnh thành giá trị center
        res = centers[labels.flatten()]
        result_image = res.reshape((framecopy.shape))
        result_image = cv2.resize(result_image, (int(frame_width), int(frame_height)))
        frame_rgb = cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB)
        # Create QImage from the sketch frame
        sketch_image = QImage(frame_rgb.data, frame_rgb.shape[1], frame_rgb.shape[0], QImage.Format_RGB888)
        # Create QPixmap from the QImage
        sketch_pixmap = QPixmap.fromImage(sketch_image)
        # Scale the QPixmap to fit the sketch label's size
        scaled_sketch_pixmap = sketch_pixmap.scaled(self.ui.lblEditVideo.size(), Qt.KeepAspectRatio)
        # Set the QPixmap on the sketch label
        self.ui.lblEditVideo.setPixmap(scaled_sketch_pixmap)

