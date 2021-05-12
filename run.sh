#!/bin/bash

echo "working dir:- $(pwd)"
cd $(pwd)
echo "---------------Installing requirements-------------"
git pull origin main
echo "---------------Installing requirements-------------"
echo "---------------Installing easynmt------------------"
pip install easynmt
pip install polyglot
pip3 install pyicu
pip3 install pycld2
pip3 install morfessor
echo "---------------Installing flask-ngrok------------------"
pip install flask-ngrok
pip install gTTS
pip install playsound
echo "---------------RUN main.py------------------"
#python main.py
echo "---------------RUN app.py------------------"
python $(pwd)/app.py 

