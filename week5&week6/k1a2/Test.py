import Preprocess
import tensorflow.keras as keras

preprocessor = Preprocess.Preprocessing('./data/learning')
test_data_sobel, test_y_sobel = preprocessor.getSobelImage('Test', (224, 224))
test_data, test_y = preprocessor.getImage('Test', (224,224))

model_sobel = keras.models.load_model('./data/model/best_model_sobel.h5')
model = keras.models.load_model('./data/model/best_model.h5')

print('소벨 모델 정확도:', model_sobel.evaluate(test_data_sobel, test_y_sobel)[1])
print('일반 모델 정확도:', model.evaluate(test_data, test_y)[1])