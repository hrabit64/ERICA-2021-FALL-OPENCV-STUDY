import cv2
import numpy as np
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing import image

def img_preprocessing(src=None, size=(224, 224)):
    if src is None:
        print("Img type error > img is None")
        raise TypeError

    src = src.resize((224,224))
    src.convert('RGB')
    dst = image.img_to_array(src)
    dst = np.expand_dims(dst, axis=0)
    dst = preprocess_input(dst)

    return dst

