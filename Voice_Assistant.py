import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser
import os
import pyaudio



engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voices[0].id)


def wishme():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    if hour>=12 and hour<18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir") 
    speak("I am Voice Assistant, How may I help you")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 500 
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"You Said {query}\n")
    except Exception as e:
        print("Say it again...")
        return "None"
    return query
        



if __name__=="__main__" :
    wishme()

    while 1:
        query=takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia...')
            print(result)
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open gmail' in query:
            webbrowser.open('mail.google.com')
        elif 'open chatgpt' in query:
            webbrowser.open('chatgpt.com')
        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strtime}")
        elif 'open code' in query:
            codepath="C:\\Users\\Aditya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath) 
        elif 'open facebook' in query:
            webbrowser.open('facebook.com')
        
        elif 'thank' in query:
            speak("Thank You")
            break    
               


