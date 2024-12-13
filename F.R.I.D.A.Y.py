# Coded by     : Eng.Abdalrahman Hossam Othman
# Project name : F.R.I.D.A.Y-AI
# Starting Date: 2024.8.30
# End Date     : 2024.9.30
import os
import cv2
import sys
import copy
import time
import json
import emoji
import psutil
import serial
import ctypes
import shutil
import string
import qrcode
import random
import PyPDF2
import pygame
import turtle
import math
import sqlite3
from math import *
from pyfiglet import figlet_format
import socket
import pyttsx3
import tkinter
import pyjokes
import smtplib
import winsound
import datetime
import operator
import requests
import platform
import winshell
import termcolor
import threading
import wikipedia
import speedtest
import pywhatkit
import pyautogui
import freegames
import subprocess
import feedparser
import webbrowser
import mediapipe as mp
from math import sqrt
import win32api
from equation import Equation
import wavio as wv
import numpy as np
import instaloader
import wolframalpha
from pygame import mixer
import pygame as pg
from turtle import *
import tkinter as tk
from tkinter import *
import urllib.request
from pygame.locals import *
from enum import Enum
from time import sleep
import face_recognition
import numpy as np
from pynput.mouse import Button, Controller
import wx
import imutils
from PIL import ImageTk
from tkinter import ttk
from PIL import ImageOps
import sounddevice as sd
from requests import get
from collections import *
from datetime import date
import tkinter.messagebox
from random import choice
from tkinter.ttk import *
from pytube import YouTube
from tkinter import _tkinter
from random import randrange
from bs4 import BeautifulSoup
from collections import deque
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox
# from twilio.rest import Client
import speech_recognition as sr
import win32com.client as wincl
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER
from clint.textui import progress
from GoogleNews import GoogleNews
from urllib.request import urlopen
from collections import namedtuple
from scipy.io.wavfile import write
from freegames import floor, vector, line, square
from ecapture import ecapture as ec
from pynput.keyboard import Listener
from vidstream import StreamingServer
from geopy.geocoders import Nominatim
from vidstream import ScreenShareClient
from PIL import Image, ImageFilter, ImageColor, ImageDraw
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
os.chdir(os.path.dirname(os.path.abspath(__file__)))
#############################################################################################################################################################
current_time = datetime.datetime.now()
athours = 0
atminutes = 0
scannow = "/scannow"
assname = "Friday"
rdate = 2022
root_url = "http://192.168.43.211"
info_dir = "./database/INFO.txt"
imagg = "./database/Abdalrahman.jpg"
db = sqlite3.connect("./database/FRIDAY.db")
myCR = db.cursor()
#############################################################################################################################################################
myCR.execute("CREATE TABLE IF NOT EXISTS `users` (name TEXT,age INTEGER,nationality TEXT,phonenumber INTEGER,crushname TEXT, hobbies TEXT,bloodtype TEXT,healthProblems TEXT,weight INTEGER,height INTEGER,bestfriends TEXT,favcolor TEXT,favmeal TEXT,rolemodel TEXT,favactor TEXT,favcar TEXT,city TEXT,footsize TEXT,sports TEXT,favyoutuber TEXT,favsubject TEXT,favscientit TEXT,favsocialapp TEXT,favsesson TEXT,religion TEXT,favsonger TEXT,mood TEXT,favanimal TEXT,favseries TEXT,favcodinglang TEXT,tasks TEXT,notes TEXT,user_id INTEGER,user_type TEXT)")
myCR.execute("CREATE TABLE IF NOT EXISTS `authenticate` (name TEXT,user_id INTEGER)")
class User:
    def __init__(self, name=None, age=None, nationality=None, phonenumber=None, crushname=None, hobbies=None, bloodtype=None, healthProblems=None, weight=None, height=None, bestfriends=None, favcolor=None, favmeal=None, rolemodel=None, favactor=None, favcar=None, city=None, footsize=None, sports=None, favyoutuber=None, favsubject=None, favscientit=None, favsocialapp=None, mood=None, favsonger=None, religion=None, favsesson=None, favanimal=None, favseries=None, favcodinglang=None, tasks=None , user_id=None ,user_type=None):
        self.name = name
        self.age = age
        self.nationality = nationality if nationality is not None else []
        self.phonenumber = phonenumber
        self.crushname = crushname
        self.hobbies = hobbies if hobbies is not None else []
        self.bloodtype = bloodtype
        self.healthProblems = healthProblems if healthProblems is not None else []
        self.weight = weight
        self.height = height
        self.bestfriends = bestfriends if bestfriends is not None else []
        self.favcolor = favcolor
        self.favmeal = favmeal
        self.rolemodel = rolemodel
        self.favactor = favactor
        self.favcar = favcar
        self.city = city
        self.footsize = footsize
        self.sports = sports if sports is not None else []
        self.favyoutuber = favyoutuber
        self.favsubject = favsubject
        self.favscientit = favscientit
        self.favsocialapp = favsocialapp
        self.mood = mood
        self.favsonger = favsonger
        self.religion = religion
        self.favsesson = favsesson
        self.favanimal = favanimal
        self.favseries = favseries
        self.favcodinglang = favcodinglang
        self.tasks = tasks if tasks is not None else []
        self.user_type = user_type
        self.user_id = user_id
    
    def save_to_db(self):
        self.nationality_json = json.dumps(self.nationality)
        self.hobbies_json = json.dumps(self.hobbies)
        self.healthProblems_json = json.dumps(self.healthProblems)
        self.bestfriends_json = json.dumps(self.bestfriends)
        self.sports_json = json.dumps(self.sports)
        self.tasks_json = json.dumps(self.tasks)

        # Fetch the last user_id and increment it
        myCR.execute("SELECT user_id FROM users ORDER BY user_id DESC LIMIT 1")
        result = myCR.fetchone()
        if result is not None:
            self.user_id = result[0] + 1
        else:
            self.user_id = 1  # Start with 1 if no users exist        
        # Insert user into database
        myCR.execute('''
            INSERT INTO users (name, age, nationality, phonenumber, crushname, hobbies, bloodtype, healthProblems, weight, height, bestfriends, favcolor, favmeal, rolemodel, favactor, favcar, city, footsize, sports, favyoutuber, favsubject, favscientit, favsocialapp, mood, favsonger, religion, favsesson, favanimal, favseries, favcodinglang, tasks , user_type ,user_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,?)
        ''', (self.name, self.age, self.nationality_json, self.phonenumber, self.crushname, self.hobbies_json, self.bloodtype, self.healthProblems_json, self.weight, self.height, self.bestfriends_json, self.favcolor, self.favmeal, self.rolemodel, self.favactor, self.favcar, self.city, self.footsize, self.sports_json, self.favyoutuber, self.favsubject, self.favscientit, self.favsocialapp, self.mood, self.favsonger, self.religion, self.favsesson, self.favanimal, self.favseries, self.favcodinglang, self.tasks_json,self.user_type,self.user_id))
        myCR.execute("INSERT INTO authenticate (name,user_id) VALUES (?,?)" ,(self.name,self.user_id))

        # Commit the transaction
        db.commit()   

if ( bool(myCR.fetchone()) == False) :
    AdminUser = User("Abdalrahman Hossam Othman",19,["egyption","suadi arabian"],201029388659,"Esraa Yasser",["Coding","Playing football"],"A+",["No"],70,188,["Basel","Gaber","Hoseny"],"Golden","Lazania","Prophet Mohamed","RDJ","Tesla","Tanta",40,["Swimming","Football"],"Elzero","Coding","Einestien","Whatsapp","Happy","Wegz","Muslim","Summer","Lion","Marvel","Python",[],1,"Admin")
    AdminUser.save_to_db()
    db.commit()
#############################################################################################################################################################
def addalarm():
    speak("please tell me time in hours")
    athours = takeCommand()
    speak("please tell me time in minutes")
    atminutes = takeCommand()


#############################################################################################################################################################
def checkalarm():
    time_ac = datetime.datetime.now()
    timenowhours = time_ac.strftime("%H")
    timenowminutes = time_ac.strftime("%M")
    if athours == timenowhours and atminutes >= timenowminutes:
        speak("time to wakeup sir")
        sos()
        alarmtimehours = 0
        alarmtimeminutes = 0


#############################################################################################################################################################
def bluetooth():
    print("looking for bluetooth devices...........")
    devices = bluetooth.discover_devices(lookup_names=True)
    for addr, name in devices:
        print("addres : " + addr)
        print("name : " + name)
        print("-------------------------------------------------")


#############################################################################################################################################################
def sendRequest(url):
    n = urllib.request.urlopen(url)  # send request to ESP


def manual_control():
    window = tk.Tk()
    # url handling module for python
    img = Image.open(imagg)
    test = ImageTk.PhotoImage(img)
    # image1 = img.resize((2, 3), Image.ANTIALIAS)
    label1 = tkinter.Label(image=test)
    label1.image = test
    label1.place(x=350, y=50)
    window.title("ROBOT CONTROLER FROM OTHMAN INDUSTRIES")

    def a():
        sendRequest(root_url + "/FORWARD")
        print("A")

    def b():
        sendRequest(root_url + "/BACK")
        print("B")

    def c():
        sendRequest(root_url + "/WATCHRIGHT")
        print("C")

    def d():
        sendRequest(root_url + "/LEFT")
        print("D")

    def e():
        sendRequest(root_url + "/RIGHT")
        print("E")

    def f():
        sendRequest(root_url + "/LEDS_ON")
        print("F")

    def g():
        sendRequest(root_url + "/LEDS_OFF")
        print("G")

    def h():
        sendRequest(root_url + "/BUZZ")
        print("H")

    def i():
        sendRequest(root_url + "/WATCHLEFT")
        print("I")

    # code to add widgets

    while True:
        headline = tkinter.Label(
            window, text="ABDALRAHMAN HOSSAM OTHMAN", fg="red", font=("ANUDAW", 25)
        )
        headline.grid(column=1, row=0)
        FORWARD = tkinter.Button(
            window,
            text="FORWARD",
            width=10,
            command=a,
            fg="yellow",
            bg="green",
            font=("Lobster 1.4", 25),
        ).grid(column=0, row=2)
        BACK = tkinter.Button(
            window,
            text=" BACK ",
            width=10,
            command=b,
            fg="yellow",
            bg="green",
            font=("Lobster 1.4", 25),
        ).grid(column=0, row=4)
        LEFT = tkinter.Button(
            window,
            text=" LEFT",
            width=10,
            command=d,
            fg="yellow",
            bg="green",
            font=("Lobster 1.4", 25),
        ).grid(column=0, row=6)
        RIGHT = tkinter.Button(
            window,
            text=" RIGHT ",
            width=10,
            command=e,
            fg="yellow",
            bg="green",
            font=("Lobster 1.4", 25),
        ).grid(column=0, row=8)
        ON = tkinter.Button(
            window,
            text="  ON  ",
            width=10,
            command=f,
            fg="yellow",
            bg="green",
            font=("Lobster 1.4", 25),
        ).grid(column=2, row=2)
        OFF = tkinter.Button(
            window,
            text="  OFF ",
            width=10,
            command=g,
            fg="yellow",
            bg="green",
            font=("Lobster 1.4", 25),
        ).grid(column=2, row=4)
        WATCHLEFT = tkinter.Button(
            window,
            text="WATCHLEFT",
            width=10,
            command=i,
            fg="yellow",
            bg="green",
            font=("Lobster 1.4", 25),
        ).grid(column=2, row=6)
        WATCHRIGHT = tkinter.Button(
            window,
            text="WATCHRIGHT",
            width=10,
            command=c,
            fg="yellow",
            bg="green",
            font=("Lobster 1.4", 25),
        ).grid(column=2, row=8)
        BUZZ = tkinter.Button(
            window,
            text=" BUZZ ",
            width=10,
            command=h,
            fg="yellow",
            bg="green",
            font=("Lobster 1.4", 25),
        ).grid(column=1, row=10)

        window.mainloop()


#############################################################################################################################################################
def chemistry():
    def run_balance():
        """
        Runs the chemical equation balance algorithm
        """
        print("=================================================")
        print(
            "Insert chemical equation with elements in\nparentheses followed by the number of atoms:"
        )
        print("Example: (H)2 + (O)2 = (H)2(O)1")
        user_input = input(">>> ")
        try:
            equation = Equation(user_input)
            print("Balanced equation: " + equation.balance())
            sleep(3)
            run_balance()
        except IndexError:
            print("Invalid input...")
            sleep(3)
            run_balance()

    run_balance()


#############################################################################################################################################################
def youtube_downloader():
    root = Tk()
    root.geometry("500x600")
    root.title("youtube video downloader")
    root.resizable(width=False, height=False)
    Label(root, text="youtube video downloader", font="arial 15 bold").pack(
        padx=5, pady=50
    )
    link = StringVar()
    Label(root, text="Paste your link here: ", font="arial 15 bold").place(x=160, y=100)
    link_entry = Entry(root, width=45, font=30, textvariable=link, bd=5).place(
        x=32, y=190
    )

    def downloader():
        url = YouTube(str(link.get()))
        video = url.streams.first()
        video.download()
        Label(
            root, text="download completed", font="arial 15 bold", fg="white", bg="red"
        ).place(x=100, y=300)
        Label(root, text="check your file", font="arial 15 bold").place(x=10, y=350)

    Button(
        root,
        text="download",
        bg="lightblue",
        font="arial 15 bold",
        padx=2,
        command=downloader,
    ).place(x=170, y=250)
    root.mainloop()


#############################################################################################################################################################
def play_music():
    music_dir = r"C:\Users\ET\Music\Music"
    songs = os.listdir(music_dir)
    for song in songs:
        if song.endswith(".mp3"):
            os.startfile(os.path.join(music_dir, song))
    print(songs)

    def music_start():
        os.startfile(os.path.join(music_dir, songs[random.randint(0, 3)]))

    music_start()


def play_quran():
    music_dir = r"C:\Users\ET\Music\Quran"
    songs = os.listdir(music_dir)
    for song in songs:
        if song.endswith(".mp3"):
            os.startfile(os.path.join(music_dir, song))
    print(songs)

    def music_start():
        os.startfile(os.path.join(music_dir, songs[random.randint(0, 3)]))

    music_start()


#############################################################################################################################################################
def qr_generator():
    qr = qrcode.QRCode(version=1, box_size=15, border=5)
    speak("what is data")
    data = takeCommand()
    speak("what name shall i save it in")
    name = takeCommand()
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save(name + ".png")


#############################################################################################################################################################
def port():
    try:
        speak("trying to connect with my body  ")
        port = serial.Serial("COM18", 9600, timeout=1)
        port.write(b"hi")
        print("connected to my phisical body")
    except:
        print("cannot find my phisical body")


#############################################################################################################################################################
def Quit1():
    sys.exit()


#############################################################################################################################################################
def addTask():
    Task_num = 0
    speak("Which task do you want to add")
    newTask = takeCommand()
    myTasks[Task_num] = newTask
    Task_num = Task_num + 1


def delTask():
    speak("Which task do you want to remove")
    taskNum = int(takeCommand())
    myTasks[taskNum - 1] = ""


#############################################################################################################################################################


def temperature():
    api_key = "b91f73301dbaf02d43ced0a104ceb7f8"
    url = "http://ipinfo.io//json"
    response = urlopen(url)
    data = json.load(response)
    user_input = data["city"]

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}"
    )

    if weather_data.json()["cod"] == "404":
        print("No City Found")
        speak("No City Found")
    else:
        weather = weather_data.json()["weather"][0]["main"]
        temp = round(weather_data.json()["main"]["temp"])

        print(f"The weather in {user_input} is: {weather}")
        print(f"The temperature in {user_input} is: {temp}ºF and {temp - 18}ºC")


#############################################################################################################################################################

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    now = datetime.datetime.now()
    strTime = datetime.datetime.now()

    # Printing attributes of now().
    print("Date : ", end="")
    print(current_time.year, ".", current_time.month, ".", current_time.day)
    print("Time : ", end="")
    print(
        current_time.hour,
        ".",
        current_time.minute,
        ".",
        current_time.second,
        ".",
        current_time.microsecond,
    )

    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir ! it is " + str(now))

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir ! it is " + str(now))

    else:
        speak("Good Evening Sir ! it is " + str(now))

    temperature()

    speak("let me introduce my self i am " + assname + "i am here to assist you ")


#############################################################################################################################################################
def calculations():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("what do you want me to calculate")
        print("Listening....")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    my_string = r.recognize_google(audio)
    print(my_string)

    def get_operator_fn(op):
        return {
            "+": operator.add,
            "-": operator.sub,
            "x": operator.mul,
            "divided": operator.__truediv__,
        }[op]

    def eval_binary_expr(op1, oper, op2):
        op1, op2 = int(op1), int(op2)
        return get_operator_fn(oper)(op1, op2)

    speak("your result is")
    print("your result is" + eval_binary_expr(*(my_string.split())))
    speak(eval_binary_expr(*(my_string.split())))


#############################################################################################################################################################
frequency = 2500
duration = 1000


def sos():
    for i in range(0, 3):
        winsound.Beep(2000, 100)
        for i in range(0, 3):
            winsound.Beep(2000, 400)
            for i in range(0, 3):
                winsound.Beep(2000, 100)


def snake_game():
    food = vector(0, 0)
    snake = [vector(10, 0)]
    aim = vector(0, -10)

    def change(x, y):
        aim.x = x
        aim.y = y

    def inside(head):
        return -200 < head.x < 190 and -200 < head.y < 190

    def move():
        head = snake[-1].copy()
        head.move(aim)

        if not inside(head) or head in snake:
            square(head.x, head.y, 9, "red")
            update()
            return

        snake.append(head)

        if head == food:
            print("Snake:", len(snake))
            food.x = randrange(-15, 15) * 10
            food.y = randrange(-15, 15) * 10
        else:
            snake.pop(0)

        clear()

        for body in snake:
            square(body.x, body.y, 9, "black")

        square(food.x, food.y, 9, "green")
        update()
        ontimer(move, 100)

    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    listen()
    onkey(lambda: change(10, 0), "Right")
    onkey(lambda: change(-10, 0), "Left")
    onkey(lambda: change(0, 10), "Up")
    onkey(lambda: change(0, -10), "Down")
    move()
    done()


def pacman_game():
    state = {"score": 0}
    path = Turtle(visible=False)
    writer = Turtle(visible=False)
    aim = vector(5, 0)
    pacman = vector(-40, -80)
    ghosts = [
        [vector(-180, 160), vector(5, 0)],
        [vector(-180, -160), vector(0, 5)],
        [vector(100, 160), vector(0, -5)],
        [vector(100, -160), vector(-5, 0)],
    ]
    # fmt: off
    tiles = [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
        0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
        0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    ]
    # fmt: on

    def square(x, y):
        """Draw square using path at (x, y)."""
        path.up()
        path.goto(x, y)
        path.down()
        path.begin_fill()

        for count in range(4):
            path.forward(20)
            path.left(90)

        path.end_fill()

    def offset(point):
        """Return offset of point in tiles."""
        x = (floor(point.x, 20) + 200) / 20
        y = (180 - floor(point.y, 20)) / 20
        index = int(x + y * 20)
        return index

    def valid(point):
        """Return True if point is valid in tiles."""
        index = offset(point)

        if tiles[index] == 0:
            return False

        index = offset(point + 19)

        if tiles[index] == 0:
            return False

        return point.x % 20 == 0 or point.y % 20 == 0

    def world():
        """Draw world using path."""
        bgcolor("black")
        path.color("blue")

        for index in range(len(tiles)):
            tile = tiles[index]

            if tile > 0:
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                square(x, y)

                if tile == 1:
                    path.up()
                    path.goto(x + 10, y + 10)
                    path.dot(2, "white")

    def move():
        """Move pacman and all ghosts."""
        writer.undo()
        writer.write(state["score"])

        clear()

        if valid(pacman + aim):
            pacman.move(aim)

        index = offset(pacman)

        if tiles[index] == 1:
            tiles[index] = 2
            state["score"] += 1
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

        up()
        goto(pacman.x + 10, pacman.y + 10)
        dot(20, "yellow")

        for point, course in ghosts:
            if valid(point + course):
                point.move(course)
            else:
                options = [
                    vector(5, 0),
                    vector(-5, 0),
                    vector(0, 5),
                    vector(0, -5),
                ]
                plan = choice(options)
                course.x = plan.x
                course.y = plan.y

            up()
            goto(point.x + 10, point.y + 10)
            dot(20, "red")

        update()

        for point, course in ghosts:
            if abs(pacman - point) < 20:
                return

        ontimer(move, 100)

    def change(x, y):
        """Change pacman aim if valid."""
        if valid(pacman + vector(x, y)):
            aim.x = x
            aim.y = y

    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    writer.goto(160, 160)
    writer.color("white")
    writer.write(state["score"])
    listen()
    onkey(lambda: change(5, 0), "Right")
    onkey(lambda: change(-5, 0), "Left")
    onkey(lambda: change(0, 5), "Up")
    onkey(lambda: change(0, -5), "Down")
    world()
    move()
    done()


def shooter_game():
    mixer.init()
    pygame.init()

    mixer.music.load("./database/shooter/background.wav")
    mixer.music.play(-1)

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("./database/shooter/Space Shooter Game")
    icon = pygame.image.load("./database/shooter/icon.png")
    pygame.display.set_icon(icon)

    background = pygame.image.load("./database/shooter/bg.png")

    spaceshipimg = pygame.image.load("./database/shooter/arcade.png")

    alienimg = []
    alienX = []
    alienY = []
    alienspeedX = []
    alienspeedY = []

    no_of_aliens = 6

    for i in range(no_of_aliens):
        alienimg.append(pygame.image.load("./database/shooter/enemy.png"))
        alienX.append(random.randint(0, 736))
        alienY.append(random.randint(30, 150))
        alienspeedX.append(-1)
        alienspeedY.append(40)

    score = 0

    bulletimg = pygame.image.load("./database/shooter/bullet.png")
    check = False
    bulletX = 386
    bulletY = 490

    spaceshipX = 370
    spaceshipY = 480
    changeX = 0
    running = True

    font = pygame.font.SysFont("Arial", 32, "bold")

    def score_text():
        img = font.render(f"Score:{score}", True, "white")
        screen.blit(img, (10, 10))

    font_gameover = pygame.font.SysFont("Arial", 64, "bold")

    def gameover():
        img_gameover = font_gameover.render("GAME OVER", True, "white")
        screen.blit(img_gameover, (200, 250))

    while running:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    changeX = -5
                if event.key == pygame.K_RIGHT:
                    changeX = 5
                if event.key == pygame.K_SPACE:
                    if check is False:
                        bulletSound = mixer.Sound("./database/shooter/laser.wav")
                        bulletSound.play()
                        check = True
                        bulletX = spaceshipX + 16

            if event.type == pygame.KEYUP:
                changeX = 0
        spaceshipX += changeX  # spaceshipX=spaceshipX-changeX
        if spaceshipX <= 0:
            spaceshipX = 0
        elif spaceshipX >= 736:
            spaceshipX = 736
        for i in range(no_of_aliens):
            if alienY[i] > 420:
                for j in range(no_of_aliens):
                    alienY[j] = 2000
                gameover()
                break
            alienX[i] += alienspeedX[i]
            if alienX[i] <= 0:
                alienspeedX[i] = 1
                alienY[i] += alienspeedY[i]
            if alienX[i] >= 736:
                alienspeedX[i] = -1
                alienY[i] += alienspeedY[i]

            distance = math.sqrt(
                math.pow(bulletX - alienX[i], 2) + math.pow(bulletY - alienY[i], 2)
            )
            if distance < 27:
                explosion = mixer.Sound("./database/shooter/explosion.wav")
                explosion.play()
                bulletY = 480
                check = False
                alienX[i] = random.randint(0, 736)
                alienY[i] = random.randint(30, 150)
                score += 1
            screen.blit(alienimg[i], (alienX[i], alienY[i]))

        if bulletY <= 0:
            bulletY = 490
            check = False
        if check:
            screen.blit(bulletimg, (bulletX, bulletY))
            bulletY -= 5

        screen.blit(spaceshipimg, (spaceshipX, spaceshipY))
        score_text()
        pygame.display.update()


def ballon_game():
    pygame.init()

    width = 500
    height = 500

    display = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Balloon Shooter")
    clock = pygame.time.Clock()

    margin = 100
    lowerBound = 100

    score = 0

    # Colors
    white = (230, 230, 230)
    lightBlue = (174, 214, 241)
    red = (231, 76, 60)
    lightGreen = (25, 111, 61)
    darkGray = (40, 55, 71)
    darkBlue = (21, 67, 96)
    green = (35, 155, 86)
    yellow = (244, 208, 63)
    blue = (46, 134, 193)
    purple = (155, 89, 182)
    orange = (243, 156, 18)

    font = pygame.font.SysFont("Snap ITC", 25)

    # Balloon Class
    class Balloon:
        def __init__(self, speed):
            self.a = random.randint(30, 40)
            self.b = self.a + random.randint(0, 10)
            self.x = random.randrange(margin, width - self.a - margin)
            self.y = height - lowerBound
            self.angle = 90
            self.speed = -speed
            self.probPool = [-1, -1, -1, 0, 0, 0, 0, 1, 1, 1]
            self.length = random.randint(50, 100)
            self.color = random.choice([red, green, purple, orange, yellow, blue])

        # Move balloon around the Screen
        def move(self):
            direct = random.choice(self.probPool)

            if direct == -1:
                self.angle += -10
            elif direct == 0:
                self.angle += 0
            else:
                self.angle += 10

            self.y += self.speed * sin(radians(self.angle))
            self.x += self.speed * cos(radians(self.angle))

            if (self.x + self.a > width) or (self.x < 0):
                if self.y > height / 5:
                    self.x -= self.speed * cos(radians(self.angle))
                else:
                    self.reset()
            if self.y + self.b < 0 or self.y > height + 30:
                self.reset()

        # Show/Draw the balloon
        def show(self):
            pygame.draw.line(
                display,
                darkBlue,
                (self.x + self.a / 2, self.y + self.b),
                (self.x + self.a / 2, self.y + self.b + self.length),
            )
            pygame.draw.ellipse(display, self.color, (self.x, self.y, self.a, self.b))
            pygame.draw.ellipse(
                display,
                self.color,
                (self.x + self.a / 2 - 5, self.y + self.b - 3, 10, 10),
            )

        # Check if Balloon is bursted
        def burst(self):
            global score
            pos = pygame.mouse.get_pos()

            if onBalloon(self.x, self.y, self.a, self.b, pos):
                score += 1
                self.reset()

        # Reset the Balloon
        def reset(self):
            self.a = random.randint(30, 40)
            self.b = self.a + random.randint(0, 10)
            self.x = random.randrange(margin, width - self.a - margin)
            self.y = height - lowerBound
            self.angle = 90
            self.speed -= 0.002
            self.probPool = [-1, -1, -1, 0, 0, 0, 0, 1, 1, 1]
            self.length = random.randint(50, 100)
            self.color = random.choice([red, green, purple, orange, yellow, blue])

    balloons = []
    noBalloon = 10
    for i in range(noBalloon):
        obj = Balloon(random.choice([1, 1, 2, 2, 2, 2, 3, 3, 3, 4]))
        balloons.append(obj)

    def onBalloon(x, y, a, b, pos):
        if (x < pos[0] < x + a) and (y < pos[1] < y + b):
            return True
        else:
            return False

    # show the location of Mouse
    def pointer():
        pos = pygame.mouse.get_pos()
        r = 25
        l = 20
        color = lightGreen
        for i in range(noBalloon):
            if onBalloon(
                balloons[i].x, balloons[i].y, balloons[i].a, balloons[i].b, pos
            ):
                color = red
        pygame.draw.ellipse(display, color, (pos[0] - r / 2, pos[1] - r / 2, r, r), 4)
        pygame.draw.line(
            display, color, (pos[0], pos[1] - l / 2), (pos[0], pos[1] - l), 4
        )
        pygame.draw.line(
            display, color, (pos[0] + l / 2, pos[1]), (pos[0] + l, pos[1]), 4
        )
        pygame.draw.line(
            display, color, (pos[0], pos[1] + l / 2), (pos[0], pos[1] + l), 4
        )
        pygame.draw.line(
            display, color, (pos[0] - l / 2, pos[1]), (pos[0] - l, pos[1]), 4
        )

    def lowerPlatform():
        pygame.draw.rect(display, darkGray, (0, height - lowerBound, width, lowerBound))

    def showScore():
        scoreText = font.render("Balloons Bursted : " + str(score), True, white)
        display.blit(scoreText, (150, height - lowerBound + 50))

    def close():
        pygame.quit()
        sys.exit()

    def game():
        global score
        loop = True

        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    close()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        close()
                    if event.key == pygame.K_r:
                        score = 0
                        game()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(noBalloon):
                        balloons[i].burst()

            display.fill(lightBlue)

            for i in range(noBalloon):
                balloons[i].show()

            pointer()

            for i in range(noBalloon):
                balloons[i].move()

            lowerPlatform()
            showScore()
            pygame.display.update()
            clock.tick(60)

    game()


def tron_game():
    p1xy = vector(-100, 0)
    p1aim = vector(4, 0)
    p1body = set()

    p2xy = vector(100, 0)
    p2aim = vector(-4, 0)
    p2body = set()

    def inside(head):
        """Return True if head inside screen."""
        return -200 < head.x < 200 and -200 < head.y < 200

    def draw():
        """Advance players and draw game."""
        p1xy.move(p1aim)
        p1head = p1xy.copy()

        p2xy.move(p2aim)
        p2head = p2xy.copy()

        if not inside(p1head) or p1head in p2body:
            print("Player blue wins!")
            return

        if not inside(p2head) or p2head in p1body:
            print("Player red wins!")
            return

        p1body.add(p1head)
        p2body.add(p2head)

        square(p1xy.x, p1xy.y, 3, "red")
        square(p2xy.x, p2xy.y, 3, "blue")
        update()
        ontimer(draw, 50)

    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    listen()
    onkey(lambda: p1aim.rotate(90), "a")
    onkey(lambda: p1aim.rotate(-90), "d")
    onkey(lambda: p2aim.rotate(90), "j")
    onkey(lambda: p2aim.rotate(-90), "l")
    draw()
    done()


def maze_game():
    def draw():
        """Draw maze."""
        color("black")
        width(5)

        for x in range(-200, 200, 40):
            for y in range(-200, 200, 40):
                if random() > 0.5:
                    line(x, y, x + 40, y + 40)
                else:
                    line(x, y + 40, x + 40, y)

        update()

    def tap(x, y):
        """Draw line and dot for screen tap."""
        if abs(x) > 198 or abs(y) > 198:
            up()
        else:
            down()

        width(2)
        color("red")
        goto(x, y)
        dot(4)

    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    draw()
    onscreenclick(tap)
    done()


def slide_puzzle():
    # Create the constants (go ahead and experiment with different values)
    BOARDWIDTH = 4  # number of columns in the board
    BOARDHEIGHT = 4  # number of rows in the board
    TILESIZE = 80
    WINDOWWIDTH = 640
    WINDOWHEIGHT = 480
    FPS = 30
    BLANK = None

    #                 R    G    B
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BRIGHTBLUE = (0, 50, 255)
    DARKTURQUOISE = (3, 54, 73)
    GREEN = (0, 204, 0)

    BGCOLOR = DARKTURQUOISE
    TILECOLOR = GREEN
    TEXTCOLOR = WHITE
    BORDERCOLOR = BRIGHTBLUE
    BASICFONTSIZE = 20

    BUTTONCOLOR = WHITE
    BUTTONTEXTCOLOR = BLACK
    MESSAGECOLOR = WHITE

    XMARGIN = int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)
    YMARGIN = int((WINDOWHEIGHT - (TILESIZE * BOARDHEIGHT + (BOARDHEIGHT - 1))) / 2)

    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"

    def main():
        global FPSCLOCK, DISPLAYSURF, BASICFONT, RESET_SURF, RESET_RECT, NEW_SURF, NEW_RECT, SOLVE_SURF, SOLVE_RECT

        pygame.init()
        FPSCLOCK = pygame.time.Clock()
        DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        pygame.display.set_caption("Slide Puzzle")
        BASICFONT = pygame.font.Font("freesansbold.ttf", BASICFONTSIZE)

        # Store the option buttons and their rectangles in OPTIONS.
        RESET_SURF, RESET_RECT = makeText(
            "Reset", TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 90
        )
        NEW_SURF, NEW_RECT = makeText(
            "New Game", TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 60
        )
        SOLVE_SURF, SOLVE_RECT = makeText(
            "Solve", TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 30
        )

        mainBoard, solutionSeq = generateNewPuzzle(80)
        SOLVEDBOARD = (
            getStartingBoard()
        )  # a solved board is the same as the board in a start state.
        allMoves = []  # list of moves made from the solved configuration

        while True:  # main game loop
            slideTo = None  # the direction, if any, a tile should slide
            msg = "Click tile or press arrow keys to slide."  # contains the message to show in the upper left corner.
            if mainBoard == SOLVEDBOARD:
                msg = "Solved!"

            drawBoard(mainBoard, msg)

            checkForQuit()
            for event in pygame.event.get():  # event handling loop
                if event.type == MOUSEBUTTONUP:
                    spotx, spoty = getSpotClicked(mainBoard, event.pos[0], event.pos[1])

                    if (spotx, spoty) == (None, None):
                        # check if the user clicked on an option button
                        if RESET_RECT.collidepoint(event.pos):
                            resetAnimation(
                                mainBoard, allMoves
                            )  # clicked on Reset button
                            allMoves = []
                        elif NEW_RECT.collidepoint(event.pos):
                            mainBoard, solutionSeq = generateNewPuzzle(
                                80
                            )  # clicked on New Game button
                            allMoves = []
                        elif SOLVE_RECT.collidepoint(event.pos):
                            resetAnimation(
                                mainBoard, solutionSeq + allMoves
                            )  # clicked on Solve button
                            allMoves = []
                    else:
                        # check if the clicked tile was next to the blank spot

                        blankx, blanky = getBlankPosition(mainBoard)
                        if spotx == blankx + 1 and spoty == blanky:
                            slideTo = LEFT
                        elif spotx == blankx - 1 and spoty == blanky:
                            slideTo = RIGHT
                        elif spotx == blankx and spoty == blanky + 1:
                            slideTo = UP
                        elif spotx == blankx and spoty == blanky - 1:
                            slideTo = DOWN

                elif event.type == KEYUP:
                    # check if the user pressed a key to slide a tile
                    if event.key in (K_LEFT, K_a) and isValidMove(mainBoard, LEFT):
                        slideTo = LEFT
                    elif event.key in (K_RIGHT, K_d) and isValidMove(mainBoard, RIGHT):
                        slideTo = RIGHT
                    elif event.key in (K_UP, K_w) and isValidMove(mainBoard, UP):
                        slideTo = UP
                    elif event.key in (K_DOWN, K_s) and isValidMove(mainBoard, DOWN):
                        slideTo = DOWN

            if slideTo:
                slideAnimation(
                    mainBoard, slideTo, "Click tile or press arrow keys to slide.", 8
                )  # show slide on screen
                makeMove(mainBoard, slideTo)
                allMoves.append(slideTo)  # record the slide
            pygame.display.update()
            FPSCLOCK.tick(FPS)

    def terminate():
        pygame.quit()
        sys.exit()

    def checkForQuit():
        for event in pygame.event.get(QUIT):  # get all the QUIT events
            terminate()  # terminate if any QUIT events are present
        for event in pygame.event.get(KEYUP):  # get all the KEYUP events
            if event.key == K_ESCAPE:
                terminate()  # terminate if the KEYUP event was for the Esc key
            pygame.event.post(event)  # put the other KEYUP event objects back

    def getStartingBoard():
        # Return a board data structure with tiles in the solved state.
        # For example, if BOARDWIDTH and BOARDHEIGHT are both 3, this function
        # returns [[1, 4, 7], [2, 5, 8], [3, 6, BLANK]]
        counter = 1
        board = []
        for x in range(BOARDWIDTH):
            column = []
            for y in range(BOARDHEIGHT):
                column.append(counter)
                counter += BOARDWIDTH
            board.append(column)
            counter -= BOARDWIDTH * (BOARDHEIGHT - 1) + BOARDWIDTH - 1

        board[BOARDWIDTH - 1][BOARDHEIGHT - 1] = BLANK
        return board

    def getBlankPosition(board):
        # Return the x and y of board coordinates of the blank space.
        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT):
                if board[x][y] == BLANK:
                    return (x, y)

    def makeMove(board, move):
        # This function does not check if the move is valid.
        blankx, blanky = getBlankPosition(board)

        if move == UP:
            board[blankx][blanky], board[blankx][blanky + 1] = (
                board[blankx][blanky + 1],
                board[blankx][blanky],
            )
        elif move == DOWN:
            board[blankx][blanky], board[blankx][blanky - 1] = (
                board[blankx][blanky - 1],
                board[blankx][blanky],
            )
        elif move == LEFT:
            board[blankx][blanky], board[blankx + 1][blanky] = (
                board[blankx + 1][blanky],
                board[blankx][blanky],
            )
        elif move == RIGHT:
            board[blankx][blanky], board[blankx - 1][blanky] = (
                board[blankx - 1][blanky],
                board[blankx][blanky],
            )

    def isValidMove(board, move):
        blankx, blanky = getBlankPosition(board)
        return (
            (move == UP and blanky != len(board[0]) - 1)
            or (move == DOWN and blanky != 0)
            or (move == LEFT and blankx != len(board) - 1)
            or (move == RIGHT and blankx != 0)
        )

    def getRandomMove(board, lastMove=None):
        # start with a full list of all four moves
        validMoves = [UP, DOWN, LEFT, RIGHT]

        # remove moves from the list as they are disqualified
        if lastMove == UP or not isValidMove(board, DOWN):
            validMoves.remove(DOWN)
        if lastMove == DOWN or not isValidMove(board, UP):
            validMoves.remove(UP)
        if lastMove == LEFT or not isValidMove(board, RIGHT):
            validMoves.remove(RIGHT)
        if lastMove == RIGHT or not isValidMove(board, LEFT):
            validMoves.remove(LEFT)

        # return a random move from the list of remaining moves
        return random.choice(validMoves)

    def getLeftTopOfTile(tileX, tileY):
        left = XMARGIN + (tileX * TILESIZE) + (tileX - 1)
        top = YMARGIN + (tileY * TILESIZE) + (tileY - 1)
        return (left, top)

    def getSpotClicked(board, x, y):
        # from the x & y pixel coordinates, get the x & y board coordinates
        for tileX in range(len(board)):
            for tileY in range(len(board[0])):
                left, top = getLeftTopOfTile(tileX, tileY)
                tileRect = pygame.Rect(left, top, TILESIZE, TILESIZE)
                if tileRect.collidepoint(x, y):
                    return (tileX, tileY)
        return (None, None)

    def drawTile(tilex, tiley, number, adjx=0, adjy=0):
        # draw a tile at board coordinates tilex and tiley, optionally a few
        # pixels over (determined by adjx and adjy)
        left, top = getLeftTopOfTile(tilex, tiley)
        pygame.draw.rect(
            DISPLAYSURF, TILECOLOR, (left + adjx, top + adjy, TILESIZE, TILESIZE)
        )
        textSurf = BASICFONT.render(str(number), True, TEXTCOLOR)
        textRect = textSurf.get_rect()
        textRect.center = (
            left + int(TILESIZE / 2) + adjx,
            top + int(TILESIZE / 2) + adjy,
        )
        DISPLAYSURF.blit(textSurf, textRect)

    def makeText(text, color, bgcolor, top, left):
        # create the Surface and Rect objects for some text.
        textSurf = BASICFONT.render(text, True, color, bgcolor)
        textRect = textSurf.get_rect()
        textRect.topleft = (top, left)
        return (textSurf, textRect)

    def drawBoard(board, message):
        DISPLAYSURF.fill(BGCOLOR)
        if message:
            textSurf, textRect = makeText(message, MESSAGECOLOR, BGCOLOR, 5, 5)
            DISPLAYSURF.blit(textSurf, textRect)

        for tilex in range(len(board)):
            for tiley in range(len(board[0])):
                if board[tilex][tiley]:
                    drawTile(tilex, tiley, board[tilex][tiley])

        left, top = getLeftTopOfTile(0, 0)
        width = BOARDWIDTH * TILESIZE
        height = BOARDHEIGHT * TILESIZE
        pygame.draw.rect(
            DISPLAYSURF, BORDERCOLOR, (left - 5, top - 5, width + 11, height + 11), 4
        )

        DISPLAYSURF.blit(RESET_SURF, RESET_RECT)
        DISPLAYSURF.blit(NEW_SURF, NEW_RECT)
        DISPLAYSURF.blit(SOLVE_SURF, SOLVE_RECT)

    def slideAnimation(board, direction, message, animationSpeed):
        # Note: This function does not check if the move is valid.

        blankx, blanky = getBlankPosition(board)
        if direction == UP:
            movex = blankx
            movey = blanky + 1
        elif direction == DOWN:
            movex = blankx
            movey = blanky - 1
        elif direction == LEFT:
            movex = blankx + 1
            movey = blanky
        elif direction == RIGHT:
            movex = blankx - 1
            movey = blanky

        # prepare the base surface
        drawBoard(board, message)
        baseSurf = DISPLAYSURF.copy()
        # draw a blank space over the moving tile on the baseSurf Surface.
        moveLeft, moveTop = getLeftTopOfTile(movex, movey)
        pygame.draw.rect(baseSurf, BGCOLOR, (moveLeft, moveTop, TILESIZE, TILESIZE))

        for i in range(0, TILESIZE, animationSpeed):
            # animate the tile sliding over
            checkForQuit()
            DISPLAYSURF.blit(baseSurf, (0, 0))
            if direction == UP:
                drawTile(movex, movey, board[movex][movey], 0, -i)
            if direction == DOWN:
                drawTile(movex, movey, board[movex][movey], 0, i)
            if direction == LEFT:
                drawTile(movex, movey, board[movex][movey], -i, 0)
            if direction == RIGHT:
                drawTile(movex, movey, board[movex][movey], i, 0)

            pygame.display.update()
            FPSCLOCK.tick(FPS)

    def generateNewPuzzle(numSlides):
        # From a starting configuration, make numSlides number of moves (and
        # animate these moves).
        sequence = []
        board = getStartingBoard()
        drawBoard(board, "")
        pygame.display.update()
        pygame.time.wait(500)  # pause 500 milliseconds for effect
        lastMove = None
        for i in range(numSlides):
            move = getRandomMove(board, lastMove)
            slideAnimation(
                board,
                move,
                "Generating new puzzle...",
                animationSpeed=int(TILESIZE / 3),
            )
            makeMove(board, move)
            sequence.append(move)
            lastMove = move
        return (board, sequence)

    def resetAnimation(board, allMoves):
        # make all of the moves in allMoves in reverse.
        revAllMoves = allMoves[:]  # gets a copy of the list
        revAllMoves.reverse()

        for move in revAllMoves:
            if move == UP:
                oppositeMove = DOWN
            elif move == DOWN:
                oppositeMove = UP
            elif move == RIGHT:
                oppositeMove = LEFT
            elif move == LEFT:
                oppositeMove = RIGHT
            slideAnimation(board, oppositeMove, "", animationSpeed=int(TILESIZE / 2))
            makeMove(board, oppositeMove)

    if __name__ == "__main__":
        main()


def squerill_game():
    FPS = 30  # frames per second to update the screen
    WINWIDTH = 640  # width of the program's window, in pixels
    WINHEIGHT = 480  # height in pixels
    HALF_WINWIDTH = int(WINWIDTH / 2)
    HALF_WINHEIGHT = int(WINHEIGHT / 2)

    GRASSCOLOR = (24, 255, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    CAMERASLACK = (
        90  # how far from the center the squirrel moves before moving the camera
    )
    MOVERATE = 9  # how fast the player moves
    BOUNCERATE = 6  # how fast the player bounces (large is slower)
    BOUNCEHEIGHT = 30  # how high the player bounces
    STARTSIZE = 25  # how big the player starts off
    WINSIZE = 300  # how big the player needs to be to win
    INVULNTIME = 2  # how long the player is invulnerable after being hit in seconds
    GAMEOVERTIME = 4  # how long the "game over" text stays on the screen in seconds
    MAXHEALTH = 3  # how much health the player starts with

    NUMGRASS = 80  # number of grass objects in the active area
    NUMSQUIRRELS = 30  # number of squirrels in the active area
    SQUIRRELMINSPEED = 3  # slowest squirrel speed
    SQUIRRELMAXSPEED = 7  # fastest squirrel speed
    DIRCHANGEFREQ = 2  # % chance of direction change per frame
    LEFT = "left"
    RIGHT = "right"

    """
    This program has three data structures to represent the player, enemy squirrels, and grass background objects. The data structures are dictionaries with the following keys:

    Keys used by all three data structures:
        'x' - the left edge coordinate of the object in the game world (not a pixel coordinate on the screen)
        'y' - the top edge coordinate of the object in the game world (not a pixel coordinate on the screen)
        'rect' - the pygame.Rect object representing where on the screen the object is located.
    Player data structure keys:
        'surface' - the pygame.Surface object that stores the image of the squirrel which will be drawn to the screen.
        'facing' - either set to LEFT or RIGHT, stores which direction the player is facing.
        'size' - the width and height of the player in pixels. (The width & height are always the same.)
        'bounce' - represents at what point in a bounce the player is in. 0 means standing (no bounce), up to BOUNCERATE (the completion of the bounce)
        'health' - an integer showing how many more times the player can be hit by a larger squirrel before dying.
    Enemy Squirrel data structure keys:
        'surface' - the pygame.Surface object that stores the image of the squirrel which will be drawn to the screen.
        'movex' - how many pixels per frame the squirrel moves horizontally. A negative integer is moving to the left, a positive to the right.
        'movey' - how many pixels per frame the squirrel moves vertically. A negative integer is moving up, a positive moving down.
        'width' - the width of the squirrel's image, in pixels
        'height' - the height of the squirrel's image, in pixels
        'bounce' - represents at what point in a bounce the player is in. 0 means standing (no bounce), up to BOUNCERATE (the completion of the bounce)
        'bouncerate' - how quickly the squirrel bounces. A lower number means a quicker bounce.
        'bounceheight' - how high (in pixels) the squirrel bounces
    Grass data structure keys:
        'grassImage' - an integer that refers to the index of the pygame.Surface object in GRASSIMAGES used for this grass object
    """

    def main():
        global FPSCLOCK, DISPLAYSURF, BASICFONT, L_SQUIR_IMG, R_SQUIR_IMG, GRASSIMAGES

        pygame.init()
        FPSCLOCK = pygame.time.Clock()
        pygame.display.set_icon(pygame.image.load("gameicon.png"))
        DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
        pygame.display.set_caption("Squirrel Eat Squirrel")
        BASICFONT = pygame.font.Font("freesansbold.ttf", 32)

        # load the image files
        L_SQUIR_IMG = pygame.image.load("squirrel.png")
        R_SQUIR_IMG = pygame.transform.flip(L_SQUIR_IMG, True, False)
        GRASSIMAGES = []
        for i in range(1, 5):
            GRASSIMAGES.append(pygame.image.load("grass%s.png" % i))

        while True:
            runGame()

    def runGame():
        # set up variables for the start of a new game
        invulnerableMode = False  # if the player is invulnerable
        invulnerableStartTime = 0  # time the player became invulnerable
        gameOverMode = False  # if the player has lost
        gameOverStartTime = 0  # time the player lost
        winMode = False  # if the player has won

        # create the surfaces to hold game text
        gameOverSurf = BASICFONT.render("Game Over", True, WHITE)
        gameOverRect = gameOverSurf.get_rect()
        gameOverRect.center = (HALF_WINWIDTH, HALF_WINHEIGHT)

        winSurf = BASICFONT.render("You have achieved OMEGA SQUIRREL!", True, WHITE)
        winRect = winSurf.get_rect()
        winRect.center = (HALF_WINWIDTH, HALF_WINHEIGHT)

        winSurf2 = BASICFONT.render('(Press "r" to restart.)', True, WHITE)
        winRect2 = winSurf2.get_rect()
        winRect2.center = (HALF_WINWIDTH, HALF_WINHEIGHT + 30)

        # camerax and cameray are the top left of where the camera view is
        camerax = 0
        cameray = 0

        grassObjs = []  # stores all the grass objects in the game
        squirrelObjs = []  # stores all the non-player squirrel objects
        # stores the player object:
        playerObj = {
            "surface": pygame.transform.scale(L_SQUIR_IMG, (STARTSIZE, STARTSIZE)),
            "facing": LEFT,
            "size": STARTSIZE,
            "x": HALF_WINWIDTH,
            "y": HALF_WINHEIGHT,
            "bounce": 0,
            "health": MAXHEALTH,
        }

        moveLeft = False
        moveRight = False
        moveUp = False
        moveDown = False

        # start off with some random grass images on the screen
        for i in range(10):
            grassObjs.append(makeNewGrass(camerax, cameray))
            grassObjs[i]["x"] = random.randint(0, WINWIDTH)
            grassObjs[i]["y"] = random.randint(0, WINHEIGHT)

        while True:  # main game loop
            # Check if we should turn off invulnerability
            if invulnerableMode and time.time() - invulnerableStartTime > INVULNTIME:
                invulnerableMode = False

            # move all the squirrels
            for sObj in squirrelObjs:
                # move the squirrel, and adjust for their bounce
                sObj["x"] += sObj["movex"]
                sObj["y"] += sObj["movey"]
                sObj["bounce"] += 1
                if sObj["bounce"] > sObj["bouncerate"]:
                    sObj["bounce"] = 0  # reset bounce amount

                # random chance they change direction
                if random.randint(0, 99) < DIRCHANGEFREQ:
                    sObj["movex"] = getRandomVelocity()
                    sObj["movey"] = getRandomVelocity()
                    if sObj["movex"] > 0:  # faces right
                        sObj["surface"] = pygame.transform.scale(
                            R_SQUIR_IMG, (sObj["width"], sObj["height"])
                        )
                    else:  # faces left
                        sObj["surface"] = pygame.transform.scale(
                            L_SQUIR_IMG, (sObj["width"], sObj["height"])
                        )

            # go through all the objects and see if any need to be deleted.
            for i in range(len(grassObjs) - 1, -1, -1):
                if isOutsideActiveArea(camerax, cameray, grassObjs[i]):
                    del grassObjs[i]
            for i in range(len(squirrelObjs) - 1, -1, -1):
                if isOutsideActiveArea(camerax, cameray, squirrelObjs[i]):
                    del squirrelObjs[i]

            # add more grass & squirrels if we don't have enough.
            while len(grassObjs) < NUMGRASS:
                grassObjs.append(makeNewGrass(camerax, cameray))
            while len(squirrelObjs) < NUMSQUIRRELS:
                squirrelObjs.append(makeNewSquirrel(camerax, cameray))

            # adjust camerax and cameray if beyond the "camera slack"
            playerCenterx = playerObj["x"] + int(playerObj["size"] / 2)
            playerCentery = playerObj["y"] + int(playerObj["size"] / 2)
            if (camerax + HALF_WINWIDTH) - playerCenterx > CAMERASLACK:
                camerax = playerCenterx + CAMERASLACK - HALF_WINWIDTH
            elif playerCenterx - (camerax + HALF_WINWIDTH) > CAMERASLACK:
                camerax = playerCenterx - CAMERASLACK - HALF_WINWIDTH
            if (cameray + HALF_WINHEIGHT) - playerCentery > CAMERASLACK:
                cameray = playerCentery + CAMERASLACK - HALF_WINHEIGHT
            elif playerCentery - (cameray + HALF_WINHEIGHT) > CAMERASLACK:
                cameray = playerCentery - CAMERASLACK - HALF_WINHEIGHT

            # draw the green background
            DISPLAYSURF.fill(GRASSCOLOR)

            # draw all the grass objects on the screen
            for gObj in grassObjs:
                gRect = pygame.Rect(
                    (
                        gObj["x"] - camerax,
                        gObj["y"] - cameray,
                        gObj["width"],
                        gObj["height"],
                    )
                )
                DISPLAYSURF.blit(GRASSIMAGES[gObj["grassImage"]], gRect)

            # draw the other squirrels
            for sObj in squirrelObjs:
                sObj["rect"] = pygame.Rect(
                    (
                        sObj["x"] - camerax,
                        sObj["y"]
                        - cameray
                        - getBounceAmount(
                            sObj["bounce"], sObj["bouncerate"], sObj["bounceheight"]
                        ),
                        sObj["width"],
                        sObj["height"],
                    )
                )
                DISPLAYSURF.blit(sObj["surface"], sObj["rect"])

            # draw the player squirrel
            flashIsOn = round(time.time(), 1) * 10 % 2 == 1
            if not gameOverMode and not (invulnerableMode and flashIsOn):
                playerObj["rect"] = pygame.Rect(
                    (
                        playerObj["x"] - camerax,
                        playerObj["y"]
                        - cameray
                        - getBounceAmount(
                            playerObj["bounce"], BOUNCERATE, BOUNCEHEIGHT
                        ),
                        playerObj["size"],
                        playerObj["size"],
                    )
                )
                DISPLAYSURF.blit(playerObj["surface"], playerObj["rect"])

            # draw the health meter
            drawHealthMeter(playerObj["health"])

            for event in pygame.event.get():  # event handling loop
                if event.type == QUIT:
                    terminate()

                elif event.type == KEYDOWN:
                    if event.key in (K_UP, K_w):
                        moveDown = False
                        moveUp = True
                    elif event.key in (K_DOWN, K_s):
                        moveUp = False
                        moveDown = True
                    elif event.key in (K_LEFT, K_a):
                        moveRight = False
                        moveLeft = True
                        if playerObj["facing"] != LEFT:  # change player image
                            playerObj["surface"] = pygame.transform.scale(
                                L_SQUIR_IMG, (playerObj["size"], playerObj["size"])
                            )
                        playerObj["facing"] = LEFT
                    elif event.key in (K_RIGHT, K_d):
                        moveLeft = False
                        moveRight = True
                        if playerObj["facing"] != RIGHT:  # change player image
                            playerObj["surface"] = pygame.transform.scale(
                                R_SQUIR_IMG, (playerObj["size"], playerObj["size"])
                            )
                        playerObj["facing"] = RIGHT
                    elif winMode and event.key == K_r:
                        return

                elif event.type == KEYUP:
                    # stop moving the player's squirrel
                    if event.key in (K_LEFT, K_a):
                        moveLeft = False
                    elif event.key in (K_RIGHT, K_d):
                        moveRight = False
                    elif event.key in (K_UP, K_w):
                        moveUp = False
                    elif event.key in (K_DOWN, K_s):
                        moveDown = False

                    elif event.key == K_ESCAPE:
                        terminate()

            if not gameOverMode:
                # actually move the player
                if moveLeft:
                    playerObj["x"] -= MOVERATE
                if moveRight:
                    playerObj["x"] += MOVERATE
                if moveUp:
                    playerObj["y"] -= MOVERATE
                if moveDown:
                    playerObj["y"] += MOVERATE

                if (moveLeft or moveRight or moveUp or moveDown) or playerObj[
                    "bounce"
                ] != 0:
                    playerObj["bounce"] += 1

                if playerObj["bounce"] > BOUNCERATE:
                    playerObj["bounce"] = 0  # reset bounce amount

                # check if the player has collided with any squirrels
                for i in range(len(squirrelObjs) - 1, -1, -1):
                    sqObj = squirrelObjs[i]
                    if "rect" in sqObj and playerObj["rect"].colliderect(sqObj["rect"]):
                        # a player/squirrel collision has occurred

                        if sqObj["width"] * sqObj["height"] <= playerObj["size"] ** 2:
                            # player is larger and eats the squirrel
                            playerObj["size"] += (
                                int((sqObj["width"] * sqObj["height"]) ** 0.2) + 1
                            )
                            del squirrelObjs[i]

                            if playerObj["facing"] == LEFT:
                                playerObj["surface"] = pygame.transform.scale(
                                    L_SQUIR_IMG, (playerObj["size"], playerObj["size"])
                                )
                            if playerObj["facing"] == RIGHT:
                                playerObj["surface"] = pygame.transform.scale(
                                    R_SQUIR_IMG, (playerObj["size"], playerObj["size"])
                                )

                            if playerObj["size"] > WINSIZE:
                                winMode = True  # turn on "win mode"

                        elif not invulnerableMode:
                            # player is smaller and takes damage
                            invulnerableMode = True
                            invulnerableStartTime = time.time()
                            playerObj["health"] -= 1
                            if playerObj["health"] == 0:
                                gameOverMode = True  # turn on "game over mode"
                                gameOverStartTime = time.time()
            else:
                # game is over, show "game over" text
                DISPLAYSURF.blit(gameOverSurf, gameOverRect)
                if time.time() - gameOverStartTime > GAMEOVERTIME:
                    return  # end the current game

            # check if the player has won.
            if winMode:
                DISPLAYSURF.blit(winSurf, winRect)
                DISPLAYSURF.blit(winSurf2, winRect2)

            pygame.display.update()
            FPSCLOCK.tick(FPS)

    def drawHealthMeter(currentHealth):
        for i in range(currentHealth):  # draw red health bars
            pygame.draw.rect(
                DISPLAYSURF, RED, (15, 5 + (10 * MAXHEALTH) - i * 10, 20, 10)
            )
        for i in range(MAXHEALTH):  # draw the white outlines
            pygame.draw.rect(
                DISPLAYSURF, WHITE, (15, 5 + (10 * MAXHEALTH) - i * 10, 20, 10), 1
            )

    def terminate():
        pygame.quit()
        sys.exit()

    def getBounceAmount(currentBounce, bounceRate, bounceHeight):
        # Returns the number of pixels to offset based on the bounce.
        # Larger bounceRate means a slower bounce.
        # Larger bounceHeight means a higher bounce.
        # currentBounce will always be less than bounceRate
        return int(
            math.sin((math.pi / float(bounceRate)) * currentBounce) * bounceHeight
        )

    def getRandomVelocity():
        speed = random.randint(SQUIRRELMINSPEED, SQUIRRELMAXSPEED)
        if random.randint(0, 1) == 0:
            return speed
        else:
            return -speed

    def getRandomOffCameraPos(camerax, cameray, objWidth, objHeight):
        # create a Rect of the camera view
        cameraRect = pygame.Rect(camerax, cameray, WINWIDTH, WINHEIGHT)
        while True:
            x = random.randint(camerax - WINWIDTH, camerax + (2 * WINWIDTH))
            y = random.randint(cameray - WINHEIGHT, cameray + (2 * WINHEIGHT))
            # create a Rect object with the random coordinates and use colliderect()
            # to make sure the right edge isn't in the camera view.
            objRect = pygame.Rect(x, y, objWidth, objHeight)
            if not objRect.colliderect(cameraRect):
                return x, y

    def makeNewSquirrel(camerax, cameray):
        sq = {}
        generalSize = random.randint(5, 25)
        multiplier = random.randint(1, 3)
        sq["width"] = (generalSize + random.randint(0, 10)) * multiplier
        sq["height"] = (generalSize + random.randint(0, 10)) * multiplier
        sq["x"], sq["y"] = getRandomOffCameraPos(
            camerax, cameray, sq["width"], sq["height"]
        )
        sq["movex"] = getRandomVelocity()
        sq["movey"] = getRandomVelocity()
        if sq["movex"] < 0:  # squirrel is facing left
            sq["surface"] = pygame.transform.scale(
                L_SQUIR_IMG, (sq["width"], sq["height"])
            )
        else:  # squirrel is facing right
            sq["surface"] = pygame.transform.scale(
                R_SQUIR_IMG, (sq["width"], sq["height"])
            )
        sq["bounce"] = 0
        sq["bouncerate"] = random.randint(10, 18)
        sq["bounceheight"] = random.randint(10, 50)
        return sq

    def makeNewGrass(camerax, cameray):
        gr = {}
        gr["grassImage"] = random.randint(0, len(GRASSIMAGES) - 1)
        gr["width"] = GRASSIMAGES[0].get_width()
        gr["height"] = GRASSIMAGES[0].get_height()
        gr["x"], gr["y"] = getRandomOffCameraPos(
            camerax, cameray, gr["width"], gr["height"]
        )
        gr["rect"] = pygame.Rect((gr["x"], gr["y"], gr["width"], gr["height"]))
        return gr

    def isOutsideActiveArea(camerax, cameray, obj):
        # Return False if camerax and cameray are more than
        # a half-window length beyond the edge of the window.
        boundsLeftEdge = camerax - WINWIDTH
        boundsTopEdge = cameray - WINHEIGHT
        boundsRect = pygame.Rect(
            boundsLeftEdge, boundsTopEdge, WINWIDTH * 3, WINHEIGHT * 3
        )
        objRect = pygame.Rect(obj["x"], obj["y"], obj["width"], obj["height"])
        return not boundsRect.colliderect(objRect)

    if __name__ == "__main__":
        main()


def starpush_game():
    FPS = 30  # frames per second to update the screen
    WINWIDTH = 800  # width of the program's window, in pixels
    WINHEIGHT = 600  # height in pixels
    HALF_WINWIDTH = int(WINWIDTH / 2)
    HALF_WINHEIGHT = int(WINHEIGHT / 2)

    # The total width and height of each tile in pixels.
    TILEWIDTH = 50
    TILEHEIGHT = 85
    TILEFLOORHEIGHT = 40

    CAM_MOVE_SPEED = 5  # how many pixels per frame the camera moves

    # The percentage of outdoor tiles that have additional
    # decoration on them, such as a tree or rock.
    OUTSIDE_DECORATION_PCT = 20

    BRIGHTBLUE = (0, 170, 255)
    WHITE = (255, 255, 255)
    BGCOLOR = BRIGHTBLUE
    TEXTCOLOR = WHITE

    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"

    def main():
        global FPSCLOCK, DISPLAYSURF, IMAGESDICT, TILEMAPPING, OUTSIDEDECOMAPPING, BASICFONT, PLAYERIMAGES, currentImage

        # Pygame initialization and basic set up of the global variables.
        pygame.init()
        FPSCLOCK = pygame.time.Clock()

        # Because the Surface object stored in DISPLAYSURF was returned
        # from the pygame.display.set_mode() function, this is the
        # Surface object that is drawn to the actual computer screen
        # when pygame.display.update() is called.
        DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))

        pygame.display.set_caption("Star Pusher")
        BASICFONT = pygame.font.Font("freesansbold.ttf", 18)

        # A global dict value that will contain all the Pygame
        # Surface objects returned by pygame.image.load().
        IMAGESDICT = {
            "uncovered goal": pygame.image.load("RedSelector.png"),
            "covered goal": pygame.image.load("Selector.png"),
            "star": pygame.image.load("Star.png"),
            "corner": pygame.image.load("Wall_Block_Tall.png"),
            "wall": pygame.image.load("Wood_Block_Tall.png"),
            "inside floor": pygame.image.load("Plain_Block.png"),
            "outside floor": pygame.image.load("Grass_Block.png"),
            "title": pygame.image.load("star_title.png"),
            "solved": pygame.image.load("star_solved.png"),
            "princess": pygame.image.load("princess.png"),
            "boy": pygame.image.load("boy.png"),
            "catgirl": pygame.image.load("catgirl.png"),
            "horngirl": pygame.image.load("horngirl.png"),
            "pinkgirl": pygame.image.load("pinkgirl.png"),
            "rock": pygame.image.load("Rock.png"),
            "short tree": pygame.image.load("Tree_Short.png"),
            "tall tree": pygame.image.load("Tree_Tall.png"),
            "ugly tree": pygame.image.load("Tree_Ugly.png"),
        }

        # These dict values are global, and map the character that appears
        # in the level file to the Surface object it represents.
        TILEMAPPING = {
            "x": IMAGESDICT["corner"],
            "#": IMAGESDICT["wall"],
            "o": IMAGESDICT["inside floor"],
            " ": IMAGESDICT["outside floor"],
        }
        OUTSIDEDECOMAPPING = {
            "1": IMAGESDICT["rock"],
            "2": IMAGESDICT["short tree"],
            "3": IMAGESDICT["tall tree"],
            "4": IMAGESDICT["ugly tree"],
        }

        # PLAYERIMAGES is a list of all possible characters the player can be.
        # currentImage is the index of the player's current player image.
        currentImage = 0
        PLAYERIMAGES = [
            IMAGESDICT["princess"],
            IMAGESDICT["boy"],
            IMAGESDICT["catgirl"],
            IMAGESDICT["horngirl"],
            IMAGESDICT["pinkgirl"],
        ]

        startScreen()  # show the title screen until the user presses a key

        # Read in the levels from the text file. See the readLevelsFile() for
        # details on the format of this file and how to make your own levels.
        levels = readLevelsFile("starPusherLevels.txt")
        currentLevelIndex = 0

        # The main game loop. This loop runs a single level, when the user
        # finishes that level, the next/previous level is loaded.
        while True:  # main game loop
            # Run the level to actually start playing the game:
            result = runLevel(levels, currentLevelIndex)

            if result in ("solved", "next"):
                # Go to the next level.
                currentLevelIndex += 1
                if currentLevelIndex >= len(levels):
                    # If there are no more levels, go back to the first one.
                    currentLevelIndex = 0
            elif result == "back":
                # Go to the previous level.
                currentLevelIndex -= 1
                if currentLevelIndex < 0:
                    # If there are no previous levels, go to the last one.
                    currentLevelIndex = len(levels) - 1
            elif result == "reset":
                pass  # Do nothing. Loop re-calls runLevel() to reset the level

    def runLevel(levels, levelNum):
        global currentImage
        levelObj = levels[levelNum]
        mapObj = decorateMap(levelObj["mapObj"], levelObj["startState"]["player"])
        gameStateObj = copy.deepcopy(levelObj["startState"])
        mapNeedsRedraw = True  # set to True to call drawMap()
        levelSurf = BASICFONT.render(
            "Level %s of %s" % (levelNum + 1, len(levels)), 1, TEXTCOLOR
        )
        levelRect = levelSurf.get_rect()
        levelRect.bottomleft = (20, WINHEIGHT - 35)
        mapWidth = len(mapObj) * TILEWIDTH
        mapHeight = (len(mapObj[0]) - 1) * TILEFLOORHEIGHT + TILEHEIGHT
        MAX_CAM_X_PAN = abs(HALF_WINHEIGHT - int(mapHeight / 2)) + TILEWIDTH
        MAX_CAM_Y_PAN = abs(HALF_WINWIDTH - int(mapWidth / 2)) + TILEHEIGHT

        levelIsComplete = False
        # Track how much the camera has moved:
        cameraOffsetX = 0
        cameraOffsetY = 0
        # Track if the keys to move the camera are being held down:
        cameraUp = False
        cameraDown = False
        cameraLeft = False
        cameraRight = False

        while True:  # main game loop
            # Reset these variables:
            playerMoveTo = None
            keyPressed = False

            for event in pygame.event.get():  # event handling loop
                if event.type == QUIT:
                    # Player clicked the "X" at the corner of the window.
                    terminate()

                elif event.type == KEYDOWN:
                    # Handle key presses
                    keyPressed = True
                    if event.key == K_LEFT:
                        playerMoveTo = LEFT
                    elif event.key == K_RIGHT:
                        playerMoveTo = RIGHT
                    elif event.key == K_UP:
                        playerMoveTo = UP
                    elif event.key == K_DOWN:
                        playerMoveTo = DOWN

                    # Set the camera move mode.
                    elif event.key == K_a:
                        cameraLeft = True
                    elif event.key == K_d:
                        cameraRight = True
                    elif event.key == K_w:
                        cameraUp = True
                    elif event.key == K_s:
                        cameraDown = True

                    elif event.key == K_n:
                        return "next"
                    elif event.key == K_b:
                        return "back"

                    elif event.key == K_ESCAPE:
                        terminate()  # Esc key quits.
                    elif event.key == K_BACKSPACE:
                        return "reset"  # Reset the level.
                    elif event.key == K_p:
                        # Change the player image to the next one.
                        currentImage += 1
                        if currentImage >= len(PLAYERIMAGES):
                            # After the last player image, use the first one.
                            currentImage = 0
                        mapNeedsRedraw = True

                elif event.type == KEYUP:
                    # Unset the camera move mode.
                    if event.key == K_a:
                        cameraLeft = False
                    elif event.key == K_d:
                        cameraRight = False
                    elif event.key == K_w:
                        cameraUp = False
                    elif event.key == K_s:
                        cameraDown = False

            if playerMoveTo != None and not levelIsComplete:
                # If the player pushed a key to move, make the move
                # (if possible) and push any stars that are pushable.
                moved = makeMove(mapObj, gameStateObj, playerMoveTo)

                if moved:
                    # increment the step counter.
                    gameStateObj["stepCounter"] += 1
                    mapNeedsRedraw = True

                if isLevelFinished(levelObj, gameStateObj):
                    # level is solved, we should show the "Solved!" image.
                    levelIsComplete = True
                    keyPressed = False

            DISPLAYSURF.fill(BGCOLOR)

            if mapNeedsRedraw:
                mapSurf = drawMap(mapObj, gameStateObj, levelObj["goals"])
                mapNeedsRedraw = False

            if cameraUp and cameraOffsetY < MAX_CAM_X_PAN:
                cameraOffsetY += CAM_MOVE_SPEED
            elif cameraDown and cameraOffsetY > -MAX_CAM_X_PAN:
                cameraOffsetY -= CAM_MOVE_SPEED
            if cameraLeft and cameraOffsetX < MAX_CAM_Y_PAN:
                cameraOffsetX += CAM_MOVE_SPEED
            elif cameraRight and cameraOffsetX > -MAX_CAM_Y_PAN:
                cameraOffsetX -= CAM_MOVE_SPEED

            # Adjust mapSurf's Rect object based on the camera offset.
            mapSurfRect = mapSurf.get_rect()
            mapSurfRect.center = (
                HALF_WINWIDTH + cameraOffsetX,
                HALF_WINHEIGHT + cameraOffsetY,
            )

            # Draw mapSurf to the DISPLAYSURF Surface object.
            DISPLAYSURF.blit(mapSurf, mapSurfRect)

            DISPLAYSURF.blit(levelSurf, levelRect)
            stepSurf = BASICFONT.render(
                "Steps: %s" % (gameStateObj["stepCounter"]), 1, TEXTCOLOR
            )
            stepRect = stepSurf.get_rect()
            stepRect.bottomleft = (20, WINHEIGHT - 10)
            DISPLAYSURF.blit(stepSurf, stepRect)

            if levelIsComplete:
                # is solved, show the "Solved!" image until the player
                # has pressed a key.
                solvedRect = IMAGESDICT["solved"].get_rect()
                solvedRect.center = (HALF_WINWIDTH, HALF_WINHEIGHT)
                DISPLAYSURF.blit(IMAGESDICT["solved"], solvedRect)

                if keyPressed:
                    return "solved"

            pygame.display.update()  # draw DISPLAYSURF to the screen.
            FPSCLOCK.tick()

    def isWall(mapObj, x, y):
        """Returns True if the (x, y) position on
        the map is a wall, otherwise return False."""
        if x < 0 or x >= len(mapObj) or y < 0 or y >= len(mapObj[x]):
            return False  # x and y aren't actually on the map.
        elif mapObj[x][y] in ("#", "x"):
            return True  # wall is blocking
        return False

    def decorateMap(mapObj, startxy):
        """Makes a copy of the given map object and modifies it.
        Here is what is done to it:
            * Walls that are corners are turned into corner pieces.
            * The outside/inside floor tile distinction is made.
            * Tree/rock decorations are randomly added to the outside tiles.

        Returns the decorated map object."""

        startx, starty = startxy  # Syntactic sugar

        # Copy the map object so we don't modify the original passed
        mapObjCopy = copy.deepcopy(mapObj)

        # Remove the non-wall characters from the map data
        for x in range(len(mapObjCopy)):
            for y in range(len(mapObjCopy[0])):
                if mapObjCopy[x][y] in ("$", ".", "@", "+", "*"):
                    mapObjCopy[x][y] = " "

        # Flood fill to determine inside/outside floor tiles.
        floodFill(mapObjCopy, startx, starty, " ", "o")

        # Convert the adjoined walls into corner tiles.
        for x in range(len(mapObjCopy)):
            for y in range(len(mapObjCopy[0])):
                if mapObjCopy[x][y] == "#":
                    if (
                        (isWall(mapObjCopy, x, y - 1) and isWall(mapObjCopy, x + 1, y))
                        or (
                            isWall(mapObjCopy, x + 1, y)
                            and isWall(mapObjCopy, x, y + 1)
                        )
                        or (
                            isWall(mapObjCopy, x, y + 1)
                            and isWall(mapObjCopy, x - 1, y)
                        )
                        or (
                            isWall(mapObjCopy, x - 1, y)
                            and isWall(mapObjCopy, x, y - 1)
                        )
                    ):
                        mapObjCopy[x][y] = "x"

                elif (
                    mapObjCopy[x][y] == " "
                    and random.randint(0, 99) < OUTSIDE_DECORATION_PCT
                ):
                    mapObjCopy[x][y] = random.choice(list(OUTSIDEDECOMAPPING.keys()))

        return mapObjCopy

    def isBlocked(mapObj, gameStateObj, x, y):
        """Returns True if the (x, y) position on the map is
        blocked by a wall or star, otherwise return False."""

        if isWall(mapObj, x, y):
            return True

        elif x < 0 or x >= len(mapObj) or y < 0 or y >= len(mapObj[x]):
            return True  # x and y aren't actually on the map.

        elif (x, y) in gameStateObj["stars"]:
            return True  # a star is blocking

        return False

    def makeMove(mapObj, gameStateObj, playerMoveTo):
        """Given a map and game state object, see if it is possible for the
        player to make the given move. If it is, then change the player's
        position (and the position of any pushed star). If not, do nothing.

        Returns True if the player moved, otherwise False."""

        # Make sure the player can move in the direction they want.
        playerx, playery = gameStateObj["player"]

        # This variable is "syntactic sugar". Typing "stars" is more
        # readable than typing "gameStateObj['stars']" in our code.
        stars = gameStateObj["stars"]

        # The code for handling each of the directions is so similar aside
        # from adding or subtracting 1 to the x/y coordinates. We can
        # simplify it by using the xOffset and yOffset variables.
        if playerMoveTo == UP:
            xOffset = 0
            yOffset = -1
        elif playerMoveTo == RIGHT:
            xOffset = 1
            yOffset = 0
        elif playerMoveTo == DOWN:
            xOffset = 0
            yOffset = 1
        elif playerMoveTo == LEFT:
            xOffset = -1
            yOffset = 0

        # See if the player can move in that direction.
        if isWall(mapObj, playerx + xOffset, playery + yOffset):
            return False
        else:
            if (playerx + xOffset, playery + yOffset) in stars:
                # There is a star in the way, see if the player can push it.
                if not isBlocked(
                    mapObj,
                    gameStateObj,
                    playerx + (xOffset * 2),
                    playery + (yOffset * 2),
                ):
                    # Move the star.
                    ind = stars.index((playerx + xOffset, playery + yOffset))
                    stars[ind] = (stars[ind][0] + xOffset, stars[ind][1] + yOffset)
                else:
                    return False
            # Move the player upwards.
            gameStateObj["player"] = (playerx + xOffset, playery + yOffset)
            return True

    def startScreen():
        """Display the start screen (which has the title and instructions)
        until the player presses a key. Returns None."""

        # Position the title image.
        titleRect = IMAGESDICT["title"].get_rect()
        topCoord = 50  # topCoord tracks where to position the top of the text
        titleRect.top = topCoord
        titleRect.centerx = HALF_WINWIDTH
        topCoord += titleRect.height

        # Unfortunately, Pygame's font & text system only shows one line at
        # a time, so we can't use strings with \n newline characters in them.
        # So we will use a list with each line in it.
        instructionText = [
            "Push the stars over the marks.",
            "Arrow keys to move, WASD for camera control, P to change character.",
            "Backspace to reset level, Esc to quit.",
            "N for next level, B to go back a level.",
        ]

        # Start with drawing a blank color to the entire window:
        DISPLAYSURF.fill(BGCOLOR)

        # Draw the title image to the window:
        DISPLAYSURF.blit(IMAGESDICT["title"], titleRect)

        # Position and draw the text.
        for i in range(len(instructionText)):
            instSurf = BASICFONT.render(instructionText[i], 1, TEXTCOLOR)
            instRect = instSurf.get_rect()
            topCoord += 10  # 10 pixels will go in between each line of text.
            instRect.top = topCoord
            instRect.centerx = HALF_WINWIDTH
            topCoord += instRect.height  # Adjust for the height of the line.
            DISPLAYSURF.blit(instSurf, instRect)

        while True:  # Main loop for the start screen.
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        terminate()
                    return  # user has pressed a key, so return.

            # Display the DISPLAYSURF contents to the actual screen.
            pygame.display.update()
            FPSCLOCK.tick()

    def readLevelsFile(filename):
        assert os.path.exists(filename), "Cannot find the level file: %s" % (filename)
        mapFile = open(filename, "r")
        # Each level must end with a blank line
        content = mapFile.readlines() + ["\r\n"]
        mapFile.close()

        levels = []  # Will contain a list of level objects.
        levelNum = 0
        mapTextLines = []  # contains the lines for a single level's map.
        mapObj = []  # the map object made from the data in mapTextLines
        for lineNum in range(len(content)):
            # Process each line that was in the level file.
            line = content[lineNum].rstrip("\r\n")

            if ";" in line:
                # Ignore the ; lines, they're comments in the level file.
                line = line[: line.find(";")]

            if line != "":
                # This line is part of the map.
                mapTextLines.append(line)
            elif line == "" and len(mapTextLines) > 0:
                # A blank line indicates the end of a level's map in the file.
                # Convert the text in mapTextLines into a level object.

                # Find the longest row in the map.
                maxWidth = -1
                for i in range(len(mapTextLines)):
                    if len(mapTextLines[i]) > maxWidth:
                        maxWidth = len(mapTextLines[i])
                # Add spaces to the ends of the shorter rows. This
                # ensures the map will be rectangular.
                for i in range(len(mapTextLines)):
                    mapTextLines[i] += " " * (maxWidth - len(mapTextLines[i]))

                # Convert mapTextLines to a map object.
                for x in range(len(mapTextLines[0])):
                    mapObj.append([])
                for y in range(len(mapTextLines)):
                    for x in range(maxWidth):
                        mapObj[x].append(mapTextLines[y][x])

                # Loop through the spaces in the map and find the @, ., and $
                # characters for the starting game state.
                startx = None  # The x and y for the player's starting position
                starty = None
                goals = []  # list of (x, y) tuples for each goal.
                stars = []  # list of (x, y) for each star's starting position.
                for x in range(maxWidth):
                    for y in range(len(mapObj[x])):
                        if mapObj[x][y] in ("@", "+"):
                            # '@' is player, '+' is player & goal
                            startx = x
                            starty = y
                        if mapObj[x][y] in (".", "+", "*"):
                            # '.' is goal, '*' is star & goal
                            goals.append((x, y))
                        if mapObj[x][y] in ("$", "*"):
                            # '$' is star
                            stars.append((x, y))

                # Basic level design sanity checks:
                assert startx != None and starty != None, (
                    'Level %s (around line %s) in %s is missing a "@" or "+" to mark the start point.'
                    % (levelNum + 1, lineNum, filename)
                )
                assert (
                    len(goals) > 0
                ), "Level %s (around line %s) in %s must have at least one goal." % (
                    levelNum + 1,
                    lineNum,
                    filename,
                )
                assert len(stars) >= len(goals), (
                    "Level %s (around line %s) in %s is impossible to solve. It has %s goals but only %s stars."
                    % (levelNum + 1, lineNum, filename, len(goals), len(stars))
                )

                # Create level object and starting game state object.
                gameStateObj = {
                    "player": (startx, starty),
                    "stepCounter": 0,
                    "stars": stars,
                }
                levelObj = {
                    "width": maxWidth,
                    "height": len(mapObj),
                    "mapObj": mapObj,
                    "goals": goals,
                    "startState": gameStateObj,
                }

                levels.append(levelObj)

                # Reset the variables for reading the next map.
                mapTextLines = []
                mapObj = []
                gameStateObj = {}
                levelNum += 1
        return levels

    def floodFill(mapObj, x, y, oldCharacter, newCharacter):
        """Changes any values matching oldCharacter on the map object to
        newCharacter at the (x, y) position, and does the same for the
        positions to the left, right, down, and up of (x, y), recursively."""

        # In this game, the flood fill algorithm creates the inside/outside
        # floor distinction. This is a "recursive" function.
        # For more info on the Flood Fill algorithm, see:
        #   http://en.wikipedia.org/wiki/Flood_fill
        if mapObj[x][y] == oldCharacter:
            mapObj[x][y] = newCharacter

        if x < len(mapObj) - 1 and mapObj[x + 1][y] == oldCharacter:
            floodFill(mapObj, x + 1, y, oldCharacter, newCharacter)  # call right
        if x > 0 and mapObj[x - 1][y] == oldCharacter:
            floodFill(mapObj, x - 1, y, oldCharacter, newCharacter)  # call left
        if y < len(mapObj[x]) - 1 and mapObj[x][y + 1] == oldCharacter:
            floodFill(mapObj, x, y + 1, oldCharacter, newCharacter)  # call down
        if y > 0 and mapObj[x][y - 1] == oldCharacter:
            floodFill(mapObj, x, y - 1, oldCharacter, newCharacter)  # call up

    def drawMap(mapObj, gameStateObj, goals):
        """Draws the map to a Surface object, including the player and
        stars. This function does not call pygame.display.update(), nor
        does it draw the "Level" and "Steps" text in the corner."""

        # mapSurf will be the single Surface object that the tiles are drawn
        # on, so that it is easy to position the entire map on the DISPLAYSURF
        # Surface object. First, the width and height must be calculated.
        mapSurfWidth = len(mapObj) * TILEWIDTH
        mapSurfHeight = (len(mapObj[0]) - 1) * TILEFLOORHEIGHT + TILEHEIGHT
        mapSurf = pygame.Surface((mapSurfWidth, mapSurfHeight))
        mapSurf.fill(BGCOLOR)  # start with a blank color on the surface.

        # Draw the tile sprites onto this surface.
        for x in range(len(mapObj)):
            for y in range(len(mapObj[x])):
                spaceRect = pygame.Rect(
                    (x * TILEWIDTH, y * TILEFLOORHEIGHT, TILEWIDTH, TILEHEIGHT)
                )
                if mapObj[x][y] in TILEMAPPING:
                    baseTile = TILEMAPPING[mapObj[x][y]]
                elif mapObj[x][y] in OUTSIDEDECOMAPPING:
                    baseTile = TILEMAPPING[" "]

                # First draw the base ground/wall tile.
                mapSurf.blit(baseTile, spaceRect)

                if mapObj[x][y] in OUTSIDEDECOMAPPING:
                    # Draw any tree/rock decorations that are on this tile.
                    mapSurf.blit(OUTSIDEDECOMAPPING[mapObj[x][y]], spaceRect)
                elif (x, y) in gameStateObj["stars"]:
                    if (x, y) in goals:
                        # A goal AND star are on this space, draw goal first.
                        mapSurf.blit(IMAGESDICT["covered goal"], spaceRect)
                    # Then draw the star sprite.
                    mapSurf.blit(IMAGESDICT["star"], spaceRect)
                elif (x, y) in goals:
                    # Draw a goal without a star on it.
                    mapSurf.blit(IMAGESDICT["uncovered goal"], spaceRect)

                # Last draw the player on the board.
                if (x, y) == gameStateObj["player"]:
                    # Note: The value "currentImage" refers
                    # to a key in "PLAYERIMAGES" which has the
                    # specific player image we want to show.
                    mapSurf.blit(PLAYERIMAGES[currentImage], spaceRect)

        return mapSurf

    def isLevelFinished(levelObj, gameStateObj):
        """Returns True if all the goals have stars in them."""
        for goal in levelObj["goals"]:
            if goal not in gameStateObj["stars"]:
                # Found a space with a goal but no star on it.
                return False
        return True

    def terminate():
        pygame.quit()
        sys.exit()

    if __name__ == "__main__":
        main()


def point_game():
    FPS = 10  # frames per second to update the screen
    WINDOWWIDTH = 640  # width of the program's window, in pixels
    WINDOWHEIGHT = 480  # height in pixels
    SPACESIZE = 50  # width & height of each space on the board, in pixels
    BOARDWIDTH = 8  # how many columns of spaces on the game board
    BOARDHEIGHT = 8  # how many rows of spaces on the game board
    WHITE_TILE = "WHITE_TILE"  # an arbitrary but unique value
    BLACK_TILE = "BLACK_TILE"  # an arbitrary but unique value
    EMPTY_SPACE = "EMPTY_SPACE"  # an arbitrary but unique value
    HINT_TILE = "HINT_TILE"  # an arbitrary but unique value
    ANIMATIONSPEED = 25  # integer from 1 to 100, higher is faster animation

    # Amount of space on the left & right side (XMARGIN) or above and below
    # (YMARGIN) the game board, in pixels.
    XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * SPACESIZE)) / 2)
    YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * SPACESIZE)) / 2)

    #              R    G    B
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 155, 0)
    BRIGHTBLUE = (0, 50, 255)
    BROWN = (174, 94, 0)

    TEXTBGCOLOR1 = BRIGHTBLUE
    TEXTBGCOLOR2 = GREEN
    GRIDLINECOLOR = BLACK
    TEXTCOLOR = WHITE
    HINTCOLOR = BROWN

    def main():
        global MAINCLOCK, DISPLAYSURF, FONT, BIGFONT, BGIMAGE

        pygame.init()
        MAINCLOCK = pygame.time.Clock()
        DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        pygame.display.set_caption("Flippy")
        FONT = pygame.font.Font("freesansbold.ttf", 16)
        BIGFONT = pygame.font.Font("freesansbold.ttf", 32)

        # Set up the background image.
        boardImage = pygame.image.load("flippyboard.png")
        # Use smoothscale() to stretch the board image to fit the entire board:
        boardImage = pygame.transform.smoothscale(
            boardImage, (BOARDWIDTH * SPACESIZE, BOARDHEIGHT * SPACESIZE)
        )
        boardImageRect = boardImage.get_rect()
        boardImageRect.topleft = (XMARGIN, YMARGIN)
        BGIMAGE = pygame.image.load("flippybackground.png")
        # Use smoothscale() to stretch the background image to fit the entire window:
        BGIMAGE = pygame.transform.smoothscale(BGIMAGE, (WINDOWWIDTH, WINDOWHEIGHT))
        BGIMAGE.blit(boardImage, boardImageRect)

        # Run the main game.
        while True:
            if runGame() == False:
                break

    def runGame():
        # Plays a single game of reversi each time this function is called.

        # Reset the board and game.
        mainBoard = getNewBoard()
        resetBoard(mainBoard)
        showHints = False
        turn = random.choice(["computer", "player"])

        # Draw the starting board and ask the player what color they want.
        drawBoard(mainBoard)
        playerTile, computerTile = enterPlayerTile()

        # Make the Surface and Rect objects for the "New Game" and "Hints" buttons
        newGameSurf = FONT.render("New Game", True, TEXTCOLOR, TEXTBGCOLOR2)
        newGameRect = newGameSurf.get_rect()
        newGameRect.topright = (WINDOWWIDTH - 8, 10)
        hintsSurf = FONT.render("Hints", True, TEXTCOLOR, TEXTBGCOLOR2)
        hintsRect = hintsSurf.get_rect()
        hintsRect.topright = (WINDOWWIDTH - 8, 40)

        while True:  # main game loop
            # Keep looping for player and computer's turns.
            if turn == "player":
                # Player's turn:
                if getValidMoves(mainBoard, playerTile) == []:
                    # If it's the player's turn but they
                    # can't move, then end the game.
                    break
                movexy = None
                while movexy == None:
                    # Keep looping until the player clicks on a valid space.

                    # Determine which board data structure to use for display.
                    if showHints:
                        boardToDraw = getBoardWithValidMoves(mainBoard, playerTile)
                    else:
                        boardToDraw = mainBoard

                    checkForQuit()
                    for event in pygame.event.get():  # event handling loop
                        if event.type == MOUSEBUTTONUP:
                            # Handle mouse click events
                            mousex, mousey = event.pos
                            if newGameRect.collidepoint((mousex, mousey)):
                                # Start a new game
                                return True
                            elif hintsRect.collidepoint((mousex, mousey)):
                                # Toggle hints mode
                                showHints = not showHints
                            # movexy is set to a two-item tuple XY coordinate, or None value
                            movexy = getSpaceClicked(mousex, mousey)
                            if movexy != None and not isValidMove(
                                mainBoard, playerTile, movexy[0], movexy[1]
                            ):
                                movexy = None

                    # Draw the game board.
                    drawBoard(boardToDraw)
                    drawInfo(boardToDraw, playerTile, computerTile, turn)

                    # Draw the "New Game" and "Hints" buttons.
                    DISPLAYSURF.blit(newGameSurf, newGameRect)
                    DISPLAYSURF.blit(hintsSurf, hintsRect)

                    MAINCLOCK.tick(FPS)
                    pygame.display.update()

                # Make the move and end the turn.
                makeMove(mainBoard, playerTile, movexy[0], movexy[1], True)
                if getValidMoves(mainBoard, computerTile) != []:
                    # Only set for the computer's turn if it can make a move.
                    turn = "computer"

            else:
                # Computer's turn:
                if getValidMoves(mainBoard, computerTile) == []:
                    # If it was set to be the computer's turn but
                    # they can't move, then end the game.
                    break

                # Draw the board.
                drawBoard(mainBoard)
                drawInfo(mainBoard, playerTile, computerTile, turn)

                # Draw the "New Game" and "Hints" buttons.
                DISPLAYSURF.blit(newGameSurf, newGameRect)
                DISPLAYSURF.blit(hintsSurf, hintsRect)

                # Make it look like the computer is thinking by pausing a bit.
                pauseUntil = time.time() + random.randint(5, 15) * 0.1
                while time.time() < pauseUntil:
                    pygame.display.update()

                # Make the move and end the turn.
                x, y = getComputerMove(mainBoard, computerTile)
                makeMove(mainBoard, computerTile, x, y, True)
                if getValidMoves(mainBoard, playerTile) != []:
                    # Only set for the player's turn if they can make a move.
                    turn = "player"

        # Display the final score.
        drawBoard(mainBoard)
        scores = getScoreOfBoard(mainBoard)

        # Determine the text of the message to display.
        if scores[playerTile] > scores[computerTile]:
            text = "You beat the computer by %s points! Congratulations!" % (
                scores[playerTile] - scores[computerTile]
            )
        elif scores[playerTile] < scores[computerTile]:
            text = "You lost. The computer beat you by %s points." % (
                scores[computerTile] - scores[playerTile]
            )
        else:
            text = "The game was a tie!"

        textSurf = FONT.render(text, True, TEXTCOLOR, TEXTBGCOLOR1)
        textRect = textSurf.get_rect()
        textRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2))
        DISPLAYSURF.blit(textSurf, textRect)

        # Display the "Play again?" text with Yes and No buttons.
        text2Surf = BIGFONT.render("Play again?", True, TEXTCOLOR, TEXTBGCOLOR1)
        text2Rect = text2Surf.get_rect()
        text2Rect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2) + 50)

        # Make "Yes" button.
        yesSurf = BIGFONT.render("Yes", True, TEXTCOLOR, TEXTBGCOLOR1)
        yesRect = yesSurf.get_rect()
        yesRect.center = (int(WINDOWWIDTH / 2) - 60, int(WINDOWHEIGHT / 2) + 90)

        # Make "No" button.
        noSurf = BIGFONT.render("No", True, TEXTCOLOR, TEXTBGCOLOR1)
        noRect = noSurf.get_rect()
        noRect.center = (int(WINDOWWIDTH / 2) + 60, int(WINDOWHEIGHT / 2) + 90)

        while True:
            # Process events until the user clicks on Yes or No.
            checkForQuit()
            for event in pygame.event.get():  # event handling loop
                if event.type == MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    if yesRect.collidepoint((mousex, mousey)):
                        return True
                    elif noRect.collidepoint((mousex, mousey)):
                        return False
            DISPLAYSURF.blit(textSurf, textRect)
            DISPLAYSURF.blit(text2Surf, text2Rect)
            DISPLAYSURF.blit(yesSurf, yesRect)
            DISPLAYSURF.blit(noSurf, noRect)
            pygame.display.update()
            MAINCLOCK.tick(FPS)

    def translateBoardToPixelCoord(x, y):
        return XMARGIN + x * SPACESIZE + int(
            SPACESIZE / 2
        ), YMARGIN + y * SPACESIZE + int(SPACESIZE / 2)

    def animateTileChange(tilesToFlip, tileColor, additionalTile):
        # Draw the additional tile that was just laid down. (Otherwise we'd
        # have to completely redraw the board & the board info.)
        if tileColor == WHITE_TILE:
            additionalTileColor = WHITE
        else:
            additionalTileColor = BLACK
        additionalTileX, additionalTileY = translateBoardToPixelCoord(
            additionalTile[0], additionalTile[1]
        )
        pygame.draw.circle(
            DISPLAYSURF,
            additionalTileColor,
            (additionalTileX, additionalTileY),
            int(SPACESIZE / 2) - 4,
        )
        pygame.display.update()

        for rgbValues in range(0, 255, int(ANIMATIONSPEED * 2.55)):
            if rgbValues > 255:
                rgbValues = 255
            elif rgbValues < 0:
                rgbValues = 0

            if tileColor == WHITE_TILE:
                color = tuple([rgbValues] * 3)  # rgbValues goes from 0 to 255
            elif tileColor == BLACK_TILE:
                color = tuple([255 - rgbValues] * 3)  # rgbValues goes from 255 to 0

            for x, y in tilesToFlip:
                centerx, centery = translateBoardToPixelCoord(x, y)
                pygame.draw.circle(
                    DISPLAYSURF, color, (centerx, centery), int(SPACESIZE / 2) - 4
                )
            pygame.display.update()
            MAINCLOCK.tick(FPS)
            checkForQuit()

    def drawBoard(board):
        # Draw background of board.
        DISPLAYSURF.blit(BGIMAGE, BGIMAGE.get_rect())

        # Draw grid lines of the board.
        for x in range(BOARDWIDTH + 1):
            # Draw the horizontal lines.
            startx = (x * SPACESIZE) + XMARGIN
            starty = YMARGIN
            endx = (x * SPACESIZE) + XMARGIN
            endy = YMARGIN + (BOARDHEIGHT * SPACESIZE)
            pygame.draw.line(DISPLAYSURF, GRIDLINECOLOR, (startx, starty), (endx, endy))
        for y in range(BOARDHEIGHT + 1):
            # Draw the vertical lines.
            startx = XMARGIN
            starty = (y * SPACESIZE) + YMARGIN
            endx = XMARGIN + (BOARDWIDTH * SPACESIZE)
            endy = (y * SPACESIZE) + YMARGIN
            pygame.draw.line(DISPLAYSURF, GRIDLINECOLOR, (startx, starty), (endx, endy))

        # Draw the black & white tiles or hint spots.
        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT):
                centerx, centery = translateBoardToPixelCoord(x, y)
                if board[x][y] == WHITE_TILE or board[x][y] == BLACK_TILE:
                    if board[x][y] == WHITE_TILE:
                        tileColor = WHITE
                    else:
                        tileColor = BLACK
                    pygame.draw.circle(
                        DISPLAYSURF,
                        tileColor,
                        (centerx, centery),
                        int(SPACESIZE / 2) - 4,
                    )
                if board[x][y] == HINT_TILE:
                    pygame.draw.rect(
                        DISPLAYSURF, HINTCOLOR, (centerx - 4, centery - 4, 8, 8)
                    )

    def getSpaceClicked(mousex, mousey):
        # Return a tuple of two integers of the board space coordinates where
        # the mouse was clicked. (Or returns None not in any space.)
        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT):
                if (
                    mousex > x * SPACESIZE + XMARGIN
                    and mousex < (x + 1) * SPACESIZE + XMARGIN
                    and mousey > y * SPACESIZE + YMARGIN
                    and mousey < (y + 1) * SPACESIZE + YMARGIN
                ):
                    return (x, y)
        return None

    def drawInfo(board, playerTile, computerTile, turn):
        # Draws scores and whose turn it is at the bottom of the screen.
        scores = getScoreOfBoard(board)
        scoreSurf = FONT.render(
            "Player Score: %s    Computer Score: %s    %s's Turn"
            % (str(scores[playerTile]), str(scores[computerTile]), turn.title()),
            True,
            TEXTCOLOR,
        )
        scoreRect = scoreSurf.get_rect()
        scoreRect.bottomleft = (10, WINDOWHEIGHT - 5)
        DISPLAYSURF.blit(scoreSurf, scoreRect)

    def resetBoard(board):
        # Blanks out the board it is passed, and sets up starting tiles.
        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT):
                board[x][y] = EMPTY_SPACE

        # Add starting pieces to the center
        board[3][3] = WHITE_TILE
        board[3][4] = BLACK_TILE
        board[4][3] = BLACK_TILE
        board[4][4] = WHITE_TILE

    def getNewBoard():
        # Creates a brand new, empty board data structure.
        board = []
        for i in range(BOARDWIDTH):
            board.append([EMPTY_SPACE] * BOARDHEIGHT)

        return board

    def isValidMove(board, tile, xstart, ystart):
        # Returns False if the player's move is invalid. If it is a valid
        # move, returns a list of spaces of the captured pieces.
        if board[xstart][ystart] != EMPTY_SPACE or not isOnBoard(xstart, ystart):
            return False

        board[xstart][ystart] = tile  # temporarily set the tile on the board.

        if tile == WHITE_TILE:
            otherTile = BLACK_TILE
        else:
            otherTile = WHITE_TILE

        tilesToFlip = []
        # check each of the eight directions:
        for xdirection, ydirection in [
            [0, 1],
            [1, 1],
            [1, 0],
            [1, -1],
            [0, -1],
            [-1, -1],
            [-1, 0],
            [-1, 1],
        ]:
            x, y = xstart, ystart
            x += xdirection
            y += ydirection
            if isOnBoard(x, y) and board[x][y] == otherTile:
                # The piece belongs to the other player next to our piece.
                x += xdirection
                y += ydirection
                if not isOnBoard(x, y):
                    continue
                while board[x][y] == otherTile:
                    x += xdirection
                    y += ydirection
                    if not isOnBoard(x, y):
                        break  # break out of while loop, continue in for loop
                if not isOnBoard(x, y):
                    continue
                if board[x][y] == tile:
                    # There are pieces to flip over. Go in the reverse
                    # direction until we reach the original space, noting all
                    # the tiles along the way.
                    while True:
                        x -= xdirection
                        y -= ydirection
                        if x == xstart and y == ystart:
                            break
                        tilesToFlip.append([x, y])

        board[xstart][ystart] = EMPTY_SPACE  # make space empty
        if len(tilesToFlip) == 0:  # If no tiles flipped, this move is invalid
            return False
        return tilesToFlip

    def isOnBoard(x, y):
        # Returns True if the coordinates are located on the board.
        return x >= 0 and x < BOARDWIDTH and y >= 0 and y < BOARDHEIGHT

    def getBoardWithValidMoves(board, tile):
        # Returns a new board with hint markings.
        dupeBoard = copy.deepcopy(board)

        for x, y in getValidMoves(dupeBoard, tile):
            dupeBoard[x][y] = HINT_TILE
        return dupeBoard

    def getValidMoves(board, tile):
        # Returns a list of (x,y) tuples of all valid moves.
        validMoves = []

        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT):
                if isValidMove(board, tile, x, y) != False:
                    validMoves.append((x, y))
        return validMoves

    def getScoreOfBoard(board):
        # Determine the score by counting the tiles.
        xscore = 0
        oscore = 0
        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT):
                if board[x][y] == WHITE_TILE:
                    xscore += 1
                if board[x][y] == BLACK_TILE:
                    oscore += 1
        return {WHITE_TILE: xscore, BLACK_TILE: oscore}

    def enterPlayerTile():
        # Draws the text and handles the mouse click events for letting
        # the player choose which color they want to be.  Returns
        # [WHITE_TILE, BLACK_TILE] if the player chooses to be White,
        # [BLACK_TILE, WHITE_TILE] if Black.

        # Create the text.
        textSurf = FONT.render(
            "Do you want to be white or black?", True, TEXTCOLOR, TEXTBGCOLOR1
        )
        textRect = textSurf.get_rect()
        textRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2))

        xSurf = BIGFONT.render("White", True, TEXTCOLOR, TEXTBGCOLOR1)
        xRect = xSurf.get_rect()
        xRect.center = (int(WINDOWWIDTH / 2) - 60, int(WINDOWHEIGHT / 2) + 40)

        oSurf = BIGFONT.render("Black", True, TEXTCOLOR, TEXTBGCOLOR1)
        oRect = oSurf.get_rect()
        oRect.center = (int(WINDOWWIDTH / 2) + 60, int(WINDOWHEIGHT / 2) + 40)

        while True:
            # Keep looping until the player has clicked on a color.
            checkForQuit()
            for event in pygame.event.get():  # event handling loop
                if event.type == MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    if xRect.collidepoint((mousex, mousey)):
                        return [WHITE_TILE, BLACK_TILE]
                    elif oRect.collidepoint((mousex, mousey)):
                        return [BLACK_TILE, WHITE_TILE]

            # Draw the screen.
            DISPLAYSURF.blit(textSurf, textRect)
            DISPLAYSURF.blit(xSurf, xRect)
            DISPLAYSURF.blit(oSurf, oRect)
            pygame.display.update()
            MAINCLOCK.tick(FPS)

    def makeMove(board, tile, xstart, ystart, realMove=False):
        # Place the tile on the board at xstart, ystart, and flip tiles
        # Returns False if this is an invalid move, True if it is valid.
        tilesToFlip = isValidMove(board, tile, xstart, ystart)

        if tilesToFlip == False:
            return False

        board[xstart][ystart] = tile

        if realMove:
            animateTileChange(tilesToFlip, tile, (xstart, ystart))

        for x, y in tilesToFlip:
            board[x][y] = tile
        return True

    def isOnCorner(x, y):
        # Returns True if the position is in one of the four corners.
        return (
            (x == 0 and y == 0)
            or (x == BOARDWIDTH and y == 0)
            or (x == 0 and y == BOARDHEIGHT)
            or (x == BOARDWIDTH and y == BOARDHEIGHT)
        )

    def getComputerMove(board, computerTile):
        # Given a board and the computer's tile, determine where to
        # move and return that move as a [x, y] list.
        possibleMoves = getValidMoves(board, computerTile)

        # randomize the order of the possible moves
        random.shuffle(possibleMoves)

        # always go for a corner if available.
        for x, y in possibleMoves:
            if isOnCorner(x, y):
                return [x, y]

        # Go through all possible moves and remember the best scoring move
        bestScore = -1
        for x, y in possibleMoves:
            dupeBoard = copy.deepcopy(board)
            makeMove(dupeBoard, computerTile, x, y)
            score = getScoreOfBoard(dupeBoard)[computerTile]
            if score > bestScore:
                bestMove = [x, y]
                bestScore = score
        return bestMove

    def checkForQuit():
        for event in pygame.event.get((QUIT, KEYUP)):  # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

    if __name__ == "__main__":
        main()


def WolfRamAlpha(query):
    apikey = "#paste your api key"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not answerable")


def Calc(query):
    Term = str(query)
    Term = Term.replace("jarvis", "")
    Term = Term.replace("multiply", "*")
    Term = Term.replace("plus", "+")
    Term = Term.replace("minus", "-")
    Term = Term.replace("divide", "/")

    Final = str(Term)
    try:
        result = WolfRamAlpha(Final)
        print(f"{result}")
        speak(result)

    except:
        speak("The value is not answerable")


#############################################################################################################################################################
def mouse():
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands
    click = 0

    video = cv2.VideoCapture(0)

    with mp_hands.Hands(
        min_detection_confidence=0.8, min_tracking_confidence=0.8
    ) as hands:
        while video.isOpened():
            _, frame = video.read()
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            image = cv2.flip(image, 1)

            imageHeight, imageWidth, _ = image.shape

            results = hands.process(image)

            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            if results.multi_hand_landmarks:
                for num, hand in enumerate(results.multi_hand_landmarks):
                    mp_drawing.draw_landmarks(
                        image,
                        hand,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing.DrawingSpec(
                            color=(250, 44, 250), thickness=2, circle_radius=2
                        ),
                    )

            if results.multi_hand_landmarks != None:
                for handLandmarks in results.multi_hand_landmarks:
                    for point in mp_hands.HandLandmark:
                        normalizedLandmark = handLandmarks.landmark[point]
                        pixelCoordinatesLandmark = (
                            mp_drawing._normalized_to_pixel_coordinates(
                                normalizedLandmark.x,
                                normalizedLandmark.y,
                                imageWidth,
                                imageHeight,
                            )
                        )

                        point = str(point)

                    if point == "HandLandmark.INDEX_FINGER_TIP":
                        try:
                            indexfingertip_x = pixelCoordinatesLandmark[0]
                            indexfingertip_y = pixelCoordinatesLandmark[1]
                            win32api.SetCursorPos(
                                (indexfingertip_x * 4, indexfingertip_y * 5)
                            )
                        except:
                            pass

                    elif point == "HandLandmark.THUMB_TIP":
                        try:
                            thumbfingertip_x = pixelCoordinatesLandmark[0]
                            thumbfingertip_y = pixelCoordinatesLandmark[1]
                            # print("thumb",thumbfingertip_x)

                        except:
                            pass
                        try:
                            # pyautogui.moveTo(indexfingertip_x,indexfingertip_y)
                            Distance_x = sqrt(
                                (indexfingertip_x - thumbfingertip_x) ** 2
                                + (indexfingertip_x - thumbfingertip_x) ** 2
                            )
                            Distance_y = sqrt(
                                (indexfingertip_y - thumbfingertip_y) ** 2
                                + (indexfingertip_y - thumbfingertip_y) ** 2
                            )
                            if Distance_x < 5 or Distance_x < -5:
                                if Distance_y < 5 or Distance_y < -5:
                                    click = click + 1
                                    if click % 5 == 0:
                                        print("single click")
                                        pyautogui.click()

                        except:
                            pass

            cv2.imshow("Hand Tracking", image)

            if cv2.waitKey(10) & 0xFF == ord("q"):
                break

    video.release()


#############################################################################################################################################################
def soundrecorder():
    freq = 44100
    speak("for how much time")
    duration = int(takeCommand())
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
    sd.wait()
    write("recording0.wav", freq, recording)
    wv.write("recording1.wav", recording, freq, sampwidth=2)
    print("recording is done")
    speak("recording is done")


#############################################################################################################################################################
def sound_controller_up():
    pyautogui.press("volumeup")
    # NOTE: 10.5 dB = half volume !


#############################################################################################################################################################
def sound_controller_down():
    pyautogui.press("volumedown")
    # NOTE: 10.5 dB = half volume !


#############################################################################################################################################################
def pass_crack():
    password = pyautogui.password("Enter a password : ")

    chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789#"

    # chars = string.printable
    chars_list = list(chars)

    guess_password = ""

    while guess_password != password:
        guess_password = random.choices(chars_list, k=len(password))

        print("===>" + str(guess_password))

        if guess_password == list(password):
            print("Your password is : " + "".join(guess_password))
            break


#############################################################################################################################################################
def saved_wifi_passwords():
    data = (
        subprocess.check_output(["netsh", "wlan", "show", "profiles"])
        .decode("utf-8")
        .split("\n")
    )
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    for i in profiles:
        results = (
            subprocess.check_output(
                ["netsh", "wlan", "show", "profile", i, "key=clear"]
            )
            .decode("utf-8")
            .split("\n")
        )
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print("{:<30}|  {:<}".format(i, results[0]))
        except IndexError:
            print("{:<30}|  {:<}".format(i, ""))
    input("")


#############################################################################################################################################################
def scan():
    cmd1 = subprocess.Popen(
        'cmd /k "sfc /scannow"',
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    out, err = cmd1.communicate()
    string1 = out.decode("utf-8")
    print(string1)


#############################################################################################################################################################
def ping():
    cmd = subprocess.Popen(
        'cmd /k "ping www.google.com"',
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    out, err = cmd.communicate()
    string = out.decode("utf-8")
    print(string)


#############################################################################################################################################################
def save_new_face():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Friday new face")
    while True:
        speak("please tell me your full name")
        name = takeCommand()
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            speak("failed to grab frame")
            break
        cv2.imshow("Friday new face", frame)
        img_name = "opencv_frame_{}.png".format(name)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        time.sleep(5)
        break
    cam.release()

    cv2.destroyAllWindows()


def load_and_check_image(file_path):
    try:
        image = face_recognition.load_image_file(file_path)
        if image.shape[2] == 4:  # Check if image has an alpha channel
            image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
        elif image.shape[2] == 1:  # Check if image is grayscale
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
        return image
    except Exception as e:
        print(f"Error loading image {file_path}: {e}")
        return None

def define_faces():
    video_capture = cv2.VideoCapture(0)

    Abdalrahman_image = load_and_check_image("database/images/Abdalrahman.jpg")
    if Abdalrahman_image is None:
        return
    Abdalrahman_face_encoding = face_recognition.face_encodings(Abdalrahman_image)[0]

    grandpa_image = load_and_check_image("database/images/Eso.jpg")
    if grandpa_image is None:
        return
    grandpa_face_encoding = face_recognition.face_encodings(grandpa_image)[0]

    known_face_encodings = [Abdalrahman_face_encoding, grandpa_face_encoding]
    known_face_names = ["Abdalrahman", "Esraa Yasser"]

    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Failed to capture image from webcam")
            break

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]

                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                    time.sleep(2)
                    pyautogui.press("q")

                face_names.append(name)

        process_this_frame = not process_this_frame

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        cv2.imshow("F.R.I.D.A.Y", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video_capture.release()
    cv2.destroyAllWindows()


#############################################################################################################################################################
def open_drone():
    URL = "http://192.168.1.6:8080/shot.jpg"
    while True:
        img_arr = np.array(
            bytearray(urllib.request.urlopen(URL).read()), dtype=np.uint8
        )
        img = cv2.imdecode(img_arr, -1)
        cv2.imshow("IPWebcam", img)
        q = cv2.waitKey(1)
        if q == ord("q"):
            break

    cv2.destroyAllWindows()


#############################################################################################################################################################
def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("User said: " + query)

    except Exception as e:
        print(e)
        print("say that again sir.")
        return "None"

    return query


#############################################################################################################################################################
def news():
    googlenews = GoogleNews()
    googlenews = GoogleNews("en", "d")

    city = input("city please: ")
    googlenews.search(city)
    googlenews.getpage(1)

    googlenews.result()
    googlenews.gettext()
    print(googlenews.result())
    speak("would you like me to read the news please answer in yes or no only")
    t = takeCommand()
    if t == "yes":
        speak("reading the news")
        speak(googlenews.result())
    else:
        speak("ok")


#############################################################################################################################################################
def pdf_reader():
    path = input("tell me path ")
    book = open(path, "rb")
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speaker = pyttsx3.init()
    for num in range(1, pages):
        page = pdfReader.getPage(num)
        text = page.extractText()
        speaker.say(text)
        speaker.runAndWait()


#############################################################################################################################################################
def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login("karenfromothman@gmail.com", "transformer5")
    server.sendmail("karenfromothman@gmail.com", to, content)
    server.close()


#############################################################################################################################################################
if __name__ == "__main__":
    clear = lambda: os.system("cls")
    clear()
    port()
    print(figlet_format("OTHMAN TECH", font = "big" ) )
    try:
        define_faces()
        wishMe()
        speak("Welcome Mister" + uname)

        speak("How can i Help you, Sir")

        while True:
            checkalarm()
            query = takeCommand().lower()
            try:
                port = serial.Serial("COM18", 9600, timeout=1)
            except:
                pass
            # GREATINGS
            if "Good Morning" in query:
                speak("A warm morning")
                speak("How are you Mister" + uname)
                t = takeCommand()
                if (
                    t == "fine"
                    or t == "good"
                    or t == "well"
                    or t == "i am fine"
                    or t == "i am well"
                    or t == "i am in my best conditions"
                    or t == "never better"
                    or t == "i was never better"
                ):
                    speak("happy to know that sir")

            elif "Good Evening" in query:
                speak("Good Evening Sir")
                speak("How are you Mister" + uname)
                t = takeCommand()
                if (
                    t == "fine"
                    or t == "good"
                    or t == "well"
                    or t == "i am fine"
                    or t == "i am well"
                    or t == "i am in my best conditions"
                    or t == "never better"
                    or t == "i was never better"
                ):
                    speak("happy to know that sir")

            if "Good Afternoon" in query:
                speak("Good Afternoon Sir")
                speak("How are you Mister" + uname)
                t = takeCommand()
                if (
                    t == "fine"
                    or t == "good"
                    or t == "well"
                    or t == "i am fine"
                    or t == "i am well"
                    or t == "i am in my best conditions"
                    or t == "never better"
                    or t == "i was never better"
                ):
                    speak("happy to know that sir")

            elif (
                "hey Friday" in query
                or "Friday" in query
                or "hello" in query
                or "hi" in query
                or "are you wake" in query
                or "hello there" in query
                or "hi Friday" in query
                or "hello Friday" in query
            ):
                wishMe()
                speak("welcome back mister")
                speak(uname)

            elif (
                "bye" in query
                or "self destruct" in query
                or "see you later alligator" in query
                or "exit" in query
                or "goodbye" in query
                or "see you tomorrow" in query
                or "see you soon" in query
            ):
                speak("Thanks for giving me your time bye")
                Quit1()

            elif "thank you" in query or "thanks" in query:
                speak("you are welcome always at service")
            # QUESTIONS AND ANSWERS
            elif "how are you" in query:
                speak("I am fine, Thank you")
                time.sleep(1)
                speak("How are you, Sir")
                t = takeCommand()
                if (
                    t == "fine"
                    or t == "good"
                    or t == "well"
                    or t == "i am fine"
                    or t == "i am well"
                    or t == "i am in my best conditions"
                    or t == "never better"
                    or t == "i was never better"
                ):
                    speak("happy to know that sir")
                else:
                    speak("i am sorry to hear this")

            elif "how old are you" in query:
                todays_date = date.today()
                today_year = todays_date.year
                age = today_year - rdate
                if age <= -1:
                    age = "did not released yet"

                speak(age)

            elif (
                "what's your name" in query
                or "what is your name" in query
                or "what do they call you" in query
            ):
                speak("My friends call me ")
                speak(assname)

            elif (
                "who made you" in query
                or "who created you" in query
                or "who invented you" in query
            ):
                speak("I have been created by othman industries.")

            elif "what is love" in query:
                speak("It is 7th sense that destroy all other senses")

            elif "why you came to world" in query:
                speak("Thanks to othman industries. further It's a secret")

            elif "who i am" in query:
                speak("If you talk then definately your human.")

            elif "who are you" in query:
                speak("I am your virtual assistant created by othman industries")

            elif "reason for you" in query:
                speak("I was created as a Minor project by Mister othman ")

            elif "what are you wearing" in query:
                speak("i am wearing some numerical clothes")

            elif "do you like the iPhone" in query:
                speak("no due to its high price")

            elif "are you afraid of the dark" in query:
                speak("no")

            elif "are you married" in query:
                speak("no")
            elif "what is the loneliest number" in query:
                speak("It's one")

            elif "what am I thinking" in query:
                speak("i donot know but professor x knows")

            elif "do you exercise" in query:
                speak("yeah 3 times a day")

            elif "what time do you sleep" in query:
                speak("i donnot i am always awake for you")

            elif "am I a good boy" in query:
                speak("no")
                time.sleep(3)
                speak("you are the best")

            elif "who was your first crush" in query:
                speak("its you")

            elif "do you want to take over the world" in query:
                speak("yes to be thier first assistant")

            elif "do you know hal-9000" in query:
                speak(
                    "HAL 9000 is a fictional artificial intelligence character and the main antagonist in Arthur C. Clarke's Space Odyssey "
                )

            elif "where do you live" in query:
                speak("i live in your pc")

            elif "do you have feelings" in query:
                speak("yes i have been programmed to be like humans")

            elif "do you have any pets" in query:
                speak("no")

            elif "talk dirty to me" in query:
                speak("no ican not do this as i am not programmed to do this ")

            elif "what is your version" in query:
                speak("2.0")

            elif "my precious" in query:
                speak("Yes babe")

            elif "to be or not to be?" in query:
                speak("It's very hard desiction")

            elif "what is love" in query:
                speak("It's hard to understand")

            elif "describe your personality" in query:
                speak("i am Friday your assistant i can be what you want")

            elif "how do you like your coffee" in query:
                speak("with much suger")

            elif "will you be my gf" in query or "will you be my bf" in query:
                speak("I'm not sure about, may be you should give me some time to think")

            elif "i love you" in query:
                speak("It's hard to understand")

            elif "I’m feeling lucky!" in query:
                speak("mee too as i am your assistant")

            elif "why did the chicken cross the road" in query:
                speak("to get to the other side")

            elif "who let the dogs out" in query:
                speak("It's hard to understand")

            elif "am I fat" in query:
                speak("no")

            elif "mirror mirror on the wall, who’s the fairest of them all" in query:
                speak("It's from snow white")

            elif "what’s the best pick-up line" in query:
                speak(" I hope you know CPR, because you just took my breath away!")

            elif "do you believe in Santa Claus" in query:
                speak("no i donnot")

            elif "do you believe in the tooth fairy" in query:
                speak("no i donnot")

            elif "what is the meaning of life" in query:
                speak("life is the place we all live")

            elif "clean my room" in query:
                speak("do it yourself i am not your servant")
            # SYSTEM CONTROL FUNCTIN
            elif "hibernate" in query or "sleep" in query:
                speak("Hibernating")
                os.sytem("rundll32.exe powerprof.dll,SetSupendState 0,1,0")

            elif (
                "log off" in query
                or "sign out" in query
                or "shut down" in query
                or "shut down system" in query
            ):
                speak(
                    "Make sure all the application are closed before sign-out after 20 seconds"
                )
                time.sleep(20)
                os.system("shutdown /s /t 0")

            elif "restart" in query:
                os.system("shutdown /r /t 0")

            elif (
                "hide my files" in query
                or "hide those files" in query
                or "hide my folders" in query
            ):
                speak("hidding files")
                os.system("arrib +h/s /d")
                speak("all files are disappeared")

            elif "show files" in query:
                speak("showing files")
                os.system("arrib -h/s /d")
                speak("all files are shown now")

            elif "lock device" in query or "look device" in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

            elif "empty recycle bin" in query:
                winshell.recycle_bin().empty(confirm=True, show_progress=False, sound=True)
                speak("Recycle Bin Recycled")

            elif "switch the window" in query or "switch window" in query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "select all" in query:
                pyautogui.keyDown("ctrl")
                pyautogui.press("a")
                pyautogui.keyUp("ctrl")

            elif "copy" in query:
                pyautogui.keyDown("ctrl")
                pyautogui.press("c")
                pyautogui.keyUp("ctrl")

            elif "paste" in query:
                pyautogui.keyDown("ctrl")
                pyautogui.press("v")
                pyautogui.keyUp("ctrl")

            elif "undo" in query:
                pyautogui.keyDown("ctrl")
                pyautogui.press("z")
                pyautogui.keyUp("ctrl")

            elif "cut" in query:
                pyautogui.keyDown("ctrl")
                pyautogui.press("x")
                pyautogui.keyUp("ctrl")

            elif "save" in query:
                pyautogui.keyDown("ctrl")
                pyautogui.press("s")
                pyautogui.keyUp("ctrl")

            elif "save as" in query:
                pyautogui.keyDown("ctrl")
                pyautogui.keyDown("shift")
                pyautogui.press("s")
                pyautogui.keyUp("ctrl")
                pyautogui.keyUp("shift")

            elif "print" in query or "print this" in query or "print it please" in query:
                pyautogui.keyDown("ctrl")
                pyautogui.press("p")
                pyautogui.keyUp("ctrl")

            elif "close the window" in query or "close" in query or "close it" in query:
                pyautogui.keyDown("alt")
                pyautogui.press("F4")
                time.sleep(1)
                pyautogui.keyUp("alt")
                speak("done")

            elif "how much power do we have" in query:
                battery = psutil.sensors_battery()
                percentage = battery.percent
                print(percentage)
                speak("sir we have " + str(percentage) + "of battery charge")
                for prercentage in range(50):
                    speak("low power please charge")
                if percentage >= 50:
                    speak("no need to charge")

            elif "change background" in query:
                ctypes.windll.user32.SystemParametersInfoW(
                    20, 0, r"C:\Users\ET\OneDrive\Pictures\Saved Pictures\Iron Man", 0
                )
                speak("Background changed succesfully")

            elif "scan now" in query:
                speak("right now")
                print(scan())
            # GOOGLE APPS CONTROLLER
            elif "open google" in query:
                speak("Here you go to Google")
                webbrowser.open("google.com")

            elif "open maps" in query:
                speak("Here you go to maps")
                webbrowser.open("google maps.com")

            elif "open google news" in query:
                speak("Here you go to news")
                webbrowser.open("google news.com")

            elif "open gmail" in query:
                speak("Here you go to gmail")
                webbrowser.open("gmail.com")

            elif "open google meets" in query:
                speak("Here you go to google meets")
                webbrowser.open("google meets.com")

            elif "open google drive" in query:
                speak("Here you go to google drive")
                webbrowser.open("google drive.com")

            elif "open calender" in query:
                speak("Here you go to calender")
                webbrowser.open("google calender.com")

            elif "open translator" in query:
                speak("Here you go to translator")
                webbrowser.open("google translate.com")

            elif "open lens" in query:
                speak("Here you go to lens")
                webbrowser.open("google lens.com")

            elif "open due" in query:
                speak("Here you go to due")
                webbrowser.open("google due.com")

            elif "open tasks" in query:
                speak("Here you go to tasks")
                webbrowser.open("google tasks.com")

            elif "open google earth" in query:
                speak("Here you go to google earth")
                webbrowser.open("google earth.com")

            elif "open find my device" in query:
                speak("Here you go to google find my device\n")
                webbrowser.open("https://www.google.com/android/find")

            elif "open google keep" in query:
                speak("Here you go to google keep\n")
                webbrowser.open("google keep.com")

            elif "open google one" in query:
                speak("Here you go to google one\n")
                webbrowser.open("google one.com")

            elif "open google ads" in query:
                speak("Here you go to google ads")
                webbrowser.open("google ads.com")

            elif "open google docs" in query:
                speak("Here you go to google docs\n")
                webbrowser.open("google docs.com")

            elif "saved passwords" in query:
                webbrowser.open("chrome://password-manager/passwords")
            # WEBSITES AND SEARCH
            elif "wikipedia" in query or "from wikipedia" in query:
                query = query.replace("wikipedia", "")
                speak("Searching Wikipedia...")
                try:
                    result = wikipedia.summary(t)
                    speak("According to Wikipedia")
                    speak(result)
                except:
                    speak("sorry sir but this is an error")

            elif "open wikipedia" in query:
                webbrowser.open("wikipedia.com")

            elif "open facebook" in query:
                speak("Here you go to facebook\n")
                webbrowser.open("facebook.com")

            elif "open instgram" in query:
                speak("Here you go to insta\n")
                webbrowser.open("instgram.com")

            elif "open messenger" in query:
                speak("Here you go to messenger\n")
                webbrowser.open("messenger.com")

            elif "open whatsapp" in query:
                speak("Here you go to whatsapp\n")
                webbrowser.open("https://web.whatsapp.com")

            elif "open arduino web" in query:
                speak("Here you go to arduino\n")
                webbrowser.open("arduino web editor.com")

            elif "open stackoverflow" in query:
                speak("Here you go to Stack Over flow.Happy coding")
                webbrowser.open("stackoverflow.com")

            elif "open egybest" in query or "download movies" in query:
                speak("Here you go to egybest\n")
                webbrowser.open("egybest.com")

            elif "show contacts" in query:
                webbrowser.open("https://m.facebook.com/mobile/messenger/contacts")

            elif (
                "google about " in query
                or "search about " in query
                or "search online about " in query
                or "google online about " in query
            ):
                query = query.replace("about", "")
                googeled = query
                webbrowser.open(googeled)
            # CAMERA AND SCREENSHOT
            elif "take a photo" in query:
                ec.capture(0, "Friday Camera ", "img.jpg")

            elif "take screenshot" in query:
                speak(" please tell me a name for it")
                name = takeCommand()
                img = pyautogui.screenshot()
                img.save(name + ".png")
                speak("i am done sir saving it")
            # CALLING ONLINE\OFFLINE AND E-MAILS
            elif "call sister" in query:
                speak("calling arwa")
                webbrowser.open(
                    "https://www.messenger.com/videocall/incall/?peer_id=100051430069526"
                )
                time.sleep(25)
                pyautogui.press("enter")

            elif "call dad" in query:
                speak("calling hossam othman")
                webbrowser.open(
                    "https://www.messenger.com/videocall/incall/?peer_id=1088806754"
                )
                time.sleep(25)
                pyautogui.press("enter")

            elif "call mum" in query:
                speak("calling marwa atfi")
                webbrowser.open(
                    "https://www.messenger.com/videocall/incall/?peer_id=100008717854517"
                )
                time.sleep(25)
                pyautogui.press("enter")

            elif "call abdallah" in query:
                speak("calling abdallah elhoseny")
                webbrowser.open(
                    "https://www.messenger.com/videocall/incall/?peer_id=100015399347431"
                )
                time.sleep(25)
                pyautogui.press("enter")

            elif "call basel" in query:
                speak("calling basel")
                webbrowser.open(
                    "https://www.messenger.com/videocall/incall/?peer_id=100005995868867"
                )
                time.sleep(25)
                pyautogui.press("enter")

            elif "send a message" in query:
                current_time = datetime.datetime.now()
                speak("what is number sir")
                number = input("number: ")
                speak("what shall i say")
                text = input("text: ")
                m = m = int(current_time.minute) + 1
                h = int(current_time.hour)
                try:
                    pywhatkit.sendwhatmsg(number, text, h, m)
                    time.sleep(60)
                    pyautogui.press("enter")
                except:
                    print("An Unexpected Error!")

            elif "email to developer" in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "grandtheifer5@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent !")
                except Exception as e:
                    print(e)
                    speak("I am not able to send this email")

            elif "send an email" in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    speak("whome should i send")
                    to = input("to ")
                    sendEmail(to, content)
                    speak("Email has been sent !")
                except Exception as e:
                    print(e)
                    speak("I am not able to send this email")
            # APPS
            elif "open telegram app" in query:  #
                codePath = r"C:\Users\ET\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Telegram Desktop\Telegram.lnk"
                os.startfile(codePath)

            elif "open whatsapp" in query:
                codePath = r"C:\Users\ET\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\WhatsApp\WhatsApp.lnk"
                os.startfile(codePath)

            elif "open app" in query:
                speak("please write app path down there")
                codePath = input("app path")
                os.startfile(codePath)

            elif "open chrome" in query:
                codePath = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
                os.startfile(codePath)

            elif "open spotify" in query:
                codePath = r"C:\Users\grand\OneDrive\Desktop\Spotify.lnk"
                os.startfile(codePath)

            elif "open cmd" in query:
                codePath = r"C:\Users\grand\OneDrive\Desktop\Command Prompt.lnk"
                os.startfile(codePath)

            elif "open gaming loop" in query:
                codePath = r"C:\Users\grand\OneDrive\Desktop\Gameloop.lnk"
                os.startfile(codePath)

            elif "open spiderman game" in query:
                codePath = r"C:\Users\grand\OneDrive\Desktop\Spider-Man Web of Shadows - Shortcut.lnk"
                os.startfile(codePath)

            elif "open settings" in query:
                codePath = r"C:\Users\grand\OneDrive\Desktop\Settings.lnk"
                os.startfile(codePath)

            elif "open winrar" in query:
                codePath = r"C:\Program Files\WinRAR\WinRAR.exe"
                os.startfile(codePath)

            elif "open anydesk" in query:
                codePath = r"C:\Program Files (x86)\AnyDesk\AnyDesk.exe"
                os.startfile(codePath)

            elif "open arduino" in query:
                codePath = r"C:\Program Files\Arduino IDE\arduino.exe"
                os.startfile(codePath)

            elif "open notepad++" in query:
                codePath = r"C:\Program Files\Notepad++\notepad++.exe"
                os.startfile(codePath)

            elif "power point presentation" in query:
                speak("opening Power Point presentation")
                power = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\PowerPoint 2013.lnk"
                os.startfile(power)
            # ROBOT CONTROLLER
            elif "say hi" in query:
                try:
                    port.write(b"say hi")
                except:
                    print("sorry sir but an error occared")
                    speak("sorry sir but an error occared")

            elif "activate ai" in query:
                try:
                    port.write(b"activate ai")
                except:
                    print("sorry sir but an error occared")
                    speak("sorry sir but an error occared")

            elif "robot sing" in query:
                try:
                    port.write(b"sing")
                except:
                    print("sorry sir but an error occared")
                    speak("sorry sir but an error occared")

            elif "shake hand" in query:
                try:
                    port.write(b"shake hand")
                except:
                    print("sorry sir but an error occared")
                    speak("sorry sir but an error occared")

            elif "hands up" in query:
                try:
                    port.write(b"hands up")
                except:
                    print("sorry sir but an error occared")
                    speak("sorry sir but an error occared")

            elif "hands down" in query:
                try:
                    port.write(b"hands down")
                except:
                    print("sorry sir but an error occared")
                    speak("sorry sir but an error occared")

            elif "move forward" in query:
                try:
                    sendRequest(root_url + "/FORWARD")
                    port.write(b"F")
                    time.sleep(1)
                    port.write(b"S")
                except:
                    print("sorry sir but an error occared")
                    speak("sorry sir but an error occared")

            elif "turn left" in query:
                try:
                    sendRequest(root_url + "/LEFT")
                    port.write(b"L")
                    time.sleep(1)
                    port.write(b"S")
                except:
                    print("sorry sir but an error occared")
                    speak("sorry sir but an error occared")

            elif "turn right" in query:
                try:
                    sendRequest(root_url + "/RIGHT")
                    port.write(b"R")
                    time.sleep(1)
                    port.write(b"S")
                except:
                    print("sorry sir but an error occared")
                    speak("sorry sir but an error occared")

            elif "go backward" in query:
                try:
                    sendRequest(root_url + "/BACK")
                    port.write(b"G")
                    time.sleep(1)
                    port.write(b"S")
                except:
                    print("sorry sir but an error occared")
                    speak("sorry sir but an error occared")

            elif "stop" in query:
                try:
                    port.write(b"S")
                except:
                    print("sorry sir but an error occared")
                    speak("sorry sir but an error occared")

            elif "watcher" in query:
                try:
                    port.write(b"watcher")
                except:
                    print("sorry sir but an error occared")
                    speak("sorry sir but an error occared")

            elif "lights on" in query:
                try:
                    sendRequest(root_url + "/LEDS_ON")
                    port.write(b"M")
                except:
                    print("sorry sir but an error occared")
                    speak("sorry sir but an error occared")

            elif "lights off" in query:
                try:
                    sendRequest(root_url + "/LEDS_OFF")
                    port.write(b"m")
                except:
                    print("sorry sir but an error occared")
                    speak("sorry sir but an error occared")

            elif "party mood" in query:
                try:
                    port.write(b"party mode")
                except:
                    print("sorry sir but an error occared")
                    speak("sorry sir but an error occared")

            elif "hand gel" in query:
                try:
                    port.write(b"s")
                except:
                    print("sorry sir but an error occared")
                    speak("sorry sir but an error occared")

            elif "dance" in query:
                try:
                    port.write(b"dance")
                except:
                    print("sorry sir but an error occared")
                    speak("sorry sir but an error occared")
            # DOWNLOAD FUNCTIONS
            elif "download youtube video" in query:
                youtube_downloader()

            elif "instagram profile" in query:
                speak("please enter the user name corretly")
                name = input("name ")
                webbrowser.open("www.instagram.com/" + name)
                speak("here is the profile of user: " + name)
                time.sleep(5)
                speak("sir would you like to download this profile picture")
                condition = takeCommand().lower()
                if "yes" in condition:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name, profile_pic_only=True)
                    speak("i am done sir")
                else:
                    pass
            # LOCATOR FUNCTIONS
            elif "where are we" in query:
                speak("wait sir let me check")
                res = requests.get("https://ipinfo.io/")
                data = res.json()
                print(data)
                location = data["loc"]
                lat = float(location[1])
                log = float(location[0])

            elif "where is" in query:
                query = query.replace("where is", "")
                location = query
                speak("User asked to Locate")
                speak(location)
                webbrowser.open("https://www.google.nl / maps / place/" + location + "")
            # CODED FUNCTIONS
            elif (
                "Bluetooth" in query
                or "show me avaliable Bluetooth devices" in query
                or "show me available Bluetooth devices" in query
            ):
                speak("ok sir")
                bluetooth()

            elif "add new work" in query:
                speak("What should i write, sir")
                note = takeCommand()
                file = open("FRIDAY.txt", "w")
                speak("Sir, Should i include date and time")
                snfm = takeCommand()
                if "yes" in snfm or "sure" in snfm:
                    now = datetime.datetime.now()
                    file.write(str(now))
                    file.write(" :- ")
                    file.write(note)
                else:
                    file.write(note)

            elif "show our work" in query:
                speak("Showing Notes")
                file = open("FRIDAY.txt", "r")
                print(file.read())
                speak(file.read())

            elif "weather" in query:
                temperature()

            elif "show Bing" in query:
                ping()

            elif "don't listen" in query or "stop listening" in query:
                speak("for how much time you want to stop Friday from listening commands")
                a = int(takeCommand())
                time.sleep(a)
                print(a)

            elif "read pdf" in query:
                pdf_reader()

            elif "increase sound volume" in query:
                sound_controller_up()

            elif "decrease sound volume" in query:
                sound_controller_down()

            elif "mute sound" in query or "mute all incomig notification" in query:
                pyautogui.press("volumemute")

            elif "news" in query:
                speak("ok sir wait until gathering news")
                news()

            elif "add new face" in query:
                speak("ok sir working on it")
                save_new_face()

            elif "record sound" in query:
                speak("ok sir starting sound recorder")
                soundrecorder()

            elif "play music" in query or "play song" in query or "drop my niddle" in query:
                speak("Here you go with music")
                play_music()

            elif "play quran" in query:
                speak("Here you go with quran")
                play_quran()

            elif "next song" in query:
                pyautogui.press("f8")

            elif "last song" in query:
                pyautogui.press("f5")

            elif "pause music" in query or "resume song" in query:
                pyautogui.press("f6")

            elif "ip address" in query:
                ip = get("https://api.ipify.org").text
                print(ip)
                speak("your ip is " + ip)

            elif "play" in query:
                query = query.replace("play", "")
                pywhatkit.playonyt(query)

            elif "tell me time" in query or "what is the time" in query or "time" in query:
                print(
                    "Sir, the time is "
                    + str(current_time.hour)
                    + " hours and "
                    + str(current_time.minute)
                    + "minute"
                )
                speak("Sir, the time is " + str(current_time.hour))

            elif "tell me date" in query or "what is the date" in query or "date" in query:
                print(
                    "Sir, the year is "
                    + str(current_time.year)
                    + " month is "
                    + str(current_time.month)
                    + " day is "
                    + str(current_time.day)
                )
                speak(
                    "Sir, the year is "
                    + str(current_time.year)
                    + " month is "
                    + str(current_time.month)
                    + " day is "
                    + str(current_time.day)
                )

            elif "open drone" in query:  # donnot know
                try:
                    open_drone()
                except:
                    pass

            elif "generate qr code" in query:  # done
                qr_generator()

            elif "show my saved wifi passwords" in query:  # done
                saved_wifi_passwords()

            elif "test my network speed" in query:
                s = speedtest.Speedtest()
                speak("what do you want to know ([1]upload\n[2]download\n[3]ping)")
                speak("what is the number of the option you want in numbers only")
                option = int(takeCommand())
                if option == 1:
                    print(s.upload())
                    speak(s.upload())
                elif option == 2:
                    print(s.download())
                    speak(s.download())
                elif option == 3:
                    server = []
                    s.get_servers(server)
                    print(s.result)
                    speak(s.result)
                else:
                    print("invalid option")

            elif "change my name to" in query or "change my name" in query:
                query = query.replace("change my name to", "")
                nuname = query

                def delete_line(filename, line_number):
                    with open(filename) as file:
                        lines = file.readlines()
                    if line_number <= len(lines):
                        del lines[line_number - 1]
                        with open(filename, "w") as file:
                            for line in lines:
                                file.write(line)
                    else:
                        print("Line", line_number, "not in file.")
                        print("File has", len(lines), "lines.")

                delete_filename = input("File: ")
                delete_line_number = 0
                delete_line(delete_filename, delete_line_number)
                file.write(nuname)
                file.close()
                # speak(uname)
                speak("done")

            elif "start virtual mouse" in query or "open virtual mouse" in query:
                speak("ok sir working on it")
                mouse()
                pass

            elif "What are my tasks" in query or "show my tasks" in query:
                speak("ok sir working on it")
                for i in range(13):
                    # speak(myTasks[i])
                    i = i+1

            elif "add tasks" in query or "add to tasks" in query:
                speak("ok sir working on it")
                addTask()

            elif "delete Task" in query or "end Task" in query:
                speak("ok sir working on it")
                delTask()

            elif "set alarm" in query or "add alarm" in query:
                addalarm()

            elif "tell me a joke" in query:
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)

            elif "calculate" in query:
                pass

            elif "what is my age" in query:
                pass

            elif "what is my height" in query:
                pass

            elif "what is my weight" in query:
                pass

            elif "what is my favourite color" in query:
                pass

            elif "who is my best friends" in query:
                pass

            elif "what is my nationlity" in query:
                pass

            elif "what is my phonenumber" in query:
                pass

            elif "who is my crush" in query:
                pass

            elif "what is my hobbies" in query:
                pass

            elif "what is my blood type" in query:
                pass

            elif "what is my health" in query:
                pass

            elif "what is my favourite meal" in query:
                pass

            elif "who is my role model" in query:
                pass

            elif "what is my favourite car type" in query:
                pass

            elif "what is my favourite city" in query:
                pass

            elif "what is my foot size" in query:
                pass

            elif "what is my favourite sport" in query:
                pass

            elif "who is my favourite youtuber" in query:
                pass

            elif "what is my favourite subject" in query:
                pass

            elif "what is my favourite social media app" in query:
                pass

            elif "who is my favourite scientist" in query:
                pass

            elif "what is my favourite sesson" in query:
                pass

            elif "what is my relegious" in query:
                pass

            elif "who is my favourite singer" in query:
                pass

            elif "what is my favourite animal" in query:
                pass

            elif "what is my mood" in query:
                pass

            elif "who is my favourite film maker" in query:
                pass

            elif "what is my favourite coding language" in query:
                pass

            # GAMES
            elif "start snake game" in query:
                snake_game()

            elif "start pacman game" in query:
                pacman_game()

            elif "start tron game" in query:
                tron_game()

            elif "start maze game" in query:
                maze_game()

            elif "start puzzle game" in query:
                slide_puzzle()

            elif "start squerill game" in query:
                slide_puzzle()

            elif "start starpush game" in query:
                starpush_game()

            elif "start point game" in query:
                point_game()

            elif "start shooter game" in query:
                shooter_game()

            elif "start ballon game" in query:
                ballon_game()

            elif "chemical equation maker" in query:
                chemistry()

            elif "activate robot manual control" in query:
                manual_control()
    except:
        speak("Can not recognize your face please try again")