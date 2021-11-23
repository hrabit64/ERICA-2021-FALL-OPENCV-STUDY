import os
import xml.etree.ElementTree as ET
import math
import cv2


class Preprocessing():
    __default_path__ = ''
    __square_size__ = 60

    def __init__(self, data_path):
        self.__default_path__ = data_path
        os.mkdir(os.path.join(data_path, 'with_mask'))
        os.mkdir(os.path.join(data_path, 'without_mask'))
        os.mkdir(os.path.join(data_path, 'mask_weared_incorrect'))

    def getDefaultPath(self):
        return  self.__default_path__

    def getListOfImages(self):
        return os.listdir(os.path.join(self.__default_path__, 'images'))