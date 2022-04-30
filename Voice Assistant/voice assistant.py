import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyautogui
import wikipedia
import pyjokes

# Initialize the recognizer
r = sr.Recognizer()

program = pyttsx3.init()
def talk(text):
    program.say(text)

    program.runAndWait()
talk("I am Jarvis")
talk("What you want")

while (1):
    try:

        with sr.Microphone() as source2:

            print("Listening...")
            r.adjust_for_ambient_noise(source2)

            audio2 = r.listen(source2)

            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            print(MyText)

        if 'search' in MyText:
            pywhatkit.search(MyText)
        if 'screenshot' in MyText:
            pywhatkit.take_screenshot(MyText)
        if 'whatsapp' in MyText:
            pywhatkit.open_web()
        if 'youtube' in MyText:
            pywhatkit.playonyt(MyText)
        if 'time' in MyText:
            time = datetime.datetime.now().strftime('%H:%M:%S')
            talk(time)
            print(time)
        if 'volume up' in MyText:
            pyautogui.press("volumeup")
        if 'volume down' in MyText:
            pyautogui.press("volumedown")
        if 'mute' in MyText:
            pyautogui.press("mute")
        if 'who is' in MyText:
            person = MyText.replace('Who is', '')
            info = wikipedia.summary(person, 1)
            talk(info)
            print(info)
        if 'joke' in MyText:
            joke=pyjokes.get_joke()
            talk(joke)
            print(joke)

        if 'stop' in MyText:
            exit()




    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")