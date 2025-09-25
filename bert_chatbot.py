import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pk

# Initialize recognizer and text-to-speech engine
listening = sr.Recognizer()
engine = pt.init()

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def hear():
    """Listen to microphone and return recognized command"""
    cmd = ""  # initialize with default
    try:
        with sr.Microphone() as mic:
            print("Listening...")
            voice = listening.listen(mic)
            cmd = listening.recognize_google(voice)
            cmd = cmd.lower()
            if 'kodi' in cmd:
                cmd = cmd.replace('kodi', '').strip()
                print("Heard command:", cmd)
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition.")
    except Exception as e:
        print("Error:", e)

    return cmd

def run():
    """Main loop to process commands"""
    cmd = hear()
    if not cmd:  # empty string means no command recognized
        return
    
    print("Command:", cmd)

    if 'play' in cmd:
        song = cmd.replace('play', '').strip()
        speak('Playing ' + song)
        pk.playonyt(song)

# Run the assistant
run()