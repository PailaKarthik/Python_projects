import requests
import json
import pyttsx3

# Getting Requests from Weather API
city=input("enter the city name For Weather : ")
url=f"http://api.weatherapi.com/v1/current.json?key=b6136a26bc8141c390f103431232905&q={city}&aqi=no"

result=requests.get(url)
# print(result.text)

# Making The information into dictonary 
wres=json.loads(result.text)
celsOFcity=wres['current']['temp_c']
print(f"The Current Weather of {city} is {celsOFcity} degrees ")

# Speaking Out By system
laptop=pyttsx3.init()
voices=laptop.getProperty("voices")
laptop.setProperty("voice",voices[1].id)
laptop.say(f" the current weather of {city} is, {celsOFcity} degrees ")
laptop.runAndWait()

