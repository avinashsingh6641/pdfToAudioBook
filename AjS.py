import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import PyPDF2
#import docx
import pyttsx3
from textblob import TextBlob
import os
from gtts import gTTS
from playsound import playsound
import time
import itertools
from tkinter import filedialog
import tempfile
#pip install googletrans==3.1.0a0
from googletrans import Translator
from PIL import Image, ImageTk
from pygame import mixer
from langdetect import detect
from googletrans import Translator
import urllib
from urllib.request import urlopen
splash_root = tk.Tk()
splash_root.title("Pdf to AudioBook")
splash_root.geometry("1000x500")
splashFrame = tk.Frame(splash_root, width=500, height=500, bg="#4a8577")
splashFrame.pack(fill=tk.BOTH, expand=True)
internetLable=tk.Label(splashFrame,text="checking for internet",bg="#4a8577")
internetLable.pack(fill=tk.BOTH, expand=True)
def is_internet():
    try:
        urlopen('https://www.google.com',timeout=1)
        return True
    except urllib.error.URLError as Error:
        return False
def main_window():
    translator = Translator()
    value = ""
    path = ""
    splash_root.destroy()
    r = tk.Tk()
    r.title('pdf to audio converter')
    r.geometry("1000x500")
    mixer.init()
    fromPage = tk.StringVar()
    toPage = tk.StringVar()
    

    clicked = tk.StringVar(r)
    tab3text = tk.StringVar()
    clickedtab3 = tk.StringVar()
    option_value=tk.IntVar()
    dict={'en':'english','hi':'hindi','mr':'marathi','ml':'malayalam','gu':'gujarati'}

    def sel():
        return option_value.get()
    
    steps_frame=tk.Frame(r,width=250,height=500,bg="#cc0066")
    steps_frame.pack(side=tk.RIGHT,expand=True)
    
    steps_Label=tk.Label(steps_frame,text="Follow the steps",bg="#cc0066",fg="white")
    steps_Label.config(font=("Bold",20))
    steps_Label.place(x=10,y=2,width=250,height=38)

    steps="""step1: click on uplaod button

step2: select the PDF file
you want to convert

step3:select the pages you
want you can select
particular page number
or you can select all pages

step4:select the language
into which you have to
convert from the drop down

step5:click on convert button

step6:you will see done
message in the below text box

    you can play to check
    or click on save button
    to save your audio book
    with specific name
"""
    
    step=tk.Text(steps_frame,bg="#cc0066", fg="white")
    step.config(font=("Bold",12))
    step.place(x=5,y=40,width=240,height=420)
    step.insert(tk.END,steps)

    happy_label=tk.Label(steps_frame,bg="#cc0066", fg="white",text="HAPPY LISTENING !!!!")
    
    happy_label.config(font=("Bold",15))
    happy_label.place(x=5,y=465,width=240,height=25)
    
    optional_frame=tk.Frame(r,width=250,height=500,bg="#cc0066")
    optional_frame.pack(side=tk.LEFT,expand=True)

    image_address=Image.open("C:/Users/AVINASH/Desktop/audiobook.png ")
    resized_image=image_address.resize((250,350))
    audiobook_image=ImageTk.PhotoImage(resized_image)
    

    image_label=tk.Label(optional_frame,image=audiobook_image)
    image_label.image=audiobook_image
    image_label.place(x=0,y=70,width=250,height=350)

    style = ttk.Style()
    style.theme_create( "dummy", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
        "TNotebook.Tab": {
            "configure": {"padding": [5, 1], "background":"white"  },
            "map":       {"background": [("selected","#F2C84B")],
                          "expand": [("selected", [1, 1, 1, 0])] } } } )

    style.theme_use("dummy")

    my_notebook = ttk.Notebook(r)
    my_notebook.pack( side=tk.LEFT,expand=True)
    

    def open_pdf():
        global pdf_file
        global page
        global pages
        global open_file
        open_file = filedialog.askopenfilename(
            initialdir="C:",
            filetypes=(
                ("PDF Files", "*.pdf"),
                ("ALL Files", "*.*"))
        )
        name1 = open_file.split('.', 1)
        #extension=name1[1]
        #print(extension)
        if open_file:     
            pdf_file = PyPDF2.PdfFileReader(open_file)
            pages = pdf_file.numPages
            e1.insert(1, open_file)
            print(pages)


    def convert():
        e2.delete(0, 4)
        Text = ""
        global speaker
        global t
        global result
        global output
        global filename
        # global l
        # global Text
        print("check point")
        global Book
        
        option=sel()
        try:
            fromPageNo=0
            toPageNo=0
            
            if option ==1:
                for i in range(0,pages):
                    pageObj = pdf_file.getPage(i)

                    Text += pageObj.extractText()
            else:
            
                From= fromPage.get()
                print(From)
                fromPageNo= int(From)
                print(fromPageNo)

                to = toPage.get()
                toPageNo = int(to)
                print(toPageNo)

            
                for i in range(fromPageNo-1,toPageNo):
                    pageObj = pdf_file.getPage(i)

                    Text += pageObj.extractText()
            

            print("check point")
            convert = str(TextBlob(Text))
            detecting = detect(convert)
            print(detecting,"detecting")
            lan=dict.get(detecting)
            print(lan,"len")
            c = clicked.get()
            print(c,"c")
        
            if c == lan:
                l= detecting
                result = Text
            elif c == 'english':
                l = 'en'
                translation = translator.translate(convert,dest=l)
                result=translation.text    
            elif c == 'hindi':
                l = 'hi'
                #convert = TextBlob(Text)
                translation = translator.translate(convert,dest=l)
                result=translation.text
            
            elif c == 'malayalam':
                l = 'ml'
                translation = translator.translate(convert,dest=l)
                result=translation.text
            elif c == 'marathi':
                l = 'mr'
                translation = translator.translate(convert,dest=l)
                result=translation.text
            elif c == 'gujarati':
                l = 'gu'
                translation = translator.translate(convert,dest=l)
                result=translation.text
            book_name = open_file.split('/', maxsplit=-1)
            n = len(book_name)
            print(n)
            name = book_name[n - 1]
            name1 = name.split('.', 1)
            AudioBook = (name1[0])
            if os.path.exists('c:/users/AVINASH/Desktop/Book'):
                AudioBook=AudioBook+'1'
                Book = (AudioBook + '.mp3')
                print(Book,"book1")
            else:
                Book = (AudioBook + '.mp3')
                print(Book,"book2")
            print(path)
            print(Book)
            output = gTTS(text=str(result), lang=l, slow=False)
            output.save(Book)
            value="done"
            e2.insert(0, value)

        except:
            if (option ==0 and (fromPageNo ==0 or toPageNo == 0)):
                
                tk.messagebox.showwarning("showwarning","provide page numbers")
                print("please select pages")

            else :
                tk.messagebox.showwarning("showwarning","first upload PDF")
                
        
    def play_check():
        os.system(Book)
    def save():
        filename=filedialog.asksaveasfilename(initialdir='c:/users/AVINASH/Desktop',title='save file',defaultextension='.mp3',filetypes=[('audio files','*.mp3'),])
        #myfile=open(filename,"w+")
        output.save(filename)
        '''
    def play():
        try:
            paused  # Checks whether the 'paused' variable is initialized or not.

        except NameError:  # If not initialized then executes the code under except condition
            try:
                mixer.music.load(Book)
                mixer.music.play()

            except:
                tk.messagebox.showerror('File not found',
                                             'Melody could not find the file. Please check again.')

        else:  # If initialized the it goes to the else condition
            mixer.music.unpause()

    def pause():
        global paused
        paused=True

        mixer.music.pause()

'''
    def play2():
        submit = tab3text.get()
        lan = clickedtab3.get()

        if lan == 'hindi':
            l = 'hi'
            translation = translator.translate(submit,dest=l)
            result=translation.text
        elif lan == 'malayalam':
            l = 'ml'
            translation = translator.translate(submit,dest=l)
            result=translation.text
        elif lan == 'marathi':
            l = 'mr'
            translation = translator.translate(submit,dest=l)
            result=translation.text
        elif lan == 'gujarati':
            l = 'gu'
            translation = translator.translate(submit,dest=l)
            result=translation.text
        else:
            l = 'en'
            translation = translator.translate(submit,dest=l)
            result=translation.text

        if l == 'en':
            output = gTTS(text=result, lang=l, slow=False)
            output.save('speech.mp3')
            os.system('speech.mp3')
        else:
            output = gTTS(text=result, lang=l, slow=False)
            output.save('speech.mp3')
            os.system('speech.mp3')


    Frame1 = tk.Frame(my_notebook, width=500, height=500, bg="#b30059")
    Frame1.pack(side=tk.LEFT, expand=True)
    my_frame3 = tk.Frame(my_notebook, width=500, height=500, bg="lightgrey")

    my_notebook.add(Frame1, text="1st Tab")
    my_notebook.add(my_frame3, text="2nd Tab")

    labeltab3 = tk.Label(my_frame3, text="Text to Speech", bg="lightgrey", font="bold, 20", pady=40).pack()
    entrytab3 = tk.Entry(my_frame3, textvariable=tab3text, width=35, bd=3, font=14)

    entrytab3.place(x=90, y=110)
    entrytab3.insert(0, "")
    btntab3 = tk.Button(my_frame3, text="SPEAK", width="15", pady=10, font="bold, 15", command=play2, bg='yellow')
    btntab3.place(x=170, y=160)

    e1 = tk.Entry(master=Frame1, bd=5)
    e1.place(x=150, y=150, width=200, height=100)

    

    def button_hover(e):
        e.widget.config(bg="white")
        
    def button_hover_leave(e):
        
        e.widget.config(bg="SystemButtonFace")

    convert_arrow=tk.Canvas(Frame1,bg="#b30059",highlightbackground="#b30059",width=40,height=40)
    convert_arrow.place(x=230, y=260, width=40, height=40)
    convert_arrow.create_line(15,35,15,10,fill="white",width=3)
    convert_arrow.create_line(5,25,15,10,fill="white",width=3)
    convert_arrow.create_line(25,5,25,30,fill="white",width=3)
    convert_arrow.create_line(25,30,35,15,fill="white",width=3)

    
    

    button1 = tk.Button(Frame1, text='convert', width=15, command=convert)
    button1.place(x=200, y=310, width=100, height=30)

    button2 = tk.Button(Frame1, text='upload', width=15, command=open_pdf)
    button2.place(x=30, y=200, width=100, height=30)

    button1.bind("<Enter>",button_hover)
    button1.bind("<Leave>",button_hover_leave)

    button2.bind("<Enter>",button_hover)
    button2.bind("<Leave>",button_hover_leave)

    options = [
        "english",
        "hindi",
        "marathi",
        "malayalam",
        "gujarati"
    ]

    clicked.set("english")
    drop = tk.OptionMenu(Frame1, clicked, *options)
    drop.place(x=400, y=200, width=100, height=30)

    clickedtab3.set("english")
    drop = tk.OptionMenu(my_frame3, clickedtab3, *options)
    drop.place(x=400, y=200, width=100, height=30)

    e2 = tk.Entry(master=Frame1, textvariable=value, bd=3)
    e2.place(x=200, y=350, width=100, height=30)

    #play = Image.open('C:/Users/AVINASH/Desktop/play.jpg')
    #play_image=ImageTk.PhotoImage(play)

    b1 = tk.Button(Frame1,text="play", width=10, command=play_check)
    b1.place(x=310, y=350, width=30, height=30)

    
    b1.bind("<Enter>",button_hover)
    b1.bind("<Leave>",button_hover_leave)
    #play_label=tk.Label(b1,image=play_image)
    #play_label.place(x=0, y=0, width=30, height=30)
    #b2 = tk.Button(Frame1,  text="pause", width=10, command=pause)
    #b2.place(x=350, y=400, width=100, height=30)

    b3 = tk.Button(Frame1,  text="save", width=10, command=save)
    b3.place(x=350, y=350, width=30, height=30)

    b3.bind("<Enter>",button_hover)
    b3.bind("<Leave>",button_hover_leave)

   
    #Eentry.insert(0, "")



    FromLabel = tk.Label(Frame1, text="From Page no:", bg="#b30059",fg="white")
    FromLabel.config(font=("Bold",10))
    FromLabel.place(x=20, y=80, width=100, height=20)

    FromEntry = tk.Entry(Frame1, textvariable=fromPage)
    FromEntry.place(x=130, y=80, width=30, height=20)

    Tolabel = tk.Label(Frame1, text="To Page no:", bg="#b30059",fg="white")
    Tolabel.config(font=("Bold",10))
    Tolabel.place(x=170, y=80, width=100, height=20)

    Toentry = tk.Entry(Frame1, textvariable=toPage)
    Toentry.place(x=280, y=80, width=30, height=20)
    
    

    c11=tk.Checkbutton(Frame1, text="All Pages",bg="#b30059",selectcolor="black",fg="white",variable=option_value,onvalue=1,offvalue=0)
    c11.config(font=("Bold",10))
    c11.place(x=20,y=30,width=80,height=30)

if is_internet():
    splash_root.after(3000, main_window)
    splash_root.mainloop()
else:
    internetLable['text']="no internet connected"
    
