
from tkinter import messagebox
import pyttsx3
import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk ,Image

from pyttsx3 import engine
engine = pyttsx3.init('sapi5')
engine.setProperty('rate',150)

base = tkinter.Tk()
base.title("@_.py__lovers")
photro = ImageTk.PhotoImage(file = r"aa.png") 
lab=Label(image=photro)
lab.pack()
label = tkinter.Label(text="ENTER YOUR SENTENCE YOU WANT TO CONVERT IN VOICE",fg="black")
label.pack()

class t2:
    def __init__(self,base) :
        self.entry_var = tkinter.StringVar()
        self.entry = tkinter.Entry(base,textvariable=self.entry_var,width=50)
        self.button = tkinter.Button(base,text="convert into voice",command=self.show_output,anchor=CENTER)
        
        self.entry.bind('<Return>',self.show_output)
        self.entry.pack()
        self.label = tkinter.Label(text="ENTER FILE NAME TO SAVE",fg="black")
        self.label.pack()
        self.entry_var2 = tkinter.StringVar()
        self.entry2 = tkinter.Entry(base,textvariable=self.entry_var2,width=50)
        self.entry2.pack()
        self.button.pack()

    def show_output(self):
        c = self.entry_var.get()
        c2 = self.entry_var2.get()
        lastname = ".mp3"
        file = c2+lastname
        engine.save_to_file(c ,file)
        engine.runAndWait()
        messagebox.showinfo("MSG","DONE!")

    def new(self):
        tk = tkinter.Tk()
        tk.title("DONE")
        Label =tkinter.Label(text="DONE!" ,anchor=CENTER,width=30,height=30)

        


t2(base) 
base.mainloop()