from flask import Flask, request, redirect, render_template
import json
from flask_ngrok import run_with_ngrok
import main
import detect_language

app = Flask(__name__)
run_with_ngrok(app)
# app.config["SECRET_KEY"] = str(urandom(24));

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/translate', methods = ['POST',"GET"])
def translate():
  ta_src_lang = request.form.get('ta_src_lang')
  src_lang = request.form.get('src_lang')
  if src_lang=="detect":
    detect = detect_language.detect_languages(ta_src_lang)
    src_lang = detect[0]['language']
  print(src_lang)
  dest_lang = request.form.get('dest_lang')
  trans_text = main.translate(src_lang,dest_lang, ta_src_lang)
  response=json.dumps({"src_lang":src_lang,"dest_lang":dest_lang,"ta_src_lang":ta_src_lang})
  print(response)
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
