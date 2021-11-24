import Model
import Preprocess
import tensorflow.keras as keras
import tensorflow as tf

def main():
    preprocessor = Preprocess.Preprocessing('./data/learning')

    train_data, train_y = preprocessor.getImage('Train', (224,224))
    val_data, val_y = preprocessor.getImage('Validation', (224,224))
    test_data, test_y = preprocessor.getImage('Test', (224,224))

    vgg16 = Model.VGG16()
    model = vgg16.build()
    model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])

    callbacks = [keras.callbacks.EarlyStopping(monitor='accuracy', mode='max', patience=5),
                 keras.callbacks.ModelCheckpoint(filepath='./data/model/best_model.h5', monitor='accuracy', save_best_only=True)]
    model.fit(train_data, train_y, epochs=50, batch_size=8,
                    validation_data=(val_data, val_y), shuffle=True, callbacks=callbacks)

if __name__ == '__main__':
    main()