# Coded by     : SWE-team
# Project name : Eva-AI
# Starting Date: 2024.8.30
# End Date     : 2024.9.30
import os
import re
from sympy import Matrix, lcm
import cv2
import sys
import time
import json
import math
import psutil
import ctypes
import qrcode
import random
import PyPDF2
import sqlite3
import winsound
from pathlib import Path
from math import *
from pyfiglet import figlet_format
import pyttsx3
import pyjokes
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
import winshell
import pyautogui
import subprocess
import webbrowser
import mediapipe as mp
import tkinter as tk
import asyncio
import statistics
import sympy as sp
from bleak import BleakScanner 
from tkinter import messagebox, scrolledtext , filedialog, ttk
import numpy as np
import instaloader
from turtle import *
from tkinter import *
import urllib.request
from pygame.locals import *
from pynput.mouse import Button
from requests import get
from collections import *
from datetime import date
from tkinter.ttk import *
from ecapture import ecapture as ec
from pynput.mouse import Button, Controller
import pyaudio
import wave
import threading
from googlesearch import search
try:
    import requests
    import wikipedia
    import speedtest
    import pywhatkit
    from bs4 import BeautifulSoup
    from pytube import YouTube
    import speech_recognition as sr
    from GoogleNews import GoogleNews
    from urllib.request import urlopen
except ImportError as e:
    messagebox.showerror("Error","System Error cannot open the libraries")
except Exception as e:
    messagebox.showerror("Error","Cannot connect to wifi network Please connect to wifi First")

os.chdir(os.path.dirname(os.path.abspath(__file__)))
current_time = datetime.datetime.now()
assname = "Friday"

class GoogleSearchBot:

    def perform_search(self, query):

        try:
            results = [url for url in search(query, num_results=1, lang="en")]
            if results:
                return results[0] 
            else:
                return None
        except Exception as e:
            messagebox.showerror("Error",f"Error during search: {e}")
            return None

    def fetch_content(self, url):

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            for script_or_style in soup(["script", "style"]):
                script_or_style.decompose()
            text = soup.get_text()
            lines = [line.strip() for line in text.splitlines()]
            content = "\n".join(line for line in lines if line)
            return content[:1000]  # Return the first 1000 characters
        except Exception as e:
            messagebox.showerror("Error",f"Could not fetch content: {e}")

    def run(self):
        # Perform search
        first_result_url = self.perform_search(query)
        if first_result_url:
            content = self.fetch_content(first_result_url)
            print(content)
        else:
            messagebox.showerror("Error","No results found. Please try a different query.")

#########################################################database################################################
# Connect to the database
db = sqlite3.connect("./database/FRIDAY.db")
myCR = db.cursor()

# Create tables if they don't exist
myCR.execute('''
    CREATE TABLE IF NOT EXISTS users (
        name TEXT,
        age INTEGER,
        nationality TEXT,
        phonenumber INTEGER,
        email TEXT UNIQUE,
        password TEXT,
        hobbies TEXT,
        bloodtype TEXT,
        healthProblems TEXT,
        weight INTEGER,
        height INTEGER,
        sports TEXT,
        tasks TEXT,
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_type TEXT
    )
''')
myCR.execute('''
    CREATE TABLE IF NOT EXISTS authenticate (
        name TEXT,
        email TEXT UNIQUE,
        user_id INTEGER
    )
''')

# User class
class User:
    def __init__(self, name=None, age=None, nationality=None, phonenumber=None, email=None, password=None, hobbies=None,
                 bloodtype=None, healthProblems=None, weight=None, height=None, tasks=None, user_type=None, sports=None):
        self.name = name
        self.age = age
        self.nationality = nationality if nationality is not None else []
        self.phonenumber = phonenumber
        self.email = email
        self.password = password
        self.hobbies = hobbies if hobbies is not None else []
        self.bloodtype = bloodtype
        self.healthProblems = healthProblems if healthProblems is not None else []
        self.weight = weight
        self.height = height
        self.tasks = tasks if tasks is not None else []
        self.user_type = user_type
        self.sports = sports if sports is not None else []

    def save_to_db(self, db_connection, db_cursor):
        # Serialize attributes to JSON
        nationality_json = json.dumps(self.nationality)
        hobbies_json = json.dumps(self.hobbies)
        healthProblems_json = json.dumps(self.healthProblems)
        sports_json = json.dumps(self.sports)
        tasks_json = json.dumps(self.tasks)

        # Insert user into the database
        db_cursor.execute('''
            INSERT INTO users (name, age, nationality, phonenumber, email, password, hobbies, bloodtype, healthProblems,
                               weight, height, sports, tasks, user_type)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (self.name, self.age, nationality_json, self.phonenumber, self.email, self.password, hobbies_json,
              self.bloodtype, healthProblems_json, self.weight, self.height, sports_json, tasks_json, self.user_type))

        # Retrieve the auto-generated user_id
        self.user_id = db_cursor.lastrowid

        # Insert into authentication table
        db_cursor.execute("INSERT INTO authenticate (name, email, user_id) VALUES (?, ?, ?)",
                          (self.name, self.email, self.user_id))

        # Commit the transaction
        db_connection.commit()

        # Return the generated user_id
        return self.user_id

# Admin check and creation
myCR.execute("SELECT user_id FROM users WHERE user_type = 'Admin'")
if not myCR.fetchone():  # If no admin exists
    AdminUser = User(
        name="Abdalrahman Hossam Othman",
        age=19,
        nationality=["Egyptian", "Saudi Arabian"],
        phonenumber=201029388659,
        email="grandtheifer5@gmail.com",
        password="starkothman5",
        hobbies=["Coding", "Playing football"],
        bloodtype="A+",
        healthProblems=["No"],
        weight=70,
        height=188,
        tasks=[],
        user_type="Admin",
        sports=[]
    )
    admin_id = AdminUser.save_to_db(db, myCR)
    print(f"Admin user created with ID {admin_id}")
else:
    print("Admin user already exists.")

# Commit and close the connection
db.commit()
#################################################################################################################
# Atomic weights for all elements in the periodic table
ATOMIC_WEIGHTS = {
    "H": 1.008, "He": 4.0026, "Li": 6.94, "Be": 9.0122, "B": 10.81, "C": 12.01, "N": 14.007, "O": 16.00,
    "F": 18.998, "Ne": 20.18, "Na": 22.99, "Mg": 24.305, "Al": 26.982, "Si": 28.085, "P": 30.974, "S": 32.06,
    "Cl": 35.45, "Ar": 39.948, "K": 39.098, "Ca": 40.078, "Sc": 44.956, "Ti": 47.867, "V": 50.942, "Cr": 51.996,
    "Mn": 54.938, "Fe": 55.845, "Co": 58.933, "Ni": 58.693, "Cu": 63.546, "Zn": 65.38, "Ga": 69.723, "Ge": 72.63,
    "As": 74.922, "Se": 78.971, "Br": 79.904, "Kr": 83.798, "Rb": 85.468, "Sr": 87.62, "Y": 88.906, "Zr": 91.224,
    "Nb": 92.906, "Mo": 95.95, "Tc": 98, "Ru": 101.07, "Rh": 102.91, "Pd": 106.42, "Ag": 107.87, "Cd": 112.41,
    "In": 114.82, "Sn": 118.71, "Sb": 121.76, "Te": 127.6, "I": 126.9, "Xe": 131.29, "Cs": 132.91, "Ba": 137.33,
    "La": 138.91, "Ce": 140.12, "Pr": 140.91, "Nd": 144.24, "Pm": 145, "Sm": 150.36, "Eu": 151.96, "Gd": 157.25,
    "Tb": 158.93, "Dy": 162.5, "Ho": 164.93, "Er": 167.26, "Tm": 168.93, "Yb": 173.04, "Lu": 174.97, "Hf": 178.49,
    "Ta": 180.95, "W": 183.84, "Re": 186.21, "Os": 190.23, "Ir": 192.22, "Pt": 195.08, "Au": 196.97, "Hg": 200.59,
    "Tl": 204.38, "Pb": 207.2, "Bi": 208.98, "Po": 209, "At": 210, "Rn": 222, "Fr": 223, "Ra": 226, "Ac": 227,
    "Th": 232.04, "Pa": 231.04, "U": 238.03, "Np": 237, "Pu": 244, "Am": 243, "Cm": 247, "Bk": 247, "Cf": 251,
    "Es": 252, "Fm": 257, "Md": 258, "No": 259, "Lr": 262, "Rf": 267, "Db": 270, "Sg": 271, "Bh": 270, "Hs": 277,
    "Mt": 278, "Ds": 281, "Rg": 282, "Cn": 285, "Nh": 286, "Fl": 289, "Mc": 290, "Lv": 293, "Ts": 294, "Og": 294
}

class ChemicalEquation:
    def __init__(self, equation):
        self.equation = equation
        self.reactants, self.products = self.parse_equation(equation)

    def parse_equation(self, equation):
        left, right = equation.split("->")
        reactants = [comp.strip() for comp in left.split("+")]
        products = [comp.strip() for comp in right.split("+")]
        return reactants, products

    def compound_to_dict(self, compound):
        element_pattern = r"([A-Z][a-z]*)(\d*)"
        elements = re.findall(element_pattern, compound)
        return {element: int(count) if count else 1 for element, count in elements}

    def calculate_molecular_mass(self, compound):
        element_counts = self.compound_to_dict(compound)
        mass = 0
        for element, count in element_counts.items():
            if element not in ATOMIC_WEIGHTS:
                raise ValueError(f"Atomic weight for {element} is not available.")
            mass += ATOMIC_WEIGHTS[element] * count
        return mass

    def is_organic(self, compound):
        return "C" in self.compound_to_dict(compound)

    def balance(self):
        matrix = self.create_matrix()
        null_space = matrix.nullspace()

        if not null_space:
            raise ValueError("No solution found; the equation may already be balanced or invalid.")

        coefficients = null_space[0]
        denominators = [coeff.q for coeff in coefficients]
        multiplier = lcm(denominators)
        coefficients = [int(coeff * multiplier) for coeff in coefficients]

        balanced_equation = []
        for i, coeff in enumerate(coefficients[:len(self.reactants)]):
            balanced_equation.append(f"{coeff}{self.reactants[i]}" if coeff > 1 else self.reactants[i])
        balanced_equation.append("->")
        for i, coeff in enumerate(coefficients[len(self.reactants):]):
            balanced_equation.append(f"{coeff}{self.products[i]}" if coeff > 1 else self.products[i])

        return " + ".join(balanced_equation)

    def create_matrix(self):
        elements = list(self.get_elements())
        matrix = []
        for element in elements:
            row = []
            for compound in self.reactants:
                counts = self.compound_to_dict(compound)
                row.append(counts.get(element, 0))
            for compound in self.products:
                counts = self.compound_to_dict(compound)
                row.append(-counts.get(element, 0))
            matrix.append(row)
        return Matrix(matrix)
 
    def classify_reaction(self, reactants, products):
        """
        Classifies a chemical reaction based on reactants and products.
        """
        if len(reactants) == 1 and len(products) > 1:
            return "Decomposition Reaction"
        elif len(reactants) > 1 and len(products) == 1:
            return "Synthesis Reaction"
        elif len(reactants) == 2 and len(products) == 2:
            return "Double Displacement Reaction"
        elif "O2" in reactants or "O2" in products:
            return "Combustion Reaction"
        else:
            return "Unknown Reaction Type"
            
    def functional_groups(self, compound):

        functional_groups = {
            "OH": "Alcohol",
            "COOH": "Carboxylic Acid",
            "CHO": "Aldehyde",
            "CO": "Ketone",
            "NH2": "Amine",
            "CN": "Nitrile",
            "NO2": "Nitro"
        }
        identified_groups = []
        for group, name in functional_groups.items():
            if group in compound:
                identified_groups.append(name)
        return identified_groups if identified_groups else ["No common functional groups identified"]

    def get_elements(self):
        element_pattern = r"[A-Z][a-z]?"
        elements = set()
        for compound in self.reactants + self.products:
            elements.update(re.findall(element_pattern, compound))
        return elements

def calculate_chemical_equation():
    equation = entry.get()
    try:
        chem_eq = ChemicalEquation(equation)
        balanced = chem_eq.balance()
        molecular_masses = {
            comp: chem_eq.calculate_molecular_mass(comp)
            for comp in chem_eq.reactants + chem_eq.products
        }
        organic_status = {
            comp: chem_eq.is_organic(comp)
            for comp in chem_eq.reactants + chem_eq.products
        }
        compound_breakdown = {
            comp: chem_eq.compound_to_dict(comp)
            for comp in chem_eq.reactants + chem_eq.products
        }

        results = (
            f"Original Equation: {equation}\n"
            f"Balanced Equation: {balanced}\n\n"
            "Molecular Masses:\n"
            + "\n".join([f"{comp}: {mass:.3f}" for comp, mass in molecular_masses.items()])
            + "\n\nOrganic Status:\n"
            + "\n".join([f"{comp}: {'Organic' if is_organic else 'Inorganic'}" for comp, is_organic in organic_status.items()])
            + "\n\nCompound Breakdown:\n"
            + "\n".join([f"{comp}: {elements}" for comp, elements in compound_breakdown.items()])
        )

        # root.withdraw()
        result_window = tk.Toplevel()
        result_window.title("Chemical Equation Solver Results")
        result_window.geometry("700x500")

        tk.Label(result_window, text="Chemical Equation Solver Results", font=("Arial", 14, "bold")).pack(pady=10)
        result_box = scrolledtext.ScrolledText(result_window, width=80, height=25, font=("Courier", 12))
        result_box.pack(pady=10, padx=10)
        result_box.insert(tk.END, results)

        def close_app():
            result_window.destroy()
            root.destroy()

        tk.Button(result_window, text="Close", command=close_app, font=("Arial", 12), bg="lightblue").pack(pady=10)

    except Exception as e:
        messagebox.showerror("Error", str(e))

    # Main GUI
    root = tk.Tk()
    root.title("Chemical Equation Solver")
    root.geometry("500x300")

    tk.Label(root, text="Chemical Equation Solver", font=("Arial", 16, "bold")).pack(pady=10)
    frame = tk.Frame(root)
    frame.pack(pady=10)
    tk.Label(frame, text="Enter Chemical Equation:", font=("Arial", 12)).grid(row=0, column=0, padx=5, sticky="w")
    entry = tk.Entry(frame, width=40, font=("Arial", 12))
    entry.grid(row=0, column=1, padx=5)

    tk.Button(root, text="Calculate", command=calculate_chemical_equation, font=("Arial", 12), bg="lightblue").pack(pady=10)

    root.mainloop()
################################################################################################################# 
class Physics:
    def __init__(self):
        pass

    # Classical Mechanics
    def newtons_second_law(self, mass, acceleration):
        return mass * acceleration

    def kinematics(self, initial_velocity, acceleration, time):
        final_velocity = initial_velocity + acceleration * time
        displacement = initial_velocity * time + 0.5 * acceleration * time**2
        return final_velocity, displacement

    def work_done(self, force, displacement, angle=0):
        return force * displacement * math.cos(math.radians(angle))

    # Thermodynamics
    def heat_transfer(self, mass, specific_heat, temperature_change):
        return mass * specific_heat * temperature_change

    # Electricity and Magnetism
    def coulombs_law(self, charge1, charge2, distance, k=8.9875517923e9):
        return k * abs(charge1 * charge2) / distance**2

    def ohms_law(self, voltage=None, current=None, resistance=None):
        if voltage is None:
            return current * resistance
        elif current is None:
            return voltage / resistance
        elif resistance is None:
            return voltage / current

    # Relativity
    def relativistic_energy(self, mass, speed_of_light=3e8):
        return mass * speed_of_light**2


class PhysicsApp:
    def __init__(self, root):
        self.physics = Physics()
        self.root = root
        self.root.title("Physics Calculator")
        self.root.geometry("600x400")

        # Main Header
        tk.Label(root, text="Physics Calculator", font=("Arial", 16, "bold")).pack(pady=10)

        # Dropdown Menu for Physics Topics
        tk.Label(root, text="Choose a Physics Formula:", font=("Arial", 12)).pack(pady=5)
        self.formula_var = tk.StringVar(value="Select Formula")
        formulas = [
            "Newton's Second Law",
            "Kinematics",
            "Work Done",
            "Heat Transfer",
            "Coulomb's Law",
            "Ohm's Law",
            "Relativistic Energy",
        ]
        self.formula_menu = tk.OptionMenu(root, self.formula_var, *formulas, command=self.show_input_fields)
        self.formula_menu.pack()

        # Frame for Dynamic Input Fields
        self.input_frame = tk.Frame(root)
        self.input_frame.pack(pady=10)

        # Calculate Button
        self.calculate_button = tk.Button(root, text="Calculate", font=("Arial", 12), bg="lightblue", command=self.calculate)
        self.calculate_button.pack(pady=5)

        # Result Label
        self.result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
        self.result_label.pack(pady=10)

    def show_input_fields(self, formula):
        for widget in self.input_frame.winfo_children():
            widget.destroy()

        self.inputs = {}

        if formula == "Newton's Second Law":
            self.create_input_field("Mass (kg):", "mass")
            self.create_input_field("Acceleration (m/s²):", "acceleration")
        elif formula == "Kinematics":
            self.create_input_field("Initial Velocity (m/s):", "initial_velocity")
            self.create_input_field("Acceleration (m/s²):", "acceleration")
            self.create_input_field("Time (s):", "time")
        elif formula == "Work Done":
            self.create_input_field("Force (N):", "force")
            self.create_input_field("Displacement (m):", "displacement")
            self.create_input_field("Angle (degrees):", "angle")
        elif formula == "Heat Transfer":
            self.create_input_field("Mass (kg):", "mass")
            self.create_input_field("Specific Heat (J/kg·K):", "specific_heat")
            self.create_input_field("Temperature Change (K):", "temperature_change")
        elif formula == "Coulomb's Law":
            self.create_input_field("Charge 1 (C):", "charge1")
            self.create_input_field("Charge 2 (C):", "charge2")
            self.create_input_field("Distance (m):", "distance")
        elif formula == "Ohm's Law":
            self.create_input_field("Voltage (V):", "voltage", optional=True)
            self.create_input_field("Current (A):", "current", optional=True)
            self.create_input_field("Resistance (Ω):", "resistance", optional=True)
        elif formula == "Relativistic Energy":
            self.create_input_field("Mass (kg):", "mass")

    def create_input_field(self, label_text, key, optional=False):
        frame = tk.Frame(self.input_frame)
        frame.pack(pady=5, fill="x")

        label = tk.Label(frame, text=label_text, font=("Arial", 12))
        label.pack(side="left", padx=5)

        entry = tk.Entry(frame, font=("Arial", 12))
        entry.pack(side="left", padx=5, fill="x", expand=True)

        self.inputs[key] = {"entry": entry, "optional": optional}

    def calculate(self):
        formula = self.formula_var.get()
        try:
            # Collect inputs
            input_values = {}
            for key, info in self.inputs.items():
                value = info["entry"].get()
                if value:
                    input_values[key] = float(value)
                elif not info["optional"]:
                    raise ValueError(f"Missing required input: {key}")

            # Perform calculation based on the selected formula
            if formula == "Newton's Second Law":
                result = self.physics.newtons_second_law(input_values["mass"], input_values["acceleration"])
                result_text = f"Force: {result:.2f} N"
            elif formula == "Kinematics":
                vf, d = self.physics.kinematics(
                    input_values["initial_velocity"], input_values["acceleration"], input_values["time"]
                )
                result_text = f"Final Velocity: {vf:.2f} m/s, Displacement: {d:.2f} m"
            elif formula == "Work Done":
                result = self.physics.work_done(
                    input_values["force"], input_values["displacement"], input_values["angle"]
                )
                result_text = f"Work Done: {result:.2f} J"
            elif formula == "Heat Transfer":
                result = self.physics.heat_transfer(
                    input_values["mass"], input_values["specific_heat"], input_values["temperature_change"]
                )
                result_text = f"Heat Transfer: {result:.2f} J"
            elif formula == "Coulomb's Law":
                result = self.physics.coulombs_law(
                    input_values["charge1"], input_values["charge2"], input_values["distance"]
                )
                result_text = f"Electrostatic Force: {result:.2e} N"
            elif formula == "Ohm's Law":
                result = self.physics.ohms_law(
                    voltage=input_values.get("voltage"),
                    current=input_values.get("current"),
                    resistance=input_values.get("resistance"),
                )
                result_text = f"Result: {result:.2f}"
            elif formula == "Relativistic Energy":
                result = self.physics.relativistic_energy(input_values["mass"])
                result_text = f"Energy: {result:.2e} J"
            else:
                result_text = "Unknown formula selected."

            self.result_label.config(text=result_text)
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", str(e))

def physicis_run():
    # Run the application
    root = tk.Tk()
    app = PhysicsApp(root)
    root.mainloop()
#########################################################database################################################ 
def signin_signup():
    def register_user(db, user_data, register_window):
        cursor = db.cursor()
        try:
            nationality_json = json.dumps(user_data['nationality'])
            hobbies_json = json.dumps(user_data['hobbies'])
            healthProblems_json = json.dumps(user_data['healthProblems'])
            sports_json = json.dumps(user_data['sports'])
            tasks_json = json.dumps(user_data['tasks'])

            cursor.execute('''
                INSERT INTO users (name, age, nationality, phonenumber, email, password, hobbies, bloodtype, healthProblems,
                                weight, height, sports, tasks, user_type)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (user_data['name'], user_data['age'], nationality_json, user_data['phonenumber'], user_data['email'],
                user_data['password'], hobbies_json, user_data['bloodtype'], healthProblems_json, user_data['weight'],
                user_data['height'], sports_json, tasks_json, "User"))

            db.commit()
            messagebox.showinfo("Success", "User registered successfully! Returning to login page.")
            register_window.destroy()
            show_signin_form()
        except sqlite3.IntegrityError as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def authenticate_user(db, email, password):
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        result = cursor.fetchone()
        if result:
            stored_password = result[5]  # Assuming password is the 6th column
            if stored_password == password:
                global uname, uage, unationality, uhobbies, ubloodtype, uhealthProblems, uweight, uheight, usports, utasks , uemail , upassword , uphonenumber , uuser_type
                uname = result[0]
                uage = result[1]
                unationality = json.loads(result[2])
                uphonenumber = result[3]
                uemail = result[4]
                upassword = result[5]
                uhobbies = json.loads(result[6])
                ubloodtype = result[7]
                uhealthProblems = json.loads(result[8])
                uweight = result[9]
                uheight = result[10]
                usports = json.loads(result[11])
                utasks = json.loads(result[12])
                uuser_type = result[13]
                global access
                access = True
                root.after(1000, root.destroy)
            else:
                access = False
                messagebox.showerror("Error", "Incorrect password!")
        else:
            messagebox.showerror("Error", "Email not found!")

    def show_register_form():
        def on_register():
            user_data = {
                "name": entry_name.get(),
                "age": int(entry_age.get()),
                "nationality": entry_nationality.get().split(","),
                "phonenumber": int(entry_phonenumber.get()),
                "email": entry_email.get(),
                "password": entry_password.get(),
                "hobbies": entry_hobbies.get().split(","),
                "bloodtype": entry_bloodtype.get(),
                "healthProblems": entry_healthProblems.get().split(","),
                "weight": int(entry_weight.get()),
                "height": int(entry_height.get()),
                "sports": entry_sports.get().split(","),
                "tasks": entry_tasks.get().split(",")
            }
            register_user(db, user_data, register_window)

        register_window = tk.Toplevel(root)
        register_window.title("Register")
        register_window.geometry("500x600")

        font_style = ("Arial", 12)

        tk.Label(register_window, text="Name:", font=font_style).grid(row=0, column=0, pady=5, padx=10, sticky="w")
        entry_name = tk.Entry(register_window, font=font_style, width=30)
        entry_name.grid(row=0, column=1, pady=5, padx=10)

        tk.Label(register_window, text="Age:", font=font_style).grid(row=1, column=0, pady=5, padx=10, sticky="w")
        entry_age = tk.Entry(register_window, font=font_style, width=30)
        entry_age.grid(row=1, column=1, pady=5, padx=10)

        tk.Label(register_window, text="Nationality (comma-separated):", font=font_style).grid(row=2, column=0, pady=5, padx=10, sticky="w")
        entry_nationality = tk.Entry(register_window, font=font_style, width=30)
        entry_nationality.grid(row=2, column=1, pady=5, padx=10)

        tk.Label(register_window, text="Phone Number:", font=font_style).grid(row=3, column=0, pady=5, padx=10, sticky="w")
        entry_phonenumber = tk.Entry(register_window, font=font_style, width=30)
        entry_phonenumber.grid(row=3, column=1, pady=5, padx=10)

        tk.Label(register_window, text="Email:", font=font_style).grid(row=4, column=0, pady=5, padx=10, sticky="w")
        entry_email = tk.Entry(register_window, font=font_style, width=30)
        entry_email.grid(row=4, column=1, pady=5, padx=10)

        tk.Label(register_window, text="Password:", font=font_style).grid(row=5, column=0, pady=5, padx=10, sticky="w")
        entry_password = tk.Entry(register_window, font=font_style, show="*", width=30)
        entry_password.grid(row=5, column=1, pady=5, padx=10)

        tk.Label(register_window, text="Hobbies (comma-separated):", font=font_style).grid(row=6, column=0, pady=5, padx=10, sticky="w")
        entry_hobbies = tk.Entry(register_window, font=font_style, width=30)
        entry_hobbies.grid(row=6, column=1, pady=5, padx=10)

        tk.Label(register_window, text="Blood Type:", font=font_style).grid(row=7, column=0, pady=5, padx=10, sticky="w")
        entry_bloodtype = tk.Entry(register_window, font=font_style, width=30)
        entry_bloodtype.grid(row=7, column=1, pady=5, padx=10)

        tk.Label(register_window, text="Health Problems (comma-separated):", font=font_style).grid(row=8, column=0, pady=5, padx=10, sticky="w")
        entry_healthProblems = tk.Entry(register_window, font=font_style, width=30)
        entry_healthProblems.grid(row=8, column=1, pady=5, padx=10)

        tk.Label(register_window, text="Weight:", font=font_style).grid(row=9, column=0, pady=5, padx=10, sticky="w")
        entry_weight = tk.Entry(register_window, font=font_style, width=30)
        entry_weight.grid(row=9, column=1, pady=5, padx=10)

        tk.Label(register_window, text="Height:", font=font_style).grid(row=10, column=0, pady=5, padx=10, sticky="w")
        entry_height = tk.Entry(register_window, font=font_style, width=30)
        entry_height.grid(row=10, column=1, pady=5, padx=10)

        tk.Label(register_window, text="Sports (comma-separated):", font=font_style).grid(row=11, column=0, pady=5, padx=10, sticky="w")
        entry_sports = tk.Entry(register_window, font=font_style, width=30)
        entry_sports.grid(row=11, column=1, pady=5, padx=10)

        tk.Label(register_window, text="Tasks (comma-separated):", font=font_style).grid(row=12, column=0, pady=5, padx=10, sticky="w")
        entry_tasks = tk.Entry(register_window, font=font_style, width=30)
        entry_tasks.grid(row=12, column=1, pady=5, padx=10)

        tk.Button(register_window, text="Register", command=on_register, font=font_style, bg="lightblue", width=15).grid(row=13, columnspan=2, pady=10)

    def show_signin_form():
        def on_signin():
            email = entry_email.get()
            password = entry_password.get()
            authenticate_user(db, email, password)

        signin_window = tk.Toplevel(root)
        signin_window.title("Sign In")
        signin_window.geometry("400x200")

        font_style = ("Arial", 12)

        tk.Label(signin_window, text="Email:", font=font_style).grid(row=0, column=0, pady=10, padx=10, sticky="w")
        entry_email = tk.Entry(signin_window, font=font_style, width=30)
        entry_email.grid(row=0, column=1, pady=10, padx=10)

        tk.Label(signin_window, text="Password:", font=font_style).grid(row=1, column=0, pady=10, padx=10, sticky="w")
        entry_password = tk.Entry(signin_window, font=font_style, show="*", width=30)
        entry_password.grid(row=1, column=1, pady=10, padx=10)

        tk.Button(signin_window, text="Sign In", command=on_signin, font=font_style, bg="lightgreen", width=15).grid(row=2, columnspan=2, pady=10)
    # Create main application window
    root = tk.Tk()
    root.title("User Management")
    root.geometry("400x300")

    font_style = ("Arial", 14)

    # Main buttons
    tk.Button(root, text="Register", command=show_register_form, font=font_style, bg="lightblue", width=20).pack(pady=20)
    tk.Button(root, text="Sign In", command=show_signin_form, font=font_style, bg="lightgreen", width=20).pack(pady=20)

    root.mainloop()

##################################################################################################
def sos():
    for _ in range(5):  # Ring SOS sound 5 times
        winsound.Beep(440, 500)  # Frequency: 440 Hz, Duration: 500 ms
        time.sleep(0.5)

alarms = []
def addalarm():
    speak("Please tell me the time in hours and minutes in 24-hour format, separated by a colon (e.g., 14:30).")
    alarm_time = takeCommand().strip()
    speak("What is the alarm for?")
    alarm_label = takeCommand().strip()
    
    try:
        # Validate time format
        datetime.strptime(alarm_time, "%H:%M")
        alarms.append({"time": alarm_time, "label": alarm_label})
        speak(f"Alarm set for {alarm_time} with label '{alarm_label}'.")
    except ValueError:
        speak("Invalid time format. Please try again.")

def checkalarm():
    now = datetime.datetime.now().strftime("%H:%M")
    for alarm in alarms:
        if alarm["time"] == now:
            speak(f"Alarm! {alarm['label']}")
            sos()
            alarms.remove(alarm)
            break

# GUI for managing alarms
def gui_alarm():
    def add_alarm():
        time = time_entry.get().strip()
        label = label_entry.get().strip()
        
        try:
            datetime.strptime(time, "%H:%M")
            alarms.append({"time": time, "label": label})
            messagebox.showinfo("Success", f"Alarm set for {time} with label '{label}'.")
        except ValueError:
            messagebox.showerror("Error", "Invalid time format. Use HH:MM in 24-hour format.")
    
    # GUI Setup
    root = tk.Tk()
    root.title("Alarm Clock")
    root.geometry("300x250")
    
    tk.Label(root, text="Alarm Time (HH:MM):", font=("Helvetica", 12)).pack(pady=5)
    time_entry = tk.Entry(root, font=("Helvetica", 12))
    time_entry.pack(pady=5)
    
    tk.Label(root, text="Alarm Label:", font=("Helvetica", 12)).pack(pady=5)
    label_entry = tk.Entry(root, font=("Helvetica", 12))
    label_entry.pack(pady=5)
    
    tk.Button(root, text="Set Alarm", command=add_alarm, bg="green", fg="white", font=("Helvetica", 12)).pack(pady=10)
    
    # Background thread for checking alarms
    threading.Thread(target=checkalarm, daemon=True).start()
    
    root.mainloop()
#################################################################################################      
def scan_bluetooth_devices():
    async def async_scan():
        try:
            # Scan for Bluetooth devices
            devices = await BleakScanner.discover(timeout=5)  # Adjust the timeout as needed
            if not devices:
                messagebox.showinfo("Bluetooth Devices", "No devices found.")
                return

            # Format the list of devices
            devices_list = "\n".join([f"{device.name or 'Unknown'} ({device.address})" for device in devices])
            messagebox.showinfo("Bluetooth Devices", f"Found devices:\n\n{devices_list}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to scan for Bluetooth devices: {e}")

    # Run the asynchronous scan
    asyncio.run(async_scan())

    # Create a hidden Tkinter root window
    root = Tk()
    root.withdraw()  # Hide the Tkinter root window

def youtube_downloader():
    def downloader():
        try:
            url = YouTube(link.get())
            video = url.streams.get_highest_resolution()
            save_path = folder_path.get() if folder_path.get() else "./"
            video.download(save_path)
            messagebox.showinfo("Success", "Download completed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to download video: {e}")

    def browse_folder():
        directory = filedialog.askdirectory()
        if directory:
            folder_path.set(directory)
        else:
            folder_path.set("./")

    # Main Window
    root = Tk()
    root.geometry("600x400")
    root.title("YouTube Video Downloader")
    root.resizable(False, False)
    root.configure(bg="#f4f4f4")

    # Title Label
    Label(
        root, text="YouTube Video Downloader", font=("Arial", 20, "bold"), fg="#333", bg="#f4f4f4"
    ).pack(pady=20)

    # Link Entry
    link = StringVar()
    Label(root, text="Paste YouTube link here:", font=("Arial", 14), bg="#f4f4f4", fg="#333").pack(pady=5)
    Entry(root, textvariable=link, width=50, font=("Arial", 14), bd=2, relief="solid").pack(pady=10)

    # Folder Selection
    folder_path = StringVar()
    Label(root, text="Select Download Folder (optional):", font=("Arial", 14), bg="#f4f4f4", fg="#333").pack(pady=5)
    folder_frame = Frame(root, bg="#f4f4f4")
    folder_frame.pack(pady=5)
    Entry(folder_frame, textvariable=folder_path, width=40, font=("Arial", 12), bd=2, relief="solid", state="readonly").pack(side=LEFT, padx=5)
    Button(folder_frame, text="Browse", command=browse_folder, font=("Arial", 12), bg="#0078D7", fg="white", activebackground="#005a9e", activeforeground="white").pack(side=LEFT, padx=5)

    # Download Button
    Button(
        root,
        text="Download",
        font=("Arial", 16, "bold"),
        bg="#28a745",
        fg="white",
        activebackground="#218838",
        activeforeground="white",
        padx=20,
        pady=10,
        command=downloader,
    ).pack(pady=30)

    # Footer
    Label(
        root,
        text="Developed by YouTube Enthusiast",
        font=("Arial", 10),
        bg="#f4f4f4",
        fg="#555",
    ).pack(side=BOTTOM, pady=10)

    # Run the GUI
    root.mainloop()
    
def get_default_music_folder():

    try:
        # Use the Path library to get the user's home directory
        music_folder = Path.home() / "Music"
        if music_folder.exists():
            return str(music_folder)
        else:
            raise FileNotFoundError("Default Music folder not found.")
    except Exception as e:
        return f"An error occurred: {str(e)}"

music_path = get_default_music_folder()

def play_music():
    music_dir = music_path + r"\Music"
    songs = os.listdir(music_dir)
    for song in songs:
        if song.endswith(".mp3"):
            os.startfile(os.path.join(music_dir, song))
    print(songs)

    def music_start():
        os.startfile(os.path.join(music_dir, songs[random.randint(0, 3)]))

    music_start()


def play_quran():
    music_dir = music_dir = music_path + r"\Quran"
    songs = os.listdir(music_dir)
    for song in songs:
        if song.endswith(".mp3"):
            os.startfile(os.path.join(music_dir, song))
    print(songs)

    def music_start():
        os.startfile(os.path.join(music_dir, songs[random.randint(0, 3)]))

    music_start()


def qr_generator(data, name, folder_path):
    try:
        qr = qrcode.QRCode(version=1, box_size=15, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white")

        # Save the QR code to the specified folder
        file_path = os.path.join(folder_path, name + ".png")
        img.save(file_path)
        return file_path
    except Exception as e:
        return str(e)

# GUI Application
class QRCodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("700x500")
        self.root.configure(bg="#f4f4f4")

        # Main Header
        tk.Label(root, text="QR Code Generator", font=("Arial", 20, "bold"), bg="#f4f4f4", fg="#333333").pack(pady=20)

        # Input Data
        tk.Label(root, text="Enter Data for QR Code:", font=("Arial", 14), bg="#f4f4f4", fg="#333333").pack(pady=5)
        self.data_entry = tk.Entry(root, width=50, font=("Arial", 14))
        self.data_entry.pack(pady=5)

        # Input Filename
        tk.Label(root, text="Enter Filename (without extension):", font=("Arial", 14), bg="#f4f4f4", fg="#333333").pack(pady=5)
        self.filename_entry = tk.Entry(root, width=50, font=("Arial", 14))
        self.filename_entry.pack(pady=5)

        # Select Folder Button
        tk.Button(root, text="Select Folder", command=self.select_folder, font=("Arial", 12), bg="#0078D7", fg="white", activebackground="#005a9e", activeforeground="white").pack(pady=10)
        self.folder_label = tk.Label(root, text="No folder selected", font=("Arial", 12), bg="#f4f4f4", fg="gray")
        self.folder_label.pack(pady=5)

        # Generate QR Code Button
        tk.Button(root, text="Generate QR Code", command=self.generate_qr_code, font=("Arial", 14), bg="#28a745", fg="white", activebackground="#218838", activeforeground="white").pack(pady=20)

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.folder_path = folder_path
            self.folder_label.config(text=f"Folder: {folder_path}", fg="#333333")
        else:
            self.folder_path = None
            self.folder_label.config(text="No folder selected", fg="red")

    def generate_qr_code(self):
        data = self.data_entry.get().strip()
        filename = self.filename_entry.get().strip()

        if not data:
            messagebox.showerror("Error", "Please enter data for the QR code.")
            return

        if not filename:
            messagebox.showerror("Error", "Please enter a filename.")
            return

        if not hasattr(self, 'folder_path') or not self.folder_path:
            messagebox.showerror("Error", "Please select a folder to save the QR code.")
            return

        # Generate and save the QR code
        file_path = qr_generator(data, filename, self.folder_path)
        if os.path.exists(file_path):
            messagebox.showinfo("Success", f"QR Code saved at: {file_path}")
        else:
            messagebox.showerror("Error", f"Failed to save QR Code: {file_path}")
def Run_QR():
    root = tk.Tk()
    app = QRCodeApp(root)
    root.mainloop()

def IOT(command, nodemcu_ip):
    try:
        url = f"http://{nodemcu_ip}/?command={command}"
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            messagebox.showinfo("Success", f"Command sent successfully!\nResponse: {response.text}")
        else:
            messagebox.showerror("Error", f"Failed to send command. HTTP Status Code: {response.status_code}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send command: {e}")

# GUI Application
def nodemcu_gui():
    def get_ip():
        ip_address = ip_var.get().strip()

        if not ip_address:
            messagebox.showerror("Input Error", "Please enter the NodeMCU IP address.")
            return

        # Save the IP address and close the GUI
        global nodemcu_ip
        nodemcu_ip = ip_address
        root.destroy()

    # Main Window
    root = Tk()
    root.geometry("400x200")
    root.title("NodeMCU IP Input")
    root.resizable(False, False)
    root.configure(bg="#f4f4f4")

    # Title Label
    Label(root, text="Enter NodeMCU IP Address", font=("Arial", 16, "bold"), bg="#f4f4f4", fg="#333").pack(pady=20)

    # IP Address Input
    ip_var = StringVar()
    Entry(root, textvariable=ip_var, width=30, font=("Arial", 12), bd=2, relief="solid").pack(pady=10)

    # Submit Button
    Button(
        root,
        text="Submit",
        font=("Arial", 14),
        bg="#28a745",
        fg="white",
        activebackground="#218838",
        activeforeground="white",
        command=get_ip,
        padx=10,
        pady=5
    ).pack(pady=20)

    # Run the GUI
    root.mainloop()

def Quit1():
    sys.exit()

def addTask():
    speak("Which task do you want to add")
    newTask = takeCommand()
    utasks.append(newTask)
    try:
        myCR.execute("INSERT INTO tasks (task) VALUES (?)", (newTask,))
        db.commit()
        speak("Task added and database updated successfully.")
    except sqlite3.Error as e:
        speak("An error occurred please try again")

    
def delTask():
    speak("Which task do you want to remove")
    taskTobeRemoved = takeCommand()
    if taskTobeRemoved in utasks:
        utasks.remove(taskTobeRemoved)
    try:
        myCR.execute("DELETE FROM tasks WHERE task = ?", (taskTobeRemoved,))
        db.commit()
        speak("Task added and database updated successfully.")
    except sqlite3.Error as e:
        speak("An error occurred please try again")

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
        speak(f"The weather in {user_input} is: {weather}")
        print(f"The temperature in {user_input} is: {temp}ºF and {(temp-32) * 5/9}ºC")
        speak(f"The temperature in {user_input} is: {temp}ºF and {int((temp-32) * 5/9)}ºC")



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


class MathCalc:
    def evaluate_expression(self, expression):
        try:
            return sp.sympify(expression).evalf()
        except Exception as e:
            return f"Error: {e}"

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"

    def modulus(self, a, b):
        return a % b

    def exponent(self, a, b):
        return a ** b

    def factorial(self, a):
        if a >= 0:
            return math.factorial(a)
        else:
            return "Error: Negative numbers"

    def gcd(self, a, b):
        return math.gcd(a, b)

    def lcm(self, a, b):
        return abs(a * b) // math.gcd(a, b) if a and b else 0

    def mean(self, data):
        return statistics.mean(data)

    def median(self, data):
        return statistics.median(data)

    def variance(self, data):
        return statistics.variance(data)

    def standard_deviation(self, data):
        return statistics.stdev(data)

    def union(self, set_a, set_b):
        return set_a.union(set_b)

    def intersection(self, set_a, set_b):
        return set_a.intersection(set_b)

    def difference(self, set_a, set_b):
        return set_a.difference(set_b)

    def derivative(self, expr, variable):
        return sp.diff(expr, variable)

    def integral(self, expr, variable):
        return sp.integrate(expr, variable)

    def solve_linear(self, equations, variables):
        return sp.solve(equations, variables)

class MathCalcGUI:
    def __init__(self, root):
        self.calc = MathCalc()
        self.root = root
        self.root.title("Enhanced Math Calculator")
        self.root.geometry("700x600")
        self.root.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = tk.Label(self.root, text="Enhanced Math Calculator", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)

        # Number of Variables Selection
        self.num_vars_label = tk.Label(self.root, text="Enter Number of Variables:", font=("Helvetica", 12))
        self.num_vars_label.pack(pady=5)

        self.num_vars_spinbox = tk.Spinbox(self.root, from_=1, to=10, font=("Helvetica", 12), width=5)
        self.num_vars_spinbox.pack(pady=5)

        # Input Label
        self.input_label = tk.Label(self.root, text="Enter Expression or Data (comma-separated):", font=("Helvetica", 12))
        self.input_label.pack(pady=5)

        # Input Field
        self.input_field = tk.Entry(self.root, font=("Helvetica", 12), width=50)
        self.input_field.pack(pady=10)

        # Operation Selection
        self.operation_label = tk.Label(self.root, text="Select Operation:", font=("Helvetica", 12))
        self.operation_label.pack(pady=5)

        self.operation_combobox = ttk.Combobox(self.root, state="readonly", font=("Helvetica", 12), width=30)
        self.operation_combobox['values'] = [
            "Evaluate Expression", "Addition", "Subtraction", "Multiplication", "Division",
            "Modulus", "Exponent", "Factorial", "GCD", "LCM",
            "Mean", "Median", "Variance", "Standard Deviation",
            "Union", "Intersection", "Difference",
            "Derivative", "Integral", "Solve Linear Equations"
        ]
        self.operation_combobox.pack(pady=10)
        self.operation_combobox.current(0)

        # Calculate Button
        self.calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate, bg="green", fg="white", font=("Helvetica", 12))
        self.calculate_button.pack(pady=10)

        # Result Display
        self.result_label = tk.Label(self.root, text="Result:", font=("Helvetica", 12))
        self.result_label.pack(pady=5)

        self.result_display = tk.Entry(self.root, font=("Helvetica", 12), state="readonly", width=50)
        self.result_display.pack(pady=10)

    def calculate(self):
        operation = self.operation_combobox.get()
        expression = self.input_field.get()
        num_vars = int(self.num_vars_spinbox.get())
        try:
            if operation == "Evaluate Expression":
                result = self.calc.evaluate_expression(expression)

            elif operation in ["Mean", "Median", "Variance", "Standard Deviation"]:
                data = list(map(float, expression.split(',')))
                if len(data) != num_vars:
                    raise ValueError("Number of variables does not match input data.")
                if operation == "Mean":
                    result = self.calc.mean(data)
                elif operation == "Median":
                    result = self.calc.median(data)
                elif operation == "Variance":
                    result = self.calc.variance(data)
                elif operation == "Standard Deviation":
                    result = self.calc.standard_deviation(data)

            elif operation in ["Union", "Intersection", "Difference"]:
                sets = expression.split(';')
                if len(sets) != 2:
                    raise ValueError("Two sets are required for this operation.")
                set_a = set(map(int, sets[0].split(',')))
                set_b = set(map(int, sets[1].split(',')))
                if operation == "Union":
                    result = self.calc.union(set_a, set_b)
                elif operation == "Intersection":
                    result = self.calc.intersection(set_a, set_b)
                elif operation == "Difference":
                    result = self.calc.difference(set_a, set_b)

            elif operation in ["Derivative", "Integral"]:
                expr, variable = expression.split(',')
                expr = sp.sympify(expr)
                variable = sp.Symbol(variable)
                if operation == "Derivative":
                    result = self.calc.derivative(expr, variable)
                elif operation == "Integral":
                    result = self.calc.integral(expr, variable)

            elif operation == "Solve Linear Equations":
                equations, variables = expression.split(';')
                equations = [sp.sympify(eq.strip()) for eq in equations.split(',')]
                variables = [sp.Symbol(var.strip()) for var in variables.split(',')]
                result = self.calc.solve_linear(equations, variables)

            else:
                numbers = list(map(float, expression.split(',')))
                if len(numbers) != num_vars:
                    raise ValueError("Number of variables does not match input data.")
                if operation == "Addition":
                    result = sum(numbers)
                elif operation == "Subtraction":
                    result = numbers[0] - sum(numbers[1:])
                elif operation == "Multiplication":
                    result = math.prod(numbers)
                elif operation == "Division":
                    result = numbers[0]
                    for num in numbers[1:]:
                        result /= num
                elif operation == "Modulus":
                    result = numbers[0] % numbers[1]
                elif operation == "Exponent":
                    result = numbers[0] ** numbers[1]
                elif operation == "Factorial":
                    result = self.calc.factorial(int(numbers[0]))
                elif operation == "GCD":
                    result = math.gcd(int(numbers[0]), int(numbers[1]))
                elif operation == "LCM":
                    result = self.calc.lcm(int(numbers[0]), int(numbers[1]))
                else:
                    result = "Invalid Operation"

            self.result_display.config(state="normal")
            self.result_display.delete(0, tk.END)
            self.result_display.insert(0, str(result))
            self.result_display.config(state="readonly")

        except ValueError as ve:
            messagebox.showerror("Input Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
def calculate():
# Run the Application
    root = tk.Tk()
    app = MathCalcGUI(root)
    root.mainloop()

def mouse():
    
    mouse = Controller()

    screen_width, screen_height = pyautogui.size()

    mpHands = mp.solutions.hands
    hands = mpHands.Hands(
        static_image_mode=False,
        model_complexity=1,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7,
        max_num_hands=1
    )

    def get_angle(a, b, c):
        radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
        angle = np.abs(np.degrees(radians))
        return angle

    def get_distance(landmark_list):
        if len(landmark_list) < 2:
            return
        (x1, y1), (x2, y2) = landmark_list[0], landmark_list[1]
        L = np.hypot(x2 - x1, y2 - y1)
        return np.interp(L, [0, 1], [0, 1000])

    def find_finger_tip(processed):
        if processed.multi_hand_landmarks:
            hand_landmarks = processed.multi_hand_landmarks[0]  # Assuming only one hand is detected
            index_finger_tip = hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP]
            return index_finger_tip
        return None, None

    def move_mouse(index_finger_tip):
        if index_finger_tip is not None:
            x = int(index_finger_tip.x * screen_width)
            y = int(index_finger_tip.y / 2 * screen_height)
            pyautogui.moveTo(x, y)

    def is_left_click(landmark_list, thumb_index_dist):
        return (
                get_angle(landmark_list[5], landmark_list[6], landmark_list[8]) < 50 and
                get_angle(landmark_list[9], landmark_list[10], landmark_list[12]) > 90 and
                thumb_index_dist > 50
        )

    def is_right_click(landmark_list, thumb_index_dist):
        return (
                get_angle(landmark_list[9], landmark_list[10], landmark_list[12]) < 50 and
                get_angle(landmark_list[5], landmark_list[6], landmark_list[8]) > 90  and
                thumb_index_dist > 50
        )

    def is_double_click(landmark_list, thumb_index_dist):
        return (
                get_angle(landmark_list[5], landmark_list[6], landmark_list[8]) < 50 and
                get_angle(landmark_list[9], landmark_list[10], landmark_list[12]) < 50 and
                thumb_index_dist > 50
        )

    def is_screenshot(landmark_list, thumb_index_dist):
        return (
                get_angle(landmark_list[5], landmark_list[6], landmark_list[8]) < 50 and
                get_angle(landmark_list[9], landmark_list[10], landmark_list[12]) < 50 and
                thumb_index_dist < 50
        )

    def detect_gesture(frame, landmark_list, processed):
        if len(landmark_list) >= 21:

            index_finger_tip = find_finger_tip(processed)
            thumb_index_dist = get_distance([landmark_list[4], landmark_list[5]])

            if thumb_index_dist < 50 and get_angle(landmark_list[5], landmark_list[6], landmark_list[8]) > 90:
                move_mouse(index_finger_tip)
            elif is_left_click(landmark_list,  thumb_index_dist):
                mouse.press(Button.left)
                mouse.release(Button.left)
                cv2.putText(frame, "Left Click", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            elif is_right_click(landmark_list, thumb_index_dist):
                mouse.press(Button.right)
                mouse.release(Button.right)
                cv2.putText(frame, "Right Click", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            elif is_double_click(landmark_list, thumb_index_dist):
                pyautogui.doubleClick()
                cv2.putText(frame, "Double Click", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
            elif is_screenshot(landmark_list,thumb_index_dist ):
                im1 = pyautogui.screenshot()
                label = random.randint(1, 1000)
                im1.save(f'my_screenshot_{label}.png')
                cv2.putText(frame, "Screenshot Taken", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

    draw = mp.solutions.drawing_utils
    cap = cv2.VideoCapture(0)

    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.flip(frame, 1)
            frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            processed = hands.process(frameRGB)

            landmark_list = []
            if processed.multi_hand_landmarks:
                hand_landmarks = processed.multi_hand_landmarks[0]  # Assuming only one hand is detected
                draw.draw_landmarks(frame, hand_landmarks, mpHands.HAND_CONNECTIONS)
                for lm in hand_landmarks.landmark:
                    landmark_list.append((lm.x, lm.y))

            detect_gesture(frame, landmark_list, processed)

            cv2.imshow('Frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()



def soundrecorder():
    
    class AudioRecorderApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Audio Recorder")
            self.root.geometry("400x300")
            self.root.resizable(False, False)

            # Title Label
            self.title_label = tk.Label(root, text="Audio Recorder", font=("Helvetica", 16, "bold"))
            self.title_label.pack(pady=10)

            # File Selection
            self.file_frame = tk.Frame(root)
            self.file_frame.pack(pady=10)
            self.file_label = tk.Label(self.file_frame, text="Output File:", font=("Helvetica", 12))
            self.file_label.pack(side=tk.LEFT, padx=5)
            self.file_button = tk.Button(self.file_frame, text="Select File", command=self.select_output_file)
            self.file_button.pack(side=tk.LEFT)

            # Recording Controls
            self.controls_frame = tk.Frame(root)
            self.controls_frame.pack(pady=20)
            self.record_button = tk.Button(self.controls_frame, text="Start Recording", command=self.start_recording, width=15, bg="green", fg="white")
            self.record_button.grid(row=0, column=0, padx=10)
            self.stop_button = tk.Button(self.controls_frame, text="Stop Recording", command=self.stop_recording, width=15, bg="red", fg="white", state=tk.DISABLED)
            self.stop_button.grid(row=0, column=1, padx=10)

            # Status Label
            self.status_label = tk.Label(root, text="Status: Ready", font=("Helvetica", 12), fg="blue")
            self.status_label.pack(pady=10)

            self.output_file = "output.wav"
            self.is_recording = False
            self.audio = None
            self.stream = None
            self.frames = []

        def select_output_file(self):
            self.output_file = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("WAV files", "*.wav")])
            if not self.output_file:
                self.output_file = "output.wav"
            self.status_label.config(text=f"Output File: {self.output_file}", fg="black")

        def start_recording(self):
            self.is_recording = True
            self.record_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.frames = []
            self.status_label.config(text="Status: Recording...", fg="green")

            self.audio = pyaudio.PyAudio()
            self.stream = self.audio.open(format=pyaudio.paInt16,
                                        channels=2,
                                        rate=44100,
                                        input=True,
                                        frames_per_buffer=1024)

            threading.Thread(target=self.record_audio_thread, daemon=True).start()

        def stop_recording(self):
            self.is_recording = False
            self.record_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.status_label.config(text="Status: Saving...", fg="orange")

            if self.stream is not None:
                self.stream.stop_stream()
                self.stream.close()
                self.audio.terminate()

            # Save the audio data to a WAV file
            with wave.open(self.output_file, "wb") as wf:
                wf.setnchannels(2)
                wf.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
                wf.setframerate(44100)
                wf.writeframes(b"".join(self.frames))

            self.status_label.config(text=f"Status: Saved to {self.output_file}", fg="blue")
            messagebox.showinfo("Recording Complete", f"Recording finished. File saved as {self.output_file}")

        def record_audio_thread(self):
            while self.is_recording:
                data = self.stream.read(1024)
                self.frames.append(data)

    def launch_app():
        root = tk.Tk()
        app = AudioRecorderApp(root)
        root.mainloop()

    launch_app()



def sound_controller_up():
    pyautogui.press("volumeup")
    # NOTE: 10.5 dB = half volume !


def sound_controller_down():
    pyautogui.press("volumedown")
    # NOTE: 10.5 dB = half volume !


def pass_crack():

    class PasswordCheckerApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Password Strength Checker")
            self.root.geometry("400x300")
            self.root.resizable(False, False)

            # Title Label
            self.title_label = tk.Label(root, text="Password Strength Checker", font=("Helvetica", 16, "bold"))
            self.title_label.pack(pady=10)

            # Input Frame
            self.input_frame = tk.Frame(root)
            self.input_frame.pack(pady=10)

            self.password_label = tk.Label(self.input_frame, text="Enter Password:", font=("Helvetica", 12))
            self.password_label.pack(side=tk.LEFT, padx=5)

            self.password_entry = tk.Entry(self.input_frame, show="*", width=30)
            self.password_entry.pack(side=tk.LEFT, padx=5)

            # Check Button
            self.check_button = tk.Button(root, text="Check Strength", command=self.check_strength, bg="blue", fg="white", width=20)
            self.check_button.pack(pady=10)

            # Result Label
            self.result_label = tk.Label(root, text="", font=("Helvetica", 12), fg="green")
            self.result_label.pack(pady=10)

            # Recommendations Frame
            self.recommendations_label = tk.Label(root, text="", font=("Helvetica", 12), fg="red")
            self.recommendations_label.pack(pady=10)

        def check_password_strength(self, password):
            # Initialize the score and recommendations
            score = 0
            recommendations = []

            # Define password strength criteria
            length_criteria = len(password) >= 8
            digit_criteria = re.search(r"\d", password) is not None
            uppercase_criteria = re.search(r"[A-Z]", password) is not None
            lowercase_criteria = re.search(r"[a-z]", password) is not None
            special_char_criteria = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

            # Evaluate criteria and update score
            if length_criteria:
                score += 2
            else:
                recommendations.append("Make the password at least 8 characters long.")

            if digit_criteria:
                score += 1
            else:
                recommendations.append("Include at least one digit (0-9).")

            if uppercase_criteria:
                score += 1
            else:
                recommendations.append("Include at least one uppercase letter (A-Z).")

            if lowercase_criteria:
                score += 1
            else:
                recommendations.append("Include at least one lowercase letter (a-z).")

            if special_char_criteria:
                score += 2
            else:
                recommendations.append("Include at least one special character (!@#$%^&*(),.?\":{}|<>).")

            return score, recommendations

        def check_strength(self):
            password = self.password_entry.get()
            if not password:
                messagebox.showerror("Error", "Please enter a password.")
                return

            score, recommendations = self.check_password_strength(password)
            self.result_label.config(text=f"Password Strength Score: {score}/7", fg="green" if score == 7 else "orange")

            if score == 7:
                self.recommendations_label.config(text="Your password is very strong!")
            else:
                recommendations_text = "\n".join(recommendations)
                self.recommendations_label.config(text=f"Recommendations:\n{recommendations_text}")

    # Launch the GUI
    root = tk.Tk()
    app = PasswordCheckerApp(root)
    root.mainloop()



def saved_wifi_passwords():
    
    class WifiPasswordViewerApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Wi-Fi Password Viewer")
            self.root.geometry("600x400")
            self.root.resizable(False, False)

            # Title Label
            self.title_label = tk.Label(root, text="Wi-Fi Password Viewer", font=("Helvetica", 16, "bold"))
            self.title_label.pack(pady=10)

            # Treeview for displaying Wi-Fi networks and passwords
            self.tree = ttk.Treeview(root, columns=("SSID", "Password"), show="headings")
            self.tree.heading("SSID", text="Wi-Fi Name (SSID)")
            self.tree.heading("Password", text="Password")
            self.tree.column("SSID", width=250, anchor=tk.W)
            self.tree.column("Password", width=250, anchor=tk.W)
            self.tree.pack(pady=20, fill=tk.BOTH, expand=True)

            # Buttons
            self.button_frame = tk.Frame(root)
            self.button_frame.pack(pady=10)
            self.fetch_button = tk.Button(self.button_frame, text="Fetch Wi-Fi Passwords", command=self.fetch_wifi_passwords, bg="blue", fg="white", width=20)
            self.fetch_button.pack(side=tk.LEFT, padx=10)
            self.clear_button = tk.Button(self.button_frame, text="Clear List", command=self.clear_list, bg="red", fg="white", width=20)
            self.clear_button.pack(side=tk.LEFT, padx=10)

        def fetch_wifi_passwords(self):
            try:
                # Run the command to get all Wi-Fi profiles
                profiles_output = subprocess.check_output("netsh wlan show profiles", shell=True, universal_newlines=True)
                profiles = [line.split(":")[-1].strip() for line in profiles_output.splitlines() if "All User Profile" in line]

                # Fetch passwords for each profile
                for profile in profiles:
                    try:
                        password_output = subprocess.check_output(f'netsh wlan show profile "{profile}" key=clear', shell=True, universal_newlines=True)
                        password_lines = [line.split(":")[-1].strip() for line in password_output.splitlines() if "Key Content" in line]
                        password = password_lines[0] if password_lines else "<No Password>"
                    except subprocess.CalledProcessError:
                        password = "<Access Denied>"

                    self.tree.insert("", tk.END, values=(profile, password))

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

        def clear_list(self):
            for item in self.tree.get_children():
                self.tree.delete(item)

    # Launch the GUI
    root = tk.Tk()
    app = WifiPasswordViewerApp(root)
    root.mainloop()



def run_sfc():

    try:
        process = subprocess.Popen(
            ['sfc', '/scannow'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        output, error = process.communicate()

        if process.returncode == 0:
            if "Windows Resource Protection did not find any integrity violations" in output:
                return "No integrity violations were found."
            elif "Windows Resource Protection found corrupt files and successfully repaired them" in output:
                return "Corrupted files were found and repaired successfully."
            elif "Windows Resource Protection found corrupt files but was unable to fix some of them" in output:
                return "Some corrupted files were found but could not be repaired."
        return "An unexpected error occurred during SFC scan."

    except Exception as e:
        return f"Error while running SFC: {e}"


def run_windows_defender():

    try:
        process = subprocess.Popen(
            ['powershell', '-Command', 'Start-MpScan -ScanType QuickScan'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        output, error = process.communicate()

        if process.returncode == 0:
            return "Quick scan completed. Check Windows Defender logs for details."
        else:
            return "An error occurred during the virus scan. Please check Windows Defender."

    except Exception as e:
        return f"Error while running Windows Defender: {e}"


def scan_system():

    root = tk.Tk()
    root.withdraw()  # Hide the main Tkinter window

    # Run SFC scan
    sfc_result = run_sfc()

    # Run Windows Defender scan
    defender_result = run_windows_defender()

    # Display results in a message box
    messagebox.showinfo("Scan Results", f"SFC Result:\n{sfc_result}\n\nWindows Defender Result:\n{defender_result}")


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

def drone():
    class DroneApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Drone Viewer")
            self.root.geometry("400x200")
            self.root.resizable(False, False)

            # IP Address Label and Entry
            self.ip_label = tk.Label(root, text="Drone IP Address:", font=("Helvetica", 12))
            self.ip_label.pack(pady=10)
            self.ip_entry = tk.Entry(root, width=30, font=("Helvetica", 12))
            self.ip_entry.pack(pady=5)

            # Start Button
            self.start_button = tk.Button(root, text="Start Drone Feed", command=self.open_drone, bg="green", fg="white", font=("Helvetica", 12))
            self.start_button.pack(pady=20)

        def open_drone(self):
            ip_address = self.ip_entry.get().strip()
            if not ip_address:
                messagebox.showerror("Error", "Please enter a valid IP address.")
                return

            url = f"http://{ip_address}:8080/shot.jpg"
            try:
                while True:
                    img_arr = np.array(bytearray(urllib.request.urlopen(url).read()), dtype=np.uint8)
                    img = cv2.imdecode(img_arr, -1)
                    cv2.imshow("Drone Feed", img)
                    q = cv2.waitKey(1)
                    if q == ord("q"):
                        break

                cv2.destroyAllWindows()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

    # Launch the GUI
    root = tk.Tk()
    app = DroneApp(root)
    root.mainloop()


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


def news():
    def fetch_news():
        city = city_entry.get().strip()
        if not city:
            messagebox.showerror("Error", "Please enter a city name.")
            return

        googlenews = GoogleNews()
        googlenews = GoogleNews("en", "d")

        googlenews.search(city)
        googlenews.getpage(1)

        global news_results
        news_results = googlenews.result()

        if news_results:
            news_text = "\n".join([article['title'] for article in news_results])
            news_display.config(state=tk.NORMAL)
            news_display.delete(1.0, tk.END)
            news_display.insert(tk.END, news_text)
            news_display.config(state=tk.DISABLED)
        else:
            messagebox.showinfo("No Results", "No news articles found for this city.")

    def read_news():
        if not news_results:
            messagebox.showinfo("No News", "No news to read. Please fetch news first.")
            return

        speak("Reading the news.")
        for article in news_results:
            speak(article['title'])

    # GUI Setup
    root = tk.Tk()
    root.title("News Fetcher")
    root.geometry("500x450")
    root.resizable(False, False)

    # City Input
    city_label = tk.Label(root, text="Enter City:", font=("Helvetica", 12))
    city_label.pack(pady=10)
    city_entry = tk.Entry(root, width=40, font=("Helvetica", 12))
    city_entry.pack(pady=5)

    # Fetch Button
    fetch_button = tk.Button(root, text="Fetch News", command=fetch_news, bg="blue", fg="white", font=("Helvetica", 12))
    fetch_button.pack(pady=10)

    # News Display
    news_display = tk.Text(root, width=60, height=15, font=("Helvetica", 10), state=tk.DISABLED)
    news_display.pack(pady=10)

    # Read News Button
    read_button = tk.Button(root, text="Read News", command=read_news, bg="green", fg="white", font=("Helvetica", 12))
    read_button.pack(pady=10)

    # Run the Application
    root.mainloop()



def pdf_reader():
    class PDFReaderApp:
        def __init__(self, root):
            self.root = root
            self.root.title("PDF Reader")
            self.root.geometry("500x300")
            self.root.resizable(False, False)

            self.pdf_path = None
            self.speaker = pyttsx3.init()
            self.is_paused = False

            # Title Label
            self.title_label = tk.Label(root, text="PDF Reader", font=("Helvetica", 16, "bold"))
            self.title_label.pack(pady=10)

            # Select PDF Button
            self.select_button = tk.Button(root, text="Select PDF", command=self.select_pdf, bg="blue", fg="white", font=("Helvetica", 12))
            self.select_button.pack(pady=10)

            # Start Reading Button
            self.start_button = tk.Button(root, text="Start Reading", command=self.start_reading, bg="green", fg="white", font=("Helvetica", 12), state=tk.DISABLED)
            self.start_button.pack(pady=10)

            # Pause Reading Button
            self.pause_button = tk.Button(root, text="Pause/Resume", command=self.toggle_pause, bg="orange", fg="white", font=("Helvetica", 12), state=tk.DISABLED)
            self.pause_button.pack(pady=10)

        def select_pdf(self):
            self.pdf_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
            if self.pdf_path:
                messagebox.showinfo("PDF Selected", f"Selected PDF: {self.pdf_path}")
                self.start_button.config(state=tk.NORMAL)
                self.pause_button.config(state=tk.NORMAL)

        def start_reading(self):
            if not self.pdf_path:
                messagebox.showerror("Error", "Please select a PDF first.")
                return

            try:
                with open(self.pdf_path, "rb") as book:
                    pdf_reader = PyPDF2.PdfFileReader(book)
                    pages = pdf_reader.numPages

                    for num in range(pages):
                        if self.is_paused:
                            self.speaker.stop()
                            while self.is_paused:
                                self.root.update()
                        page = pdf_reader.getPage(num)
                        text = page.extractText()
                        self.speaker.say(text)
                        self.speaker.runAndWait()

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

        def toggle_pause(self):
            self.is_paused = not self.is_paused
            if self.is_paused:
                self.speaker.pause()
                messagebox.showinfo("Paused", "Reading paused. Click again to resume.")
            else:
                self.speaker.resume()
                messagebox.showinfo("Resumed", "Reading resumed.")

    # Run the Application
    root = tk.Tk()
    app = PDFReaderApp(root)
    root.mainloop()



def send_email(sender_email, sender_password, recipient_email, subject, message):
    try:
        # Set up the server
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        
        # Log in to the email account
        server.login(sender_email, sender_password)
        
        # Create the email
        email = MIMEMultipart()
        email['From'] = sender_email
        email['To'] = recipient_email
        email['Subject'] = subject
        email.attach(MIMEText(message, 'plain'))
        
        # Send the email
        server.send_message(email)
        print("Email sent successfully!")
    
    except Exception as e:
        print(f"Failed to send email: {e}")
    
    finally:
        server.quit()
 
def gui_send_email():
    def send():
        sender = "othman.mohamed.1142005@gmail.com"
        password = "gkve qhih vwcm nsvv"  # App Password
        recipient = recipient_entry.get().strip()
        subject = ""  # Empty subject
        message = "This is a test email sent from Python."

        if not recipient:
            messagebox.showwarning("Input Error", "Recipient email is required.")
            return

        send_email(sender, password, recipient, subject, message)

    # GUI Setup
    root = tk.Tk()
    root.title("Send Email")
    root.geometry("400x200")

    tk.Label(root, text="Recipient Email:", font=("Helvetica", 12)).pack(pady=5)
    recipient_entry = tk.Entry(root, font=("Helvetica", 12), width=40)
    recipient_entry.pack(pady=5)

    send_button = tk.Button(root, text="Send Email", command=send, bg="green", fg="white", font=("Helvetica", 12))
    send_button.pack(pady=10)

    root.mainloop()
    
def get_username():
    # For Windows systems
    if os.name == 'nt':
        return os.environ.get('USERNAME')  # Fetches the username for Windows
    else:
        # For Unix-like systems (Linux/Mac)
        return os.environ.get('USER')  # Fetches the username for Linux/Mac

def find_app_in_common_dirs(app_name):
    username = get_username()  # Get the current username
    common_dirs = [f"C:\\Program Files",f"C:\\Program Files (x86)",f"C:\\Windows\\System32",f"C:\\Users\\{username}\\AppData\\Local",f"C:\\Users\\{username}\\AppData\\Roaming"]
    # Search through the common directories
    for dir in common_dirs:
        for root, dirs, files in os.walk(dir):
            if app_name.lower() in (file.lower() for file in files):  # Case-insensitive match
                return os.path.join(root, app_name)
    return None

def open_app(app_name):
    app_path = find_app_in_common_dirs(app_name)
    if app_path:
        try:
            # Open the app using the found path
            subprocess.run([app_path], check=True)
            print(f"{app_name} opened successfully!")
        except subprocess.CalledProcessError:
            print(f"Error: Failed to open {app_name}.")
    else:
        print(f"Error: {app_name} not found on this system.")

if __name__ == "__main__":
    clear = lambda: os.system("cls")
    clear()
    print(figlet_format("OTHMAN TECH", font = "big" ) )
    try:
        signin_signup()
    except Exception as e:
        speak("There is error try again please")
        messagebox.showerror("There is unkwon error try again please",f"Cannot start the program {e}")
    if access == True:
        wishMe()
        speak("Welcome Mister" + uname)
        speak("How can i Help you, Sir")
        while True:
            checkalarm()
            query = takeCommand().lower()
            # GREATINGS
            if "Good Morning" in query:
                speak("A warm morning")
                speak("How are you Mister" + uname)
                t = takeCommand()
                if ( t == "fine" or t == "good" or t == "well" or t == "i am fine" or t == "i am well" or t == "i am in my best conditions" or t == "never better" or t == "i was never better"):
                    speak("happy to know that sir")

            elif "Good Evening" in query:
                speak("Good Evening Sir")
                speak("How are you Mister" + uname)
                t = takeCommand()
                if (t == "fine" or t == "good" or t == "well" or t == "i am fine" or t == "i am well" or t == "i am in my best conditions" or t == "never better" or t == "i was never better"):
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
                
                start_date = date(2024,12,26)  
                today = date.today()
                delta = today - start_date
                speak(f"It has been {delta} days Since i have first run it means i have {delta/356} years")

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

            elif "redo" in query:
                pyautogui.keyDown("ctrl")
                pyautogui.press("y")
                pyautogui.keyUp("ctrl")

            elif "cut" in query:
                pyautogui.keyDown("ctrl")
                pyautogui.press("x")
                pyautogui.keyUp("ctrl")

            elif "open" in query:
                pyautogui.keyDown("ctrl")
                pyautogui.press("o")
                pyautogui.keyUp("ctrl")

            elif "refresh" in query:
                pyautogui.keyDown("ctrl")
                pyautogui.press("r")
                pyautogui.keyUp("ctrl")

            elif "fullscreen" in query:
                pyautogui.keyDown("f11")
                pyautogui.keyUp("f11")

            elif "new" in query:
                pyautogui.keyDown("ctrl")
                pyautogui.press("n")
                pyautogui.keyUp("ctrl")

            elif "open task manager" in query:
                pyautogui.keyDown("ctrl")
                pyautogui.keyDown("shift")
                pyautogui.press("esc")
                pyautogui.keyUp("shift")
                pyautogui.keyUp("ctrl")

            elif "toggle desktop" in query:
                pyautogui.keyDown("win")
                pyautogui.press("d")
                pyautogui.keyUp("win")
                
            elif "rename" in query:
                pyautogui.press("f2")
                
            elif "delete" in query:
                pyautogui.press("delete")
                
            elif "properties" in query:
                pyautogui.hotkey("alt", "enter")
               
            elif "magnifier" in query:
                pyautogui.hotkey("win", "+")
                 
            elif "narrator" in query:
                pyautogui.hotkey("win", "ctrl", "enter")
                
            elif "ease of access" in query:
                pyautogui.hotkey("win", "u")
               
            elif "new tab" in query:
                pyautogui.hotkey("ctrl", "shift", "t")
                 
            elif "close tab" in query:
                pyautogui.hotkey("ctrl", "w")
                
            elif "reopen tab" in query:
                pyautogui.hotkey("ctrl", "shift", "t")

            elif "minimize all windows" in query:
                pyautogui.keyDown("ctrl")
                pyautogui.keyDown("shift")
                pyautogui.press("esc")
                pyautogui.keyUp("shift")
                pyautogui.keyUp("ctrl")

            elif "create virtual desktop" in query:
                pyautogui.keyDown("ctrl")
                pyautogui.keyDown("win")
                pyautogui.press("d")
                pyautogui.keyUp("win")
                pyautogui.keyUp("ctrl")

            elif "close virtual desktop" in query:
                pyautogui.keyDown("ctrl")
                pyautogui.keyDown("win")
                pyautogui.press("f4")
                pyautogui.keyUp("win")
                pyautogui.keyUp("ctrl")

            elif "next desktop" in query:
                pyautogui.keyDown("ctrl")
                pyautogui.keyDown("win")
                pyautogui.press("right")
                pyautogui.keyUp("win")
                pyautogui.keyUp("ctrl")

            elif "previous desktop" in query:
                pyautogui.keyDown("ctrl")
                pyautogui.keyDown("win")
                pyautogui.press("left")
                pyautogui.keyUp("win")
                pyautogui.keyUp("ctrl")

            elif "find" in query:
                pyautogui.keyDown("ctrl")
                pyautogui.press("f")
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
                pyautogui.keyUp("alt")

            elif "lock screen" in query or "close" in query or "close it" in query:
                pyautogui.keyDown("win")
                pyautogui.press("l")
                pyautogui.keyUp("win")


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
                    20, 0, r"C:\Users\grand\OneDrive\Pictures\Saved Pictures\Iron Man", 0
                )
                speak("Background changed succesfully")

            elif "scan now" in query:
                speak("right now")
                scan_system()
                
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
                speak("Here you go to google find my device")
                webbrowser.open("https://www.google.com/android/find")

            elif "open google keep" in query:
                speak("Here you go to google keep")
                webbrowser.open("google keep.com")

            elif "open google one" in query:
                speak("Here you go to google one")
                webbrowser.open("google one.com")

            elif "open google ads" in query:
                speak("Here you go to google ads")
                webbrowser.open("google ads.com")

            elif "open google docs" in query:
                speak("Here you go to google docs")
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
                speak("Here you go to facebook")
                webbrowser.open("facebook.com")

            elif "open instgram" in query:
                speak("Here you go to insta")
                webbrowser.open("instgram.com")

            elif "open messenger" in query:
                speak("Here you go to messenger")
                webbrowser.open("messenger.com")

            elif "open whatsapp" in query:
                speak("Here you go to whatsapp")
                webbrowser.open("https://web.whatsapp.com")

            elif "open arduino web" in query:
                speak("Here you go to arduino")
                webbrowser.open("arduino web editor.com")

            elif "open stackoverflow" in query:
                speak("Here you go to Stack Over flow.Happy coding")
                webbrowser.open("stackoverflow.com")

            elif "open egybest" in query or "download movies" in query:
                speak("Here you go to egybest")
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
                sender = "othman.mohamed.1142005@gmail.com"
                password = "gkve qhih vwcm nsvv"  # Replace with your email password
                recipient = "graandtheifer5@gmail.com"
                speak("What do you want to send about")
                subject = takeCommand()
                speak("What do you want to say about")
                message = takeCommand()
                message = "This is a test email sent from Python."
                send_email(sender, password, recipient, subject, message)

            elif "send an email" in query:
                gui_send_email()
            # APPS
            elif "open app" in query:  #
                speak("Can you give the app name to me ")
                appName = takeCommand()
                appName = appName + ".exe"
                open_app(appName)
                
            # ROBOT CONTROLLER
            elif "Change IP" in query:
                nodemcu_gui()
                
            elif "send command" in query:
                speak("What do you want to send ?")
                command = takeCommand()
                IOT(command,nodemcu_ip)
                
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
                scan_bluetooth_devices()

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
                    drone()
                except:
                    pass

            elif "generate qr code" in query:  # done
                Run_QR()

            elif "show my saved wifi passwords" in query:  # done
                saved_wifi_passwords()

            elif "test my network speed" in query:
                s = speedtest.Speedtest()
                speak("what do you want to know ([1]upload[2]download\n[3]ping)")
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
                
            elif "Chemistry" in query:
                ChemicalEquation()
                
            elif "Physicis" in query:
                physicis_run()

            elif "tell me a joke" in query:
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)

            else:
                GoogleSearchBot().run()