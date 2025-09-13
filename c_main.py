from tkinter import *
import tkinter
import customtkinter as ctk
from PIL import ImageTk,Image
from tkinter import *
from tkinter import ttk #import tkinter module externaly
from PIL import ImageTk,Image
from chatbot import Chatbot #import pillow module externaly
from student import Student
from train import Train
from face import Face_recoginition
import os

class Main_win:
    def __init__(self,ra):
        self.root=ra
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        root.geometry("1530x780+0+0")
        
      
if __name__=="__main__":
    root=ctk.CTk()
    app=Main_win(root)
    root.mainloop()
# code to make main window
class face_recog_sys:
    def __init__(self,r):
        self.root=r
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")
        # image 1 code

        img=Image.open(r"D:\Users\chaitanya\face recognition\stud.jpeg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photo=ImageTk.PhotoImage(img)

        f_label=ctk.CTkLabel(self.root,image=self.photo)
        f_label.place(x=0,y=0,width=500,height=130)

        # image 2 code

        img1=Image.open(r"D:\Users\chaitanya\face recognition\images.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)

        f_label=ctk.CTkLabel(self.root,image=self.photo1)
        f_label.place(x=500,y=0,width=500,height=130)

        # image 3 code
        img2=Image.open(r"D:\Users\chaitanya\face recognition\mach.jpeg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img2)

        f_label=ctk.CTkLabel(self.root,image=self.photo2)
        f_label.place(x=1000,y=0,width=540,height=130)
        #background img

        img3=Image.open(r"D:\Users\chaitanya\face recognition\help.jpeg")
        img3=img3.resize((1900,970),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img3)

        bg_img=ctk.CTkLabel(self.root,image=self.photo3)
        bg_img.place(x=0,y=0,width=1530,height=820)

        title=lab=ctk.CTkLabel(bg_img,text="FACE  RECOGNITION  ATTENDENCE  SYSTEM  SOFTWARE",font=("Century Gothic",30))
        title.place(x=0,y=0,width=1530,height=55)

        # #student button creation

        # img4=Image.open(r"D:\Users\chaitanya\face recognition\stud.jpeg")
        # img4=img4.resize((220,220),Image.ANTIALIAS)
        # self.photoimg4=ImageTk.PhotoImage(img4)

        # b1=ctk.CTkButton(bg_img,image=self.photoimg4,command=self.stud,cursor="hand2")
        # b1.place(x=200,y=100,width=220,height=220)

        # b1_1=ctk.CTkButton(bg_img,text="student Details",command=self.stud,cursor="hand2",font=("Century Gothic",30))
        # b1_1.place(x=200,y=300,width=220,height=40)

        # #Detect face button

        # img5=Image.open(r"D:\Users\chaitanya\face recognition\recog.jpeg")
        # img5=img5.resize((220,220),Image.ANTIALIAS)
        # self.photoimg5=ImageTk.PhotoImage(img5)

        # b1=ctk.CTkButton(bg_img,image=self.photoimg5,cursor="hand2",command=self.FACE_DATA)
        # b1.place(x=500,y=100,width=220,height=220)

        # b1_1=ctk.CTkButton(bg_img,text="Face Detector",cursor="hand2",command=self.FACE_DATA,font=("Century Gothic",30))
        # b1_1.place(x=500,y=300,width=220,height=40)

        # #Attendence button

        # img6=Image.open(r"D:\Users\chaitanya\face recognition\img.jpeg")
        # img6=img6.resize((220,220),Image.ANTIALIAS)
        # self.photoimg6=ImageTk.PhotoImage(img6)

        # b1=ctk.CTkButton(bg_img,image=self.photoimg6,cursor="hand2")
        # b1.place(x=800,y=100,width=220,height=220)

        # b1_1=ctk.CTkButton(bg_img,text="Attendence creator",cursor="hand2",font=("Century Gothic",30))
        # b1_1.place(x=800,y=300,width=220,height=40)

        # #chatbot or help desk

        # img7=Image.open(r"D:\Users\chaitanya\face recognition\help.jpeg")
        # img7=img7.resize((220,220),Image.ANTIALIAS)
        # self.photoimg7=ImageTk.PhotoImage(img7)

        # b1=ctk.CTkButton(bg_img,image=self.photoimg7,command=self.chat,cursor="hand2")
        # b1.place(x=1100,y=100,width=220,height=220)

        # b1_1=ctk.CTkButton(bg_img,text="Help Desk",command=self.chat,cursor="hand2",font=("Century Gothic",30))
        # b1_1.place(x=1100,y=300,width=220,height=40)

        # #train face detection

        # img8=Image.open(r"D:\Users\chaitanya\face recognition\train.jpeg")
        # img8=img8.resize((220,220),Image.ANTIALIAS)
        # self.photoimg8=ImageTk.PhotoImage(img8)

        # b1=ctk.CTkButton(bg_img,image=self.photoimg8,cursor="hand2",command=self.TRAIN)
        # b1.place(x=200,y=380,width=220,height=220)

        # b1_1=ctk.CTkButton(bg_img,text="Train Data",cursor="hand2",command=self.TRAIN,font=("Century Gothic",30))
        # b1_1.place(x=200,y=580,width=220,height=40)

        # #photos face button

        # img9=Image.open(r"D:\Users\chaitanya\face recognition\bg.jpeg")
        # img9=img9.resize((220,220),Image.ANTIALIAS)
        # self.photoimg9=ImageTk.PhotoImage(img9)

        # b1=ctk.CTkButton(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_photo)
        # b1.place(x=500,y=380,width=220,height=220)

        # b1_1=ctk.CTkButton(bg_img,text="Photos Storage",cursor="hand2",command=self.open_photo,font=("Century Gothic",30))
        # b1_1.place(x=500,y=580,width=220,height=40)

        # #Developer button

        # img10=Image.open(r"D:\Users\chaitanya\face recognition\backg.jpeg")
        # img10=img10.resize((220,220),Image.ANTIALIAS)
        # self.photoimg10=ImageTk.PhotoImage(img10)

        # b1=ctk.CTkButton(bg_img,image=self.photoimg10,cursor="hand2")
        # b1.place(x=800,y=380,width=220,height=220)

        # b1_1=ctk.CTkButton(bg_img,text="Developer Details",cursor="hand2",font=("Century Gothic",30))
        # b1_1.place(x=800,y=580,width=220,height=40)
        
        # #Exit button

        # img11=Image.open(r"D:\Users\chaitanya\face recognition\exit.jpeg")
        # img11=img11.resize((220,220),Image.ANTIALIAS)
        # self.photoimg11=ImageTk.PhotoImage(img11)

        # b1=ctk.CTkButton(bg_img,image=self.photoimg11,cursor="hand2")
        # b1.place(x=1100,y=380,width=220,height=220)

        # b1_1=ctk.CTkButton(bg_img,text="Exit Or Return",cursor="hand2",font=("Century Gothic",30))
        # b1_1.place(x=1100,y=580,width=220,height=40)
        
        
        
    def open_photo(self):
        os.startfile("fphotos")
        # ======================================functions buttons==========================================================
    def stud(self):
            self.new_window=Toplevel(self.root)
            self.app=Student(self.new_window)
    def chat(self):
            self.new_window=Toplevel(self.root)
            self.app=Chatbot(self.new_window)
    
    def TRAIN(self):
            self.new_window=Toplevel(self.root)
            self.app=Train(self.new_window)
                 
    def FACE_DATA(self):
            self.new_window=Toplevel(self.root)
            self.app=Face_recoginition(self.new_window)
            
if __name__=="__main__":
    root=ctk.CTk()
    a=face_recog_sys(root)
    root.mainloop()

