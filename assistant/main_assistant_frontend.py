import opening_a_file_backend
from pyttsx3 import *

print("Hi! i am your assistant")

name = input("\nhi what is your name")

print()

m = opening_a_file_backend.Mainfunction()

def heart():

    def again():
        print("")
        heart()

    speaker = input(":)")
    if speaker == 'hi' or speaker  == "Hi"or speaker == 'hello':
       print(f'good morning {name}')
       speak(f'good morning{name}')
       again()

    if speaker  == 'open draw pad' :
       speak("opening draw pad")
       m.game_assistant()
       if m.game_assistant() != exit():
           again()
       again()

    if speaker == 'open vs code':
       speak("opening vs code")
       m.vs_code()
       again()

    if speaker  == 'open chrome' or speaker  == 'open google chrome':
       speak("opening google chrome")
       m.opening_chrome()
       again()

    if speaker  == "open cmd":
       speak("opening cmd")
       m.opening_cmd()
       again()

    if  speaker  == "open calculator":
       speak('opening calculator')
       m.opening_calculator()
       again()

    if speaker  == "cm to m converter":
       speak("cm to m converter activated")
       m.opening_cmtom()
       again()

    if speaker  == "find leap year":
       speak("find leap year activated")
       m.find_leap_year()
       again()

    if speaker == 'open a file':
       speak("opening a file")
       m.opening_file()
       again()

    if speaker  == "open dice":
       speak('dice activated')
       m.diceig()
       again()

    if speaker == "exit" or speaker == "bye" or speaker == "ok bye" :
        print(f"ok bye {name}")
        speak(f"ok bye {name}")
        exit()

    if speaker== "good morning":
        speak(f"good morning {name}")

    if speaker == "good night":
        speak(f'good morning{name}')

    if speaker == "open arduino":
        speak("opening arduino i d e")
        m.arduino()
        # if m.arduino() != exit():
        #     again()
        again()

    if speaker == "what is your name":
        print("my name is assistant")
        speak("my name is assistant")
        heart()

    if speaker == "open note pad":
        print("note pad opened")
        speak("note pad opened")
        m.notpad()
        heart()


    else:
        print("sorry i dint get it:(")
        speak("sorry i dint get it")
        heart()


heart()

# for more information visit (information to add new command.txt)