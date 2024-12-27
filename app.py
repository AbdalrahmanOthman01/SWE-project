import pyttsx3  # Text-to-Speech
import speech_recognition as sr  # Speech Recognition
import datetime  # For date and time functions
import webbrowser  # For web searching
import os  # To open applications/files

# Initialize Text-to-Speech engine
engine = pyttsx3.init()


def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()


def wish_user():
    """Greet the user based on time"""
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your assistant, EVA. How can I help you?")


def take_command():
    """Listen for user commands"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            print("Recognizing...")
            command = recognizer.recognize_google(audio, language="en-in")
            print({command})  # Displaying the user's spoken words

            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Could you please repeat?")
            return None
        except sr.RequestError:
            speak("I'm having trouble connecting. Please check your internet.")
            return None


def execute_command(command):
    """Execute basic commands"""
    if "what is time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")
    elif "search" in command:
        search_query = command.replace("search", "").strip()
        if search_query:
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
            speak(f"Searching for {search_query}")
        else:
            speak("What should I search for?")
    elif "open notepad" in command:
        os.system("notepad")
        speak("Opening Notepad.")
    elif "open my whatsapp" in command:
        try:
            webbrowser.open("https://web.whatsapp.com")
            speak("Opening WhatsApp Web.")
        except Exception as e:
            speak("I encountered an issue opening WhatsApp Web. Please try again.")
            print(f"Error: {e}")
    elif "what is your name" in command or "who are you" in command:
        speak("I am EVA, your personal assistant.")
    elif "thanks" in command or "exit" in command:
        speak("Goodbye! Have a great day!")
        exit()
    else:
        speak("I'm sorry, I don't know how to do that yet.")


# Main Program
if __name__ == "__main__":
    wish_user()
    while True:
        user_command = take_command()
        if user_command:
            execute_command(user_command)