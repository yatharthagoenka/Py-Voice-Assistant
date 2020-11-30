import pyaudio
import speech_recognition as sr
from playsound import playsound
from gtts import gTTS
from time import ctime
import wikipedia
import webbrowser
import calendar
from PyDictionary import PyDictionary
from splinter import Browser
import smtplib


r=sr.Recognizer()
r.energy_threshold=4000

dict=PyDictionary()

#INTRODUCTION TO SANE

print("HI, This is SANE! Standard Automated Nuerological Engine. Please enter the password.")
playsound("command.mp3")

with sr.Microphone() as source2:
    audio2=r.listen(source2)
    r.adjust_for_ambient_noise(source2, duration=1)
try:
    voice2=r.recognize_google(audio2)
    print("Speech was: " + voice2)
except LookupError:
    print("speech not understod")

#####ACTIVATED#####
    
if "hello world" in voice2:
    print("SANE Activated. How may I Help You?")
    #pass=gTTS("SANE Activated. How may I Help You?")
    #pass.save("activate.mp3")
    playsound("activate.mp3")

    print("SANE works on the following commands: \n", "1) What is under your hood \n", "2) What time is it \n", "3) Search \n", "4) Show me the calendar \n", "5) Show me your source \n", "6) Open Dictionary \n", "7) Translate \n", "8) News Update \n", "9) Get me my location. \n", "10) Open Google \n", "11) Open facebook \n", "12) Send Mail \n")


#TAKING IN USER COMMAND
    def listen():
        with sr.Microphone() as source:
            print("Enter Command")    
            audio=r.listen(source)
            r.adjust_for_ambient_noise(source, duration=1)
        try:
            voice=r.recognize_google(audio)
            print("Speech was: " + voice)
        except LookupError:
            print("speech not understod")
        return voice

#PERFORMING FUNCTIONS
    def sane(voice):
        if "what is under your Hood" in voice:
            #response1=gTTS("SANE uses an Analog to digital converter to translate the analog waves of the user's voice into digital data that the computer can read. Several python modules have been made to work simultaneously to provide the desired functionality.")
            #response1.save("hood.mp3")
            print("SANE uses an Analog to digital converter to translate the analog waves of the user's voice into digital data that the computer can read. Several python modules have been made to work simultaneously to provide the desired functionality.")
            playsound("hood.mp3")

        if "what time is it" in voice:
            response3=gTTS(ctime())
            response3.save("time.mp3")
            print(ctime())
            playsound("time.mp3")

        if "search" in voice:
            #response2=gTTS("what should i search for")
            #response2.save("wiki.mp3")
            playsound("wiki.mp3")
            with sr.Microphone() as source3:
                audio3=r.listen(source3)
                r.adjust_for_ambient_noise(source3, duration=1)
            try:
                voice3=r.recognize_google(audio3)
                print("Keyword was: " + voice3)
            except LookupError:
                print("speech not understod")
            
            a=voice3
            print(wikipedia.summary(a, sentences=1))
            response5=gTTS(wikipedia.summary(a, sentences=1))
            response5.save("wikians.mp3")
            playsound("wikians.mp3")


        if 'show me the calendar' in voice:
            print("Which year's calender do you want?")
            #response3=gTTS("Which year's calendar do you want?")
            #response3.save("calendar.mp3")
            playsound("calendar.mp3")
            with sr.Microphone() as source4:
                audio4=r.listen(source4)
                r.adjust_for_ambient_noise(source4, duration=1)
            try:
                voice4=r.recognize_google(audio4)
                print("Year was: " + voice4)
            except LookupError:
                print("Speech not understood")
            b=voice4
            print("The calendar of the year", b, "is :")
            print(calendar.calendar(int(b) ,2,1,6))


        if 'show me your source' in voice:
            print("Which year's calender do you want?")
            #response4=gTTS("Here's my source code")
            #response4.save("source.mp3")
            playsound("source.mp3")
            c=open("SANE.py", "r")
            for line in c:
                print(line)

        if 'open dictionary' in voice:
            print("Enter the Word")
            #response5=gTTS("Enter the Word")
            #response5.save("dict.mp3")
            playsound("dict.mp3")
            with sr.Microphone() as source5:
                audio5=r.listen(source5)
                r.adjust_for_ambient_noise(source5, duration=1)
            try:
                voice5=r.recognize_google(audio5)
                print("Word: " + voice5)
            except LookupError:
                print("Speech not understood")
            d=voice5
            mean=str(dict.meaning(d))
            print(mean)
            meaning=gTTS(mean)
            meaning.save("meaning.mp3")
            playsound("meaning.mp3")
            
        if 'translate' in voice:
            print("Enter the Word, you want to translate")
            #response6=gTTS("Enter the Word, you want to translate")
            #response6.save("trans1.mp3")
            playsound("trans1.mp3")
            with sr.Microphone() as source6:
                audio6=r.listen(source6)
                r.adjust_for_ambient_noise(source6, duration=1)
            try:
                voice6=r.recognize_google(audio6)
                print("Word: " + voice6)
            except LookupError:
                print("Speech not understood")
            e=voice6
            #response7=gTTS("Enter the language you want to translate to")
            #response7.save("trans2.mp3")
            playsound("trans2.mp3")
            f=(str(input("Enter the language you want to translate to: ")))
            print(dict.translate(e,f))
            trans=gTTS(dict.translate(e,f))
            trans.save("trans2.mp3")
            playsound("trans2.mp3")

        if "news update" in voice:
            #response8=gTTS("Here is the latest news updates I found on the web")
            #response8.save("news.mp3")
            playsound("news.mp3")
            urL='https://timesofindia.indiatimes.com/india'
            chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(urL)

        if 'get me my location' in voice:
            #response9=gTTS("Please type in the address")
            #response9.save("location.mp3")
            playsound("location.mp3")
            h=str(input("Please type in the address: "))
            browser=Browser('chrome')
            url="https://www.google.com/maps"
            browser.visit(url)
            browser.fill('q', h)
            #browser.find_by_id('btnK').first.click()

        if 'open Google' in voice:
            #response10=gTTS("What should I fill in?")
            #response10.save("google.mp3")
            playsound("google.mp3")
            print("What should I fill in?")
            with sr.Microphone() as source7:
                audio7=r.listen(source7)
                r.adjust_for_ambient_noise(source7, duration=1)
            try:
                voice7=r.recognize_google(audio7)
                print("Keyword was: " + voice7)
            except LookupError:
                print("speech not understod")
            i=voice7
            browser=Browser('chrome')
            url="https://www.google.com"
            browser.visit(url)
            browser.fill('q', i)

        if 'send mail' in voice:
            smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
            smtpObj.starttls()
            smtpObj.login('goenkayathartha2002@gmail.com','dpsgv@12345')
            recepient=str(input("Please enter the recepient Email ID: "))
            #response11=gTTS("What do you want to say in your mail")
            #response11.save("mail.mp3")
            print("What do you want to say in your mail")
            playsound("mail.mp3")
            with sr.Microphone() as source10:
                audio10=r.listen(source10)
                r.adjust_for_ambient_noise(source10, duration=1)
            try:
                voice10=r.recognize_google(audio10)
                print("Keyword was: " + voice10)
            except LookupError:
                print("speech not understod")
            text=str(voice10)

            smtpObj.sendmail("goenkayathartha2002@gmail.com",recepient,text)
            smtpObj.quit()
            print("Mail Sent Successfully. Check your inbox!")


        if 'open facebook' in voice:
            browser=Browser('chrome')
            url="https://www.facebook.com"
            browser.visit(url)
        
            

    while True:
        sane(listen())


else:
    print("Incorrect password. Terminating program.")
    #pass2=gTTS("Incorrect password. Terminating program")
    #pass2.save("invalid.mp3")
    playsound("invalid.mp3")




