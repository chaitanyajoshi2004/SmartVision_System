from tkinter import*
from tkinter import ttk
from tkinter.font import BOLD
from PIL import Image,ImageTk

class Chatbot:
    def __init__(self,Root):
        self.root=Root
        self.root.title("ChatBot")
        self.root.geometry("900x700+0+0")
        self.root.wm_iconbitmap("hack.ico")


        main_frame=Frame(self.root,bd=4,bg='powder blue',width=660)
        main_frame.pack()

        imgchat=Image.open("stud.jpeg")
        imgchat=imgchat.resize((200,70),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(imgchat)

        Titlelab=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,compound=LEFT,image=self.photoimg,text='WLECOME TO AN AI BOT ',font=("times new roman",30,BOLD),fg="red",bg="white")
        Titlelab.pack(side=TOP)



        self.scrolly=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=3,relief=RAISED,font=('arial',14),yscrollcommand=self.scrolly.set)
        self.scrolly.pack(side=RIGHT,fill=Y)
        self.text.pack()



        btn_frame=Frame(self.root,bd=4,bg='white',width=610)
        btn_frame.pack()



        label1=Label(btn_frame,text="ASK YOUR QUESTION HERE",font=('arial',14,'bold'),fg='green',bg='white')
        label1.grid(row=0,column=0,padx=5,sticky=W)

        self.entry=ttk.Entry(btn_frame,width=40,font=('times new roman',14,'bold'))
        self.entry.grid(row=0,column=1,padx=5,sticky=W)


        self.send=Button(btn_frame,text="SEND",command=self.send,font=('arial',15,'bold'),width=8,bg='green')
        self.send.grid(row=0,column=2,padx=5,sticky=W)


        self.clear=Button(btn_frame,text="CLEAR CHAT",font=('arial',15,'bold'),width=15,bg='red',fg="white")
        self.clear.grid(row=1,column=0,padx=5,sticky=W)

        self.msg=''
        self.label11=Label(btn_frame,text=self.msg,font=('arial',14,'bold'),fg='red',bg='white')
        self.label11.grid(row=0,column=0,padx=5,sticky=W)
        


        
    def send(self):
        send='\t\t\t'+'You :'+self.entry.get()
        self.text.insert(END,'\n'+send)


        if(self.entry.get()==''):
            self.msg="Please enter some input"
            self.label11.config(text=self.msg,fg='red')
        
        else:
            self.msg=''
            self.label11.config(text=self.msg,fg='red')


        if(self.entry.get()=='Hey'):
            self.text.insert(END,'\n\n'+'Bot : Hey......')

        
if __name__ == "__main__":
    root=Tk()
    a=Chatbot(root)
    root.mainloop()