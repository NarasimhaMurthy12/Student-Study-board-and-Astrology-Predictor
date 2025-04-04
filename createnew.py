stdnt=[]
def create():
    #from usernameandpassword import user
    import tkinter as tk
    from tkinter import messagebox as mb
    import os
    root=tk.Tk()
    root.title('Create a new account')
    root.geometry("750x500")


    canvas = tk.Canvas(root, width = 500, height = 500)
    canvas.pack(fill = "both", expand = True)
    #Welcome
    btn = tk.Label(canvas, text = "Create a new account",font = ("Calibri",25), fg ="red",state = "normal")
    btn.place(x=50,y=25)

    #name
    btn = tk.Label(canvas, text = "Name",font = ("Calibri",25),state = "normal")
    btn.place(x=100,y=100)
    etnn = tk.Entry(canvas, width =50,selectbackground = "red", selectforeground = "white")
    etnn.place(x = 275, y = 120)
    #username
    btn = tk.Label(canvas, text = "Username",font = ("Calibri",25),state = "normal")
    btn.place(x=100,y=150)
    etnu = tk.Entry(canvas, width =50,selectbackground = "red", selectforeground = "white")
    etnu.place(x = 275, y = 170)
    #password
    btn = tk.Label(canvas, text = "Password",font = ("Calibri",25),state = "normal")
    btn.place(x=100,y=200)
    etnp = tk.Entry(canvas, width =50,selectbackground = "red", selectforeground = "white")
    etnp.place(x = 275, y = 220)
    #confirm password
    btn = tk.Label(canvas, text = "Confirm Password",font = ("Calibri",25),state = "normal")
    btn.place(x=100,y=250)
    etnc = tk.Entry(canvas, width =50,selectbackground = "red", selectforeground = "white")
    etnc.place(x = 360, y = 270)
    #phone no.
    btn = tk.Label(canvas, text = "Phone no.",font = ("Calibri",25),state = "normal")
    btn.place(x=100,y=300)
    etnpn = tk.Entry(canvas, width =50,selectbackground = "red", selectforeground = "white")
    etnpn.place(x = 275, y = 320)

    var=tk.StringVar()
    var.set("Group")
    rad_box=tk.Label(canvas,text="Group",font = ("Calibri",25))
    rad_box2=tk.Entry(canvas,text="Science Group")
    a=tk.Label(canvas,text='Science Group or Commerce Group')
    a.place(x=450,y=355)
    rad_box.place(x=100,y=340)
    rad_box2.place(x=290,y=360)
    global stdnt

    #create button
    def cret():
        global stdnt, var
        a=[]
        if etnn.get().isdigit() or etnn.get()=='':
            msgbox = mb.showerror("Invalid", "Enter a valid username")
        else:
           a.append(etnn.get())
        if etnu.get().isalnum:
            a.append(etnu.get())
        if etnp.get().isalnum:
            if etnc.get()==etnp.get():
                a.append(etnp.get())
        elif etnp.get()=='' or etnc.get()=='':
            msgbox = mb.showerror("Password", "Enter the Password")
        if etnpn.get().isdigit() and len((etnpn.get()))==10 :
            a.append(etnpn.get())
        else:
            msgbox = mb.showerror("Invalid", "Enter a valid phone number")
        z=rad_box2.get()
        if z[0]=='S' or z[0]=='s':
            y='MCBP'
        elif z[0]=='C' or z[0]=='c':
            y='MCAE'
        #a.append(y)
        if len(a)==4:
            file = open(str(etnu.get()), "w")
            file.write(str(etnn.get()) + "\n")
            file.write(str(etnu.get()) + "\n")
            file.write(str(etnp.get()) + "\n")
            file.write(str(etnpn.get()) + "\n")
            file.write(str(y) + "\n")
            file.close()
            etnn.delete(0, 'end')
            etnu.delete(0, 'end')
            etnp.delete(0, 'end')
            etnc.delete(0, 'end')
            etnpn.delete(0, 'end')
            root.destroy()
    btn=tk.Button(canvas,text="Create",font=('calibri',25),command=cret)
    btn.place(x=350,y=400)
if __name__ == "__main__":
    create()
