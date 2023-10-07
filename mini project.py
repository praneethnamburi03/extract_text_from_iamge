#duplicate
#color changed
import cv2
#import pytesseract
from tkinter import *
from tkinter import filedialog
from PIL import Image
from pytesseract import pytesseract
from autocorrect import Speller
from iso639 import Lang
from deep_translator import *
from googletrans import Translator
def upload():
    try:
        global path  
        path=""
        path=filedialog.askopenfilename()
        #print(path)
        #image=Image.open(path)
        #img=ImageTk.PhotoImage(image)
        #uploaded_img.configure(image=img)
        #uploaded_img.image=img
        #uploadbtn.config(state="disabled")
        
    except Exception:
        #path="C:\whatsapp images\englishquote.jpg"
        root.destroy()
        

def show_extract_button(path,language):
    if(path==""):
            path="C:\project\images\sample.jpg"
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    pytesseract.tesseract_cmd = path_to_tesseract
    root.destroy()
    root1=Tk()
    root1.configure(bg='#283149')
    root1.geometry("600x600")
    spell = Speller(lang='en')
    try:
        language1 = spell(language)
        lg = Lang(language1.capitalize())
        language1  = lg.pt3
    except Exception:
        language1 = spell("English")
        lg = Lang(language1.capitalize())
        language1  = lg.pt3
    img = Image.open(path)
    #img = cv2.imread(path)
    global text
    text = pytesseract.image_to_string(img, lang=language1)
    #Label(root1,text=text[:-1],font=('arial',20)).pack()
    T = Text(root1, height=15, width=75, font=("Arial", 15), bg='white', fg='black', selectbackground='blue',
                 selectforeground='yellow')
    T.insert(END, text[:-1]) #inserts the text into text box
    T.place(x=0,y=50)
    global variable
    
    '''variable = StringVar(root1) # a variable which to store language
    variable.set("Select Any Language") 
    lanuages=["English", "Hindi","Telugu","French","Arabic"]  # language list
    dropDown= OptionMenu(root1,variable,*lanuages) # option menu for selecting language
    dropDown.config(bg="GREEN") # drop down color
    dropDown["menu"].config(bg="yellow") #option menu color
    dropDown.place(x=100, y=500)'''
    global finalLang
    finalLang=StringVar()
    label1  = Label(root1,text="Enter Language:",font=('arial',15),bg='#fff7c2').place(x=100,y=450)
    entry=Entry(bd='2px',textvariable=finalLang,font=("Arial", 15),fg='black',selectbackground='blue',selectforeground='yellow'
            ,width='15',bg='white',cursor='arrow')
    entry.place(x=100, y=500)
    Button(root1,text='submit',command=submit,font=('arial',15),bg="#fff7c2").place(x=300, y=500)
    
def submit():
    top = Tk()
    top.configure(bg='#283149')
    top.geometry('600x600')
    lang1 = language_module(language)
    lang2=finalLang.get()
    if(lang2==""):
        lang2='english'
    lang2 = language_module(lang2)
    translator = Translator()
    translated = translator.translate(text, src=lang1, dest=lang2)
    #translated = MyMemoryTranslator(source=lang1, target=lang2).translate(text=text)
    #(top,text=,font=('arial',15)).pack()
    T = Text(top, height=15, width=75, font=("Arial", 15), bg='white', fg='black', selectbackground='blue',
                 selectforeground='yellow') 
    T.insert(END, translated.text) #inserts the text into text box
    T.place(x=0,y=50)
def entry_language():
    label = Label(root,text="Enter Language:",font=('arial',15),bg='#fff7c2').place(x=150,y=120)
    entry=Entry(bd='2px',textvariable=lang,font=("Arial", 15),fg='black',selectbackground='blue',selectforeground='yellow'
            ,width='15',bg='white',cursor='arrow')
    entry.place(x=150,y=150)
    Button(text='Submit',command=submit1,font=('arial',15),bg="#fff7c2").place(x=150,y=200)
    
def submit1():
    global language
    language=lang.get()
    if(language==""):
        language='english'
    show_extract_button(path,language)
  
def language_module(lang):
    try:
        spell = Speller(lang='en')
        lang = spell(lang)
        lang = Lang(lang.capitalize())
        lang = lang.pt1
        return lang
    except Exception:
        lang='english'
        spell = Speller(lang='en')
        lang = spell(lang)
        lang = Lang(lang.capitalize())
        lang = lang.pt1
        return lang
    
root = Tk()
root.configure(bg='#283149')
root.geometry("600x600")
lang=StringVar()  
global path  
path=""
uploadbtn = Button(root,text="Upload an image",command=upload,bg="#fef4e8",fg="black",height=2,width=20,font=('Times',15,'bold')).place(x=150,y=50)
entry_language()

root.mainloop()
