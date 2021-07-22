import cv2
import numpy as np
from tkinter import *
#import tkinter as tk
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
win.title("Vote")
win.resizable(0,0)
canvas_width = 768
canvas_height =600
canvas = Canvas(win, 
           width=canvas_width, 
           height=canvas_height)
canvas.place(x=0,y=0)
win.geometry("768x600+400+0")
win.configure(background='#2a8db8')
top = Frame(win,width = 1600,height=2,bg="#2a8db8")
top.pack(side=TOP)
f1 = Frame(win,width = 800,height=3,bg="#c9d1ca")
f1.pack()
f4 = Frame(win,width = 800,height=600,bg="#c9d1ca")
f4.pack()
bg = PhotoImage( file = "bgg.png")
label1 = Label( f4, image = bg) 
label1.place(x = 0,y = 0)
image2=PhotoImage(file="ev.png")
labelimage2=Label(top,image=image2,bg="blue")
labelimage2.pack(side=TOP)
def close_window(): 
    win.destroy()    
def detect():
    faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
    cam=cv2.VideoCapture(0);
    rec= cv2.face.LBPHFaceRecognizer_create()
    rec.read("trainer\\trainer.yml")
    id=0
    def getinfo(id):
        conn=sq.connect("Form.db")
        cmd="SELECT * FROM Voter WHERE Id="+str(id)
        profile=None
        cursor=conn.execute(cmd)
        for row in cursor:
            profile=row
        while(profile!=None):
            a=str(profile[0])
            b=str(profile[1])
            c="BJP"
            cursor.execute('CREATE TABLE IF NOT EXISTS Vote (Id Text,Name Text,Candidate Text)')
            cursor.execute('INSERT INTO Vote(Id,Name,Candidate) VALUES(?,?,?)',(b,a,c))
            break        
        #else:
            #print("end")        
        conn.commit()                        
        conn.close()
        return profile        
    #font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,5,1,0,4)
    font = cv2.FONT_HERSHEY_SIMPLEX
    while(True):
        ret,img=cam.read();
        gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        faces=faceDetect.detectMultiScale(gray,1.3,5)
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            id,conf=rec.predict(gray[y:y+h,x:x+w])
            profile=getinfo(id)
            if (profile!=None):
                cv2.putText(img,str(profile[0]),(x,y+h+30),font,0.75,(0,255,0),4)
                cv2.putText(img,str(profile[1]),(x,y+h+60),font,0.55,(0,255,0),2)
                cv2.putText(img,str(profile[2]),(x,y+h+90),font,0.55,(0,255,0),2)
                cv2.putText(img,str(profile[3]),(x,y+h+120),font,0.55,(0,255,0),2)                
            else:
                cv2.putText(img,str("unknown"),(x,y+h+30),font,0.75,(0,255,0),4)                         
        cv2.imshow("face",img)
        if(cv2.waitKey(30)):
            print(id)
            a=str(profile[0])
            b=str(profile[1])
            c="BJP"
            minfo="Name: "+a+"\n"+"Id: "+b+"\n"+"Party: "+c
            messagebox.showinfo("Voting Done",minfo) 
            break
    cam.release()
    cv2.destroyAllWindows()
def detect2():
    faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
    cam=cv2.VideoCapture(0);
    rec= cv2.face.LBPHFaceRecognizer_create()
    rec.read("trainer\\trainer.yml")
    id=0
    def getinfo(id):
        conn=sq.connect("Form.db")
        cmd="SELECT * FROM Voter WHERE Id="+str(id)
        profile=None
        cursor=conn.execute(cmd)
        for row in cursor:
            profile=row
        
        while (profile!=None):
            a=str(profile[0])
            b=str(profile[1])
            c="Congress"
            cursor.execute('CREATE TABLE IF NOT EXISTS Vote (Id Text,Name Text,Candidate Text)')
            cursor.execute('INSERT INTO Vote(Id,Name,Candidate) VALUES(?,?,?)',(a,b,c))
            break
        
        #else:
            #print("end")
        
        conn.commit()                        
        conn.close()
        return profile
        
    #font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,5,1,0,4)
    font = cv2.FONT_HERSHEY_SIMPLEX
    while(True):
        ret,img=cam.read();
        gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        faces=faceDetect.detectMultiScale(gray,1.3,5)
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            id,conf=rec.predict(gray[y:y+h,x:x+w])
            profile=getinfo(id)
            if (profile!=None):
                cv2.putText(img,str(profile[0]),(x,y+h+30),font,0.75,(0,255,0),4)
                cv2.putText(img,str(profile[1]),(x,y+h+60),font,0.55,(0,255,0),2)
                cv2.putText(img,str(profile[2]),(x,y+h+90),font,0.55,(0,255,0),2)
                cv2.putText(img,str(profile[3]),(x,y+h+120),font,0.55,(0,255,0),2)
                
            else:
                cv2.putText(img,str("unknown"),(x,y+h+30),font,0.75,(0,255,0),4)
                         
        cv2.imshow("face",img)
        if(cv2.waitKey(30)):
            print(id)
            a=str(profile[0])
            b=str(profile[1])
            c="Congress"
            minfo="Name: "+a+"\n"+"Id: "+b+"\n"+"Party: "+c
            messagebox.showinfo("Voting Done",minfo) 
            break
    cam.release()
    cv2.destroyAllWindows()

def detect3():
    faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
    cam=cv2.VideoCapture(0);
    rec= cv2.face.LBPHFaceRecognizer_create()
    rec.read("trainer\\trainer.yml")
    id=0
    def getinfo(id):
        conn=sq.connect("Form.db")
        cmd="SELECT * FROM Voter WHERE Id="+str(id)
        profile=None
        cursor=conn.execute(cmd)
        for row in cursor:
            profile=row
        
        while (profile!=None):
            a=str(profile[0])
            b=str(profile[1])
            c="AAP"
            cursor.execute('CREATE TABLE IF NOT EXISTS Vote (Id Text,Name Text,Candidate Text)')
            cursor.execute('INSERT INTO Vote(Id,Name,Candidate) VALUES(?,?,?)',(a,b,c))
            break
        
        #else:
            #print("end")
        
        conn.commit()                        
        conn.close()
        return profile
        
    #font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,5,1,0,4)
    font = cv2.FONT_HERSHEY_SIMPLEX
    while(True):
        ret,img=cam.read();
        gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        faces=faceDetect.detectMultiScale(gray,1.3,5)
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            id,conf=rec.predict(gray[y:y+h,x:x+w])
            profile=getinfo(id)
            if (profile!=None):
                cv2.putText(img,str(profile[0]),(x,y+h+30),font,0.75,(0,255,0),4)
                cv2.putText(img,str(profile[1]),(x,y+h+60),font,0.55,(0,255,0),2)
                cv2.putText(img,str(profile[2]),(x,y+h+90),font,0.55,(0,255,0),2)
                cv2.putText(img,str(profile[3]),(x,y+h+120),font,0.55,(0,255,0),2)
                
            else:
                cv2.putText(img,str("unknown"),(x,y+h+30),font,0.75,(0,255,0),4)
                         
        cv2.imshow("face",img)
        if(cv2.waitKey(30)):
            print(id)
            a=str(profile[0])
            b=str(profile[1])
            c="AAP"
            minfo="Name: "+a+"\n"+"Id: "+b+"\n"+"Party: "+c
            messagebox.showinfo("Voting Done",minfo) 
            break
    cam.release()
    cv2.destroyAllWindows()

def detect4():
    faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
    cam=cv2.VideoCapture(0);
    rec= cv2.face.LBPHFaceRecognizer_create()
    rec.read("trainer\\trainer.yml")
    id=0
    def getinfo(id):
        conn=sq.connect("Form.db")
        cmd="SELECT * FROM Voter WHERE Id="+str(id)
        profile=None
        cursor=conn.execute(cmd)
        for row in cursor:
            profile=row
        
        while (profile!=None):
            a=str(profile[0])
            b=str(profile[1])
            c="BSP"
            cursor.execute('CREATE TABLE IF NOT EXISTS Vote (Id Text,Name Text,Candidate Text)')
            cursor.execute('INSERT INTO Vote(Id,Name,Candidate) VALUES(?,?,?)',(a,b,c))
            break
        
        #else:
            #print("end")
        
        conn.commit()                        
        conn.close()
        return profile
        
    #font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,5,1,0,4)
    font = cv2.FONT_HERSHEY_SIMPLEX
    while(True):
        ret,img=cam.read();
        gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        faces=faceDetect.detectMultiScale(gray,1.3,5)
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            id,conf=rec.predict(gray[y:y+h,x:x+w])
            profile=getinfo(id)
            if (profile!=None):
                cv2.putText(img,str(profile[0]),(x,y+h+30),font,0.75,(0,255,0),4)
                cv2.putText(img,str(profile[1]),(x,y+h+60),font,0.55,(0,255,0),2)
                cv2.putText(img,str(profile[2]),(x,y+h+90),font,0.55,(0,255,0),2)
                cv2.putText(img,str(profile[3]),(x,y+h+120),font,0.55,(0,255,0),2)
                
            else:
                cv2.putText(img,str("unknown"),(x,y+h+30),font,0.75,(0,255,0),4)
                         
        cv2.imshow("face",img)
        if(cv2.waitKey(30)):
            print(id)
            a=str(profile[0])
            b=str(profile[1])
            c="BSP"
            minfo="Name: "+a+"\n"+"Id: "+b+"\n"+"Party: "+c
            messagebox.showinfo("Voting Done",minfo) 
            break
    cam.release()
    cv2.destroyAllWindows()


def detect5():
    faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
    cam=cv2.VideoCapture(0);
    rec= cv2.face.LBPHFaceRecognizer_create()
    rec.read("trainer\\trainer.yml")
    id=0
    def getinfo(id):
        conn=sq.connect("Form.db")
        cmd="SELECT * FROM Voter WHERE Id="+str(id)
        profile=None
        cursor=conn.execute(cmd)
        for row in cursor:
            profile=row
        
        while (profile!=None):
            a=str(profile[0])
            b=str(profile[1])
            c="CPOI"
            cursor.execute('CREATE TABLE IF NOT EXISTS Vote (Id Text,Name Text,Candidate Text)')
            cursor.execute('INSERT INTO Vote(Id,Name,Candidate) VALUES(?,?,?)',(a,b,c))
            break
        
        #else:
            #print("end")
        
        conn.commit()                        
        conn.close()
        return profile
        
    #font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,5,1,0,4)
    font = cv2.FONT_HERSHEY_SIMPLEX
    while(True):
        ret,img=cam.read();
        gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        faces=faceDetect.detectMultiScale(gray,1.3,5)
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            id,conf=rec.predict(gray[y:y+h,x:x+w])
            profile=getinfo(id)
            if (profile!=None):
                cv2.putText(img,str(profile[0]),(x,y+h+30),font,0.75,(0,255,0),4)
                cv2.putText(img,str(profile[1]),(x,y+h+60),font,0.55,(0,255,0),2)
                cv2.putText(img,str(profile[2]),(x,y+h+90),font,0.55,(0,255,0),2)
                cv2.putText(img,str(profile[3]),(x,y+h+120),font,0.55,(0,255,0),2)
                
            else:
                cv2.putText(img,str("unknown"),(x,y+h+30),font,0.75,(0,255,0),4)
                         
        cv2.imshow("face",img)
        if(cv2.waitKey(30)):
            print(id)
            a=str(profile[0])
            b=str(profile[1])
            c="CPOI"
            minfo="Name: "+a+"\n"+"Id: "+b+"\n"+"Party: "+c
            messagebox.showinfo("Voting Done",minfo) 
            break
    cam.release()
    cv2.destroyAllWindows()

def detect6():
    faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
    cam=cv2.VideoCapture(0);
    rec= cv2.face.LBPHFaceRecognizer_create()
    rec.read("trainer\\trainer.yml")
    id=0
    def getinfo(id):
        conn=sq.connect("Form.db")
        cmd="SELECT * FROM Voter WHERE Id="+str(id)
        profile=None
        cursor=conn.execute(cmd)
        for row in cursor:
            profile=row
        
        while (profile!=None):
            a=str(profile[0])
            b=str(profile[1])
            c="Samajwadi Party"
            cursor.execute('CREATE TABLE IF NOT EXISTS Vote (Id Text,Name Text,Candidate Text)')
            cursor.execute('INSERT INTO Vote(Id,Name,Candidate) VALUES(?,?,?)',(a,b,c))
            break
        
        #else:
            #print("end")
        
        conn.commit()                        
        conn.close()
        return profile
        
    #font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,5,1,0,4)
    font = cv2.FONT_HERSHEY_SIMPLEX
    while(True):
        ret,img=cam.read();
        gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        faces=faceDetect.detectMultiScale(gray,1.3,5)
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            id,conf=rec.predict(gray[y:y+h,x:x+w])
            profile=getinfo(id)
            if (profile!=None):
                cv2.putText(img,str(profile[0]),(x,y+h+30),font,0.75,(0,255,0),4)
                cv2.putText(img,str(profile[1]),(x,y+h+60),font,0.55,(0,255,0),2)
                cv2.putText(img,str(profile[2]),(x,y+h+90),font,0.55,(0,255,0),2)
                cv2.putText(img,str(profile[3]),(x,y+h+120),font,0.55,(0,255,0),2)
                
            else:
                cv2.putText(img,str("unknown"),(x,y+h+30),font,0.75,(0,255,0),4)
                         
        cv2.imshow("face",img)
        if(cv2.waitKey(30)):
            print(id)
            a=str(profile[0])
            b=str(profile[1])
            c="Samajwadi Party"
            minfo="Name: "+a+"\n"+"Id: "+b+"\n"+"Party: "+c
            messagebox.showinfo("Voting Done",minfo) 
            break
    cam.release()
    cv2.destroyAllWindows()
i1=PhotoImage(file="11.png")
labelimage2=Label(f4,image=i1,bg="#eb348c",width=450).place(x=10,y=20)

voteimage=PhotoImage(file="button.png")
labelimage=Button(f4,image=voteimage,bg="black",command=detect).place(x=550,y=20)

i2=PhotoImage(file="22.png")
labelimage2=Label(f4,image=i2,bg="#eb348c",width=450).place(x=10,y=90)

voteimage1=PhotoImage(file="button.png")
labelimage=Button(f4,image=voteimage1,bg="black",command=detect2).place(x=550,y=90)

i3=PhotoImage(file="33.png")
labelimage2=Label(f4,image=i3,bg="#eb348c",width=450).place(x=10,y=160)

voteimage2=PhotoImage(file="button.png")
labelimage=Button(f4,image=voteimage2,bg="black",command=detect3).place(x=550,y=160)

i4=PhotoImage(file="44.png")
labelimage2=Label(f4,image=i4,bg="#eb348c",width=450).place(x=10,y=230)

voteimage3=PhotoImage(file="button.png")
labelimage=Button(f4,image=voteimage3,bg="black",command=detect4).place(x=550,y=230)

i5=PhotoImage(file="55.png")
labelimage2=Label(f4,image=i5,bg="#eb348c",width=450).place(x=10,y=300)

voteimage4=PhotoImage(file="button.png")
labelimage=Button(f4,image=voteimage4,bg="black",command=detect5).place(x=550,y=300)

i6=PhotoImage(file="66.png")
labelimage2=Label(f4,image=i6,bg="#eb348c",width=450).place(x=10,y=370)

voteimage5=PhotoImage(file="button.png")
labelimage=Button(f4,image=voteimage5,bg="black",command=detect6).place(x=550,y=370)
cv2.destroyAllWindows()
win.mainloop()
