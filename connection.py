
# import mysql.connector 
# conn=mysql.connector.Connect(host="localhost",user="id20439429_student",passwd="12345678910_Abc",database="id20439429_face_recognizer")


# if conn.is_connected():
#     print("successfully connected")  
#     mycursor=conn.cursor()
#     mycursor.execute("select * from trial ")
#     a=mycursor.fetchone()
#     # b=mycursor.fetchall()
#     print(a)      
# else:
#     print("error")

# # # # import face_recognition
# # # # import cv2

# # # import random

# from twilio.rest import Client

# # Your Twilio account SID and auth token
# account_sid = 'ACf8fc24c2f608b089cf14a20f2ba53484'
# auth_token = '7b1e3d4d6873def50aa45a4a621d6346'

# # The Twilio phone number to send the SMS from
# twilio_number = '+918830897171'

# # # # Get the mobile number to send the OTP to from the user
# # # mobile_number = input('Enter your mobile number: ')

# # # # Generate a random 6-digit OTP
# # # otp = str(random.randint(100000, 999999))

# # # # Send the OTP to the mobile number using the Twilio API
# # # client = Client(account_sid, auth_token)
# # # message = client.messages.create(
# # #     body='Your OTP is ' + otp,
# # #     from_=twilio_number,
# # #     to=mobile_number
# # # )

# # # # Print the message SID
# # # print('OTP sent. Message SID:', message.sid)



# # import os
# # from twilio.rest import Client

# # # Set environment variables for your credentials
# # # Read more at http://twil.io/secure
# # account_sid = "ACf8fc24c2f608b089cf14a20f2ba53484"
# # auth_token = "7b1e3d4d6873def50aa45a4a621d6346"
# # verify_sid = "VA4dbbfa216402a455167a0d4d52de1ee9"
# # verified_number = "+919021657398"

# # client = Client(account_sid, auth_token)

# # verification = client.verify.v2.services(verify_sid) \
# #   .verifications \
# #   .create(to=verified_number, channel="sms")
# # print(verification.status)

# # otp_code = input("Please enter the OTP:")

# # verification_check = client.verify.v2.services(verify_sid) \
# #   .verification_checks \
# #   .create(to=verified_number, code=otp_code)
# # print(verification_check.status)


# # import pywhatkit
# # pywhatkit.sendwhatmsg("+919021657398","hiiiiii",21,46)



import tkinter as tk
from twilio.rest import Client

# Twilio Account SID and Auth Token
account_sid = "ACf8fc24c2f608b089cf14a20f2ba53484"
auth_token = "7b1e3d4d6873def50aa45a4a621d6346"

# create a Twilio client object
client = Client(account_sid, auth_token)

# GUI application
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # username label and entry
        self.username_label = tk.Label(self, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        # password label and entry
        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        # OTP label and entry
        self.otp_label = tk.Label(self, text="OTP:")
        self.otp_label.pack()
        self.otp_entry = tk.Entry(self)
        self.otp_entry.pack()

        # submit button
        self.submit_button = tk.Button(self, text="Submit", command=self.submit)
        self.submit_button.pack()

    def submit(self):
        # get the username, password, and OTP from the entries
        username = self.username_entry.get()
        password = self.password_entry.get()
        otp = self.otp_entry.get()

        # validate the username, password, and OTP
        if username == "" or password == "" or otp == "":
            tk.messagebox.showerror("Error", "Please enter all fields.")
            return
        elif username != "example_user" or password != "example_password" or otp != "123456":
            tk.messagebox.showerror("Error", "Invalid credentials.")
            return

        # send the OTP via Twilio
        message = client.messages.create(
            body=f"Your OTP is {otp}",
            from_="",
            to=""
        )

        # print the message SID to the console
        print(message.sid)

        # show success message
        tk.messagebox.showinfo("Success", "OTP sent successfully.")

        # clear the entries
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.otp_entry.delete(0, tk.END)

# create the root window
root = tk.Tk()
root.title("Twilio OTP Validation")

# create the application instance
app = Application(master=root)

# run the application
app.mainloop()


# # import tkinter as tk
# # from twilio.rest import Client

# # # Set up the Twilio API client
# # account_sid = 'ACf8fc24c2f608b089cf14a20f2ba53484'
# # auth_token = '7b1e3d4d6873def50aa45a4a621d6346'
# # client = Client(account_sid, auth_token)

# # # Define the GUI
# # root = tk.Tk()
# # root.geometry('350x250')
# # root.title('OTP Verification')

# # # Define the function to send OTP
# # def send_otp():
# #     receiver_number = receiver_entry.get()
# #     verification = client.verify.services('VA4dbbfa216402a455167a0d4d52de1ee9').verifications.create(to=receiver_number, channel='sms')
# #     otp_status_label.config(text='OTP Sent!', fg='green')

# # # Define the function to verify the OTP
# # def verify_otp():
# #     entered_otp = otp_entry.get()
# #     receiver_number = receiver_entry.get()
# #     try:
# #         verification_check = client.verify.services('VA4dbbfa216402a455167a0d4d52de1ee9').verification_checks.create(to=receiver_number, code=entered_otp)
# #         if verification_check.status == 'approved':
# #             otp_status_label.config(text='OTP Verified!', fg='green')
# #         else:
# #             otp_status_label.config(text='OTP Verification Failed!', fg='red')
# #     except:
# #         otp_status_label.config(text='Invalid OTP or Phone Number!', fg='red')

# # # Add GUI elements
# # receiver_label = tk.Label(root, text='Enter Receiver Phone Number:')
# # receiver_label.pack(pady=5)
# # receiver_entry = tk.Entry(root)
# # receiver_entry.pack()
# # send_otp_button = tk.Button(root, text='Send OTP', command=send_otp)
# # send_otp_button.pack(pady=5)
# # otp_label = tk.Label(root, text='Enter OTP:')
# # otp_label.pack(pady=5)
# # otp_entry = tk.Entry(root)
# # otp_entry.pack()
# # verify_button = tk.Button(root, text='Verify', command=verify_otp)
# # verify_button.pack(pady=5)
# # otp_status_label = tk.Label(root, text='')
# # otp_status_label.pack(pady=5)

# # # Start the GUI
# # root.mainloop()



# # Download the helper library from https://www.twilio.com/docs/python/install
# # import os
# # from twilio.rest import Client

# # # Set environment variables for your credentials
# # # Read more at http://twil.io/secure
# # account_sid = "AC0d33b7a6b985c7ecfd27a1dc9417d21c"
# # auth_token = "aece763bb2aacf7bab861fd7238a0ef2"
# # verify_sid = "VAaf9cc284f3b00ead4146190cde367a4f"
# # verified_number = "+919021657398"

# # client = Client(account_sid, auth_token)

# # verification = client.verify.v2.services(verify_sid) \
# #   .verifications \
# #   .create(to=verified_number, channel="sms")
# # print(verification.status)

# # otp_code = input("Please enter the OTP:")

# # verification_check = client.verify.v2.services(verify_sid) \
# #   .verification_checks \
# #   .create(to=verified_number, code=otp_code)
# # print(verification_check.status)


# import cv2
# import tkinter as tk

# import pyttsx3

# # Initialize the text-to-speech engine
# engine = pyttsx3.init()

# # Define the function to detect the face and output the name
# def detect_face():
#     # Load the pre-trained face detection model
#     face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
#     # Start the webcam
#     cap = cv2.VideoCapture(0)
#     cap.set(cv2.CAP_PROP_FPS,30)
#     cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
#     cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
    
#     while True:
#         # Read a frame from the webcam
#         ret, frame = cap.read()
        
#         # Convert the frame to grayscale
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
#         # Detect faces in the grayscale frame
#         faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
#         # Loop through the detected faces
#         for (x, y, w, h) in faces:
#             # Draw a rectangle around the detected face
#             cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
#             # Get the name from the user input
#             name = name_input.get()
            
#             # Output the name as voice
#             engine.say(f'Hello {name}! I can see your face.')
#             engine.runAndWait()
        
#         # Display the webcam feed
#         cv2.imshow('Webcam', frame)
        
#         # Stop the program if the 'q' key is pressed
#         if cv2.waitKey(1) == 13:
#             break
    
#     # Release the webcam and close the window
#     cap.release()
#     cv2.destroyAllWindows()

# # Create the Tkinter GUI window
# root = tk.Tk()
# root.title('Face Detection')

# # Create the label and input field for the name
# name_label = tk.Label(root, text='Enter your name:')
# name_label.pack()
# name_input = tk.Entry(root)
# name_input.pack()

# # Create the button to start the face detection
# detect_button = tk.Button(root, text='Detect Face', command=detect_face)
# detect_button.pack()

# # Run the GUI window
# root.mainloop()


# import pymysql
# import cryptography

# # Connect to the MySQL database
# # connection = pymysql.connect(
# #     host='localhost',
# #     # port=your_port_number,
# #     user='id20439429_student',
# #     password='12345678910_Abc',
# #     db='id20439429_face_recognizer'
# # )

# # # Create a cursor object
# # cursor = connection.cursor()

# # # Execute an SQL query
# # cursor.execute("SELECT * FROM student")

# # # Fetch the results of the query
# # results = cursor.fetchall()

# # # Print out the results
# # for row in results:
# #     print(row)

# # # Close the cursor and the database connection
# # cursor.close()
# # connection.close()


# import sqlite3
# con =sqlite3.connect("My_student.db")

# import mysql.connector

# # Replace the placeholders with your database credentials
# cnx = mysql.connector.connect(user='id20439429_student', password='12345678910_Abc',
#                               host='localhost', database='id20439429_face_recognizer')



# cursor = cnx.cursor()
# cursor.execute('SELECT * FROM student')
# results = cursor.fetchall()
# cursor.close()
# cnx.close()

# import pymysql

# connection=pymysql.connect(user='chaitanya', password='12345678910_Abc',host='localhost', database='chaitanya',charset='utf8',cursorclass=pymysql.cursors.DictCursor)
# with connection.cursor() as cursor:
#     sql="SELECT * FROM student"
#     cursor.execute(sql)
#     result=cursor.fetchall()
#     print(result)