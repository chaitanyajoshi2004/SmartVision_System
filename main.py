# from tkinter import *
# from tkinter import ttk 
# from PIL import ImageTk,Image
# from chatbot import Chatbot
# from student import Student
# from train import Train
# from face import Face_recoginition
# from attend import Attendance

# import os


# # code to make main window
# class face_recog_sys:
#     def __init__(self,r):
#         self.root=r
#         self.root.geometry("1720x870+0+0")
#         self.root.title("FACE RECOGNITION SYSTEM")
#         # self.root.wm_iconbitmap("hack.ico")
#         # image 1 code

#         img=Image.open(r"F:\face recognition\Images\stud.jpeg")
#         img=img.resize((500,130),Image.ANTIALIAS)
#         self.photo=ImageTk.PhotoImage(img)

#         f_label=Label(self.root,image=self.photo)
#         f_label.place(x=0,y=0,width=500,height=130)

#         # image 2 code

#         img1=Image.open(r"F:\face recognition\Images\images.jpg")
#         img1=img1.resize((500,130),Image.ANTIALIAS)
#         self.photo1=ImageTk.PhotoImage(img1)

#         f_label=Label(self.root,image=self.photo1)
#         f_label.place(x=500,y=0,width=500,height=130)

#         # image 3 code
#         img2=Image.open(r"F:\face recognition\Images\mach.jpeg")
#         img2=img2.resize((500,130),Image.ANTIALIAS)
#         self.photo2=ImageTk.PhotoImage(img2)

#         f_label=Label(self.root,image=self.photo2)
#         f_label.place(x=1000,y=0,width=540,height=130)
#         #background img

#         img3=Image.open(r"F:\face recognition\Images\help.jpeg")
#         img3=img3.resize((1900,970),Image.ANTIALIAS)
#         self.photo3=ImageTk.PhotoImage(img3)

#         bg_img=Label(self.root,image=self.photo3)
#         bg_img.place(x=0,y=0,width=1920,height=970)

#         title=lab=Label(bg_img,text="FACE  RECOGNITION  ATTENDENCE  SYSTEM  SOFTWARE",font=("times new roman",45,"bold"),bg="white",fg="red")
#         title.place(x=0,y=0,width=1920,height=70)

#         #student button creation

#         img4=Image.open(r"F:\face recognition\Images\stud.jpeg")
#         img4=img4.resize((300,300),Image.ANTIALIAS)
#         self.photoimg4=ImageTk.PhotoImage(img4)

#         b1=Button(bg_img,image=self.photoimg4,command=self.stud,cursor="hand2")
#         b1.place(x=150,y=100,width=300,height=300)

#         b1_1=Button(bg_img,text="student Details",command=self.stud,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
#         b1_1.place(x=150,y=401,width=300,height=40)

#         #Detect face button

#         img5=Image.open(r"F:\face recognition\Images\recog.jpeg")
#         img5=img5.resize((300,300),Image.ANTIALIAS)
#         self.photoimg5=ImageTk.PhotoImage(img5)

#         b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.FACE_DATA)
#         b1.place(x=600,y=100,width=300,height=300)

#         b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.FACE_DATA,font=("times new roman",15,"bold"),bg="blue",fg="white")
#         b1_1.place(x=600,y=401,width=300,height=40)

#         #Attendence button

#         img6=Image.open(r"F:\face recognition\Images\img.jpeg")
#         img6=img6.resize((300,300),Image.ANTIALIAS)
#         self.photoimg6=ImageTk.PhotoImage(img6)

#         b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance)
#         b1.place(x=1050,y=100,width=300,height=300)

#         b1_1=Button(bg_img,text="Attendence creator",cursor="hand2",command=self.attendance,font=("times new roman",15,"bold"),bg="blue",fg="white")
#         b1_1.place(x=1050,y=401,width=300,height=40)

#         #chatbot or help desk

#         img7=Image.open(r"F:\face recognition\Images\help.jpeg")
#         img7=img7.resize((300,300),Image.ANTIALIAS)
#         self.photoimg7=ImageTk.PhotoImage(img7)

#         b1=Button(bg_img,image=self.photoimg7,command=self.chat,cursor="hand2")
#         b1.place(x=1500,y=100,width=300,height=300)

#         b1_1=Button(bg_img,text="Help Desk",command=self.chat,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
#         b1_1.place(x=1500,y=401,width=300,height=40)

#         #train face detection

#         img8=Image.open(r"F:\face recognition\Images\train.jpeg")
#         img8=img8.resize((300,300),Image.ANTIALIAS)
#         self.photoimg8=ImageTk.PhotoImage(img8)

#         b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.TRAIN)
#         b1.place(x=150,y=580,width=300,height=300)

#         b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.TRAIN,font=("times new roman",15,"bold"),bg="blue",fg="white")
#         b1_1.place(x=150,y=881,width=300,height=40)

#         #photos face button

#         img9=Image.open(r"F:\face recognition\Images\bg.jpeg")
#         img9=img9.resize((300,300),Image.ANTIALIAS)
#         self.photoimg9=ImageTk.PhotoImage(img9)

#         b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_photo)
#         b1.place(x=600,y=580,width=300,height=300)

#         b1_1=Button(bg_img,text="Photos Storage",cursor="hand2",command=self.open_photo,font=("times new roman",15,"bold"),bg="blue",fg="white")
#         b1_1.place(x=600,y=881,width=300,height=40)

#         #Developer button

#         img10=Image.open(r"F:\face recognition\Images\backg.jpeg")
#         img10=img10.resize((300,300),Image.ANTIALIAS)
#         self.photoimg10=ImageTk.PhotoImage(img10)

#         b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
#         b1.place(x=1050,y=580,width=300,height=300)

#         b1_1=Button(bg_img,text="Developer Details",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
#         b1_1.place(x=1050,y=881,width=300,height=40)
        
#         #Exit button

#         img11=Image.open(r"F:\face recognition\Images\exit.jpeg")
#         img11=img11.resize((300,300),Image.ANTIALIAS)
#         self.photoimg11=ImageTk.PhotoImage(img11)

#         b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
#         b1.place(x=1500,y=580,width=300,height=300)

#         b1_1=Button(bg_img,text="Exit Or Return",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
#         b1_1.place(x=1500,y=881,width=300,height=40)
        
        
        
#     def open_photo(self):
#         os.startfile("fphotos")
#         # ======================================functions buttons==========================================================
#     def stud(self):
#             self.new_window=Toplevel(self.root)
#             self.app=Student(self.new_window)
#     def chat(self):
#             self.new_window=Toplevel(self.root)
#             self.app=Chatbot(self.new_window)
    
#     def TRAIN(self):
#             self.new_window=Toplevel(self.root)
#             self.app=Train(self.new_window)
                 
#     def FACE_DATA(self):
#             self.new_window=Toplevel(self.root)
#             self.app=Face_recoginition(self.new_window)
#     def attendance(self):
#             self.new_window=Toplevel(self.root)
#             self.app=Attendance(self.new_window)
            
# if __name__=="__main__":
#     root=Tk()
#     a=face_recog_sys(root)
#     root.mainloop()






# Actual revised code starts here
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os

# Import the user-provided modules
from chatbot import Chatbot
from student import Student
from train import Train
from face import Face_recoginition
from attend import Attendance

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("FACE RECOGNITION SYSTEM")
        # Sets the window to a "zoomed" state, making it full-screen and responsive
        self.root.state('zoomed')

        # List to hold references to PhotoImage objects to prevent garbage collection
        self.photos = []

        # Assuming images are in a subdirectory named 'Images'
        self.image_dir = 'Images'
        
        # --- Create a main frame to contain all widgets ---
        main_frame = Frame(self.root)
        main_frame.pack(fill=BOTH, expand=True)

        # Configure rows and columns to be resizable with the window
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(0, weight=1)
        
        # --- Top banners using a Grid layout ---
        header_frame = Frame(main_frame)
        header_frame.grid(row=0, column=0, sticky="ew")

        # Configure columns for the three top images
        header_frame.columnconfigure(0, weight=1)
        header_frame.columnconfigure(1, weight=1)
        header_frame.columnconfigure(2, weight=1)

        # Image 1
        self.load_and_place_image(header_frame, 'stud.jpeg', 0)
        # Image 2
        self.load_and_place_image(header_frame, 'images.jpg', 1)
        # Image 3
        self.load_and_place_image(header_frame, 'mach.jpeg', 2)

        # --- Main title placed in a separate frame ---
        title_frame = Frame(main_frame)
        title_frame.grid(row=1, column=0, pady=20)
        title_label = Label(title_frame, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",
                            font=("times new roman", 40, "bold"), fg="red")
        title_label.pack()
        
        # --- Button grid frame ---
        button_frame = Frame(main_frame)
        button_frame.grid(row=2, column=0, pady=20)

        # Configure columns for the button grid
        for i in range(4):
            button_frame.columnconfigure(i, weight=1, uniform="buttons")
        for i in range(2):
            button_frame.rowconfigure(i, weight=1, uniform="buttons")

        # Button data organized in a list for easy management
        self.button_data = [
            {'text': 'Student Details', 'image': 'stud.jpeg', 'command': self.open_student},
            {'text': 'Face Detector', 'image': 'recog.jpeg', 'command': self.open_face_data},
            {'text': 'Attendance Creator', 'image': 'img.jpeg', 'command': self.open_attendance},
            {'text': 'Help Desk', 'image': 'help.jpeg', 'command': self.open_chat},
            {'text': 'Train Data', 'image': 'train.jpeg', 'command': self.open_train},
            {'text': 'Photos Storage', 'image': 'bg.jpeg', 'command': self.open_photo_folder},
            {'text': 'Developer Details', 'image': 'backg.jpeg', 'command': self.open_developer},
            {'text': 'Exit', 'image': 'exit.jpeg', 'command': self.root.destroy},
        ]

        # Dynamically create buttons from the list
        for i, data in enumerate(self.button_data):
            row = i // 4
            col = i % 4
            self.create_button(button_frame, row, col, data)
            
    def load_and_place_image(self, parent_frame, filename, column):
        """Loads and resizes an image, then places it in the parent frame."""
        try:
            image_path = os.path.join(self.image_dir, filename)
            img = Image.open(image_path)
            
            # Use Image.LANCZOS for better resizing quality
            img = img.resize((300, 100), Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            self.photos.append(photo) # Keep a reference

            label = Label(parent_frame, image=photo)
            label.grid(row=0, column=column, sticky="ew")
        except FileNotFoundError:
            print(f"Error: Image file not found at {image_path}")
            
    def create_button(self, parent_frame, row, col, data):
        """Creates a button with an image and text."""
        try:
            image_path = os.path.join(self.image_dir, data['image'])
            img = Image.open(image_path)
            img = img.resize((150, 150), Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            self.photos.append(photo) # Keep a reference

            btn_frame = Frame(parent_frame)
            btn_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

            btn_img = Button(btn_frame, image=photo, command=data['command'], cursor="hand2")
            btn_img.pack()

            btn_text = Button(btn_frame, text=data['text'], command=data['command'], cursor="hand2",
                              font=("times new roman", 12, "bold"), bg="blue", fg="white")
            btn_text.pack(fill=X)
        except FileNotFoundError:
            print(f"Error: Image file not found at {image_path}")

    # --- Functions to open new windows from imported modules ---
    def open_student(self):
        new_window = Toplevel(self.root)
        Student(new_window)

    def open_face_data(self):
        new_window = Toplevel(self.root)
        Face_recoginition(new_window)

    def open_attendance(self):
        new_window = Toplevel(self.root)
        Attendance(new_window)

    def open_chat(self):
        new_window = Toplevel(self.root)
        Chatbot(new_window)

    def open_train(self):
        new_window = Toplevel(self.root)
        Train(new_window)
    
    def open_photo_folder(self):
        """Opens the 'photos' folder."""
        folder_path = 'fphotos'
        if os.path.exists(folder_path):
            os.startfile(folder_path)
        else:
            print(f"Error: Folder not found at {folder_path}")
    
    def open_developer(self):
        # Placeholder for developer details window
        new_window = Toplevel(self.root)
        Label(new_window, text="Developer Details Coming Soon!").pack(pady=20)


if __name__ == "__main__":
    root = Tk()
    app = FaceRecognitionSystem(root)
    root.mainloop()
