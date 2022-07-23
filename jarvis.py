import urllib.request
import pyautogui as pt
from time import sleep
import pyperclip
import re
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

# it will be used for giving voice output
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)
def speak(str):
    engine.say(str)
    engine.runAndWait()





#  It will be used for sending email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kartikrajput77041@gmail.com', 'btryntxulycewews')
    server.sendmail('kartikrajput77041@gmail.com', to, content)
    server.close()




# it will be used for wishing 
def WishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("good morning")
    elif hour >= 12 and hour < 18:
        speak("good Afternoon")
    else:
        speak("Good Evening")
    speak("I am rama sir. Please tell me how may I help you ?")




#it will take voice input
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        speak("listening")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query)
    except Exception as e:
        print(e)
        print("say that again please...")
        return "None"
    return query


# main function for all queries
if __name__ == "__main__":
    WishMe() #it will be used for wishing
    a = True

    # while loop for continuous running of loop which will allows for different and continuous queries
    while (a == True):
        query = takeCommand().lower()
        
        #1 it will serach in wikipedia
        if 'wikipedia' in query: 
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            speak(results)
         
        #2 it will make new folder
        elif 'make new folder' in query:
            path = "C:\\Users\\Hp\\Desktop\\rama_project_make_new folder"
            os.chdir(path)
            speak('what should be the name of folder?')
            P = takeCommand()
            os.makedirs(P)
            speak("folder created")
        
        #3 it will speak time when we ask for it 
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
        #4 it will be used for sending emails
        elif 'email' in query:
            try:
                speak("what should I say?")
                content = takeCommand()
                to = "sangeetadevi77041@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry my friend. I am not able to send this email")
        
        #5 it will paly music 
        elif 'play' in query:
            search_keyword = ''
            v = query.split()
            if 'rama' in query:
                v.remove("rama")
            if len(v) >= 2:
                for i in range(len(v)-1):
                    search_keyword = search_keyword + "+" + v[i + 1]
            print(search_keyword[1:])
            html = urllib.request.urlopen(
                "https://www.youtube.com/results?search_query=" + search_keyword)
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            webbrowser.open("https://www.youtube.com/watch?v=" + video_ids[0])
            sleep(15)
        
        #6 it will allow us to chat using voice commands
        elif 'open whatsapp' in query.lower():
            def get_message():
                    global x, y
                    position = pt.locateOnScreen("whatsapp/smile_clip.jpg", confidence=.6)
                    x = position[0]
                    y = position[1]
                    pt.moveTo(x, y, duration=.05)
                    pt.moveTo(x + 85, y-50, duration=.5)
                    pt.tripleClick()
                    pt.rightClick()
                    pt.moveRel(17, -170)
                    pt.click() 
                    whatsapp_message = pyperclip.paste()
                    print("message reveived and it is " + whatsapp_message)
                    speak(whatsapp_message)
            def post_response(message):
                global x, y
                position__ = pt.locateOnScreen("whatsapp/smile_clip.jpg", confidence = .6)
                pt.moveTo(position__[0]+200, position__[1] + 20, duration= .5)
                pt.click()
                pt.typewrite(message, interval= 0.01)
                pt.typewrite("\n", interval= 0.01)
            def check_for_new_messages(query_):
                global x1,y1
                j = True               
                while (j):
                    #continuously check for green dot and new messages
                    if query_[0] != "message":
                        position2 = pt.locateOnScreen("whatsapp/green_dot.jpg", confidence = .8)
                        if position2 is not None:
                            pt.moveTo(position2)
                            pt.moveRel(-100,0)
                            pt.click()
                        else:
                            speak("no new other users with new messages located")
                    position1 = pt.locateOnScreen("whatsapp/smile_clip.jpg", confidence = .6)
                    pt.moveTo(position1)
                    while(j == True):
                        if pt.pixelMatchesColor(776, 924, (255,255,255), tolerance=10):
                            speak("user said")
                            get_message()
                        speak("speak, what you wants to tell")
                        messa_ge = takeCommand()
                        if messa_ge.lower() == "stop":
                            j == False
                        post_response(messa_ge)
                        sleep(7)
            webbrowser.open("https://web.whatsapp.com/")
            sleep(7)
            speak("what you wants to do")
            query_ = takeCommand().split()


            if query_[0] == "message":
                search_name = query_[1]
                pt.moveTo(441,200 , duration= .05)
                sleep(2)
                pt.click()
                pt.typewrite(search_name, interval= 0.01)
                pt.moveTo(382,335, duration= .05)
                sleep(2)
                pt.click()
                v = True
                while(v):
                    check_for_new_messages(query_)
                    qui_t = takeCommand().lower()
                    if qui_t == "stop":
                        v == False
            else:
                check_for_new_messages(query_)
        
        #7 it will be used for quiting the program
        elif 'quit'or 'exit' or 'stop' or 'break' in query:
            a = False