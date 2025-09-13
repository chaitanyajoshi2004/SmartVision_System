from ast import Raise, main
from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
from PIL import Image,ImageTk
from main import face_recog_sys

class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN SYSTEM")
        self.root.geometry("1550x750+0+0")
        self.root.wm_iconbitmap("hack.ico")
        img=Image.open(r"F:\face recognition\Images\bg.jpeg")
        img=img.resize((1550,750),Image.ANTIALIAS)
        self.photo=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photo)
        bg_img.place(x=0,y=0,width=1550,height=750)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=470) 

        img1=Image.open(r"F:\face recognition\Images\download.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)

        log_img=Label(image=self.photo1,bg="black",borderwidth=0)
        log_img.place(x=730,y=175,width=100,height=100)

        get_label=Label(frame,text="Get Started!!!",font=("times new roman",20,BOLD),fg="white",bg="black")
        get_label.place(x=95,y=105)

        # labels
        user_n=Label(frame,text="Username",font=("times new roman",15,BOLD),fg="white",bg="black")
        user_n.place(x=70,y=155)

        self.text_user=ttk.Entry(frame,font=("times new roman",15,BOLD))
        self.text_user.place(x=40,y=180,width=270)

        passwd=Label(frame,text="Password",font=("times new roman",15,BOLD),fg="white",bg="black")
        passwd.place(x=70,y=230)

        self.text_passwd=ttk.Entry(frame,font=("times new roman",15,BOLD))
        self.text_passwd.place(x=40,y=260,width=270)

        # =======================================icons for labels===========================================
        
        img2=Image.open(r"F:\face recognition\Images\download.png")
        img2=img1.resize((20,20),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img2)

        log_img=Label(image=self.photo2,bg="black",borderwidth=0)
        log_img.place(x=650,y=320,width=20,height=20)

        img3=Image.open(r"F:\face recognition\Images\download.png")
        img3=img1.resize((20,20),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img3)

        log_img=Label(image=self.photo3,bg="black",borderwidth=0)
        log_img.place(x=650,y=400,width=20,height=20)

        login_b=Button(frame,text="Login",font=("times new roman",15,BOLD),bd=3,command=self.face,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        login_b.place(x=110,y=300,width=120,height=45)
        
        register_b=Button(frame,text="New User Register",font=("times new roman",15,BOLD),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        register_b.place(x=20,y=350,width=160)

        passwd_b=Button(frame,text="Forget Password",font=("times new roman",15,BOLD),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        passwd_b.place(x=20,y=400,width=160)
    def face(self):
        self.new_window=Toplevel(self.root)
        self.app=face_recog_sys(self.new_window) 


if __name__ == "__main__":
    root=Tk()
    log=Login_window(root)
    root.mainloop()