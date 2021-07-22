from tkinter import *
import sqlite3
import cv2
import os
import numpy as np
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image,ImageTk
import tkinter as tk
from PIL import Image


root=Tk()

fln=0
def showimage():
    global fln
    fln=filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetypes=(("JPG File","*.jpg"),("PNG file","*.png"),("All Files","*.*")))
    img=Image.open(fln)
    img.thumbnail((350,350))
    img=ImageTk.PhotoImage(img)
    lbl.configure(image = img)
    lbl.image=img
    

idd=StringVar()

def convertToBinaryData():
# Convert digital data to binary format
    with open(fln, 'rb') as file:
        binaryData = file.read()
    return binaryData


def insertBLOB():
    Id=idd.get()
    conn=sqlite3.connect('Form.db')

    cursor = conn.cursor()
    sql_insert_blob_query = """ INSERT INTO ID
                  (Id,Image) VALUES (?,?)"""
    empPicture = convertToBinaryData()
    insert_blob_tuple = (Id, empPicture)
    result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
    conn.commit()
    messagebox.showinfo("Stored","ID Stored")

   



frm=Frame(root)
frm.pack(side=BOTTOM,padx=15,pady=15)
 
lbl=Label(root)
lbl.pack()

lbl1=Label(root,text="Enter ID")
lbl1.pack()

entry_id = Entry(root,textvar=idd)
entry_id.pack()

btn=Button(frm,text="Browse Image",command=showimage)
btn.pack(side=tk.LEFT)

btn3=Button(frm,text="Store",command=lambda: insertBLOB())
btn3.pack(side=tk.LEFT,padx=10)

btn2=Button(frm,text="Exit",command=lambda: exit())
btn2.pack(side=tk.LEFT,padx=10)

root.title("Image Browser")
root.geometry("300x350")
root.mainloop()

    


