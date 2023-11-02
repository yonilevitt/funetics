# This software is released under the MIT License.
# See the LICENSE file for details.

import tkinter as tk
from tkinter import scrolledtext, filedialog
import json,random,re,io,os

if __name__ == "__main__":
    # Change the working directory to the script's directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))


############################# Module Specific Stuff ###########################################
from gtts import gTTS
import pygame

# Initialize the mixer module
pygame.mixer.init()

def speak(text):
    # Create a gTTS object and convert text to audio
    tts = gTTS(text)

    # Store the audio data in memory
    audio_data = io.BytesIO()
    tts.write_to_fp(audio_data)

    # Initialize the mixer module
    pygame.mixer.init()

    # Load the audio from memory
    audio_data.seek(0)  # Reset the pointer
    pygame.mixer.music.load(audio_data)

    # Play the audio
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pass  # Continue doing other tasks
    # Wait for the audio to finish
    pygame.mixer.music.set_endevent(pygame.USEREVENT)

############################# Module Specific Stuff ###########################################   

import spelling_common as spelling
spelling.speak = speak
spelling.play_sound(f"Press the start button to begin the fun")
spelling.app.mainloop()
