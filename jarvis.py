import speech_recognition as sr
from googletrans import Translator

#step: 1 ----> listening

def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... ")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing... ")
        query=r.recognize_google(audio,language="en-US")
    except:
        return "Not Understand"
    query = str(query).lower()
    return query
    
# step:2 -----> translation

def translateHinToEng(Text):
    line= str(Text)
    translate=Translator()
    result=translate.translate(line) # default translation is english
    data=result.text
    print(f"You : {data}")
    return data

def connect1():
    query=listen()
    data=translateHinToEng(query)
    print(data)
    return data

connect1()


