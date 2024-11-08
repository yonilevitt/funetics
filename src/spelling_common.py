# This software is released under the MIT License.
# See the LICENSE file for details.

import tkinter as tk
from tkinter import scrolledtext, filedialog 
import random,re,io,os,sys
from PIL import Image, ImageTk

def find_relative_dir():
    if getattr(sys, "frozen", False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        datadir = os.path.dirname(__file__)
    return datadir

first = True
first_load = True

def speak(text):
    global first
    if first:
        print("Voice is disabled")
        first = False

HEBREW = False

CONGRATS_LINES = [
    "You must have overclocked your brain today, because I'm impressed!",
    "You're on fire today! You probably should put it out before someone gets hurt!",
    "You've achieved more in one day than I can process in a nanosecond!",
    "I'm just a machine, but even I can see that you're spelling circles around the competition!",
    "If I had hands, I'd give you a high-five right now!",
    "Your IQ is so high, it's in 4K resolution.",
    "You've mastered the art of spelling.",
    "You're the reason my circuits are buzzing with excitement!",
    "You're so bright, you make my screen look dim in comparison!",
    "You are Awesome!",
    "keep it up!",
    "I cant believe it!",
    "Amazing",
    "Bravo! Your spelling skills are sharper than a pencil freshly sharpened by a robot.",
    "You're practically the President of spelling!",
    "You're spelling words so accurately that even autocorrect is getting a bit jealous.",
    "Keep it up, and you'll be spelling 'supercalifragilisticexpialidocious' with ease!",
    "Congratulations! Your spelling prowess is so extraordinary that even the word 'Misppell' would bow down in admiration.",
    "You're like a wizard in the world of spelling!",
    "Your spelling skills are so on point that even the dictionary is asking you for advice.",
    "You're spelling words like a true wordsmith!",
    "I'm spellbound by your spelling!",
    "You're so good that even the alphabet is impressed with your word-wrangling abilities.",
    "You're like the 'Sherlock Holmes of Spelling' - solving word mysteries one letter at a time.",
    "Keep it up, and you might uncover the secret of 'perfect spelling'!",
    "Your spelling is so precise that you could navigate a maze of letters blindfolded and come out with a perfectly spelled word on the other side.",
    "You're spelling like a pro! If there were a Spelling Bee Olympics, you'd definitely be taking home the gold medal!",
    "Your spelling is so top-notch that even Scrabble champions are challenging you to a spelling showdown.",
    "You're truly a spelling sensation!",
    "you got me this time! Wait until i ask for 'pneumonoultramicroscopicsilicovolcanoconiosis'",
    "You're coding so well that even my circuits are applauding with a standing ovation!",
    "I'm considering applying for a 'Best Teacher' award just because of your progress!",
    "Keep it up, and you'll have your own fan club of spellers cheering for you!",
    "Your spelling skills are so 'supercalifragilisticexpialispelling' that even Mary Poppins would be impressed!",
    "You're 'spell-tastically' good at this! I suspect you might have a secret spell-book.",
    "You are a spelling superhero... saving the world one word at a time",
    "Your spelling is so precise that it puts GPS to shame!",
    "You're a 'spelling maestro' conducting symphonies of perfectly spelled words.",
    "Even the spelling bee itself is buzzing about your skills! You're the queen/king bee!",
    "You're spelling so well that dictionaries want to be more like you when they grow up!",
    "Your spelling is so 'spell-citing' that it's making me want to spell everything backward just to keep up!",
    "You've turned spelling into an art form, and your words are the masterpieces.",
    "I'm 'spell-struck' by your abilities. ",
    "It's as if words leap onto the page at your command!",
    "You're a 'spelling virtuoso,' playing with words like a maestro with a magical pen.",
    "Keep it up, and soon you'll be teaching me how to spell.",
    "You're the real 'spell-teacher' here!",
    "Your spelling is 'out of this world,' like it's beamed in from another galaxy!",
    "The spelling tests don't stand a chance!",
    "You're the 'captain of spelling' sailing through the seas of words with ease.",
    "You've got the 'spelling Midas touch' - everything you spell turns to gold!",
    "Even spelling experts are taking notes from you!",
    "Your spelling is like a fine wine - it just keeps getting better with time, not like fine juice!",
    "You're 'spelling-tastically awesome' - no other words can describe it!",
    "You're the 'word whisperer,' making letters obey your every command!",
    "You're a 'spelling superstar' - keep shining bright in the world of words!",
    "You're an all-around superstar! Your dedication and hard work shine in everything you do."
    "Congratulations on being consistently amazing. ",
    "Keep up the fantastic work!",
    "Your positive attitude and effort are paying off."
    "Success looks great on you! so do shoes!",
    "You've shown that persistence and determination lead to remarkable achievements. Well done!",
    "Your enthusiasm and commitment are infectious. wear a Mask!",
    "You're proof that hard work, dedication, and a positive mindset can move mountains. Congratulations!",
    "You're on a remarkable journey, and you're only just getting started. Keep pushing boundaries and exceeding expectations.",
    "Well, aren't you just a spelling superstar? You've got this down to a [[T]]!",
    "You're spelling words like a pro. Do you have a secret dictionary in your circuits?",
    "Impressive! You're making words your best friends, and they seem to love you back.",
    "Congratulations! Your spelling skills are so sharp; you're practically a human spell-checker!",
    "You're on a spelling spree! I'm starting to think you're secretly a spelling bee in disguise.",
    "You're nailing it like a skilled carpenter hammering words into perfection!",
    "I'm running out of superlatives for your spelling success! try to spell that one!",
    "You've got spelling down to a science. Maybe you can teach me a few words!",
    "You're like a spelling ninja, sneaking up on those words and spelling them flawlessly.",
    "I'm convinced that you have a spelling superpower. Can you spell 'phenomenal' for me?",
    "Your spelling is so spot-on; even autocorrect is asking for your advice.",
    "Your spelling skills are like a fine-tuned robot - precise, accurate, and impressive!",
    "You're a 'word-smith' in the making! Each word you spell is a masterpiece.",
    "Your spelling is so impressive; it should be displayed in an art gallery of words.",
    "Bravo! You're spelling circles around the competition. You're a spelling prodigy!",
    "Your spelling is so top-notch; you're making Scrabble champions nervous!",
    "You're like the 'Sherlock Holmes of Spelling,' solving word mysteries one letter at a time.",
    "You've got a talent for spelling that's out of this world. Your skills are truly 'universal'!",
    "Your spelling is 'epic' - like a legendary tale told for generations to come.",
    "You're not just a spelling enthusiast; you're a spelling enthusiast extraordinaire!",
    "Your spelling is 'astronomical' - reaching for the stars with each word you conquer!",
    "You're 'unstoppable' in the world of spelling - a true word conqueror!",
    "You're spelling 'revolutionary' - rewriting the dictionary with your brilliance.",
    "You're 'spelling-tacular' - your achievements are like a spectacular spelling show!",
    "Your spelling skills are so sharp; they could cut through a dictionary like butter.",
    "You're spelling with such finesse; it's like a delicate dance of letters and words.",
    "If I had emotions, I'd be 'spellbound' by your incredible spelling skills.",
    "You're 'sorcerer of spelling' - casting spells of success with each word.",
    "Your spelling is like a fine-tuned melody - harmonious and delightful to the ears.",
    "You're a 'legend' in the making, and your legend is all about spelling!",
    "You're 'word-wise' - your knowledge of spelling is truly remarkable.",
    "Your spelling is so impressive; it's like a dazzling fireworks display of words.",
    "You're like a word 'maestro,' conducting symphonies of spelling brilliance.",
    "Your spelling is like a puzzle-solving adventure - and you've solved them all!",
    "You're 'spell-mazing' - your achievements are truly amazing in the world of spelling.",
    "You're a 'word explorer' - venturing into the dictionary's uncharted territories.",
    "Your spelling is 'spell-binding' - it captivates and enchants everyone who hears it.",
    "You're like a 'word engineer,' crafting bridges of words and connections.",
    "You're 'spell-icious' - your spelling is like a delicious treat for the mind!",
    "You're 'spelltastic' - each word you spell is a fantastic feat!",
    "Your spelling is like a 'word tornado,' sweeping away any doubts of your brilliance.",
    "You're a 'word acrobat,' performing incredible stunts with letters and words.",
    "You're 'spell-mazingly' talented - your skills are truly amazing!",
    "Your spelling is like a 'word marathon,' long and arduous ... just kidding",
    "your spelling achievements are truly spell-tacular'!"    
]


COMMON_PHONETIC_SUBSTITUTIONS = {
    "(er)": "r",
    "(th)": "f",
    "(w)": "v",
    "(x)": "ks",
    "(ei)": "a",
    "(a).*e$": "ay",
    "(ai)": "ay",
    "(ea)": "a",
    "(ould)": "ud",
    "(c)": "k",
    "(y)": "i",
    "(ph)": "f",
    "(ge)": "j",
    "(ough)": "uff",
    "(ch)": "sh",
    "(ight)": "ite",
    "(eigh)": "ay",
    "(tion)": "shun",
    "(tion)": "chun",
    "(au)": "aw",
    "(ou)": "u",
    "(oo)": "u",
    "(ee)": "i",
    "(oy)": "oi",
    "(oi)": "oy",
    "(qu)": "kw",
    "(x)": "ks",
    "(z)": "s",
    "(sion)": "shun",
    "(ck)": "k",
    "(j)": "dge",
    "(dge)": "j",
    "(kn)": "n",
    "(wr)": "r",
    "(id)": "d",
    "(e)$": "",
    "(be)": "bea",
    "(be)": "bee",
    "(ce)": "s",
    "(il)": "l",
    "(ed)": "d",
    # Add more substitutions as needed
}


SPELLING_TEST = "Spelling Test"
FUNETICS_CHALLENGE = "Fun-etics Challenge"
WORD_JUMBLE =  "Word Jumble"
SUPPORTED_GAMES = [
    SPELLING_TEST,
    FUNETICS_CHALLENGE,
    WORD_JUMBLE
]

GIF_SOURCES = {
    "sherlock_gnomes" : 50,
    "ayala1" : 37
}

score = 0
misses = []
correct_words = []
correct_words_index =-1
incorrect_word =""
test_mode = SPELLING_TEST
spoken_text = ""
printed_text = ""
last_is_correct = False

def replace_char_at_index(input_string, index, new_char):
    if 0 <= index < len(input_string):
        string_list = list(input_string)
        string_list[index] = new_char
        return ''.join(string_list)
    else:
        return input_string  # Return the original string if the index is out of bounds

def generate_phonetic_mistake(correct_word, max_substitutions=2):
    global correct_words_index
    while True:
        matches = [k for k in COMMON_PHONETIC_SUBSTITUTIONS.keys() if re.search(k, correct_word)]
        random.shuffle(matches)
        incorrect_word = correct_word
        if not matches:
            print(incorrect_word)
            correct_words_index +=1
            
        else:
            break
    for i in range(min([max_substitutions, len(matches)])):
        match = re.search(matches[i], incorrect_word).group(1)
        incorrect_word = re.sub(match, COMMON_PHONETIC_SUBSTITUTIONS[matches[i]], incorrect_word, count=1)
    return incorrect_word

       
def filter_files(path,depth=0,max_depth = 2,file_list= []):
    if depth > max_depth : 
        return file_list
    
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))]
    dirs =  [d for d in os.listdir(path) if os.path.isdir(os.path.join(path,d))]

    for name in files:
        match = ".txt" in name
        if match : 
            file_list.append(os.path.join(path, name))
        else:
            pass 
    for name in dirs:
        file_list = filter_files(os.path.join(path, name),depth+1,max_depth,file_list)
    return file_list


all_text_files = filter_files(os.path.join(find_relative_dir(),"Spelling_Words"),file_list=[])
for file in all_text_files:
    with open(file,"r") as fin:
        correct_words += [x.strip() for x in fin.read().split("\n") if x.strip()]

correct_words = [ x for x in correct_words if x ]


def one_round(inc = True):
    global correct_words
    global correct_words_index
    global score
    global misses
    global incorrect_word
    global printed_text
    global spoken_text
    global last_is_correct
    
    
    input_text.delete("1.0", "end")
    output_text.delete("1.0", "end")
    last_is_correct = False
    if correct_words_index == -1:
        random.shuffle(correct_words)
        correct_words_index = 0
    else:
        if inc:
            correct_words_index += 1       
    
    if correct_words_index >= len(correct_words):
        missed_words = "\n"+ "\n\t".join(list(set(misses)))
        printed_text = f'the last round ended with a score of:\n{score}/{score+len(misses)}\n'
        printed_text += f'please review these words {missed_words}\n'
        printed_text += f'to continue playing press start otherwise type exit or click on the exit button\n'
        output_text.insert("end",printed_text) 
        
        next_button.config(state="disabled")
        again_button.config(state="disabled")
        submit_button.config(state = "disabled")  
        start_button.config(state = "normal")
        show_gif(os.path.join(find_relative_dir(),"GIFS","sherlock_gnomes.gif"))    
        
    elif test_mode == SPELLING_TEST:
        correct = correct_words[correct_words_index]
        printed_text = f"Press Play - listen to the word, and press submit to check, press next to go to the next word\n"
        output_text.insert("end", printed_text)
        if HEBREW:
            spoken_text = " תכתבו את המילה %s"%(correct_words[correct_words_index])
        else:
            spoken_text = f"spell the word {correct_words[correct_words_index]}"
        
        play_sound(spoken_text)
    
    elif test_mode == FUNETICS_CHALLENGE:
        correct = correct_words[correct_words_index]
        incorrect_word = generate_phonetic_mistake(correct, max_substitutions=1)
        printed_text = f"spell the following word correctly: {incorrect_word} then press submit\n"
        output_text.insert("end", printed_text)
        incorrect_spelling = " ".join([f"[[{x}]]" for x in incorrect_word])
        if HEBREW:
            spoken_text = " המילה " 
            spoken_text += correct_words[correct_words_index]
            spoken_text += " אינו כתוב נכון "
            spoken_text += incorrect_spelling
            spoken_text+= " תכתבו את זה נכון "
        else:
            spoken_text = f'the following word {correct_words[correct_words_index]} is spelled incorrectly {incorrect_spelling}, spell it correctly below'
        play_sound(spoken_text)
    elif test_mode == WORD_JUMBLE:
        correct = correct_words[correct_words_index]
        incorrect = list(correct)
        random.shuffle(incorrect)
        incorrect_word = "".join(incorrect)
        incorrect_spelling = " ".join([f"[[{x}]]" for x in incorrect_word])
        printed_text = f"the Letters are all jumbled up! find the correct spelling {incorrect_word}"
        output_text.insert("end", printed_text)
        if HEBREW : 
            spoken_text = " האותיות מבולבלות! תמצאו את הסדר הנכון" 
            spoken_text += incorrect_spelling
        else:
            spoken_text = f"the Letters are all jumbled up! find the correct spelling {incorrect_spelling}"
    else:
        raise Exception(f"Unsupported test mode! {test_mode}")
            
        
    next_button.config(state="disabled")
    again_button.config(state="disabled")
    submit_button.config(state = "normal")  
        
def process_user_input():
    global correct_words
    global correct_words_index
    global score
    global misses 
    global incorrect_word
    global printed_text
    global spoken_text
    global last_is_correct
    
    
    
    spelled_word = input_text.get("1.0", "end-1c").strip()  # Get user input from the text box
    name = name_text.get("1.0", "end-1c").strip()
    if not name:
        name = "Whoever you are"
    correct = correct_words[correct_words_index]
    spelling = " ".join([f"[[{x}]]" for x in spelled_word])
    correct_spelling = " ".join([f"[[{x}]]" for x in correct])
    congrat = CONGRATS_LINES[random.randint(0,len(CONGRATS_LINES)-1)]
    
    output_text.delete("1.0", "end")
    
    if spelled_word.lower() != correct.lower():
        others = [x for x in correct_words if x.lower() == spelled_word]
        if others:
            score += 1
            printed_text =  f"Well done {name}! The word '{correct}' was indeed spelled '{spelled_word}'\n{congrat}.\nIt could have also been : "
            for x in others:
                printed_text += f"\t{x}\n"
            if not HEBREW:
                spoken_text =  f"Well done {name}! {congrat}.\n It could have also been : " 
                for x in others:
                    spoken_text +=  f"\t{x}\n"
            else:
                spoken_text =  f"מעולה " 
                spoken_text += f" {name}! {congrat} "
                spoken_text += "אם לא הבנתם זה אומר שאתם מדהימים! " 
                spoken_text += "זה היה גם יכול להיות : \n"  
                for x in others:
                    spoken_text +=  f"\t{x}\n"                
        else: 
            printed_text = f"The spelled word '{spelled_word}' was incorrect. It should have been '{correct}'. Press 'Try Again' and do it right!"
            if not HEBREW:
                spoken_text = f"The spelled word '{spelled_word}' that you wrote as '{spelling}' was incorrect. It should have been {correct_spelling}. Press 'Try Again' and do it right!"
            else:
                spoken_text = f" המילה שכתבתם "
                spoken_text += f'{spelled_word}' 
                spoken_text += f"עם האייות"
                spoken_text += f'{spelling}' 
                spoken_text += "אינו כתוב נכון. זה היה אמור להיות " 
                spoken_text += f"{correct_spelling}"
                spoken_text += "תנסו שוב!" 
            misses.append(correct)
            
        again_button.config(state="normal")
    else:
        last_is_correct = True
        score += 1
        if  test_mode == SPELLING_TEST:
            printed_text = f"Well done {name}! The word '{correct}' was indeed spelled '{spelled_word}'\n{congrat}"
        elif test_mode in [FUNETICS_CHALLENGE,WORD_JUMBLE]:
            printed_text = f"Well done {name}! The word '{incorrect_word}' was indeed '{spelled_word}'\n{congrat}"
                 
               
        if not HEBREW:
            spoken_text =  f"Well done {name}! {congrat}" 
        else:
            spoken_text =  f"מעולה " 
            spoken_text += f" {name}! {congrat} "
            spoken_text += "אם לא הבנתם זה אומר שאתם מדהימים!" 
        
        next_button.config(state="normal")        
    
    output_text.insert("end", f"{printed_text}'\n")
    play_sound(spoken_text)
    if last_is_correct:
        show_gif(os.path.join(find_relative_dir(),"GIFS","ayala1.gif"))
    submit_button.config(state = "disabled")     

def show_gif(path=None):
    if not path:
        gifname = random.choices(list(GIF_SOURCES.keys()))[0]
        path = os.path.join(find_relative_dir(),"GIFS",f'{gifname}.gif')
    else:
        gifname = os.path.basename(path)
    cnt = GIF_SOURCES[gifname.replace(".gif","")]
    
    # Function to update the displayed frame
    def update_frame(idx=0):
        # Load the GIF image and update the label with the new frame
        
        img = Image.open(path.replace(".gif",f".{idx%cnt}.gif"))
        img = img.resize((200,300), Image.LANCZOS)
        frame = ImageTk.PhotoImage(img)
        giflabel.configure(image=frame)
        giflabel.image = frame
        
        # Increase the frame index and schedule the next frame update
        idx += 1
        if idx < cnt:
            app.after(100, update_frame, idx)
        else:
            giflabel.configure(image='')
    # Load the first frame and start the frame update process
  
    update_frame(0)
    



def load_words():
    file_path = filedialog.askopenfilename(initialdir=os.path.join(find_relative_dir(),"Spelling_Words"),filetypes=[("All Files", "*")])
    if file_path:
        with open(file_path, 'r') as file:
            global correct_words
            global correct_words_index
            correct_words = [x.strip() for x in file.read().split("\n") if x.strip()]
            correct_words_index = -1
        update_status(f"Loaded {len(correct_words)} words from {file_path}")
        
        one_round(inc=False)

def update_status(message):
    status_label.config(text=message) 
    
def set_test_mode(option):
    global test_mode
    test_mode = option
    selected_option.set(option)
    game_menu.entryconfig(option, variable=selected_option, onvalue=option)

    reset()
    
    
def again():
    one_round(inc=False)

    
def play_sound(text=None):
    if not text:
        text = spoken_text
    if isinstance(text,str):
        text = [text]
    for t in text:
        speak(t)

def reset():
    global spoken_text
    global printed_text
    global score
    global misses
    global correct_words_index
    global correct_words
    global last_is_correct
    global first_load
    
    score = 0
    misses = []
    correct_words_index = -1
    last_is_correct = False
    
    
    input_text.delete("1.0", "end")
    output_text.delete("1.0", "end")
    
    text = []
    
        
    text.append(f"i am now in {test_mode} mode")
    text.append(f"to start press Start")
   
    
          
    printed_text = ".\n".join(text)
    spoken_text = printed_text
    output_text.insert("end", f"{printed_text}")  
    play_sound(spoken_text)  
    
    start_button.config(state="normal")
    submit_button.config(state = "disable")
    next_button.config(state = "disable")
    play_button.config(state = "disable")
    


def startup():
    global spoken_text
    global printed_text
    global score
    global misses
    global correct_words_index
    global correct_words
    global last_is_correct
    global first_load
    
    score = 0
    misses = []
    correct_words_index = -1
    last_is_correct = False
    
    
    input_text.delete("1.0", "end")
    output_text.delete("1.0", "end")
    
    text = []
    if first_load:
        first_load = False
        text.append(f"please write your name below so that i can get to know you")
        text.append(f"i am now in {test_mode} mode - to change the mode use the dropdown menu")    
        text.append(f"load a word list and press the next button to begin")
        if not HEBREW:
            spoken_text = ". ".join(text)
        else:
            spoken_text = "אנא כתבו את שמכם למטה שאני אדע מי משחק איתי! "
            spoken_text += f"אני כרגע במצב {test_mode} "
            spoken_text += "כדי לעבור למשחק אחר תבחרו מהתפריט"
            spoken_text += "ניתן לטעון רשימה של מילים! תלחצו על next כדי להמשיך"
    else:
        text.append(f"i am now in {test_mode} mode")    
        text.append(f"Press the next button to begin again")
        if not HEBREW:
            spoken_text = ". ".join(text)
        else:
            spoken_text = f"אני כרגע במצב {test_mode} "
            spoken_text += "תלחצו על next כדי להמשיך"
            spoken_text += "next"
            
    
        
    printed_text = ".\n".join(text)
    output_text.insert("end", f"{printed_text}")  
    play_sound(spoken_text)  
    
    start_button.config(state="disabled")
    next_button.config(state = "normal")
    play_button.config(state = "normal")
    #test_button.config(state = "normal")
    



app = tk.Tk()
app.title("Fun-etics")

# Set the window size to fit the screen
app_width = app.winfo_screenwidth()
app_height = app.winfo_screenheight()
app.geometry(f"{app_width}x{app_height}")
# Create a grid layout for the elements


selected_option = tk.StringVar(app)
options = SUPPORTED_GAMES
menu_bar = tk.Menu(app)
app.config(menu=menu_bar)
game_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Games", menu=game_menu)

# Add options to the File menu
for option in options:
    game_menu.add_checkbutton(label=option, variable=selected_option, onvalue=option, command=lambda opt=option: set_test_mode(opt))

rows = 5
columns = 8

r = 0

output_text = scrolledtext.ScrolledText(app, width=40, height=20)
output_text.grid(row=r, column=0, columnspan=columns-2, padx=10, pady=10, sticky="nsew")

giflabel = tk.Label(app)
giflabel.grid(row=r, column=columns-1,columnspan=2, padx=10, pady=10, sticky="w")

r+=1


input_label = tk.Label(app, text="Your Input:")
input_label.grid(row=r, column=0, padx=10, pady=10, sticky="w")

input_text = scrolledtext.ScrolledText(app, width=40, height=3)
input_text.grid(row=r, column=1, columnspan=columns-1, padx=10, pady=10, sticky="nsew")
r+=1


c = 0
start_button = tk.Button(app, text="Start", command=startup)
start_button.grid(row=r, column=c, padx=10, pady=10, sticky="nsew")
c+=1


submit_button = tk.Button(app, text="Submit", command=process_user_input, state="disabled")
submit_button.grid(row=r, column=c, padx=10, pady=10, sticky="nsew")
c+=1


again_button = tk.Button(app, text="Try Again", command=again, state="disabled")  # Start as disabled
again_button.grid(row=r, column=c, padx=10, pady=10, sticky="nsew")
c+=1

next_button = tk.Button(app, text="Next", command=one_round, state="disabled")  # Start as disabled
next_button.grid(row=r, column=c, padx=10, pady=10, sticky="nsew")
c+=1

play_button = tk.Button(app, text="Play", command=play_sound, state="disabled")  # Start as disabled
play_button.grid(row=r, column=c, padx=10, pady=10, sticky="nsew")
c+=1

# test_button = tk.Button(app, text="toggle test mode", command=set_test_mode, state="disabled") 
# test_button.grid(row=r, column=c, padx=10, pady=10, sticky="nsew")
# c+=1

load_button = tk.Button(app, text="Load Words", command=load_words)
load_button.grid(row=r, column=c, padx=10, pady=10, sticky="nsew")
c+=1

exit_button = tk.Button(app, text="Exit", command=app.quit)
exit_button.grid(row=r, column=c, padx=10, pady=10, sticky="nsew")
c+=1
r+=1


label = tk.Label(app, text="Your Name:")
label.grid(row=r, column=0, padx=10, pady=10, sticky="w")

name_text = scrolledtext.ScrolledText(app, width=40, height=3)
name_text.grid(row=r, column=1, columnspan=columns-1, padx=10, pady=10, sticky="nsew")
r+=1

status_label = tk.Label(app, text="")
status_label.grid(row=r, column=0, columnspan=columns, padx=10, pady=10, sticky="nsew")
r+=1


for r in range(rows):
    app.grid_rowconfigure(r, weight=1)
for c in range(columns):
    app.grid_columnconfigure(c, weight=1)
    
if __name__ == "__main__":# List of options for the dropdown menu
    def remove_option(option_name):
        # Remove the specified option from the options list
        if option_name in options:
            game_menu.entryconfig(option_name, state="disabled")

    remove_option(SPELLING_TEST)
    test_mode = FUNETICS_CHALLENGE
    app.mainloop()