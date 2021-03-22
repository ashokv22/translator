from flask import Flask, request, redirect, render_template
from flask_ngrok import run_with_ngrok
import main
# from os import urandom
# import functions
# import detect_language

app = Flask(__name__)
run_with_ngrok(app)
# app.config["SECRET_KEY"] = str(urandom(24));

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/translate', methods = ['POST'])
def translate():
  src=request.form["src_lang"]
  trg=request.form["trg_lang"]
  src_text = request.form["name"]
  trans_text = main.translate(src,trg, src_text)
  return render_template("index.html", name = trans_text)

if __name__ == '__main__':
	app.run()
