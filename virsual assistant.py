import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


def speak(audio):
    engine = pyttsx3.init("sapi5")
    engine.setProperty('rate', 190)
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Female voice
    engine.say(audio)
    engine.runAndWait()


def greetUser():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning! How can I assist you today?")
    elif 12 <= hour < 18:
        speak("Good Afternoon! How can I assist you today?")
    else:
        speak("Good Evening! How can I assist you today?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 0.7
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print("User said: ", query)
            return query.lower()
        except Exception as e:
            print("Error: ", e)
            return "None"


def get_weather(city):
    API_KEY = "d527159adab7593515bed463cfc7e738"
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    try:
        response = requests.get(f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric")
        data = response.json()
        if data["cod"] == 200:
            main = data["main"]
            weather_desc = data["weather"][0]["description"]
            temp = main["temp"]
            humidity = main["humidity"]
            weather_report = f"The temperature in {city} is {temp}°C with {weather_desc}. The humidity level is {humidity}%."
            print(weather_report)
            speak(weather_report)
        else:
            speak("Sorry, I couldn't find the weather information for that city.")
    except Exception as e:
        speak("There was an error while fetching the weather information.")
        print(e)




def Hello():
    speak("Hello sir, I am EVA assistant.")
    

def calculate(self, command):
    try:
        # Remove "calculate" or "what is" from the command to extract the expression
        expression = command.replace("calculate", "").replace("what is", "").strip()
        
        # Evaluate the mathematical expression
        result = eval(expression)
        
        # Speak and display the result
        self.speak(f"The result of {expression} is {result}.")
    except Exception as e:
        self.speak("Sorry, I couldn't calculate that. Please try again.")
        
        

def Take_query():
    greetUser()
    Hello()
    
    while True:
        query = takeCommand()
        
        if "open whatsapp" in query:
            speak("Opening WhatsApp...")
            webbrowser.open("https://web.whatsapp.com")
            
            
        elif "search youtube for" in query:
            query1 = query.replace("search youtube for", "").strip()
            if query1:
                webbrowser.open(f"https://www.youtube.com/results?search_query={query1}")

        elif "search google for" in query:
            query1 = query.replace("search google for", "").strip()
            if query1:
                webbrowser.open(f"https://www.google.com/search?q={query1}")
            
            
            
        elif "what's the time" in query :
            now = datetime.datetime.now()
            current_time = now.strftime("%I:%M %p")
            speak(f"The current time is {current_time}.")
            
        elif "open email" in query:
           speak("Opening your email...")
           webbrowser.open("https://mail.google.com/")

        elif "weather" in query:
            speak("Which city's weather would you like to know?")
            city = takeCommand()
            get_weather(city)
        
            
        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")
            
             
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
            
        elif "who made you" in query or "who created you" in query: 
            speak("I have been created by eva team.")

        elif "bye" in query:
            speak("Goodbye! Have a great day.")
            exit()


if __name__ == '__main__':
    Take_query()
