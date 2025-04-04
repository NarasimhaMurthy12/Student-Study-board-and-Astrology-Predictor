import tkinter as tk

def ga():
    root=tk.Tk()
    root.title('Games')
    root.geometry('750x500')

    lbl=tk.Label(root,text='Play Games',font=('calibri',25))
    lbl.pack()

    lbl=tk.Label(root,text='1.',font=('calibri',20))
    lbl.place(x=10,y=40)

    lbl=tk.Label(root,text='Space Invaders',font=('calibri',20))
    lbl.place(x=40,y=40)

    lbl=tk.Label(root,text='Guard the space with the space ship that you have and'+'\n'+'fire bullets at the space invaders before they reach you',font=('calibri',15))
    lbl.place(x=40,y=80)

    def gam():
        import spaceinvaders
        
    btn=tk.Button(root,text='Play game',font=('calibri',15),command=gam)
    btn.place(x=80,y=140)
