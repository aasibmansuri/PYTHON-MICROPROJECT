import pyttsx3
import pyaudio
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def speak(audio):
    """Function to convert text to speech"""
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    """Function to greet the user based on the current time"""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    elif hour >= 18 and hour < 23:
        speak("Good Evening!")
    else:
        speak("Good Night!")
    speak("I am FRIDAY Boss. Please tell me how can I help you")
        

def takeCommand():
    """Function to take voice input from the user and return it as a string"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry Boss,I can't understand please tell me again")
        speak("Sorry Boss,I can't understand please tell me again")
        return "None"
    except sr.RequestError:
        print("Sorry Boss, Network erorr. Please connect to the network")
        speak("Sorry Boss, Network error, Please connect to the network")
        return "None"
    return query

def sendEmail(to, content):
    """Function to send an email"""
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        # Use environment variables or configuration file for credentials
        server.login(os.environ['EMAIL_USER'], os.environ['EMAIL_PASS'])
        server.sendmail(os.environ['EMAIL_USER'], to, content)
        server.close()
        speak("Email has been sent!")
    except Exception as e:
        print(e)
        speak("Sorry boss. I am not able to send this email")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'google' in query:
            webbrowser.open("google.com")

        elif 'stackoverflow' in query:
            webbrowser.open("stack overflow.com")


        elif 'what is time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'code' in query:
            codePath = "C:\\Users\\Aasib\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)

        elif 'spotify' and 'play music' in query:
            spotifyPath = "C:\\Users\Aasib\OneDrive\Desktop\Spotify - Shortcut.lnk"
            os.startfile(spotifyPath)    

        elif 'email to aasib' and 'email to asif ' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "rojddinali..com@gmail.com"
                sendEmail(to, content)
            except Exception as e:
                print(e)

        elif 'stop program ' in query :
            exit(0)
