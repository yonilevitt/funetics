import os,sys,subprocess
import shutil
import zipfile

# Change the working directory to the script's directory
BASE_PATH =  os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_PATH)
scripts = [
    "setup.py",
    "setup_nonverbal.py",
    "setup_offline.py",
    "setup_hebrew_audio.py",
]

for script in scripts:
    cmdline = f"python {script} build"
        
    print(f'running {cmdline}')
        
    return_code = subprocess.run(cmdline,shell=True).returncode
    if return_code != 0:
        print(f"the run with {cmdline} failed - continuing on")
        exit(0)

COMPILED = os.path.join(os.path.dirname(BASE_PATH),"precompiled")
output_zip_file = os.path.join(COMPILED,'Funetics.zip')
if os.path.exists(output_zip_file):
    os.remove(output_zip_file)


directories = [os.path.join(COMPILED,x) for x in os.listdir(COMPILED) if ("Funetics" in x) and not ("zip" in x)]
for i in directories:
    if not os.path.isdir(i):
        raise Exception(i)    

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
    
        