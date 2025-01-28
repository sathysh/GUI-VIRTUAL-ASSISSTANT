import pyjokes
import pywhatkit
import speech_recognition as sr
import pyttsx3
import time
import pyaudio
from time import ctime
import playsound
import respond
import os
import random
import wikipedia
from gtts import gTTS
from tkinter import *
from PIL import ImageTk, Image


r = sr.Recognizer()
speaker = pyttsx3.init()
rate = speaker.getProperty('rate')
speaker.setProperty('rate', 160)
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)


def record_audio(ask=False):
    # user voice record
    with sr.Microphone() as source:
        if ask:
            lee_voice(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print('Recognized voice :' + voice_data)
        except Exception:
            print('Oops something went Wrong')
        # lee_voice('Oops something went Wrong')
        return voice_data

def lee_voice(text):
    speaker.say(text)
    print(text)
    speaker.runAndWait()

"""def lee_voice(audio_string):
    # Play audio text to voice
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)"""


class Widget:
    def __init__(self):
        root = Tk()
        root.title('Kate')
        root.geometry('700x499')
        img = ImageTk.PhotoImage(Image.open('Voice ASSISTANT KATE(1).jpg'))
        panel = Label(root, image=img)
        panel.pack(side='right', fill='both', expand='no')
        compText = StringVar()
        userText = StringVar()
        userText.set('Your Virtual Assistant')
        userFrame = LabelFrame(root, text='Kate', font=('Railways', 24, 'bold'))
        userFrame.pack(fill='both', expand='yes')
        top = Message(userFrame, textvariable=userText, bg='black', fg='white')
        top.config(font=("Century Gothic", 15, 'bold'))
        top.pack(side='top', fill='both', expand='yes')
        btn = Button(root, text='Speak', font=('railways', 10, 'bold'), bg='red', fg='white',command=self.clicked).pack(fill='x', expand='no')
        btn2 = Button(root, text='Close', font=('railways', 10, 'bold'), bg='yellow', fg='black',command=root.destroy).pack(fill='x', expand='no')
        lee_voice('How can i help you?')
        root.mainloop()

    def clicked(self):
        # BUTTON CALLING
        print("Listening....")
        voice_data = record_audio()
        voice_data = voice_data.lower()

        if 'what is the time' in voice_data:
            lee_voice("Sir the time is :" + ctime())

        if 'hey kate' in voice_data:
            lee_voice("i am here to help you!")

        if 'play' in voice_data:
            song = voice_data.replace('play', '')
            lee_voice('playing' + song)
            pywhatkit.playonyt(song)

        if 'what is your name' in voice_data:
            lee_voice("i am kate,How can i help you?")

        if 'who is' in voice_data:
            z = lee_voice().replace("who is", '')
            person = wikipedia.summary(z, 1)
            lee_voice(person)

        if 'who are you' in voice_data:
            lee_voice("i am Kate, i am your Assistant")

        if 'joke' in voice_data:
            x = pyjokes.get_joke()
            lee_voice(x)

        if 'what is mean by' in voice_data:
            a = voice_data.replace("what is mean by", '')
            word = wikipedia.summary(a, 1)
            lee_voice(word)

        if 'search' in voice_data:
            w = voice_data.replace("search",'')
            wo = wikipedia.summary(w, 1)
            lee_voice(wo)

        if 'who programmed you' and 'who invented you' in voice_data:
            lee_voice('I was created by Girijesh')


        if 'exit' in voice_data:
            lee_voice('Thanks have a good day ')
            exit()


if __name__ == '__main__':
    widget = Widget()
time.sleep(1)
while 1:
    voice_data = record_audio()
    respond(voice_data)

speaker.runAndWait()
