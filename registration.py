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


win=Tk()
win.resizable(0,0)
win.geometry("800x700+400+0")
win.configure(background="#abd0f5")
canvas_width = 800
canvas_height =700


canvas = Canvas(win, 
           width=canvas_width, 
           height=canvas_height)
canvas.place(x=0,y=0)

        
f1 = Frame(win,width = 800,height=2)
f1.pack()

f2= Frame(win,width=800,height=700)
f2.pack(side=TOP)
        


img1 = PhotoImage(file="bg10.png")
canvas.create_image(0,0, anchor=NW, image=img1)



win.title("Registration Form")




Fullname=StringVar()
Enroll=StringVar()
gender =StringVar()
email=StringVar()
var1= StringVar()
Address=StringVar()



def database():
   name1=Fullname.get()
   Id=Enroll.get()
   #genderr=gender.get()
   emaill=email.get()
   add=Address.get()
   shift=var1.get()
   conn = sqlite3.connect('Form.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Voter (Fullname TEXT,Id TEXT,Gender TEXT,email TEXT,Address TEXT)')
   cursor.execute('INSERT INTO Voter (FullName,Id,gender,email,Address) VALUES(?,?,?,?,?)',(name1,Id,shift,emaill,add))
   conn.commit()
   messagebox.showinfo("Registered for Voting", "Done") 
   
   
canvas = Canvas(f2, 
           width=canvas_width, 
           height=canvas_height)
canvas.place(x=0,y=0)
img = PhotoImage(file="bg10.png")
canvas.create_image(0,0, anchor=NW, image=img)
   
img1 = PhotoImage(file="registration.png")   
             
label_0 = Label(f1,image=img1,text="Registration form",bg="#abd0f5",width=1600)
label_0.pack()

entry_2 = Entry(f2,textvar=Enroll,width=15,font=("bold", 15))
entry_2.place(x=300,y=120)
 
 
name=StringVar()

def store():
    path = os.path.dirname(os.path.abspath(__file__))
    cam = cv2.VideoCapture(0)
    #address="http://192.168.0.101:8080/video"
    #cam.open(address)
    detector=cv2.CascadeClassifier(path+r'\Classifiers\face.xml')
    i=0
    offset=50
    #name=input('enter your id')
    name=entry_2.get()
    while True:
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=detector.detectMultiScale(gray, 1.3, 5)
        for(x,y,w,h) in faces:
            i=i+1
            cv2.imwrite("dataSet/face-"+name +'.'+ str(i) + ".jpg", gray[y-offset:y+h+offset,x-offset:x+w+offset])
            cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
            cv2.imshow('im',im[y-offset:y+h+offset,x-offset:x+w+offset])
            cv2.waitKey(100)
        if i>9:
            cam.release()
            
            break


def train():
    path = os.path.dirname(os.path.abspath(__file__))
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    cascadePath = path+r"\Classifiers\face.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);
    dataPath = path+r'\dataSet'
    
    def get_images_and_labels(datapath):
         image_paths = [os.path.join(datapath, f) for f in os.listdir(datapath)]
         # images will contains face images
         images = []
         # labels will contains the label that is assigned to the im5ge
         labels = []
         for image_path in image_paths:
             # Read the image and convert to grayscale
             image_pil = Image.open(image_path).convert('L')
             # Convert the image format into numpy array
             image = np.array(image_pil, 'uint8')
             # Get the label of the image
             nbr = int(os.path.split(image_path)[1].split(".")[0].replace("face-", ""))
             #nbr=int(''.join(str(ord(c)) for c in nbr))
             print(nbr)
             # Detect the face in the image
             faces = faceCascade.detectMultiScale(image)
             # If face is detected, append the face to images and the label to labels
             for (x, y, w, h) in faces:
                 images.append(image[y: y + h, x: x + w])
                 labels.append(nbr)
                 #cv2.imshow("Adding faces to traning set...", image[y: y + h, x: x + w])
                 cv2.waitKey(10)
         # return the images list and labels list
         return images, labels
    
    
    images, labels = get_images_and_labels(dataPath)
    #cv2.imshow('test',images[0])
    cv2.waitKey(1)
    
    recognizer.train(images, np.array(labels))
    recognizer.save(path+r'\trainer\trainer.yml')

def both():
    store()
    train()


def fun():
   os.popen('image.py')


imgfn = PhotoImage(file="full.png") 
label_1 = Label(f2,image=imgfn,bg="orange")
label_1.place(x=10,y=10)

entry_1 = Entry(f2,textvar=Fullname,width=15,font=("bold", 15))
entry_1.place(x=300,y=30)

imgid = PhotoImage(file="id.png")
label_2 = Label(f2,image=imgid)
label_2.place(x=10,y=100)
 
imggen = PhotoImage(file="gender.png")
label_3 = Label(f2,image=imggen)
label_3.place(x=10,y=200)

#var2= IntVar()
Radiobutton(f2, text="Male",font=("bold", 15),bg="white",variable=var1,value="Male").place(x=300,y=220)
  
Radiobutton(f2, text="Female",font=("bold", 15),bg="white",variable=var1,value="Female").place(x=400,y=220)


 


img4 = PhotoImage(file="upload.png")  

Button(f2,text="Store Picture",image=img4,command=both).place(x=600,y=100)

imgemail = PhotoImage(file="email.png") 
label_5=Label(f2,image=imgemail)
label_5.place(x=10,y=300)
  
entry_5 = Entry(f2,textvar=email,width=15,font=("bold", 15))
entry_5.place(x=300,y=320)

imgeadd = PhotoImage(file="add.png") 
label_5=Label(f2,image=imgeadd)
label_5.place(x=10,y=400)
  
entry_5 = Entry(f2,textvar=Address,width=15,font=("bold", 15))
entry_5.place(x=300,y=410)
  
img_upload = PhotoImage(file="uploadid.png")    
n=Button(f2,image=img_upload,borderwidth=0,bg="#88f299",command=fun).place(x=290,y=470)
  

img2 = PhotoImage(file="submit.png")    
Button(f2, text='Submit',image=img2,borderwidth=0,command=database).place(x=290,y=550)




win.mainloop()




















