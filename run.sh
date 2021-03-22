#!/bin/bash
echo "---------------Installing requirements-------------"
git pull origin main
echo "---------------Installing requirements-------------"
echo "---------------Installing easynmt------------------"
pip install easynmt
echo "---------------Installing flask-ngrok------------------"
pip install flask-ngrok
echo "---------------RUN main.py------------------"
cd /content/colab1/
python main.py
echo "---------------RUN app.py------------------"
python app.py >> /dev/null &

