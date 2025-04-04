#OM sri sai ram

import tkinter as tk
import datetime
import time
from PIL import Image,ImageTk
from tkinter import messagebox as mb
import os
#from read import user
#main window
root=tk.Tk()
root.title('User Friendly Framework')
root.geometry("750x500")
now=datetime.datetime.now()
#display date and time

# Creating first screen canvas
canvas1 = tk.Canvas(root,bg='grey',height=500,width=750)
canvas1.pack()
btn_img = ImageTk.PhotoImage(file=r"files\1.png")
canvas = tk.Label(canvas1,bg='white',height=500,width=750,image=btn_img)
canvas.place(x=0,y=0)


def clock():
    
    t=time.strftime('%I:%M:%S',time.localtime())
    if t!='':
        label1.config(text=t,font='times 15',)
    root.after(100,clock)
    
label1=tk.Label(canvas1,justify='center')
label1.place(x=600,y=25)
t=time.strftime('%Y-%m-%d',time.localtime())
label=tk.Label(canvas1,text=t,font='times 15',)
label.place(x=600,y=75)
clock()

#Welcome
#bt_im = ImageTk.PhotoImage(file=r"files\welcome.png")
#btn = tk.Label(canvas1, text = "Welcome!",font = ("Calibri",25), fg ="red",state = "normal",image=bt_im)
#btn.place(x=50,y=25)

#User name 
#btn1 = tk.Label(canvas1, text = "User Name",font = ("Calibri",25), state = "normal")
#btn1.place(x=100,y=100)
etn = tk.Entry( canvas1,selectbackground = "red", selectforeground = "white",font=('calibri',20))
etn.place(x = 320, y = 125)

#password
#btn = tk.Label(canvas, text = "Password",font = ("Calibri",25), state = "normal")
#btn.place(x=100,y=200)
etnp = tk.Entry( canvas1,selectbackground = "red", selectforeground = "white",font=('calibri',20),show='*')
etnp.place(x = 320, y = 220)
bt_i = ImageTk.PhotoImage(file=r"files\shps.png")
def see():
    etnp.config(show='')
    btn1.config(state='disabled')
    btn2.config(state='normal')
btn1 = tk.Button(canvas1, text = "Welcome!",font = ("Calibri",25), fg ="red",state = "normal",image=bt_i,command=see)
btn1.place(x=515,y=222)
bt_im = ImageTk.PhotoImage(file=r"files\dshps.jpg")
def hide():
    etnp.config(show='*')
    btn1.config(state='normal')
    btn2.config(state='disabled')
btn2 = tk.Button(canvas1, text = "Welcome!",font = ("Calibri",25), fg ="red",state = "disabled",image=bt_im,command=hide)
btn2.place(x=560,y=222)
#forgot Password
def forgo():
    import forgotpassword
    forgotpassword.fopa()
btn = tk.Button(canvas1, text="Forgot Password",font = ("Calibri",15), state = "normal",command=forgo)
btn.place(x=100,y=300)
#new account
def create():
    import createnew
    createnew.create()

btn = tk.Button(canvas1, text = "Create a new account",font = ("Calibri",12), state = "normal",command=create)
btn.place(x=500,y=300)

#login
username1=''
def login():
    global username1
    username1 = etn.get()
    print(username1)
    password1= etnp.get()
    print(password1)
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            print(verify)
            if 'MCAE' in verify:
                root.destroy()
                import studentcae
                studentcae.student(verify[0])
                
            elif 'MCBP' in verify:
                root.destroy()
                import studentmpc
                studentmpc.student(verify[0])
            else:
                msgbox = mb.showerror("Invalid", "Incorrect Password")
    else:
        msgbox = mb.showerror("Invalid", "Enter valid Username and Password")

btn = tk.Button(canvas1, text = "LOGIN",font = ("Calibri",28), state = "normal",command=login)
btn.place(x=300,y=350)
root.mainloop()
