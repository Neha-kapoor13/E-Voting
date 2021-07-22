import cv2
import numpy as np
from tkinter import *
import tkinter as tk
import tkinter .messagebox
from tkinter import messagebox 
import sqlite3 as sq
import os
from cv2 import COLOR_BGR2XYZ
from itertools import cycle
from tkinter import Tk, PhotoImage, Label
from itertools import cycle
from os import listdir
from PIL import Image, ImageTk , ImageDraw,ImageFont 
import webbrowser
win=Tk()
win.resizable(0,0)
canvas_width = 768
canvas_height =600
canvas = Canvas(win, 
           width=canvas_width, 
           height=canvas_height)
canvas.place(x=0,y=0)
win.geometry("768x600+400+0")
win.title("Voting Result")
top = Frame(win,width = 768,height=2,bg="#2a8db8")
top.pack(side=TOP)
image2=PhotoImage(file="vresult.png")
labelimage2=Label(top,image=image2)
labelimage2.pack(side=TOP)
f1 = Frame(win,width = 768,height=600)
f1.pack()
bg = PhotoImage( file = "resultbg.png")
label1 = Label( f1, image = bg) 
label1.pack()
def getinfo_bjp():
    conn=sq.connect("Form.db")
    cmd="SELECT count(candidate) from vote where Candidate='BJP'"
    cursor=conn.execute(cmd)
    global row
    for row in cursor.fetchall():
        print(row)
    conn.commit()                        
    conn.close()
    return row
def getinfo_con():
    conn=sq.connect("Form.db")
    cmd1="SELECT count(candidate) from vote where Candidate='Congress'"
    cursor=conn.execute(cmd1)
    global row1
    for row1 in cursor.fetchall():
        print(row1)
    conn.commit()                        
    conn.close()
    return row1
def getinfo_aap():
    conn=sq.connect("Form.db")
    cmd2="SELECT count(candidate) from vote where Candidate='AAP'"
    cursor=conn.execute(cmd2)
    global row2
    for row2 in cursor.fetchall():
        print(row2)
    conn.commit()                        
    conn.close()
    return row2
def getinfo_bsp():
    conn=sq.connect("Form.db")
    cmd3="SELECT count(candidate) from vote where Candidate='BSP'"
    cursor=conn.execute(cmd3)
    global row3
    for row3 in cursor.fetchall():
        print(row3)
    conn.commit()                        
    conn.close()
    return row3
def getinfo_com():
    conn=sq.connect("Form.db")
    cmd4="SELECT count(candidate) from vote where Candidate='CPOI'"
    cursor=conn.execute(cmd4)
    global row4
    for row4 in cursor.fetchall():
        print(row4)
    conn.commit()                        
    conn.close()
    return row4
def getinfo_smj():
    conn=sq.connect("Form.db")
    cmd5="SELECT count(candidate) from vote where Candidate='Samajwadi Party'"
    cursor=conn.execute(cmd5)
    global row5
    for row5 in cursor.fetchall():
        print(row5)
    conn.commit()                        
    conn.close()
    return row5          
image3=PhotoImage(file="bjp.png")
labelimage3=Label(f1,image=image3,bg="#f54290")
labelimage3.place(x=10,y=0)
e_bjp=tk.StringVar()
entry_bjp = Entry(f1,width=15,font=("bold", 15),textvariable=e_bjp,justify="center")
entry_bjp.place(x=450,y=0)
getinfo_bjp()
e_bjp.set(row)
image4=PhotoImage(file="congress.png")
labelimage4=Label(f1,image=image4,bg="#f54290")
labelimage4.place(x=10,y=80)
e_con=tk.StringVar()
entry_cong = Entry(f1,width=15,font=("bold", 15),textvariable=e_con,justify="center")
entry_cong.place(x=450,y=80)
getinfo_con()
e_con.set(row1)
image5=PhotoImage(file="aap.png")
labelimage5=Label(f1,image=image5,bg="#f54290")
labelimage5.place(x=10,y=160)
e_aap=tk.StringVar()
entry_aap = Entry(f1,width=15,font=("bold", 15),textvariable=e_aap,justify="center")
entry_aap.place(x=450,y=160)
getinfo_aap()
e_aap.set(row2)
image6=PhotoImage(file="bsp.png")
labelimage6=Label(f1,image=image6,bg="#f54290")
labelimage6.place(x=10,y=240)
e_bsp=tk.StringVar()
entry_bsp = Entry(f1,width=15,font=("bold", 15),textvariable=e_bsp,justify="center")
entry_bsp.place(x=450,y=240)
getinfo_bsp()
e_bsp.set(row3)
image7=PhotoImage(file="comparty.png")
labelimage7=Label(f1,image=image7,bg="#f54290")
labelimage7.place(x=10,y=320)
e_com=tk.StringVar()
entry_com = Entry(f1,width=15,font=("bold", 15),textvariable=e_com,justify="center")
entry_com.place(x=450,y=320)
getinfo_com()
e_com.set(row4)
image8=PhotoImage(file="samparty.png")
labelimage8=Label(f1,image=image8,bg="#f54290")
labelimage8.place(x=10,y=400)
e_smj=tk.StringVar()
entry_sam = Entry(f1,width=15,font=("bold", 15),text="0",textvariable=e_smj,justify="center")
entry_sam.place(x=450,y=400)
getinfo_smj()
e_smj.set(row5)

win.mainloop()
