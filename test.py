import cv2
import mysql.connector
import numpy as np

# # Open a connection to the MySQL database
# connection = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='12345678910',
#     database='face_recognizer'
# )

# # Create a table to store the images
# cursor = connection.cursor()
# # cursor.execute('CREATE TABLE Test_images (id INT AUTO_INCREMENT PRIMARY KEY, image BLOB)')

# # Initialize the camera
# camera = cv2.VideoCapture(0)

# # Start capturing images
# while True:
#     # Capture an image from the camera

#     # Convert the image to a byte array for storage in the database
#     image_data = np.asarray(frame)
#     image_data = cv2.imencode('.jpg', image_data)[1].tostring()

#     # Insert the image data into the database
#     cursor = connection.cursor()
#     query = 'INSERT INTO Test_images (image) VALUES (%s)'
#     cursor.execute(query, (image_data,))
#     connection.commit()

#     # Display the captured image
#     cv2.imshow('image', frame)

#     # Exit if the 'q' key is pressed
#     if cv2.waitKey(1) == ord('q'):
#         break

# # Release the camera and close the database connection
# camera.release()
# cv2.destroyAllWindows()
# connection.close()

# import tkinter as tk
# import csv


# class UpdateCSVApp(tk.Frame):
#     def _init_(self, master=None):
#         super()._init_(master)
#         self.master = master
#         self.pack()
#         self.create_widgets()

#     def create_widgets(self):
#         # Create the entry fields
#         self.name_label = tk.Label(self, text='Name:')
#         self.name_entry = tk.Entry(self)
#         self.time_label = tk.Label(self, text='Time:')
#         self.time_entry = tk.Entry(self)
#         self.date_label = tk.Label(self, text='Date:')
#         self.date_entry = tk.Entry(self)
#         self.department_label = tk.Label(self, text='Department:')
#         self.department_entry = tk.Entry(self)
#         self.name_label.grid(row=0, column=0, padx=10, pady=5)
#         self.name_entry.grid(row=0, column=1, padx=10, pady=5)
#         self.time_label.grid(row=1, column=0, padx=10, pady=5)
#         self.time_entry.grid(row=1, column=1, padx=10, pady=5)
#         self.date_label.grid(row=2, column=0, padx=10, pady=5)
#         self.date_entry.grid(row=2, column=1, padx=10, pady=5)
#         self.department_label.grid(row=3, column=0, padx=10, pady=5)
#         self.department_entry.grid(row=3, column=1, padx=10, pady=5)
        
#         # Create the OK and Cancel buttons
#         self.ok_button = tk.Button(self, text='OK', command=self.ok)
#         self.cancel_button = tk.Button(self, text='Cancel', command=self.cancel)
#         self.ok_button.grid(row=4, column=0, padx=10, pady=5)
#         self.cancel_button.grid(row=4, column=1, padx=10, pady=5)
        
#     def ok(self):
#         # Open the existing CSV file in append mode
#         with open('mega.csv', 'a', newline='') as csvfile:
#             writer = csv.writer(csvfile)
            
#             # Write the data from the entry fields to the CSV file
#             name = self.name_entry.get()
#             time = self.time_entry.get()
#             date = self.date_entry.get()
#             department = self.department_entry.get()
#             writer.writerow([name, time, date, department])
            
#         # Destroy the window
#         self.master.destroy()
        
#     def cancel(self):
#         # Destroy the window
#         self.master.destroy()


# if __name__ == '__main__':
#     root = tk.Tk()
#     app = UpdateCSVApp(master=root)
#     app.mainloop()


# import tkinter as tk
# import csv

# class UpdateCSVGUI:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Update CSV")
        
#         # create entry widgets for CSV fields
#         tk.Label(self.master, text="Row number: ").grid(row=0, column=0)
#         self.row_entry = tk.Entry(self.master)
#         self.row_entry.grid(row=0, column=1)
        
#         tk.Label(self.master, text="Name: ").grid(row=1, column=0)
#         self.name_entry = tk.Entry(self.master)
#         self.name_entry.grid(row=1, column=1)
        
#         tk.Label(self.master, text="Time: ").grid(row=2, column=0)
#         self.time_entry = tk.Entry(self.master)
#         self.time_entry.grid(row=2, column=1)
        
#         tk.Label(self.master, text="Date: ").grid(row=3, column=0)
#         self.date_entry = tk.Entry(self.master)
#         self.date_entry.grid(row=3, column=1)
        
#         tk.Label(self.master, text="Department: ").grid(row=4, column=0)
#         self.dept_entry = tk.Entry(self.master)
#         self.dept_entry.grid(row=4, column=1)
        
#         # create button to update CSV
#         update_btn = tk.Button(self.master, text="Update CSV", command=self.update_csv)
#         update_btn.grid(row=5, column=0, columnspan=2, pady=10)
    
#     def update_csv(self):
#         # get data from entry widgets
#         row_num = int(self.row_entry.get())
#         name = self.name_entry.get()
#         time = self.time_entry.get()
#         date = self.date_entry.get()
#         dept = self.dept_entry.get()
        
#         # update CSV file
#         with open('m.csv', 'r') as csv_file:
#             reader = csv.reader(csv_file)
#             rows = list(reader)
        
#         rows[row_num][0] = row_num
#         rows[row_num][1] = name
#         rows[row_num][2] = time
#         rows[row_num][3] = date
#         rows[row_num][4] = dept
        
#         with open('m.csv', 'w', newline='') as csv_file:
#             writer = csv.writer(csv_file)
#             writer.writerows(rows)
            
#         # # clear entry widgets
#         # self.row_entry.delete(0, tk.END)
#         # self.name_entry.delete(0, tk.END)
#         # self.time_entry.delete(0, tk.END)
#         # self.date_entry.delete(0, tk.END)
#         # self.dept_entry.delete(0, tk.END)
        
#         # show message box with confirmation
#         tk.messagebox.showinfo("CSV Updated", "CSV updated successfully.")

# # create main window
# root = tk.Tk()

# # create update CSV GUI
# update_csv_gui = UpdateCSVGUI(root)

# # start GUI event loop
# root.mainloop()

# import tkinter as tk
# import calendar


# class CalendarApp(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.selected_date = None
#         self.pack()
#         self.create_widgets()

#     def create_widgets(self):
#         # Create the calendar
#         year = int(input("enter the year:")) # Change this to set the default year
#         month = int(input("enter the month:"))  # Change this to set the default month
#         self.cal = calendar.monthcalendar(year, month)
        
#         # Create the month and year labels
#         self.month_label = tk.Label(self, text=calendar.month_name[month])
#         self.year_label = tk.Label(self, text=str(year))
#         self.month_label.grid(row=0, column=0, padx=10, pady=5)
#         self.year_label.grid(row=0, column=2, padx=10, pady=5)
        
#         # Create the calendar buttons
#         for i in range(1):
#             day_label = tk.Label(self, text=calendar.day_abbr[i])
#             day_label.grid(row=1, column=i, padx=10, pady=5)
#         for r in range(len(self.cal)):
#             for c in range(7):
#                 if self.cal[r][c] != 0:
#                     date_button = tk.Button(self, text=str(self.cal[r][c]), command=lambda r=r, c=c: self.select_date(r, c))
#                     date_button.grid(row=r+2, column=c, padx=10, pady=5)
#                 else:
#                     date_label = tk.Label(self, text='')
#                     date_label.grid(row=r+2, column=c, padx=10, pady=5)
        
#         # Create the OK and Cancel buttons
#         self.ok_button = tk.Button(self, text='OK', command=self.ok)
#         self.cancel_button = tk.Button(self, text='Cancel', command=self.cancel)
#         self.ok_button.grid(row=len(self.cal)+2, column=2, padx=10, pady=5)
#         self.cancel_button.grid(row=len(self.cal)+2, column=4, padx=10, pady=5)
        
#     def select_date(self, row, col):
#         self.selected_date = (self.cal[row][col], self.month_label['text'], self.year_label['text'])
#         for widget in self.winfo_children():
#             widget.destroy()
#         self.create_widgets()
        
#     def ok(self):
#         if self.selected_date:
#             print('Selected date:', self.selected_date)
#             self.master.destroy()
        
#     def cancel(self):
#         self.master.destroy()


# if __name__ == '__main__':
#     root = tk.Tk()
#     app = CalendarApp(master=root)
#     app.mainloop()

# import tkinter as tk
# from student import Student

# # create a tkinter window
# window = tk.Tk()

# # create labels and entry widgets for input
# year_label = tk.Label(window, text="Enter birth year:")
# year_entry = tk.Entry(window)

# month_label = tk.Label(window, text="Enter birth month:")
# month_entry = tk.Entry(window)

# day_label = tk.Label(window, text="Enter birth day:")
# day_entry = tk.Entry(window)

# # create a label to display the output
# output_label = tk.Entry(window, text="")

# # function to handle button click
# def calculate_age():
#     year = year_entry.get()
#     month = month_entry.get()
#     day = day_entry.get()

#     # calculate age
#     age = str(year+"-"+month+"-"+day)

#     # update output label
#     output_label.config(text=f" {age}")

# # create a button to trigger age calculation
# calculate_button = tk.Button(window, text="Calculate Age", command=calculate_age)

# # grid the widgets
# year_label.grid(row=0, column=0)
# year_entry.grid(row=0, column=1)

# month_label.grid(row=1, column=0)
# month_entry.grid(row=1, column=1)

# day_label.grid(row=2, column=0)
# day_entry.grid(row=2, column=1)

# calculate_button.grid(row=3, column=0)
# output_label.grid(row=3, column=1)

# # start the event loop
# window.mainloop()

# import tkinter as tk
# import pyttsx3
# import speech_recognition as sr

# class ChatBotApp(tk.Tk):
#     def _init_(self, *args, **kwargs):
#         super()._init_(*args, **kwargs)
        
#         # Set up the chatbot screen
#         self.title('ChatBot')
#         self.geometry('400x300')
#         self.resizable(False, False)
        
#         # Set up the text box for displaying the conversation
#         self.conversation_text = tk.Text(self)
#         self.conversation_text.pack(fill='both', expand=True)
#         self.conversation_text.config(state=tk.DISABLED)
        
#         # Set up the input form for the user's query
#         self.input_label = tk.Label(self, text='Enter your query:')
#         self.input_label.pack()
#         self.input_entry = tk.Entry(self)
#         self.input_entry.pack()
#         self.input_entry.focus_set()
        
#         # Set up the voice input button
#         self.voice_button = tk.Button(self, text='Voice input', command=self.get_voice_input)
#         self.voice_button.pack()
        
#         # Set up the submit button for sending the user's query
#         self.submit_button = tk.Button(self, text='Submit', command=self.send_query)
#         self.submit_button.pack()
        
#         # Set up the chatbot engine
#         self.engine = pyttsx3.init()
#         self.engine.setProperty('rate', 150)
#         self.engine.setProperty('voice', 'english')
#         self.conversation_text.insert(tk.END, 'ChatBot: Hi, how can I help you?\n')
    
#     def get_voice_input(self):
#         # Use speech recognition to get the user's query from voice input
#         r = sr.Recognizer()
#         with sr.Microphone() as source:
#             self.conversation_text.insert(tk.END, 'ChatBot: Speak your query.\n')
#             self.update_idletasks()
#             audio = r.listen(source)
#         try:
#             query = r.recognize_google(audio)
#             self.input_entry.delete(0, tk.END)
#             self.input_entry.insert(0, query)
#         except sr.UnknownValueError:
#             self.conversation_text.insert(tk.END, 'ChatBot: Sorry, I could not understand that.\n')
#         except sr.RequestError:
#             self.conversation_text.insert(tk.END, 'ChatBot: Sorry, there was an error processing your request.\n')
    
#     def send_query(self):
#         # Get the user's query from the input form and send it to the chatbot engine
#         query = self.input_entry.get()
#         self.conversation_text.config(state=tk.NORMAL)
#         self.conversation_text.insert(tk.END, 'You: {}\n'.format(query))
#         self.conversation_text.config(state=tk.DISABLED)
#         self.input_entry.delete(0, tk.END)
#         response = self.get_response(query)
#         self.conversation_text.config(state=tk.NORMAL)
#         self.conversation_text.insert(tk.END, 'ChatBot: {}\n'.format(response))
#         self.conversation_text.config(state=tk.DISABLED)
#         self.engine.say(response)
#         self.engine.runAndWait()
    
#     def get_response(self, query):
#         # Generate a response to the user's query
#         if query == 'hello':
#             return 'Hello, how are you?'
#         elif query == 'goodbye':
#             return 'Goodbye, have a nice day!'
#         else:
#             return 'Sorry, I don\'t understand.'
        
# # Create the application
# app = ChatBotApp()

# # Run the event loop
# app.mainloop()



