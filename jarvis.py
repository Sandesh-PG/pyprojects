import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good morning!")

    elif hour >=12 and hour<=15:
        speak("Good afternoon!")

    else:
        speak("Good evening!")

    speak("hello sandy I am jarvis what can i do for you")
   

def takecommand():#it takes input from the user and returns string as output
   r = sr.Recognizer()
   with sr.Microphone() as source:
    print("Listening...")
    r.pause_threshold = 1
    audio = r.listen(source)

    try:
       print("Recognising...")
       query = r.recognize_google(audio, language ="en-in")
       print(f"User said: {query}\n")

    except Exception as e:
       # print(e)

        print("Say that again please...")
        return "none"
    return query

if __name__ =="__main__":
    wishme()
    #while True:
    if 1:
       query = takecommand().lower()

       if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

       elif 'open youtube' in query:
         webbrowser.open("youtube.com")

       elif 'open google' in query:
             webbrowser.open("google.com")

       elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")       
        speak(f"The time is {strTime}")

       elif 'open chess' in query:
            webbrowser.open("chess.com")


       elif 'open python' in query:
            codepath = "C:\\Users\\MITHUN\\AppData\\Local\\Programs\\Python\\Python310"
            os.startfile(codepath)

       elif 'open vs code' in query:
        codePath = "C:\\Users\\MITHUN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

       