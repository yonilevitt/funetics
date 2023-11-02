# funetics
A Fun and helpful Spelling program to allow children to practice spelling as well as help with phonetic misspelling issues
the name is a good way to describe the program - a spelling app targeted to phonetically similar words.

Funetics is a Windows GUI based program that has 2 modes : 
1.  spelling Bee - test out the spelling prowess of a child on a list of words
2.  the Phonetic Challenge -  a fun game where a word is purposely spelled wrong in a phonetically similar fashion the child must figure out the correct spelling based the the list of words available.

any list of words can be loaded. the format required for this is a Json List.
the contents of the file should look like : 
[
    "word1",
    "word2",
    ...
    "wordn"
]
the list may be loaded by pressing the load button in the gui


positive reinforcement is given through funny comments when a student gets the question correct.
the supported languages are hebrew and english.

the base here is Windows - no effort has been done to support other platforms

-   precompiled
    - for the basic distribution purposes i have supplied a precompiled version. 
      - in the folder precompiled there is a Zip file - copy it anywhere on your computer, unzip it and let the funetics begin!


- build
    -   either build all the flavors
        -   python setup_all.py

    -   or you can run individually :
        -   python setup.py build
        -   python setup_offline.py build
        -   python setup_nonverbal.py build
        -   python setup_hebrew_audio.py build

    -   the required packages beyond the baseline are : 

        -   pip install pygame
        -   pip install gtts
        -   pip install pyttsx3
        -   pip install cx_Freeze

