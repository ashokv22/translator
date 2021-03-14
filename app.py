from flask import Flask, request, redirect, render_template, jsonify
from os import urandom
import functions
import detect_language

app = Flask(__name__)
app.debug = True
##app.config["SECRET_KEY"] = str(urandom(24));


@app.route('/')
def index():
	return render_template("index.html")
	

@app.route('/', methods = ["POST"])
def lang():
	res_name = request.form["name"]
	# src_lang = detect_language.detect_lang(res_name)
	trans_text = functions.trans(res_name)
	trg_output = ''.join(trans_text)
	trg_op=trg_output[2:]
	trg_op=trg_output[:-2]

	return render_template("index.html", name = trg_op)

if __name__ == '__main__':
	app.run(debug = True)
