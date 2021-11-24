from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.models import Model
from utils.preprocessing import img_preprocessing
import numpy as np

class FeatureExtractor:

    def __init__(self):
        vgg16_model = VGG16(weights='imagenet')
        self.extract_model = Model(inputs=vgg16_model.input, outputs=vgg16_model.get_layer('fc1').output)


    def run(self, src):

        dst = img_preprocessing(src,size=(224,224))
        model_pred = self.extract_model.predict(dst)[0]
        feature = model_pred / np.linalg.norm(model_pred)

        return feature
