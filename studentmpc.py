import tkinter as tk
import datetime
import time
from PIL import Image,ImageTk

import bhajans
import veda
import browser
import note
#main window
def student(username):
    root1=tk.Tk()
    root1.title('User Friendly Framework')
    root1.geometry("1399x768")
    now=datetime.datetime.now()
    # Creating first screen canvas
    canvas1 = tk.Canvas(root1,height=768,width=1399)
    canvas1.pack()
    #display date and time
    def clock():
        
        t=time.strftime('%I:%M:%S',time.localtime())
        if t!='':
            label1.config(text=t,font='times 18')
        root1.after(100,clock)
        
    label1=tk.Label(root1,justify='center',background="blue")
    label1.place(x=1208,y=630)
    t=time.strftime('%Y-%m-%d',time.localtime())
    label=tk.Label(root1,text=t,font='times 18',background="blue")
    label.place(x=1200,y=660)
    clock()
    

    #Background
    btn_img = ImageTk.PhotoImage(file=r"files\bg12.jpg")
    bgim = tk.Label(canvas1,image=btn_img)
    bgim.place(x=0,y=0)
    #User name display
    bt_img = ImageTk.PhotoImage(file=r"files\user.png")
    bgim = tk.Label(canvas1,image=bt_img)
    bgim.place(x=999,y=75)
    bgim = tk.Label(canvas1,text=username,font=("Times new roman",15))
    bgim.place(x=1055,y=84)
    #Sign out
    def signot():
        root1.destroy()
        import main
    btn=tk.Button(canvas1,font=("Times new roman",15),text="Sign out",command=signot)
    btn.place(x=1250,y=75)
    #physics button
    def ph():
        import physics
        physics.mat()
    btnmg = ImageTk.PhotoImage(file=r"files\phy.png")
    btn=tk.Button(canvas1,font=("Times new roman",30),image=btnmg,command=ph)
    btn.place(x=20,y=190)
    #chemistry button
    def chem():
        import chemistry
        chemistry.mat()
    btmg = ImageTk.PhotoImage(file=r"files\chem.png")
    btn=tk.Button(canvas1,text="CHEMISTRY",font=("Times new roman",30),image=btmg,command=chem)
    btn.place(x=375,y=190)
    #maths button
    def ma():
        import maths
        maths.mat()
    btg = ImageTk.PhotoImage(file=r"files\maths.png")
    btn=tk.Button(canvas1,text="MATHS",font=("Times new roman",30),image=btg,command=ma)
    btn.place(x=730,y=190)
    #bio button
    def bio():
        import biology
        biology.mat()
    btni = ImageTk.PhotoImage(file=r"files\bio.png")
    btn=tk.Button(canvas1,text="BIOLOGY",font=("Times new roman",30),image=btni,command=bio)
    btn.place(x=1070,y=190)
    #browser button
    def bro():
        
        browser.br()
    t= ImageTk.PhotoImage(file=r"files\browser.jpg")
    btn=tk.Button(canvas1,text="browser",font=("Times new roman",30),image=t,command=bro)
    btn.place(x=100,y=575)
    #calculatorbutton
    def cal():
        import calculator
    bti = ImageTk.PhotoImage(file=r"files\calculator.png")
    btn=tk.Button(canvas1,text="clculator",font=("Times new roman",30),image=bti,command=cal)
    btn.place(x=250,y=575)
    #vedam button
    def vedam():
        
        veda.ved()
    bt= ImageTk.PhotoImage(file=r"files\veda.png")
    btn=tk.Button(canvas1,text="veda",font=("Times new roman",30),image=bt,command=vedam)
    btn.place(x=400,y=575)
    def gme():
        import game
        game.ga()    
    #game button
    b= ImageTk.PhotoImage(file=r"files\g.png")
    btn=tk.Button(canvas1,text="game",font=("Times new roman",30),image=b,command=gme)
    btn.place(x=550,y=575)
    def bhaj():
        bhajans.bha()
    #bhajans button
    ti= ImageTk.PhotoImage(file=r"files\bhajan.png")
    btn=tk.Button(canvas1,text="Bhajans",font=("Times new roman",30),image=ti,command=bhaj)
    btn.place(x=700,y=575)
    #notepad button
    def notee():
        
        note.no()
    i= ImageTk.PhotoImage(file=r"files\notes.jpg")
    btn=tk.Button(canvas1,text="notepad",font=("Times new roman",30),image=i,command=notee)
    btn.place(x=850,y=575)

    


    tk.mainloop()

