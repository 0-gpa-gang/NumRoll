import numpy as np
import tensorflow as tf
from PIL import Image
from io_file import *
from tensorflow import keras
from tensorflow.keras.models import load_model
from Database import *

class Classify:
    def __init__(self):
        self.model = load_model("NumRoll.h5")
    def classify(self, np_arr):
        prediction = self.model.predict(np.array([np_arr]))
        return np.argmax(prediction)

    def classify_all(self, lst):
        num_list = []
        for i in lst:
            num_list.append(int(self.classify(i)))
        return num_list

class DataSet:
    def __init__(self):
        self.position = read_from_db() # a list of string locations
        self.num_array = [] #a list of numpy arrays

    def get_num_array(self):
        return self.num_array

    def image_to_array(self):
        total_arrays = []
        for i in self.position:
            image = Image.open(i)
            data = np.array(image)
            total_arrays.append(data)
        self.num_array = total_arrays


def test():
    create()
    data = DataSet()
    data.image_to_array()
    print(data.num_array)

    classifier = Classify()
    final = classifier.classify_all(data.num_array)
    output_to_db(final)

if __name__ == "__main__":
    test()