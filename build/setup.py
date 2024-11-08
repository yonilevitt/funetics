# This software is released under the MIT License.
# See the LICENSE file for details.

from cx_Freeze import setup, Executable
import os,sys
from PIL import Image

# Change the working directory to the script's directory
BASE_PATH =  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_PATH)
os.chdir(BASE_PATH)
sys.path.append(BASE_PATH)
sys.path.append(os.path.join(BASE_PATH,"src"))

script = os.path.join(BASE_PATH,"src","spelling_app.py")
output_path =  os.path.join(BASE_PATH,"precompiled","Funetics")
if "offline" in script:
    output_path += " Offline"
elif "hebrew" in script:
    output_path += " Hebrew"
elif "common" in script:
    output_path += " Non Verbal"

os.makedirs(output_path,exist_ok=True)
#os.chdir(output_path)


def create_ico_from_png(png_file, ico_file):
    img = Image.open(png_file)
    img.save(ico_file, format="ICO")

icon_png = os.path.join(os.path.dirname(__file__),"icon.png")    
icon_ico = os.path.join(os.path.dirname(__file__),"icon.ico")    

if not os.path.isfile(icon_ico):
    create_ico_from_png(icon_png,icon_ico)


excludes =  ["PyQt5","PyQt4","matplotlib","numpy","pytz","pandas","openpxl","cryptography","OpenSSL","tcl","tcl8.6"]
includes =  ["tkinter","json","os","random","re","io","threading"]           
packages = []

if ("common" in script):
    excludes +=["gtts","pygame","email","http","html","pyttsx3"]  
elif "offline" in script:
    includes+= ["pyttsx3"]
    excludes+=["gtts","pygame","email","http","html"]
    packages += [
        #'spelling_app_offline',
        'pyttsx3.drivers',
        'pyttsx3.drivers.dummy',
        'pyttsx3.drivers.espeak',
        'pyttsx3.drivers.nsss',
        'pyttsx3.drivers.sapi5',
    ]
else:
    includes+=["gtts","pygame"]
    excludes+= ["pyttsx3"]

setup(
    name="Funetics",
    version="1.0",
    description="A spelling App to help practice spelling tests and phonetic spelling problems",
    options={
        "build_exe": {
               # "include_files" : [(os.path.join("src","Spelling_Words"),"Spelling_Words"),(os.path.join("src","GIFS"),"GIFS")],
                "includes" : includes,
                "excludes":  excludes,
                "packages" : packages,
                "include_msvcr": True,
                "optimize":2,
                "build_exe" : output_path
            }
        },
    executables=[
        Executable(
            script=script,
            target_name="Funetics",
            base = ("Win32GUI" if sys.platform == "win32"  else None),
            icon= icon_ico            
            )
        ],
)