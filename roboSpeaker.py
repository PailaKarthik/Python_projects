import pyttsx3
laptop=pyttsx3.init()
print("welccome to the Zuki 1.1 version Created by Karthik")
while True:
        Word=input('enter the sentence you want to pronounce : ')
        if Word == 'q':
                laptop.say('Bye,Bye, My Dear friend ')
                laptop.runAndWait()
                break
        laptop.say(Word)
        laptop.runAndWait()
        

