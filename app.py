from flask import Flask, request, redirect, render_template
import json
from flask_ngrok import run_with_ngrok
# import main
# import detect_language
import speech

app = Flask(__name__)
run_with_ngrok(app)
# app.config["SECRET_KEY"] = str(urandom(24));

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/translate', methods = ['POST',"GET"])
def translate():
  form_data=request.get_json(force = True)
  ta_src_lang   = form_data['ta_src_lang']
  src_lang      = form_data['src_lang']
  dest_lang     = form_data['dest_lang']
  trans_text = main.translate(src_lang,dest_lang, ta_src_lang)
  response=json.dumps({"src_lang": src_lang,"dest_lang": dest_lang,"ta_src_lang": ta_src_lang,"ta_dest_lang":trans_text})
  return response


@app.route('/speech_to_text', methods = ['POST'])
def speech_to_text():
  form_data     = request.get_json(force = True)
  dest_lang     = form_data['dest_lang']
  ta_dest_lang  = form_data['ta_dest_lang']
  path          = speech.play_text(ta_dest_lang,dest_lang)
  response=json.dumps({"dest_lang": dest_lang,"ta_dest_lang":ta_dest_lang,"path":path})
  return response

if __name__ == '__main__':
	app.run()
