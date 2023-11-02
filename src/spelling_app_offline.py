# This software is released under the MIT License.
# See the LICENSE file for details.

import tkinter as tk
from tkinter import scrolledtext, filedialog
import json,random,re,io,os

############################# Module Specific Stuff ###########################################
import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate')  # Get the current speech rate (words per minute)
engine.setProperty('rate', 120)  # Set a new speech rate (e.g., 150 words per minute for slower speech)

def speak(text):
    engine.say(text)
    engine.runAndWait()

############################# Module Specific Stuff ###########################################   

import spelling_common as spelling
spelling.speak = speak
spelling.play_sound(f"Press the start button to begin the fun")
spelling.app.mainloop()
