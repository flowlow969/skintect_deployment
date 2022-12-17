#app.py
from flask import Flask, flash, request, redirect, url_for, render_template, app
import urllib.request
import os
from werkzeug.utils import secure_filename
from model import predict

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 2048 * 2048

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part', category="error")
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading', category="basic")
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        detection,i = predict(filename)
        #print('upload_image filename: ' + filename)
        if i == 1:
            flash('Diese Hautveränderung ist wahrscheinlich  ein ' + detection + " und wahrscheinlich maligne.", category="error")
        else:
            flash('Diese Hausveränderung ist wahrscheinlich  ein ' + detection + " und wahrscheinlich beligine.", category="success")
        return render_template('home.html', filename=filename)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif', category="error")
        return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

@app.route('/wir')
def wir():
    return render_template("wir.html")

@app.route('/HL')
def hl():
    return render_template("HL.html")

if __name__ == "__main__":
    app.run( host='0.0.0.0')
