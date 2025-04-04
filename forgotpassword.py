import tkinter as tk
import os
from tkinter import messagebox as mb
def fopa():
    root=tk.Tk()
    root.title('Forgot Password')
    root.geometry("750x500")

    lbl=tk.Label(root,text='Forgot Password  ?',font=('Times','25'))
    lbl.place(x=10,y=10)

    lbl=tk.Label(root,text='Enter Your Username',font=('Times','25'))
    lbl.place(x=30,y=60)

    btn=tk.Entry(root,font=('Times','15'))
    btn.place(x=50,y=120)

    lbl=tk.Label(root,text='Enter Your Registered Phone Number',font=('Times','25'))
    lbl.place(x=50,y=160)

    bt=tk.Entry(root,font=('Times','15'))
    bt.place(x=50,y=210)
    a='normal'
    def pas():
        global a
        username1 = btn.get()
        print(username1)
        phoneno= bt.get()
        print(phoneno)
        #pat=r'D:/Python/Created/Self/Cs Project/signin/'
        list_of_files = os.listdir()
        if username1 in list_of_files:
            file1 = open(username1, "r")
            verify = file1.read().splitlines()
            if phoneno in verify:
                b=tk.Label(root,font=('Times','15'),text='Your Password is')
                b.place(x=180,y=350)
                lbl=tk.Label(root,text=verify[2],font=('Times','25'))
                lbl.place(x=200,y=380)
                a='disabled'
                b=tk.Button(root,font=('Times','20'),text='Show Password',stat=a,command=pas)
                b.place(x=180,y=260)
            else:
                msgbox = mb.showerror("Error", "Phone Number not Matched")
        else:
            msgbox = mb.showerror("Invalid", "Incorrect username")
        
    b=tk.Button(root,font=('Times','20'),text='Show Password',stat=a,command=pas)
    b.place(x=180,y=260)



