from tkinter import *
import sqlite3
import cv2
import os
import numpy as np
from tkinter import messagebox
from PIL import Image,ImageTk
import tkinter as tk
from PIL import Image
win=Tk()
win.resizable(0,0)
win.geometry("768x600+400+0")
canvas_width = 768
canvas_height =600
canvas = Canvas(win, 
           width=canvas_width, 
           height=canvas_height)
canvas.place(x=0,y=0)        
f1 = Frame(win,width = 768,height=3,bg="white")
f1.pack(side=TOP)
f2= Frame(win,width=800,height=700)
f2.pack()
Feedback=StringVar()
email=StringVar()
def fback():
   feed1=Feedback.get()
   emaill=email.get()
   conn = sqlite3.connect('Form.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Feedback (Email TEXT,Feedback TEXT)')
   cursor.execute('INSERT INTO Feedback (Email,Feedback) VALUES(?,?)',(emaill,feed1))
   conn.commit()
   messagebox.showinfo("Feedback Received", "Done") 
img1 = PhotoImage(file="bgg.png")
bg=Label(f2,image=img1)
bg.pack()
img2 = PhotoImage(file="feedback.png")
head=Label(f1,image=img2)
head.pack(side=TOP)
win.title("Feedback")
img3 = PhotoImage(file="below.png")
label1=Label(f2,image=img3,bg="#011c45")
label1.place(x=70,y=20)
feed=Entry(f2,textvar=Feedback,width=15,font=("bold", 15))
feed.place(x=80,y=110,width=600,height=200)
feed.insert(INSERT,"Your Comments")
img4 = PhotoImage(file="email1.png")
label2=Label(f2,image=img4,bg="#011c45")
label2.place(x=70,y=330)
emailentry=Entry(f2,textvar=email,width=15,font=("bold", 15))
emailentry.place(x=300,y=335,width=350,height=40)
emailentry.insert(INSERT,"Your Email")
img5 = PhotoImage(file="feedsubmit.png")
Button(f2,text="submit",image=img5,command=fback).place(x=280,y=400)
win.mainloop()
