import cv2
from simple_facerec import SimpleFacerec
import pyttsx3 as text_speech
import datetime
from datetime import datetime
import mysql.connector
# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("image/")

# Load Camera
cap = cv2.VideoCapture(0)

        


while True:

    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
   
    for face_loc, name in zip(face_locations, face_names):
    #     a=name
    # if(( a==name)):
    #     engine=text_speech.init()
    #     engine.say("welcome to class"+name)
    #     engine.runAndWait()
    #     engine.stop()
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 200,0 ), 1)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 200, 0), 1)
        def mark_attendance(name):
            
            with open("mega.csv","r+",newline="\n")as f:
                mydatalist=f.readlines()
                name_list=[]
                for line in mydatalist:
                    entry=line.split((","))  
                    name_list.append(entry[0])
                    now=datetime.now()
                    d1=now.strftime("%d/%m/%Y")
                    dtstring=now.strftime("%H:%M:%S")
                    
                if((name not in name_list)):
                    f.writelines(f"\n{name},present")
                if((name not in name_list)):
                    engine=text_speech.init()
                    engine.say("welcome to class"+name)
                    engine.runAndWait()
                    engine.stop()
        mark_attendance(name)
               
        

    # a=name
    # if(( a==name)):
    #     engine=text_speech.init()
    #     engine.say("welcome to class"+name)conn=mysql.connector.Connect(host="localhost",user="root",passwd="12345678910",database="face_recognizer")
                   
    #     engine.runAndWait()
    #     engine.stop()


    cv2.imshow("Frame", frame)


    key = cv2.waitKey(1)

    if key == 13:
        break


cap.release()
cv2.destroyAllWindows()



 
            #     # f.writelines("Student_id,Roll-no,Date,Time,Attendance")
            # if((i not in name_list) and  (r not in name_list) and  (d not in name_list)):
            #     engine=text_speech.init()
            #     engine.say("welcome to class"+i)
            #     engine.runAndWait()
            #     engine.stop()