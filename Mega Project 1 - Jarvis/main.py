import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

# This object listens to the microphone and converts speech into text.
recognizer = sr.Recognizer()

# This object speaks the text back to us using the computer's voice.
engine = pyttsx3.init()


def speak(text):
    # Convert text into speech and play it.
    engine.say(text)
    engine.runAndWait()


def processCommand(command):
    # Make everything lowercase so we can check commands without worrying about uppercase/lowercase.
    lower_command = command.lower()

    # Example: if the user says "open google" then open Google in the browser.
    if "open google" in lower_command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    # Example: if the user says "open youtube" then open YouTube.
    elif "open youtube" in lower_command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    # Example: if the user says "open linkedin" then open LinkedIn.
    elif "open linkedin" in lower_command:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")

    # If the command starts with "play", we try to play a song from the music library.
    elif lower_command.startswith("play"):
        # Split the command into words and take the second word as the song name.
        song = lower_command.split(" ")[1]

        # Look up the song in the music library.
        link = musicLibrary.music[song]

        # Open that link in the browser.
        webbrowser.open(link)

    # If the user says "news", open Google News.
    elif "news" in lower_command:
        speak("Opening News")
        webbrowser.open("https://news.google.com")


if __name__ == "__main__":
    # This block runs only when we execute this file directly.
    speak("initializing Jarvis........")

    # The program keeps listening forever.
    while True:
        # We create a recognizer object each time just for learning simplicity.
        r = sr.Recognizer()

        # Try to listen from the microphone.
        with sr.Microphone() as source:
            print("recognizing speech...")

            try:
                # Listen for audio from the microphone.
                # timeout=2 means wait for 2 seconds before giving up.
                # phrase_time_limit=1 means a phrase may last at most 1 second.
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = r.listen(source, timeout=2, phrase_time_limit=1)

                # Convert the spoken audio to text using Google Speech Recognition.
                word = r.recognize_google(audio)

                # If the user says "jarvis", respond with "Ya".
                if "jarvis" in word.lower():
                    speak("Ya")

                    # After the wake word, listen for the actual command.
                    with sr.Microphone() as source:
                        print("Jarvis Active...")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)

                        # Send the actual command to our command processor.
                        processCommand(command)

            except Exception as e:
                # If speech recognition fails, print the error.
                print("Google phook gaya {0}".format(e))