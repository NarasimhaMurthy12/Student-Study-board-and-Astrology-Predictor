import tkinter as tk
import subprocess
def mat():
    root=tk.Tk()
    root.title("Biology")

    bt=tk.Label(root,text='Biology',font=('calibri',20))
    bt.place(x=10,y=5)
    def chapter():
        def opch(pa):
            path=pa
            subprocess.Popen([path],shell=True)
        c=tk.Canvas(root,height=500)
        c.place(x=30,y=90)
        btnhj=tk.Button(c,text='Chapter 1',font=('calibri',15),command=lambda :opch(r'files\bio\bioch1.pdf'))
        btnhj.place(x=30,y=40)

        btnh=tk.Button(c,text='Chapter 2',font=('calibri',15),command=lambda :opch(r'files\bio\bioch2.pdf'))
        btnh.place(x=30,y=90)

        btn=tk.Button(c,text='Chapter 3',font=('calibri',15),command=lambda :opch(r'files\bio\bioch3.pdf'))
        btn.place(x=30,y=140)

        bt=tk.Button(c,text='Chapter 4',font=('calibri',15),command=lambda :opch(r'files\bio\bioch4.pdf'))
        bt.place(x=30,y=190)

        b=tk.Button(c,text='Chapter 5',font=('calibri',15),command=lambda :opch(r'files\bio\bioch5.pdf'))
        b.place(x=30,y=240)
        brn.config(bg='grey')
        btr.config(bg='white')
    btr=tk.Button(root,text='Ncert Textbook',font=('calibri',15),activebackground='white',command=chapter)
    btr.place(x=20,y=45)
    def imf():
        c=tk.Canvas(root,height=500)
        c.place(x=30,y=90)
        bt=tk.Button(c,text='Circulation of heart',command=lambda :opch('files\qui.png'))
        bt.place(x=30,y=40)
        btr.config(bg='grey')
        brn.config(bg='white')
    brn=tk.Button(root,text='Important Diagrms',font=('calibri',15),command=imf)
    brn.place(x=200,y=45)
    def opch(pa):
        path=pa
        subprocess.Popen([path],shell=True)
        
    root.geometry('500x500')

    
    root.mainloop()
