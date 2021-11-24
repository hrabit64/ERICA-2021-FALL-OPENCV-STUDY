import os
import cv2
import numpy as np

class Preprocessing():
    __default_path__ = ''
    __square_size__ = 60

    def __init__(self, data_path):
        self.__default_path__ = data_path

    def getDefaultPath(self):
        return self.__default_path__

    def getListOfImages(self, path):
        return os.listdir(path)

    def getSobelImage(self, mode, size):
        images = []
        labels = []
        for idx, now in enumerate(['Mask', 'Non Mask']):
            default_path = os.path.join(self.__default_path__, mode, now)
            img_name_list = self.getListOfImages(default_path)

            for img_name in img_name_list:
                img = cv2.imread(os.path.join(default_path, img_name))
                img = cv2.resize(img, size)
                channels = cv2.split(img)

                for i, c in enumerate(channels):
                    channels = list(channels)
                    dx = cv2.Sobel(c, cv2.CV_64F, 1, 0, ksize=3)
                    dx = cv2.convertScaleAbs(dx)
                    dy = cv2.Sobel(c, cv2.CV_64F, 0, 1, ksize=3)
                    dy = cv2.convertScaleAbs(dy)
                    c = cv2.addWeighted(dx, 1, dy, 1, 0)
                    channels[i] = c
                img = cv2.merge(channels)
                images.append(img)
                labels.append(idx)
        return np.asarray(images) / 225, np.asarray(labels)

    def getImage(self, mode, size):
        images = []
        labels = []
        for idx, now in enumerate(['Mask', 'Non Mask']):
            default_path = os.path.join(self.__default_path__, mode, now)
            img_name_list = self.getListOfImages(default_path)

            for img_name in img_name_list:
                img = cv2.imread(os.path.join(default_path, img_name))
                img = cv2.resize(img, size)
                images.append(img)
                labels.append(idx)
        return np.asarray(images) / 225, np.asarray(labels)