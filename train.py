from array import array
from tkinter import *
from tkinter import ttk
from turtle import title
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np




class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recogition System")
        self.root.wm_iconbitmap("hack.ico")


        title_lb1=Label(self.root,text="TRIAN DATASET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lb1.place(x=0,y=0,width=1530,height=45)

        img_top1=Image.open(r"F:\face recognition\Images\recog.jpeg")
        img_top1=img_top1.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top1)
        
        f_lb1=Label(self.root,image=self.photoimg_top)
        f_lb1.place(x=0,y=55,width=1530,height=325)



        btn_1=Button(self.root,text="TRAIN DATA",cursor="hand2",command=self.train_classifier,font=("times new roman",28,"bold"),bg="red",fg="white")
        btn_1.place(x=0,y=380,width=1530,height=60)




        img_bottom=Image.open(r"F:\face recognition\Images\train.jpeg")
        img_bottom=img_bottom.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        
        f_lb1=Label(self.root,image=self.photoimg_bottom)
        f_lb1.place(x=0,y=440,width=1530,height=325)


    def train_classifier(self):
        data_dir=("fphotos")
        path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]



        faces=[]
        ids=[]


        for image in path:
            # grayscale image
            img=Image.open(image).convert('L')
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[-1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13

        ids=np.array(ids)



        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("Classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","training Dataset Completed !!!")


if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()