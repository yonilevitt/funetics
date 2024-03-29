# This software is released under the MIT License.
# See the LICENSE file for details.

import tkinter as tk
from tkinter import scrolledtext, filedialog
import json,random,re,io,os
import threading

############################# Module Specific Stuff ###########################################
from gtts import gTTS
import pygame

# Initialize the mixer module
pygame.mixer.init()

# def speak(text):
#     # Create a gTTS object and convert text to audio
#     tts = gTTS(text)

#     # Store the audio data in memory
#     audio_data = io.BytesIO()
#     tts.write_to_fp(audio_data)

#     # Initialize the mixer module
#     pygame.mixer.init()

#     # Load the audio from memory
#     audio_data.seek(0)  # Reset the pointer
#     pygame.mixer.music.load(audio_data)

#     # Play the audio
#     pygame.mixer.music.play()

#     while pygame.mixer.music.get_busy():
#         pass  # Continue doing other tasks

#     # Wait for the audio to finish
#     pygame.mixer.music.set_endevent(pygame.USEREVENT)
    
audio_thread = None    
def speak(text):
    # Function to play audio in a separate thread
    global audio_thread
    
    if audio_thread is not None:
        if audio_thread.is_alive():
            print("Interrupting the sound...")
            pygame.mixer.music.stop()
    
    
    def play_audio():
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

        # Wait for the audio to finish
        pygame.mixer.music.set_endevent(pygame.USEREVENT)
        while pygame.mixer.music.get_busy():
            pass  # Continue doing other tasks

    # Create a thread and start playing audio in the background
    audio_thread = threading.Thread(target=play_audio)
    audio_thread.start()

    return audio_thread  # Return the thread object for later use

############################# Module Specific Stuff ###########################################   

import spelling_common as spelling
spelling.speak = speak
spelling.play_sound(f"Press the start button to begin the fun")
spelling.app.mainloop()
