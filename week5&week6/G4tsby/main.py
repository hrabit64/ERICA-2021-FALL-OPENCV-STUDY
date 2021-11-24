import cv2
import easyocr
import mss
import sys
import numpy as np
from PIL import Image
import time
import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import *

reader = easyocr.Reader(['ko','en'])
mon = {'top': 0, 'left':0, 'width':1920, 'height':1080}
sct = mss.mss()
start = time.time()

class over(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 0, 300, 100)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.hp = PySide6.QtWidgets.QLabel('NONE', self)
        self.hp.move(0, 50)
        self.hp.setStyleSheet("Color: rgb(255,0,0); font-size: 32px;")
        self.show()


class m(QMainWindow):
    def __init__(self):
        super().__init__()
        self.a = over()
        self.initUI()

    def initUI(self):
        self.setGeometry(50,0,100,100)
        self.setWindowTitle('Main')
        self.show()



app = QApplication(sys.argv)
window = m()
temp = cv2.imread('temp2.png')

while True:
    sct = mss.mss()
    sct_img = sct.grab(mon)
    img = Image.frombytes('RGB', (sct_img.size.width, sct_img.size.height), sct_img.rgb)
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    # HP
    res = reader.readtext(img[35:35+65, 1250:1250+65])
    if res != [] and res[0][1][0] == 'X':
        window.a.hp.setText(res[0][1])
        window.a.hp.repaint()

    # Party
    res = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if max_val > 0.8:
        x, y = max_loc
        x = x - 193  # +422
        y = y - 34  # +33

        title = reader.readtext(img[y:y+33, x:x+422])
        print(title[1][1])


sys.exit(app.exec())
