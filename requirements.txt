#!/bin/bash
echo "---------------Installing requirements-------------"
git pull origin venkat-new-branch
echo "---------------Installing requirements-------------"
echo "---------------Installing easynmt------------------"
pip install easynmt
echo "---------------Installing flask-ngrok------------------"
pip install flask-ngrok
echo "---------------RUN main.py------------------"
python /content/colab1/main.py
echo "---------------RUN app.py------------------"
python /content/colab1/app.py >> /dev/null &

