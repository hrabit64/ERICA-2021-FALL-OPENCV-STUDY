import Model
import Preprocess
import tensorflow.keras as keras
import tensorflow as tf
# tf.debugging.set_log_device_placement(True)

def main():
    preprocessor = Preprocess.Preprocessing('./data/learning')

    train_data_sobel, train_y_sobel = preprocessor.getSobelImage('Train', (224,224))
    val_data_sobel, val_y_sobel = preprocessor.getSobelImage('Validation', (224,224))
    test_data_sobel, test_y_sobel = preprocessor.getSobelImage('Test', (224,224))

    vgg16 = Model.VGG16()
    model_sobel = vgg16.build()
    model_sobel.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])

    callbacks = [keras.callbacks.EarlyStopping(monitor='accuracy', mode='max', patience=5),
                 keras.callbacks.ModelCheckpoint(filepath='./data/model/best_model_sobel.h5', monitor='accuracy', save_best_only=True)]
    model_sobel.fit(train_data_sobel, train_y_sobel, nb_epoch=50, batch_size=32,
                    validation_data=(val_data_sobel, val_y_sobel), shuffle=True, callbacks=callbacks)

    train_data, train_y = preprocessor.getImage('Train', (224,224))
    val_data, val_y = preprocessor.getImage('Validation', (224,224))
    test_data, test_y = preprocessor.getImage('Test', (224,224))

    vgg16 = Model.VGG16()
    model = vgg16.build()
    model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])

    callbacks = [keras.callbacks.EarlyStopping(monitor='accuracy', mode='max', patience=5),
                 keras.callbacks.ModelCheckpoint(filepath='./data/model/best_model.h5', monitor='accuracy', save_best_only=True)]
    model.fit(train_data, train_y, nb_epoch=50, batch_size=32,
                    validation_data=(val_data, val_y), shuffle=True, callbacks=callbacks)

    model_sobel = keras.models.load_model('./data/model/best_model_sobel.h5')
    model = keras.models.load_model('./data/model/best_model.h5')

    print('소벨 모델 정확도:', model_sobel.evaluate(test_data_sobel, test_y_sobel)[1])
    print('일반 모델 정확도:', model.evaluate(test_data, test_y)[1])

if __name__ == '__main__':
    main()