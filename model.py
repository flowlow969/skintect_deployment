#model.py
import numpy as np
from PIL import Image
import tensorflow as tf

# Typenden definieren
CATEGORIES = ["Melanozytäre Nävi","Melanom","Gutartige keratoseähnliche Läsion","Basalzellkarzinom","Aktinische Keratose","Vaskuläre Läsionen","Dermatofibrom"]
# Gefährlichkeit den Typen zuordnen
lesion_danger = [0, 1, 0, 1, 1,  0, 0]

# Vortrainertes Model laden
model = tf.keras.models.load_model("256x3_128x3_64x3-CNN.model")


def prepare(filepath):
    """Diese Funktion bereitet die Daten für die Analyse vor."""
    IMG_SIZE = 100  # Bildgröße festlegen
    new_array = np.asarray(Image.open(filepath).resize((IMG_SIZE,IMG_SIZE)))  # Bild laden und auf die zuvor definierte Größe runterrechnen
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 3) #Bild im passenden Format zurückgeben

def predict(filename):
    """Diese Funktion ermittelt die klassifizierung des Bildes und gibt diese zurück"""
    prediction = model.predict([prepare('static/uploads/'+ filename)]) # klassifizierung vornemen
    print(prediction)  # klassifizierung ausgeben
    return CATEGORIES[int(prediction[0][0])], lesion_danger[int(prediction[0][0])] # lesions typ und gefärlickeit zurückgeben
