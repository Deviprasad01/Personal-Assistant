import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
newvoicerate = 150
engine.setProperty('rate',newvoicerate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("wecome back sir! nairobi on your service")
    hour = datetime.datetime.now().hour

    if hour>=6 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    elif hour>=18 and hour<=24:
        speak("good evening")
    else:
        speak("good night")

def name():
    speak("My name is Nairobi the assistant")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #speak("taking your command...")
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google (audio, language="en-in")
        print(query)
    except Exception as e:
        print(e)
        speak("say that again please...")
        return"none"

    return query

def screenshot():
    img=pyautogui.screenshot()
    img.save('D://Users//Pictures//Screenshots//ss.png')

def cpu():
    usage = str(psutil.cpu_percent())
    speak("cpu is a"+ usage)
    battery= psutil.sensors_battery
    speak("battery is at")
    speak("battery.percent")

def jokes():
    speak(pyjokes.get_joke())

def introduce():
    speak("I have lot to do for you sir, you can ask me for time, day and what not")

def crazy1():
    speak("oh! you have a great taste sir! i love me too...")



if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        print(query)
        
        if "time" in query:
            time()
        elif "date" in query:
            date()

        elif "name" in query:
            name()

        elif "offline" in query:
            speak("Going offline")
            quit()
        elif "wikipedia" in query:
            speak("searching...")
            query = query.replace("wikipedia" , "")
            result = wikipedia.summary(query,sentences=2)
            speak(result)
        elif "search" in query:
            speak("what should i search?")
            search = takecommand().lower()
            chromepath = 'C://Program Files//Google//Chrome//Application//chrome.exe %s'
            wb.get(chromepath).open_new_tab(search+".com")

        elif "logout" in query:
            speak("loging out")
            os.system("shutdown-1")
        elif "shutdown" in query:
            speak("shutting down")
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            speak("loging out")
            os.system("shutdown /r /t 1")
        
        elif "play song" in query:
            songs_dir ="D://Nairobi//MUSIC"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))

        elif "you should remember" in query:
            speak("what should i remember?")
            data = takecommand()
            speak=("you said me to remember that"+ data)
            remember= open("data.txt","w")
            remember.write(data)
            remember.close()

        elif "do you remember" in query:
            remember=open("data.txt","r")
            speak("you had said me to remember that"+ remember.read())

        elif "screenshot" in query:
            screenshot()
            speak("done!")

        elif "cpu" in query:
            cpu()

        elif "joke" in query:
            jokes()

        elif "can you do" in query:
            introduce()

        elif "i love" in query:
            crazy1()


        