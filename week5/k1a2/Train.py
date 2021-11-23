import Model
import Preprocess

def main():
    preprocessor = Preprocess.Preprocessing('./data/learning')
    train_data, train_y = preprocessor.getImage('Train', (224,224))
    test_data, test_y = preprocessor.getImage('Test', (224,224))
    val_data, val_y = preprocessor.getImage('Validation', (224,224))

    vgg16 = Model.VGG16()
    model = vgg16.build()
    model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])

    model.fit(train_data, train_y, nb_epoch=50, batch_size=32, validation_data=(val_data, val_y), shuffle=True)

if __name__ == '__main__':
    main()