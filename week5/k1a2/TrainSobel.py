import Preprocess
import Model
import tensorflow.keras as keras

def main():
    preprocessor = Preprocess.Preprocessing('./data/learning')

    train_data_sobel, train_y_sobel = preprocessor.getSobelImage('Train', (224,224))
    val_data_sobel, val_y_sobel = preprocessor.getSobelImage('Validation', (224,224))

    vgg16 = Model.VGG16()
    model_sobel = vgg16.build()
    model_sobel.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])

    print(model_sobel.summary())

    callbacks = [keras.callbacks.EarlyStopping(monitor='accuracy', mode='max', patience=5),
                 keras.callbacks.ModelCheckpoint(filepath='./data/model/best_model_sobel.h5', monitor='accuracy', save_best_only=True)]
    model_sobel.fit(train_data_sobel, train_y_sobel, epochs=50, batch_size=8,
                    validation_data=(val_data_sobel, val_y_sobel), shuffle=True, callbacks=callbacks)

if __name__ == '__main__':
    main()