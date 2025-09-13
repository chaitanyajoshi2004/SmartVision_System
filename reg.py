from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class Register:
    def __init__(self,r):
        self.root=r
        self.root.title("Registeration page")
        self.root.geometry("1530x790+0+0")
        self.root.wm_iconbitmap("hack.ico")

        img=Image.open(r"F:\face recognition\Images\bg.jpeg")
        img=img.resize((1900,970),Image.ANTIALIAS)
        self.photo=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photo,bd=2,relief=RAISED)
        bg_img.place(x=0,y=0,width=1540,height=790)

        logo_img=Image.open(r"F:\face recognition\Images\download.png")
        logo_img=logo_img.resize((60,60),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(logo_img)

        title_frame=Frame(root,bd=1,relief=RIDGE)
        title_frame.place(x=490,y=30,width=570,height=80)

        title_lbl=Label(title_frame,image=self.photo_logo,compound=LEFT,text="USER REGISTERATION FORM",font=("times new roman",25,"bold"),fg="Red")
        title_lbl.place(x=0,y=10)

# info_main frame=====================================
        main_frame=Frame(root,bd=1,relief=RIDGE)
        main_frame.place(x=490,y=110,width=570,height=600)
        
        # username
        user_name=ttk.Label(main_frame,text="Username:",font=("times new roman",16,"bold"))
        user_name.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        # user_entry_field
        user_entry=ttk.Entry(main_frame,font=("times new roman",16,"bold"),width=30)
        user_entry.grid(row=0,column=1,padx=10,pady=10)

        # Email
        Email_lbl=ttk.Label(main_frame,text="Eamil-ID:",font=("times new roman",16,"bold"))
        Email_lbl.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        # Email_entry_field
        email_entry=ttk.Entry(main_frame,font=("times new roman",16,"bold"),width=30)
        email_entry.grid(row=1,column=1,padx=10,pady=10)

        # contact
        contact=ttk.Label(main_frame,text="Moblie-NO:",font=("times new roman",16,"bold"))
        contact.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        # contact_entry
        contact_entry=ttk.Entry(main_frame,font=("times new roman",16,"bold"),width=30)
        contact_entry.grid(row=2,column=1,padx=10,pady=10)

        # staff_name
        staff_name=ttk.Label(main_frame,text="Staff-Name:",font=("times new roman",16,"bold"))
        staff_name.grid(row=3,column=0,padx=10,pady=10,sticky=W)
        # staff_entry
        staff_entry=ttk.Entry(main_frame,font=("times new roman",16,"bold"),width=30)
        staff_entry.grid(row=3,column=1,padx=10,pady=10)

            # gender_selection
        staff_name=ttk.Label(main_frame,text="Select-Gender:",font=("times new roman",16,"bold"))
        staff_name.grid(row=4,column=0,padx=10,pady=10,sticky=W)

        # GENDER_FRAME
        GENDER_frame=Frame(main_frame)
        GENDER_frame.place(x=170,y=210,width=330,height=40)

        # # radiobuttons
        radio_male=Radiobutton(GENDER_frame,value="Male",text="Male",font=("times new roman",15))
        radio_male.grid(row=4,column=0,padx=30,sticky=W)

        radio_female=Radiobutton(GENDER_frame,value="Female",text="Female",font=("times new roman",15))
        radio_female.grid(row=4,column=1,padx=70,sticky=W)

         # department_name
        department_name=ttk.Label(main_frame,text="Department-Name:",font=("times new roman",16,"bold"))
        department_name.grid(row=5,column=0,padx=10,pady=10,sticky=W)
        # # department_entry
        # department_entry=ttk.Entry(main_frame,font=("times new roman",16,"bold"),width=30)
        # department_entry.grid(row=5,column=1,padx=10,pady=10)

        self.combo_id_type=ttk.Combobox(main_frame,font=("times new roman",18),justify="center",state="readonly",width=23)
        self.combo_id_type["values"]=("select your Department","computer","civil","electrical","auto-mobile","mechanical")
        self.combo_id_type.grid(row=5,column=1,padx=10,pady=10)
        self.combo_id_type.current(0)



         # password_name
        password_name=ttk.Label(main_frame,text="Enter Password:",font=("times new roman",16,"bold"))
        password_name.grid(row=6,column=0,padx=10,pady=10,sticky=W)
        # password_entry
        password_entry=ttk.Entry(main_frame,font=("times new roman",16,"bold"),width=30,show="*")
        password_entry.grid(row=6,column=1,padx=10,pady=10)



         # confirm_password_name
        confirm_password_name=ttk.Label(main_frame,text="Confirm-Password:",font=("times new roman",16,"bold"))
        confirm_password_name.grid(row=7,column=0,padx=10,pady=10,sticky=W)
        # confirm_entry
        confirm_password_entry=ttk.Entry(main_frame,font=("times new roman",16,"bold"),width=30,show="*")
        confirm_password_entry.grid(row=7,column=1,padx=10,pady=10)

        btn_frame=Frame(main_frame)
        btn_frame.place(x=30,y=450,width=500,height=100)

        b1=Button(btn_frame,text="Save",font=("times new roman",16,"bold"),width=13,cursor="hand2",fg="white",bg="Blue")
        b1.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        b2=Button(btn_frame,text="Verify Data",font=("times new roman",16,"bold"),width=10,cursor="hand2",fg="white",bg="Blue")
        b2.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        b3=Button(btn_frame,text="Clear Data",font=("times new roman",16,"bold"),width=10,cursor="hand2",fg="white",bg="Blue")
        b3.grid(row=0,column=2,padx=10,pady=10,sticky=W)









      
        




if __name__ =="__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()