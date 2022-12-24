# Functions that speak to the user to help them execute 

# import library
import pyttsx3

# Function to tell user to hold down button when they are recording their voice
def recordVoiceCommand(text):
    print("Program : "+text)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[-1].id)
    engine.say(text)
    engine.runAndWait()

# function to tell user to hold down button and stare at camera to capture images for training
def takePicturesCommand(text):
    print("Program : "+text)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[-1].id)
    engine.say(text)
    engine.runAndWait()
