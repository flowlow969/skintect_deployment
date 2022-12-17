import numpy as np
from PIL import Image
import tensorflow as tf

CATEGORIES = ["Melanozytäre Nävi","Melanom","Gutartige keratoseähnliche Läsion","Basalzellkarzinom","Aktinische Keratose","Vaskuläre Läsionen","Dermatofibrom"]
size = 100

lesion_danger = [0, 1, 0, 1, 1,  0, 0]

model = tf.keras.models.load_model("256x3_128x3_64x3-CNN.model")


def prepare(filepath):
    IMG_SIZE = 100  # 50 in txt-based
    new_array = np.asarray(Image.open(filepath).resize((size,size)))  # resize image to match model's expected sizing
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 3)

def predict(filename):
    prediction = model.predict([prepare('static/uploads/'+ filename)])
    print(prediction)  # will be a list in a list.
    return CATEGORIES[int(prediction[0][0])], lesion_danger[int(prediction[0][0])]
