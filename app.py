#app.py
from flask import Flask, flash, request, redirect, url_for, render_template, app
import urllib.request
import os
from werkzeug.utils import secure_filename
from model import predict

app = Flask(__name__)   # app initialisieren

UPLOAD_FOLDER = 'static/uploads/'   # Pfad zu uploads definieren

app.secret_key = "secret key"   # Verschlüsselung festlegen (muss bei deployment ausgetauscht werden)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER # Pfad zu uploads zuweisen
app.config['MAX_CONTENT_LENGTH'] = 16 * 2048 * 2048 # max Größe festlegen

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif']) # erlaubte Datentypen festlegen

def allowed_file(filename):
    """Funktion überptüft, ob die Datei in einem erlaubten Datentyp vorliegt"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home():
    """Funktion ruft Hauptseite auf"""
    return render_template('home.html')


@app.route('/', methods=['POST'])
def upload_image():
    """Funktion regelt den upload von Bildern"""
    if 'file' not in request.files: # Datentyp prüfen
        flash('No file part', category="error") # Fehler auf Website ausgeben
        return redirect(request.url)
    file = request.files['file']    #Daten laden
    if file.filename == '': # überprüfen, ob ein Bild vorliegt
        flash('No image selected for uploading', category="basic")   # Fehler auf Website ausgeben
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)   # Dateinamen übertragen
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) # Datei speichern
        detection,i = predict(filename) # Klassifizierung vornehmen
        #print('upload_image filename: ' + filename)
        if i == 1:  # überprüfen ob die Hautveränderung benigne oder maligne ist
            flash('Diese Hautveränderung ist wahrscheinlich  ein ' + detection + " und wahrscheinlich maligne.", category="error") # Art der veränderung ausgeben (maligne=bössartig)
        else:
            flash('Diese Hausveränderung ist wahrscheinlich  ein ' + detection + " und wahrscheinlich beligine.", category="success") # Art der veränderung ausgeben (benigne=Gutartige)
        return render_template('home.html', filename=filename)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif', category="error") # Fehler auf Website ausgeben(falscher Datentyp)
        return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
    """Diese Funktion zeigt das Bild auf der Website an"""
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

@app.route('/wir')
def wir():
    """Funktion ruft Über uns Seite auf"""
    return render_template("wir.html")

@app.route('/HL')
def hl():
    """Funktion ruft die Seite auf, auf der die Hautveränderung erläutert werden"""
    return render_template("HL.html")

if __name__ == "__main__":
    """App laufenlassen auf Localhost"""
    app.run( host='0.0.0.0')
