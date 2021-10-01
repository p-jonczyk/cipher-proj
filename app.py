from flask import Flask, render_template, request, flash
import b_coder
import s_coder

app = Flask(__name__)
# should be secret but it's just for learning purpose
app.secret_key = "password123"


@app.route("/")
def index():
    flash("")
    return render_template("binary.html")


@app.route("/shift")
def shift_index():
    flash("")
    return render_template("shift.html")


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


@app.route("/binary", methods=["POST", "GET"])
def binary():
    if request.form['submit_button'] == "ENCODE":
        flash(b_coder.binary_encoder(str(request.form['msg_input'])))
        return render_template("binary.html")
    elif request.form['submit_button'] == "DECODE":
        flash(b_coder.binary_decoder(str(request.form['msg_input'])))
        return render_template("binary.html")
