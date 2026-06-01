import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import pyjokes 

def talk(text):
    engine =pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id) # 0 for male voice, 1 for female
    engine.say(text)
    engine.stop()

def take_command():
    listener=sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice=listener.listen(source)
            command = listener.recognize_google(voice)
            command=command.lower()
            if 'alex' in command:
                command=command.replace('alex', '').strip()
                print(f'Command: {command}')
                return command
    except Exception:
            pass
    return ''
def run_alex():
     command = take_command()
     if not command:
          return
     if 'play' in command:
          song = command.replace('play','').strip()
          talk(f'Playing {song}')
          pywhatkit.playonyt(song)
     elif 'time' in command:
          time=datetime.datetime.now().strftime('%I:%M %p')
          print(f'Current time is {time}')
          talk(f'Current time is {time}')
     elif 'who is' in command:
          person= command.replace('who is', '').strip()
          try:
               info = wikipedia.summary(person, sentences=2)
               print(info)
               talk(info)
          except Exception:
               talk(f'Sorry, I could not find information about {person}')
     elif 'are you single' in command:
          talk('I am in relationship with wifi')
     elif 'joke' in command:
          joke= pyjokes.get_joke()
          print(joke)
          talk(joke)
     elif 'stop' in command or 'exit' in command:
          talk("goodbye")
          exit()
     else:
          talk('please say again')
talk("Hello I am ALex HOW CAN I HELP YOU")
while True:
     run_alex()
     