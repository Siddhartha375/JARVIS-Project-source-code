import pyttsx3
from bs4 import BeautifulSoup
import requests
import speech_recognition 
import datetime
import os
import pyautogui
import webbrowser
from plyer import notification
from pygame import mixer
import random
import speedtest
import time
from requests import get

for i in range(3):
    a = input("Enter Password to open Jarvis :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-hi')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query
def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can me call anytime")
                    break
                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}") 
                elif "schedule my day" in query:
                    tasks = [] #Empty list 
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()   
                #elif "open" in query:   #EASY METHOD
                    #query = query.replace("open","")
                    #query = query.replace("jarvis","")
                    #pyautogui.press("super")
                    #pyautogui.typewrite(query)
                    #pyautogui.sleep(2)
                    #pyautogui.press("enter")
                elif 'Who are you' in query or 'what can you do' in query:
                    speak('I am your personal assistant. I am Programmed to minor tasks like opening youtube,google chrome,gmail and stackvoerflow,predict time , take a screenshot,search wikipedia,predict weather in different cities ,get top headline news from times of india and you can ask me computational or geographical questions too!')
                    print('I am your personal assistant. I am Programmed to minor tasks like opening youtube,google chrome,gmail and stackvoerflow,predict time , take a screenshot,search wikipedia,predict weather in different cities ,get top headline news from times of india and you can ask me computational or geographical questions too!')
                elif 'who made you' in query or 'who created you'in query:
                    speak('I was created by siddhartha kumar and souvik kumar sir.')
                    print('I was created by siddhartha kumar and souvik kumar sir.')

                elif "open gmail" in query:
                    webbrowser.open_new_tab("gmail.com")
                    speak("Opening gmail sir..")
                    time.sleep(5)    
                elif "where i am" in query:
                    speak("wait sir, let me check")
                    try:
                        ipAdd= requests.get('https://api.ipify.org').text
                        print(ipAdd)
                        url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json' 
                        geo_requests= requests.get(url) 
                        geo_data= geo_requests.json()
                        #state= geo_data['state']
                        city= geo_data['city']
                        country= geo_data['country']
                        speak(f"Sir i am not sure , but i think we are  in {city} city of {country} country")
                    except Exception as e:
                        speak("sorry sir, due to network issue i am not able to find where we are.")
                        pass
                elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")      
                         
                elif "ipl score" in query:
                    from plyer import notification  #pip install plyer
                    import requests #pip install requests
                    from bs4 import BeautifulSoup #pip install bs4
                    url = "https://www.cricbuzz.com/"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text,"html.parser")
                    team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                    team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                    team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
                    team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()

                    a = print(f"{team1} : {team1_score}")
                    b = print(f"{team2} : {team2_score}")

                    notification.notify(
                        title = "IPL SCORE :- ",
                        message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                        timeout = 15
                    )    
                elif "screenshot" in query:
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")

                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")

                elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("jarvis","")
                    query = query.replace("translate","")
                    translategl(query)

                elif "play a game" in query:
                    from game import game_play
                    game_play() 

                elif "show my schedule" in query:
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.mp3")
                    mixer.music.play()
                    notification.notify(
                        title = "My schedule :-",
                        message = content,
                        timeout = 15
                        )           
                elif "hi" in query or 'hello' in query:
                    speak("Hello sir, how are you ?")
                    print("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                    print("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                    print("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
                    print("you are welcome, sir")

                elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    music_dir='E:\\Non Critical\\songs\\Favorite Songs2'
                    songs=os.listdir(music_dir)
                    rd=random.choice(songs)
                    os.startfile(os.path.join(music_dir,rd))
                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()
                elif "ip address" in query:
                    ip=get('https://api.ipify.org').text
                    print(f"your ip address is {ip}")
                    speak(f"your ip address is {ip}")    
                
                elif "whatsapp" in query:
                    from whatsapp import sendMessage
                    sendMessage()
                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")
                    elif shutdown == "no":
                        break
                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)
                           
                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()    

                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)    
                elif "temperature" in query:
                    search = "temperature in midnapore"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                    print(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "temperature in midnapore"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")  
                    print(f"current{search} is {temp}")  
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")
                    print(f"Sir, the time is {strTime}")
                elif "finally sleep" in query:
                    speak("Going to sleep,sir")
                    print("Going to sleep,sir")
                    exit()
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me to "+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to " + remember.read())
                    print("You told me to " + remember.read())