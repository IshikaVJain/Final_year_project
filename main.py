import subprocess
import pyttsx3
import datetime
import speech_recognition as sr

script1="objectdetection.py"
script2="VoiceAsst.py"


engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("Welcome to Jyothi , an disabled assistant system, which application you want 1 Object detection 2 Voice assistant, Let me know you choice : ")
engine.runAndWait()


r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening....")
    r.pause_threshold = 1
    audio = r.listen(source)

try:
    print("Recognising.....")
    query = r.recognize_google(audio, language='en-in')
    print(f"User said: {query}\n")

    if "object" in query:
        subprocess.run(['python',script1],bufsize=4096)

    if "voice" in query:
         subprocess.run(['python',script2],bufsize=4096)

except Exception as e:
    print(e)
    print("Say that again please.....")



