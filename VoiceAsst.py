import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pyaudio
import os
import requests
import requests
from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk
import pyjokes
import pyautogui

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

engine = pyttsx3.init('sapi5')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def screenshot():
    pic = pyautogui.screenshot()
    pic.save(r'C:\Users\user\OneDrive\Pictures\Screenshots\example.jpg')

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 6:
        speak("Hey Owl")
    elif 6 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Hello sir")

    speak("I'm your assistant")
    speak("Please tell me how may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please.....")
        return "None"
    return query


def joke():
    speak(pyjokes.get_jokes(language='en', category='all'))

def emergency_message( msg ):
    TOKEN = '7046690791:AAE2s8z8qpbLniQlYX-snEz8FcZkNJfJEGE'
    CHAT_ID='1719117292'

    # message='hello how are you'
    url=f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}"
    r=requests.get(url)
    print(r.json())



def launch_application(application_name):
    if "word" in application_name:
        speak("launching")
        os.system("start winword")
    elif "powerpoint" in application_name:
        os.system("start powerpnt")
    elif "calculator" in application_name:
        os.system("start calc")
    elif "paint" in application_name:
        os.system("start mspaint")
    elif "notepad" in application_name:
        os.system("start notepad")
    else:
        speak("Sorry, I couldn't understand which application to launch.")

def main():
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            speak(results)
            print(results)
 

        elif 'start youtube' in query:
            webbrowser.open("youtube.com")


        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

    
        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")


        elif 'emergency' in query:
            speak('Tell the message to be sent')
            query = takeCommand().lower()
            emergency_message(query)
            speak('Message sent to telegram')


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H,%M,%S")
            speak(f"Sir, the time is {strTime}")

        elif "the date" in query:
            strDate = datetime.datetime.now().strftime("%Y-%m-%d")
            speak(f"Sir, the date is {strDate}")


        elif 'shutdown' in query:
            print("Shutting down...")
            speak("Shutting down")
            quit()


        elif 'joke' in query:
            joke()

        elif 'screenshot' in query:
            screenshot()

        elif 'launch' in query:
            launch_application(query)

if __name__ == "__main__":
    main()
