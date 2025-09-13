from tkinter import *
import tkinter
import customtkinter as ctk
from PIL import ImageTk,Image
from main import face_recog_sys
  
class Login_win:
    def __init__(self,ra):
        self.root=ra
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        # root=ctk.CTk()
        root.geometry("1530x780+0+0")
        root.title("Face Recognition Attendance System")
        # img1=ImageTk.PhotoImage(Image.open("back.jpeg"))
        # l1=ctk.CTkLabel(root,image=img3)

        
        img3=Image.open(r"Images\b.jpg")
        img3=img3.resize((1920,970),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img3)

        l1=Label(self.root,image=self.photo3)
        l1.place(x=0,y=0,width=1530,height=820)



        frame=ctk.CTkFrame(master=l1,width=520,height=500,corner_radius=75)
        frame.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
        frame._set_appearance_mode("dark")
        l1.pack()

        l2=ctk.CTkLabel(master=frame,text="LOG INTO YOUR ACCOUNT",font=("Century Gothic",30))
        l2.place(x=50,y=45)
        entry1=ctk.CTkEntry(master=frame,width=350,height=40,placeholder_text="USERNAME")
        entry1.place(x=80,y=110)

        entry2=ctk.CTkEntry(master=frame,width=350,height=40,placeholder_text="PASSWORD",show="#")
        entry2.place(x=80,y=200)

        button1=ctk.CTkButton(master=frame,width=350,height=40,text="LOGIN",corner_radius=35,command=self.register_window)
        button1.place(x=80,y=300)

        button2=ctk.CTkButton(master=frame,width=170,height=40,text="SIGN UP",corner_radius=35)
        button2.place(x=80,y=400)

        button3=ctk.CTkButton(master=frame,width=100,height=40,text="FORGOT PASSWORD ?",corner_radius=35)
        button3.place(x=270,y=400)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=face_recog_sys(self.new_window)

if __name__=="__main__":
    root=ctk.CTk()
    a=Login_win(root)
    root.mainloop()

