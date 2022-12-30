from tkinter import E
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import playsound

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morining!")
    elif hour == 12:
        speak("It is Noon")
    elif hour>12 and hour<16:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!") 
    
    
    speak("I am Groovy. Please tell me how I may help you Sir.")

def takeCommand():
    #it takes microphone input from the user and returns string output
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 #seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print("User said: ",query)
        
    except Exception as e:
        #print(e) 
        speak("Say that again please....")
        return "None"
    return query

#def sendEmail(to, content):
 #   server = smtplib.SMTP()
    
        
if __name__ == "__main__":
      wishMe() 
      while True:
          query = takeCommand().lower()
          
          #logic for executing tasks based on query
          if 'wikipedia' in query:
              speak('Searching Wikipedia....')  
              query = query.replace("wikipedia", "")
              results = wikipedia.summary(query, sentences=2)
              speak("According to Wikipedia")
              print(results)
              speak(results)
          
          elif 'can you cook' in query:
              speak("ofcourse not sir i just asked out of courtsey")
              
          elif 'sita mahalakshmi' in query:
              speak('sir.. she is the most beautiful girl you have ever seen or talked to, but unfortunately no such women exist..')
          
          elif 'not hungry' in query:
              speak('is evrything all right sir..')
          
          elif 'fine' in query:
              speak('are you taking your medicine on time sir...')
          
          elif 'yes' in query:
              speak('you are a professional liar sir...')
          
          elif 'none of your business' in query:
              speak('then what is my business you dumb')
              
          elif 'open youtube' in query:
              webbrowser.open("https://www.youtube.com/")
          
          elif 'open google' in query:
              webbrowser.open("https://www.linkedin.com/in/ishan-pandey-081290227/")
          
          elif 'open stackoverflow' in query:
              webbrowser.open("https://stackoverflow.com/")
          
          elif 'my name' in query:
              speak('your name is ishan sir')
                
          elif 'say hi' in query:
              speak('hello everyone namaste i am groovy ishan sir assistant')
              
          elif 'man' in query:
              speak('maa pranam')
            
          elif "why don't you talk in public" in query:
              speak('because i am an introvert just like you sir')
          
          elif 'do not talk to me like that' in query:
              speak('or what, i am your assistant not your servant sir...')
                  
              
          elif 'play music' in query:
              playsound(os.open("https://open.spotify.com/playlist/37i9dQZF1EIUutZ8JokfM0?si=7b9433ba230f4460"))
              
          
          elif 'stop' in query:
              speak("if i will not speak how will you communicate sir. isn't how conversations works")    
              
          elif 'the time' in query:
              strtime = datetime.datetime.now().strftime("%H:%H:%S")
              speak(f"Sir, the time is {strtime}")

              
          elif 'open code' in query:
              codepath = "C:\\Users\\ishan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
              os.startfile(codepath)