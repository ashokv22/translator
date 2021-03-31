from flask import Flask, request, redirect, render_template
from flask_ngrok import run_with_ngrok
import main
# from os import urandom
# import functions
import detect_language

app = Flask(__name__)
run_with_ngrok(app)
# app.config["SECRET_KEY"] = str(urandom(24));

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/translate', methods = ['POST'])
def translate():
  ta_src_lang = request.form.get('ta_src_lang')
  src_lang = request.form.get('src_lang')
  if src_lang=="detect":
    src_lang = detect_language.detect_lang(src_lang)
  dest_lang = request.form.get('dest_lang')
  trans_text = main.translate(src_lang,dest_lang, ta_src_lang)
  return trans_text

# @app.route('/change_lang', methods = ['POST'])
# def change_lang():
#   ta_src_lang = request.form.get('ta_src_lang')
#   src_lang = request.form.get('src_lang')
#   dest_lang = request.form.get('dest_lang')
#   trans_text = demo(src_lang,dest_lang, ta_src_lang)
#   return trans_text

if __name__ == '__main__':
	app.run()
