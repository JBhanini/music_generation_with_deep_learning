from keras.layers import *
from keras.models import *
import keras.backend as K
from cnn_preprocessing import unique_x,unique_y,network_input,network_output,validation_data
from keras.utils import np_utils
from keras.callbacks import ModelCheckpoint


def create_cnn_model():
    K.clear_session()
    model = Sequential()

    # embedding layer
    model.add(Embedding(len(unique_x), 100, input_length=32, trainable=True))

    model.add(Conv1D(64, 3, padding='causal', activation='relu'))
    model.add(Dropout(0.2))
    model.add(MaxPool1D(2))

    model.add(Conv1D(128, 3, activation='relu', dilation_rate=2, padding='causal'))
    model.add(Dropout(0.2))
    model.add(MaxPool1D(2))

    model.add(Conv1D(256, 3, activation='relu', dilation_rate=4, padding='causal'))
    model.add(Dropout(0.2))
    model.add(MaxPool1D(2))

    # model.add(Conv1D(256,5,activation='relu'))
    model.add(GlobalMaxPool1D())

    model.add(Dense(256, activation='relu'))
    model.add(Dense(len(unique_y), activation='softmax'))

    model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')

    return model


def train(model):
    """ train the neural network """
    filepath = "cnn-weights-improvement-{epoch:02d}-{loss:.4f}-bigger.hdf5"
    checkpoint = ModelCheckpoint(
        filepath,
        monitor='val_loss',
        verbose=1,
        save_best_only=True,
        mode='min'
    )
    callbacks_list = [checkpoint]
    model.fit(network_input, network_output, epochs=50, batch_size=128, validation_data=validation_data, callbacks=callbacks_list)