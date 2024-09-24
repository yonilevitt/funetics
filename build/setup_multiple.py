# This software is released under the MIT License.
# See the LICENSE file for details.

from cx_Freeze import setup, Executable
import os,sys
from PIL import Image
import zipfile,shutil

ZIPME= False

# Change the working directory to the script's directory
BASE_PATH =  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(BASE_PATH)
sys.path.append(BASE_PATH)
sys.path.append(os.path.join(BASE_PATH,"src"))

baseline_script = os.path.join(BASE_PATH,"src","spelling_app.py")
hebrew_audio_script = os.path.join(BASE_PATH,"src","spelling_app_hebrew_audio.py")
offline_script = os.path.join(BASE_PATH,"src","spelling_app_offline.py")
nonverbal_script = os.path.join(BASE_PATH,"src","spelling_common.py")
output_path =  os.path.expanduser("~/Downloads/Funetics") #os.path.join(BASE_PATH,"precompiled","Funetics")

os.makedirs(output_path,exist_ok=True)

def create_ico_from_png(png_file, ico_file):
    img = Image.open(png_file)
    img.save(ico_file, format="ICO")

icon_png = os.path.join(os.path.dirname(__file__),"icon.png")    
icon_ico = os.path.join(os.path.dirname(__file__),"icon.ico")    

if not os.path.isfile(icon_ico):
    create_ico_from_png(icon_png,icon_ico)


excludes =  [
    "PyQt5",
    "PyQt4",
    "matplotlib","numpy","pandas","openpxl",
    "pytz","cryptography","OpenSSL","tcl8","tcl8.6",
    "jupyter_client","jupyter_core","arrow","polars",
    "jedi","jinja2","matplotlib_inline","ipkernel","IPython",
    "dill","colorama","debugpy"
    ]
includes =  ["tkinter","json","os","random","re","io","pyttsx3","gtts","pygame","threading"]           
packages = [
        'pyttsx3.drivers',
        'pyttsx3.drivers.dummy',
        'pyttsx3.drivers.espeak',
        'pyttsx3.drivers.nsss',
        'pyttsx3.drivers.sapi5',
        ]

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
            script=baseline_script,
            target_name="Funetics",
            base = ("Win32GUI" if sys.platform == "win32"  else None),
            icon= icon_ico            
            ),
        Executable(
            script=hebrew_audio_script,
            target_name="Funetics-Hebrew",
            base = ("Win32GUI" if sys.platform == "win32"  else None),
            icon= icon_ico            
            ),
        Executable(
            script=offline_script,
            target_name="Funetics-Offline",
            base = ("Win32GUI" if sys.platform == "win32"  else None),
            icon= icon_ico            
            ),
        Executable(
            script=nonverbal_script,
            target_name="Funetics-Nonverbal",
            base = ("Win32GUI" if sys.platform == "win32"  else None),
            icon= icon_ico            
            )
        ],
)

for (i,o) in [(os.path.join(BASE_PATH,"src","Spelling_Words"),"Spelling_Words"),(os.path.join(BASE_PATH,"src","GIFS"),"GIFS")]:
    if os.path.isdir(os.path.join(output_path,o)):
        shutil.rmtree(os.path.join(output_path,o))
    shutil.copytree(i,os.path.join(output_path,o))
    
if ZIPME:
    COMPILED = os.path.join(BASE_PATH,"precompiled")
    
    output_zip_file = os.path.join(COMPILED,'Funetics.zip')
    if os.path.exists(output_zip_file):
        os.remove(output_zip_file)

    directories = [output_path]
        
    # Create a new zip file or open an existing one in write mode
    with zipfile.ZipFile(output_zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for directory in directories:
            # Add the top-level directory itself to the zip file
            arcname = os.path.basename(directory)
            zipf.write(directory, arcname=arcname)

            # Walk through the directory and add its contents to the zip file
            for foldername, subfolders, filenames in os.walk(directory):
                for filename in filenames:
                    file_path = os.path.join(directory,foldername, filename)
                    arcname = os.path.relpath(file_path, COMPILED)
                    zipf.write(file_path, arcname=arcname)
                    
    for dir in directories:
        shutil.rmtree(dir)      