#importing win32 package
import win32com.client as wincom

#creating voice dispatcher object
speak = wincom.Dispatch("SAPI.SpVoice")
#sending the text we want it to speak
text = "Hello, I am a simple program that converts text to speech"
speak.Speak(text)

while True:
    text = input("Enter the text you want me to speak: ")
    if text == "q":
        speak.Speak("Quitting...")
        break
    speak.Speak(text)