from gtts import gTTS
import os
from playsound import playsound

def play_text(text,language):
    tts = gTTS(text, lang=language)
    tts.save("static/welcome.mp3")
    playsound('static/welcome.mp3')
    return 'static/welcome.mp3'
