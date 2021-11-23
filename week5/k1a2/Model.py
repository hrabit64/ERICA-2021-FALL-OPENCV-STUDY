import tensorflow.keras as keras

class VGG16():
    def build(self):
        pre_trained_vgg = keras.applications.VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
        pre_trained_vgg.trainable = False

        model = keras.models.Sequential()
        model.add(pre_trained_vgg)
        model.add(keras.layers.Flatten())
        model.add(keras.layers.Dense(2048, kernel_regularizer=keras.regularizers.l1_l2(l1=0.001,l2=0.001), activation='relu'))
        model.add(keras.layers.Dropout(0.5))
        model.add(keras.layers.Dense(1024, kernel_regularizer=keras.regularizers.l1_l2(l1=0.001,l2=0.001), activation='relu'))
        model.add(keras.layers.Dropout(0.5))
        model.add(keras.layers.Dense(512, kernel_regularizer=keras.regularizers.l1_l2(l1=0.001,l2=0.001), activation='relu'))
        model.add(keras.layers.Dropout(0.5))
        model.add(keras.layers.Dense(1, activation='sigmoid'))

        return model