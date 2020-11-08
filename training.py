import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.regularizers import l1, l2
from tensorflow.keras.datasets import mnist
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
from PIL import Image
import matplotlib.pyplot as plt

gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
    except RuntimeError as e:
        print(e)


batch_size = 32



class MLModel:
    def __init__(self):
        self.inputs = keras.Input(shape=(28, 28, 1))
        self.x = self.conv_module(self.inputs, f=32, ks=(3, 3), s=(1, 1), p="same", a="relu", kr=l2(0.001), br=l2(0.001), do=0.3, mp=True)
        self.x = self.conv_module(self.inputs, f=64, ks=(3, 3), s=(1, 1), p="same", a="relu", kr=l2(0.001), br=l2(0.001), do=0.3, mp=True)
        self.x = self.flatten_module(self.x)
        self.x = self.dense_module(self.x, u=10, a="softmax", kr=l2(0.001), br=l2(0.001))

        self.outputs = self.x 

    def conv_module(self, x, f, ks, s, p, a, kr, br, do=None, mp=False):
        x = Conv2D(filters=f, kernel_size=ks, strides=s, padding=p, activation=a, kernel_regularizer=kr, bias_regularizer=br)(x)
        if mp:
            x = MaxPooling2D(pool_size=(2, 2))(x)
        if do != None:
            x = Dropout(do)(x)
        return x
    def flatten_module(self, x):
        x = Flatten()(x)
        x = Dense(100, activation="relu", kernel_regularizer=l2(0.001), bias_regularizer=l2(0.001))(x)
        return x
    def dense_module(self, x, u, a, kr, br, do=None):
        x = Dense(units=u, activation=a, kernel_regularizer=kr, bias_regularizer=br)(x)
        return x

    def define_model(self):
        self.model = keras.Model(inputs=self.inputs, outputs=self.outputs, name="mnist_model")
    def compile_model(self, optimizer, loss, metrics):
        self.model.compile(optimizer=optimizer, loss=loss, metrics=metrics)

def train():
    mlmodel = MLModel()
    mlmodel.define_model()
    mlmodel.compile_model(optimizer=Adam(lr=0.00008), loss="categorical_crossentropy", metrics=['accuracy'])

    (trainX, trainY), (testX, testY) = mnist.load_data()
    trainX = trainX.reshape((trainX.shape[0], 28, 28, 1)).astype("float32")
    testX = testX.reshape((testX.shape[0], 28, 28, 1)).astype("float32")
    trainX /= 255
    testX /= 255

    trainY = to_categorical(trainY)
    testY = to_categorical(testY)

    mlmodel.model.fit(x=trainX, y=trainY, batch_size=None, epochs=30, verbose=1, use_multiprocessing=True)
    mlmodel.model.save("NumRoll.h5")

if __name__ == "__main__":
    train()
