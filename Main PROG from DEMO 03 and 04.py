import time
import pyjokes
import pywhatkit
import respond as respond
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
from tkinter import *
from PIL import ImageTk,Image

r = sr.Recognizer()
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 160)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    print(text)
    engine.runAndWait()

def t_c():
    try:
        with sr.Microphone() as source:
            r.energy_threshold = 100000
            r.adjust_for_ambient_noise(source, 1.2)
            voice = r.listen(source)
            c = r.recognize_google(voice)
            print("Recognized voice: " + c)
            if 'kate' in c:
                print(c)
    except:
        pass
    return c

class Widget:
    def __init__(self):

        def bquit():
            talk("thank you, i am getting out of here!")
            breakpoint(root.destroy())

        root = Tk()

        root.title('kate')
        root.geometry('700x499')

        img = ImageTk.PhotoImage(Image.open('Voice ASSISTANT KATE(1).jpg'))
        panel = Label(root, image=img)
        panel.pack(side='right', fill='both', expand='no')

        uT = StringVar()
        uT.set('Your Virtual Assistant')
        uF = LabelFrame(root, text='Kate', font=('Railways', 24, 'bold'))
        uF.pack(fill='both', expand='yes')

        top = Message(uF, textvariable=uT, bg='black', fg='white')
        top.config(font=('Century Gothic', 15, 'bold'))
        top.pack(side='top', fill='both', expand='no')

        btn = Button(root, text='Run', font=('railways', 10, 'bold'), bg='red', fg='white', command=self.clicked).pack(fill='x', expand='no')
        btn2 = Button(root, text='Close', font=('railways', 10, 'bold'), bg='blue', fg='white',command=bquit).pack(fill='x', expand='no')
        root.mainloop()


    def clicked(self):

        talk("I am kate, How can i help you?")
        print("Listening....")
        c = t_c()

        if 'hey kate' in c:
            talk("i am here to help you!")

        if 'play' in c:
            song = c.replace('play', '')
            talk('playing' + song)
            pywhatkit.playonyt(song)

        if 'what is your name' in c:
            talk("i am kate,How can i help you?")

        if 'time' in c:
            time = datetime.datetime.now().strftime('%H:%M %p')
            talk('Current time is ' + time)

        if 'who is' in c:
            z = c.replace("who is", '')
            person = wikipedia.summary(z, 1)
            talk(person)

        if 'who are you' in c:
            talk("i am Kate, i am your Assistant")

        if 'joke' in c:
            x = pyjokes.get_joke()
            talk(x)

        if 'what is mean by' in c:
            a = c.replace("what is mean by", '')
            word = wikipedia.summary(a, 1)
            talk(word)

        if 'search' in c:
            w = c.replace("search",'')
            wo = wikipedia.summary(w, 1)
            talk(wo)

        if 'who programmed you' and 'who invented you' in c:
            talk('someone better than you')


if __name__ == '__main__':
    widget = Widget()

time.sleep(1)
while 1:
    c = t_c()
    respond(c)

engine.runAndWait()



