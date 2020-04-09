from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import cv2 as cv
import numpy as np
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import (QApplication, QDialog, QFileDialog, QGridLayout,
                             QLabel, QPushButton)
fname=''

class Ui_Form(QWidget):
    def __init__(self):

        super(Ui_Form,self).__init__()

        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(603, 596)
        self.center()  # 使窗口居中
        self.setWindowTitle("label显示图片")
        self.setWindowIcon(QIcon('1.jpg'))
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 281, 281))
        self.groupBox.setObjectName("groupBox")
        self.btn1 = QtWidgets.QPushButton(self.groupBox)
        self.btn1.setGeometry(QtCore.QRect(100, 10, 75, 23))
        self.btn1.setObjectName("btn1")
        self.btn1.clicked.connect(self.open)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 40, 261, 231))
        self.label.setText("")
        self.label.setObjectName("label")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(9, 289, 281, 281))
        self.groupBox_3.setObjectName("groupBox_3")
        self.btn3 = QtWidgets.QPushButton(self.groupBox_3)
        self.btn3.setGeometry(QtCore.QRect(190, 10, 71, 23))
        self.btn3.setObjectName("btn3")
        self.btn3.clicked.connect(self.tuxiangzengqiang)
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(10, 41, 261, 231))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox.setGeometry(QtCore.QRect(80, 10, 91, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.currentTextChanged.connect(self.xuanxiang)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(310, 0, 281, 281))
        self.groupBox_2.setObjectName("groupBox_2")
        self.btn2 = QtWidgets.QPushButton(self.groupBox_2)
        self.btn2.setGeometry(QtCore.QRect(110, 10, 75, 23))
        self.btn2.setObjectName("btn2")
        self.btn2.clicked.connect(self.guolv)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 41, 261, 231))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(310, 290, 281, 281))
        self.groupBox_4.setObjectName("groupBox_4")
        self.btn4 = QtWidgets.QPushButton(self.groupBox_4)
        self.btn4.setGeometry(QtCore.QRect(110, 10, 75, 23))
        self.btn4.setObjectName("btn4")
        self.btn4.clicked.connect(self.erzhihua)
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(10, 41, 261, 231))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "原图"))
        self.btn1.setText(_translate("Form", "打开"))
        self.groupBox_3.setTitle(_translate("Form", "图像增强"))
        self.btn3.setText(_translate("Form", "处理"))
        self.comboBox.setItemText(0, _translate("Form", "对数变换"))
        self.comboBox.setItemText(1, _translate("Form", "非线性变换"))
        self.comboBox.setItemText(2, _translate("Form", "伽马变换"))
        self.comboBox.setItemText(3, _translate("Form", "直方图均衡"))
        self.comboBox.setItemText(4, _translate("Form", "限制性均衡"))
        self.groupBox_2.setTitle(_translate("Form", "过滤"))
        self.btn2.setText(_translate("Form", "处理"))
        self.groupBox_4.setTitle(_translate("Form", "二值化"))
        self.btn4.setText(_translate("Form", "处理"))

    def open(self):
        global fname
        global one
        global two
        QMessageBox.question(self, '提醒', '选择图片时要是绝对路径(且全英文路径)',
                             QMessageBox.Ok)
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*;;*.png;;All Files(*)")
        # jpg = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
        # self.label.setPixmap(QPixmap(jpg))
        # self.label2.setPixmap(QPixmap(jpg))

        image = cv.imread(imgName)
        if image is None:
            print("未选择图片")
        else:
            size = (int(self.label.width()), int(self.label.height()))
            shrink = cv.resize(image, size, interpolation=cv.INTER_AREA)
            shrink = cv.cvtColor(shrink, cv.COLOR_BGR2RGB)
            self.QtImg = QtGui.QImage(shrink.data,
                                      shrink.shape[1],
                                      shrink.shape[0],
                                      shrink.shape[1]*3,
                                      QtGui.QImage.Format_RGB888)
            self.label.setPixmap(QtGui.QPixmap.fromImage(self.QtImg))
            #self.label2.setPixmap(QtGui.QPixmap.fromImage(self.QtImg))
            fname = imgName
            print(imgName)
            one = 50
            two = 50


    def guolv(self):
        global fname
        image = cv.imread(fname)
        if image is None:
            print("未选择图片")
        else:
            image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
            image = cv.blur(image,(5,5))
            size = (int(self.label_2.width()), int(self.label_2.height()))
            shrink = cv.resize(image, size, interpolation=cv.INTER_AREA)
            shrink = cv.cvtColor(shrink, cv.COLOR_BGR2RGB)
            self.QtImg = QtGui.QImage(shrink.data,
                                      shrink.shape[1],
                                      shrink.shape[0],
                                      shrink.shape[1]*3,
                                      QtGui.QImage.Format_RGB888)
            self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.QtImg))


    def erzhihua(self):
        global fname
        image = cv.imread(fname)
        if image is None:
            print("未选择图片")
        else:
            image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
            ret, binary = cv.threshold(image, 0, 255, cv.THRESH_OTSU | cv.THRESH_BINARY)
            print("二值化的阈值为:", ret)
            size = (int(self.label_4.width()), int(self.label_4.height()))
            shrink = cv.resize(binary, size, interpolation=cv.INTER_AREA)
            shrink = cv.cvtColor(shrink, cv.COLOR_BGR2RGB)
            self.QtImg = QtGui.QImage(shrink.data,
                                      shrink.shape[1],
                                      shrink.shape[0],
                                      shrink.shape[1]*3,
                                      QtGui.QImage.Format_RGB888)
            self.label_4.setPixmap(QtGui.QPixmap.fromImage(self.QtImg))

    def tuxiangzengqiang(self):
        global fname
        image = cv.imread(fname)
        if image is None:
            print("未选择图片")
        else:
            if self.str == '伽马变换':
                image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
                def gamma(img, c, v):
                    lut = np.zeros(256, dtype=np.float32)
                    for i in range(256):
                        lut[i] = c * i ** v
                    output_img = cv.LUT(img, lut)  # 像素灰度值的映射
                    output_img = np.uint8(output_img + 0.5)
                    return output_img
                out_put = gamma(image,0.0000005,4)
                out_image = out_put

            if self.str =='非线性变换':
                image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
                height = image.shape[0]
                width = image.shape[1]
                result = np.zeros((height,width),np.uint8)
                for i in range(height):
                    for j in range(width):
                        gray = int(image[i, j]) * int(image[i, j]) / 255
                        result[i, j] = np.uint8(gray)
                out_image = result

            if self.str =='对数变换':
                image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
                def log(c,img):
                    out_put = c*np.log(1.0+img)
                    out_put = np.uint8(out_put+0.5)
                    return out_put
                out_image = log(42,image)
            if self.str =='直方图均衡':
                image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
                out_image = cv.equalizeHist(image)

            if self.str =='限制性均衡':
                image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
                clahe = cv.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
                out_image = clahe.apply(image)


            size = (int(self.label_3.width()), int(self.label_3.height()))
            shrink = cv.resize(out_image, size, interpolation=cv.INTER_AREA)
            shrink = cv.cvtColor(shrink, cv.COLOR_BGR2RGB)
            self.QtImg = QtGui.QImage(shrink.data,
                                    shrink.shape[1],
                                    shrink.shape[0],
                                    shrink.shape[1] * 3,
                                    QtGui.QImage.Format_RGB888)
            self.label_3.setPixmap(QtGui.QPixmap.fromImage(self.QtImg))

    def xuanxiang(self):
        self.str = self.comboBox.currentText()
        print(self.str)




    def center(self):  # 控制窗口显示在屏幕中心的方法

        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fileload =  Ui_Form()
    fileload.show()
    sys.exit(app.exec_())
