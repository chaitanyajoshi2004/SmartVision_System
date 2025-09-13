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
# from simple_facerec import SimpleFacerec
import pyttsx3 as text_speech
import datetime


class Face_recoginition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recogition System")
        self.root.wm_iconbitmap("hack.ico")

        title_lb1=Label(self.root,text="FACE RECOGNITION ",font=("times new roman",35,"bold"),bg="red",fg="white")
        title_lb1.place(x=0,y=0,width=1530,height=45)
        
        img_top1=Image.open(r"F:\face recognition\Images\recog.jpeg")
        img_top1=img_top1.resize((750,700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top1)
        
        f_lb1=Label(self.root,image=self.photoimg_top)
        f_lb1.place(x=0,y=55,width=750,height=700)
        
        
        img_bottom=Image.open(r"F:\face recognition\Images\detect.jpeg")
        img_bottom=img_bottom.resize((800,700),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        
        f_lb1=Label(self.root,image=self.photoimg_bottom)
        f_lb1.place(x=750,y=55,width=800,height=700)
        
        
        btn_1=Button(f_lb1,text="DETECT FACE",cursor="hand2",command=self.recog,font=("times new roman",20,"bold"),bg="red",fg="white")
        btn_1.place(x=300,y=620,width=200,height=40)
        
        
        # =========================================face Face_recoginition=====================================
        
    def recog(self):
            def ex(img,Classfier,scaleFactor,min_neighbours,color,text,clf):
                gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                features=Classfier.detectMultiScale(gray_image,scaleFactor,min_neighbours)  
                
                coord=[]
                
                for (x,y,w,h) in features:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,200),2)
                    id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                    conf=int((100*(1-predict/300)))
                    
                    conn=mysql.connector.Connect(host="localhost",user="root",passwd="12345678910",database="test")
                    mycursor=conn.cursor()
                    mycursor.execute("select Student_name from student where Student_id="+str(id))
                    fetch1=mycursor.fetchone()
                    fetch1="+".join(fetch1)
                    
                    # conn=mysql.connector.Connect(host="localhost",user="root",passwd="12345678910",database="test")
                    # mycursor=conn.cursor()
                    # mycursor.execute("select Enrollment_no from student where Student_id="+str(id))
                    # fetch2=mycursor.fetchone()
                    # fetch2="+".join(fetch2)
                    
                    # conn=mysql.connector.Connect(host="localhost",user="root",passwd="12345678910",database="test")
                    # mycursor=conn.cursor()
                    # mycursor.execute("select Gender from student where Student_id="+str(id))
                    # fetch3=mycursor.fetchone()
                    # fetch3="+".join(fetch3)
                    
                    # conn=mysql.connector.Connect(host="localhost",user="root",passwd="12345678910",database="test")
                    # mycursor=conn.cursor()
                    # mycursor.execute("select Department from student where Student_id="+str(id))
                    # fetch4=mycursor.fetchone()
                    # fetch4="+".join(fetch4)
                    
                    # conn=mysql.connector.Connect(host="localhost",user="root",passwd="12345678910",database="test")
                    # mycursor=conn.cursor()
                    # mycursor.execute("select Teacher_name from student where Student_id="+str(id))
                    # fetch5=mycursor.fetchone()
                    # fetch5="+".join(fetch5)
                    
                    
                    if conf>75:
                        
                         cv2.putText(img,f" name:{fetch1}",(x,y-35),cv2.FONT_HERSHEY_COMPLEX,1.0,(0,0,200),1)
                        #  cv2.putText(img,f"Gender:{fetch3}",(x,y-35),cv2.FONT_HERSHEY_COMPLEX,1.0,(255,0,200),1)
                        #  cv2.putText(img,f"Department:{fetch4}",(x,y-25),cv2.FONT_HERSHEY_COMPLEX,1.0,(255,0,200),1)
                        #  cv2.putText(img,f"Teacher_name:{fetch5}",(x,y-15),cv2.FONT_HERSHEY_COMPLEX,1.0,(255,0,200),1)
                         
                    else:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                        cv2.putText(img,"UNKNOWN FACE",(x,y-15),cv2.FONT_HERSHEY_COMPLEX,1.0,(0,0,200),1)
                    coord=[x,y,w,h]
                return coord
            def recognize(img,clf,faceCascade):
                Coord=ex(img,faceCascade,1.1,10,(0,0,255),"Face",clf)
                return img   
            facecascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.read("Classifier.xml")
            
            video_cap=cv2.VideoCapture(0)
            
            
            while TRUE:
                ret,img=video_cap.read()
                img=recognize(img,clf,facecascade)
                cv2.imshow("WELCOME TO FACE DECTECTION SYSTEM",img)
                
                if cv2.waitKey(1)==13:
                    break
            video_cap.release()
            cv2.destroyAllWindows()
    # Encode faces from a folder

        # def s():
        #     # a=face_names
        #     # for a in face_names:
        #     #     engine=text_speech.init()
        #     #     engine.say("welcome to class"+name)
        #     #     engine.runAndWait()
        #     #     engine.stop()
        #         break
        
                
    
       
        # cap = cv2.VideoCapture(0)
        # ret,frame = cap.read()
        # face_locations, face_names = sfr.detect_known_faces(frame)
        # for c in range(1):
        #         for face_loc, name in zip(face_locations, face_names):
        #             a=name
        #             engine=text_speech.init()
        #             engine.say("welcome to class"+name)
        #             engine.runAndWait()
        #             engine.stop()
        #             break
        # Load Camera
       
        # cap = cv2.VideoCapture(0)
        # ret, frame = cap.read()
        # Detect Faces
        # face_locations, face_names = sfr.detect_known_faces(frame)
        # for c in range(1):
        #     for face_loc, name in zip(face_locations, face_names):
        #         a=name
        #         engine=text_speech.init()
        #         engine.say("welcome to class"+name)
        #         engine.runAndWait()
        #         engine.stop()
        #         break
            
        
        # for face_loc, name in zip(face_locations, face_names):
        #     y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        #     cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 200,0 ), 1)
        #     cv2.rectangle(frame, (x1, y1), (x2, y2), (200, 0, 0), 1)
        
        # cv2.imshow("Frame", frame)
    #     key = cv2.waitKey(1)

    #     if key == 13:
    #         break


    # cap.release()
    # cv2.destroyAllWindows()
    # video_cap=cv2.VideoCapture(0)
   
    # while TRUE:

    #     ret,frame=video_cap.read()
    #     cv2.imshow("WELCOME TO FACE DECTECTION SYSTEM",frame)     
    #     if cv2.waitKey(1)==13:
    #              break
    # video_cap.release()
    # cv2.destroyAllWindows()
        
                      
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=Face_recoginition(root)
    root.mainloop()