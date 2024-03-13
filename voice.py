
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os 
import random
import smtplib

 

 
#Speech to text 
engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices')  #getting details of current voice

engine.setProperty('voice', voices[1].id)
def speak(audio):
    

  engine.say(audio) 
  engine.runAndWait()



#wish 
def wish():

    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <=12 :
        speak("Good Morning !")
    elif hour >= 12 and hour <15 :
        speak ("Good Afternoon")
    else :
        speak ("good evening")

    
    speak("Sir , how can i help you ?")

#taking instructions take command function

def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        
        audio = r.listen(source)
 
    try:
        print("Recognizing...")  
        query = r.recognize_google(audio)  
        print(f"User said: {query}\n")
        
        
    except Exception as e:
        print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "none"  #None string will be returned
    return query  

# email fuction   smtp lib module
def sendEmail(to,content ):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sriramkaushikjayanti784@gmail.com', 'chooseurpassword@06/09')
    server.sendmail('sriramkaushikjayanti784@gmail.com', to , content)
    server.close


if __name__ == "__main__":
    wish()
    while True:
    
        query = takeCommand().lower() #Converting user query into lower case

#wikipedia       
        if 'wikipedia' in query:   
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            speak(results)
        
        elif 'hello' in query :
           speak("Hello sir , what can i do for you ")
        
#webbrowser module  
        elif 'open youtube' in query :
           webbrowser.get('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" %s').open("youtube.com")
           speak("Opening youtube")
        elif 'open google' in query :
           webbrowser.get('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" %s').open("")
           speak("Opening...")
        elif 'open mail' in query :
            print(query)
            webbrowser.get('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" %s').open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#sent")
        elif 'open' in query :
            query =query.replace("open","")
            print(query)
            webbrowser.get('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" %s').open(query)
            speak(f"Opening {query} ")
        elif 'temperature' in query :
           webbrowser.get('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" %s').open("https://www.google.com/search?q=temperature+in+my+current+location&rlz=1C1GGRV_enIN928IN928&oq=tempe&aqs=chrome.0.69i59j69i57j35i39j69i59j0i131i433i512j0i131i433i457i512j0i402j0i131i433i512l3.3294j1j15&sourceid=chrome&ie=UTF-8")
        elif 'mam' in query :
           query =query.replace("open","")
           print(query)
           webbrowser.get('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" %s').open(query)
           speak(f"Opening {query} ")
            
           
           



#music   os module
        elif 'music' in query :
            music_dir = 'D:\songs python'
            songs = os.listdir(music_dir)
            r = random.randint(0,5) #random
            os.startfile(os.path.join(music_dir,songs[r]))
            speak(f"Sir, playing") 
        
        elif 'next' in query :
            m=r+1
            os.startfile(os.path.join(music_dir,songs[m]))
        

         
#time       
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
       
#os mudule       
        elif 'open code' in query:
            codePath = "C:\\Users\\Sri ram Kaushik\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codePath)
        elif 'open teams' in query:
            codePath = "C:\\Users\\Sri ram Kaushik\\AppData\\Local\\Microsoft\\Teams\\previous\\Teams.exe"
            os.startfile(codePath)
        elif 'open ms word' in query :
            codepath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\winword.exe"
            os.startfile(codepath)
        

# calling mail function
        elif 'send email' in query:
            try:
                speak("what should i say ?")
                content = takeCommand()
                to = "sriramkaushik1729@gmail.com"
                sendEmail(to , content)
                speak("Email has been sent")
            except Exception as e :
                print(e)
                speak("Sorry the email is not sent")

        elif 'stop' in query : 
            print("exited")
            speak ("bye sir")
            exit()
        elif 'bye' in query : 
            print("exited")
            speak ("bye sir , meet you again, have a nice day")
            exit()

        elif 'great' in query :
            speak("thank you sir")
            
        




        


