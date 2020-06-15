import pyttsx3l
import datetime 
import speech_recognition as sr
import wikipedia 
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning sir!")
    elif hour>=12 and hour<=16:
        speak("Good Afternoon sir!")
    else:
        speak("Good evening sir!")
    speak("My name is Tina. how may i help you ?")

def takeCommand():
  

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)    
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":  
 #speak("Arindom is the best")
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()
    
         
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening youtube")
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Opening google")
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")  
            speak("Opening gmail")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com") 
            speak("Opening facebook")    
        elif 'play music' in query: 
            music_dir = 'C:\\Users\\Arindom\\Desktop\\Music'
            songs = os.listdir(music_dir)
            speak("opening mp3 songs")
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'play video songs' in query:
            video_dir = 'C:\\Users\\Arindom\\Desktop\\Videos\\songs'
            videosongs = os.listdir(video_dir)
            speak("opening video songs") 
            print(videosongs)    
            os.startfile(os.path.join(video_dir, videosongs[0]))
        
        elif 'open code' in query:
            codePath = "C:\\Users\\Arindom\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("visual studio codes") 
            os.startfile(codePath)

        elif 'open education' in query:
            aPath = "C:\\Academic Contents"
            speak("opening education contents") 
            os.startfile(aPath)

        elif 'tell me about yourself' in query:
            speak("I am Tina, a powerful AI virtual intelligenge created by arindom sharma as a project for national institute of electronics and information technology during winter internship tow thousand twenty")
         
        
        elif "exit" in query or "bye-bye" in query or "sleep" in query:
            speak("I am shutting down, Good bye sir")
            break
