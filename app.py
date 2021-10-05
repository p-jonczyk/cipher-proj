from PIL.Image import EXTENSION
from flask import Flask, render_template, request, flash, redirect, url_for
import time
import os
import shutil
from flask.app import _make_timedelta
from werkzeug.utils import secure_filename
import s_coder
import b_coder
import i_coder
import const
import glob

app = Flask(__name__)
# should be secret but it's just for learning purpose
app.secret_key = const.SECRET_KEY
app.config['UPLOAD_FOLDER'] = 'static/uploads'


@app.route("/")
def index():
    flash("")
    return render_template("binary.html")


@app.route("/shift")
def shift_index():
    flash("")
    return render_template("shift.html")


@app.route('/image_encoder')
def encode_img():
    return render_template('/image_encoder.html')


@app.route('/image_encoder_img')
def encode_img_img():
    return render_template('/image_encoder_img.html')


@app.route('/image_encoder_save')
def encode_img_save():
    return render_template('/image_encoder_save.html')


@app.route('/image_decoder')
def decode_img():
    return render_template('/image_decoder.html')


@app.route('/image_decoder_img')
def decode_img_img():
    return render_template('/image_decoder_img.html')
#####################################################################

# SHIFT CODER


@app.route("/shift", methods=["POST", "GET"])
def shift():
    try:
        shift_order = int(request.form['shift_order'])
        if shift_order not in range(1, 11):
            shift_order = 3
    except ValueError:
        print("Shift order was incorrect. Default order 3 was set")
        shift_order = 3

    if request.form['submit_button'] == "ENCODE":
        flash(s_coder.s_encoder(
            str(request.form['msg_input']), shift_order))
        return render_template("shift.html")
    elif request.form['submit_button'] == "DECODE":
        flash(s_coder.s_decoder(
            str(request.form['msg_input']), shift_order))
        return render_template("shift.html")

##########################################################################

# BINARY CODER


@app.route("/binary", methods=["POST", "GET"])
def binary():
    if request.form['submit_button'] == "ENCODE":
        flash(b_coder.binary_encoder(str(request.form['msg_input'])))
        return render_template("binary.html")
    elif request.form['submit_button'] == "DECODE":
        flash(b_coder.binary_decoder(str(request.form['msg_input'])))
        return render_template("binary.html")

##########################################################################

# IMAGE ENCODER -  STEGANOGRAPHY


@app.route('/image_encoder', methods=['POST', 'GET'])
def upload_image():
    # clean after previous encoding
    i_coder.clean_uploads()

    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    elif file and i_coder.allowed_file(file.filename, 'encoder'):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template('image_encoder_img.html', filename=filename)
    else:
        flash('Allowed image types are: .png, .jpg, .jpeg')
        return redirect(request.url)


@app.route('/image_encoder_save', methods=['POST', 'GET'])
def image_encode():
    if request.form['submit_button'] == "ENCODE":
        filearr = os.listdir('./static/uploads/')
        filename, _ = os.path.splitext(filearr[0])
        filepath = f'./static/uploads/{filearr[0]}'
        new_filename = f"{filename}_encoded.png"
        i_coder.i_encoder(filepath, str(request.form['msg_input']))
        os.remove(filepath)
        flash("")
        return render_template("image_encoder_save.html", filename=new_filename)


# IMAGE DECODER

@app.route('/image_decoder', methods=['POST', 'GET'])
def upload_image_decoder():
    # clean after previous decoding
    i_coder.clean_uploads()

    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    elif file and i_coder.allowed_file(file.filename, 'decoder'):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template('image_decoder_img.html', filename=filename)
    else:
        flash('Allowed image type is: .png')
        return redirect(request.url)


@app.route('/image_decoder_img', methods=['POST', 'GET'])
def image_decode():
    if request.form['submit_button'] == "DECODE":
        filearr = os.listdir('./static/uploads/')
        filepath = f'./static/uploads/{filearr[0]}'
        msg = i_coder.i_decoder(filepath)
        os.remove(filepath)
        flash(msg)
        return render_template("image_decoder_img.html")

# IMAGE DISPLAY


@app.route('/display/<filename>', methods=['POST', 'GET'])
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)
