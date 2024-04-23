import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
        
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def process_query(query):
    if "open google" in query:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")
    elif "what time is it" in query:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}.")
    elif "play music" in query:
        music_dir = "C:\\Users\\User\\Music"  # Change this to your music directory
        songs = os.listdir(music_dir)
        if songs:
            os.startfile(os.path.join(music_dir, songs[0]))
        else:
            speak("No music found in your directory.")
    else:
        speak("Sorry, I can't do that yet.")

def main():
    speak("Hello! How can I help you today?")
    while True:
        query = listen()
        if query:
            if "exit" in query:
                speak("Goodbye!")
                break
            process_query(query)

if __name__ == "__main__":
    main()
