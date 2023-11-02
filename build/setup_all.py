import os,sys,subprocess

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

        
    
        