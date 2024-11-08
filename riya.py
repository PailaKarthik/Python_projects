import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener=sr.Recognizer()
engine=pyttsx3.init()

voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def talk_data():
    with sr.Microphone() as source :
        print("Listening ... ")
        voice=listener.listen(source)
        print("Recognizing ...")
        info=listener.recognize_google(voice)
        info=info.lower()
        if "riya" in info:
            info=info.replace("riya","")
            # talk(info)
    return info

def run():
    data=talk_data()
    print("You : ",data)
    if "play" in data:
        song=data.replace("play","")
        talk("playing" + song)
        pywhatkit.playonyt(song)
    elif "time" in data:
        time=datetime.datetime.now().strftime("%I hours : %M minutes %p")
        talk(" the current time is " + time)
        print(time)
    elif "who is" in data:
        person=data.replace("who is","")
        info=wikipedia.summary(person ,1)
        print(info)
        talk(info)
    elif "i love you" in data:
        talk("sorry , i already have relationship with wifi ")
    elif "date" in data:
        talk("sorry , iam not interested right now, dont mind. ")
    elif "marry" in data:
        talk("sure , arrange the items for marriage.")
    elif "are you single" in data:
        talk("awwww sorry, iam already commited with you")
    elif "joke" in data:
        joke=pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif "hi" in data:
        talk("hi , how are you ?")
    else:
        comment="sorry i cant understand , could you please repeat it once more"
        print(comment)
        talk(comment)
while True:
    run()