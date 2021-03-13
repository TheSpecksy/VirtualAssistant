import pyttsx3
import os
import speech_recognition as sr
import datetime
import pyaudio
import webbrowser
import wikipedia
import pywhatkit as kit  #module to search something in youtube and google

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):           #this function makes the assistant speak
    engine.say(audio)
    engine.runAndWait()

def wishme():           #this function will greet you according to the actual time 
    hour = int(datetime.datetime.now().hour)
    if(hour>=6 and hour<12):
        speak("Good Morning")
    elif(hour>=12 and hour<17):
        speak("Good Afternoon")
    elif(hour>=17 and hour<24):
        speak("Good Evening")
    speak("I am chotu, Your V.A.")

def resp():         #this is the funtion that will only be called when you call the Assistant by its name
    r = sr.Recognizer()
    my_mic = sr.Microphone() 
    with my_mic as source:
        r.adjust_for_ambient_noise(source,duration=0.5)
        r.pause_threshold = 1
        non_speaking_duration = 3600
        aud = r.listen(source)
        assistantCalled = r.recognize_google(aud, language = 'en-IN')
        if 'chotu' in assistantCalled:
            print("...")
            speak("Yes? How can i help You")
            jawab=takeComm().lower()
            return jawab
        elif '' in assistantCalled:
            return ''

def takeComm():                 #to take the command and return it to a string
     
    r = sr.Recognizer()
    my_mic = sr.Microphone() 
    with my_mic as source:
        r.adjust_for_ambient_noise(source,duration=0.5)
        print("...")
        r.pause_threshold = 0.6
        aud = r.listen(source)
        print("kettu")
    try:
        print("Recognizing...")    
        query =r.recognize_google(aud, language = 'en-IN')
        print(f"U said: {query}")
    except Exception as e: 
            speak("The voice wasn't clear.Pardon please")  
            return ""
     
    return query

if __name__ == '__main__':          #main function
    wishme()

    while True:
        query = resp()
        print(query)
        
        if "wikipedia" in query:            #to fetch data from wiki
            speak("searching on wikipedia")
            query = query.replace("wikipedia",'')
            results = wikipedia.summary(query,sentences=2)
            speak("according to Wikipedia")
            print(results)
            speak(results)

        
        elif 'search on google' in query:       #to search on google
            query = query.replace('search on google','')
            kit.search(query)

        elif 'the time' in query:       #to tell the current time
            currenttime = str(datetime.datetime.now().strftime("%H:%M:%S"))
            speak("The current time right now is")
            print(currenttime)
            speak(currenttime)

        elif 'steam' in query:      #to open steam library
            speak('opening steam library')
            path = "D:\\Steam\\Steam.exe"
            os.startfile(path)

        elif 'discord' in query:        #to open discord
            speak("opening discord")
            path2 = "C:\\Users\\thesp\AppData\Local\\Discord\\Update.exe --processStart Discord.exe"
            os.startfile(path2)
        elif 'youtube' in query:        #to search on youtube
            query = query.replace("search on youtube",'')
            speak("playing")
            speak(query)
            kit.playonyt(query)
        
        else:
            continue        #infinite loop

        

        