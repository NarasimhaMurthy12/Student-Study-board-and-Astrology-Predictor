import tkinter as tk
from tkinter import ttk
def ved():
       root = tk.Tk()
       container = ttk.Frame(root,width=900)
       canvas = tk.Canvas(container)
       scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
       scrollable_frame = ttk.Frame(canvas,width=900)

       scrollable_frame.bind(
           "<Configure>",
           lambda e: canvas.configure(
               scrollregion=canvas.bbox("all")
           )
       )

       canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
       root.geometry('750x500')
       root.title('Learn Vedam')
       
       def runa():
              global na
              te=open(r'files\Rudranamakam.txt',encoding='utf8')
              t=te.read()
              na=ttk.Label(scrollable_frame, text=t,width=900,font=('times',12))
              na.pack()
       def close():
              na.destroy()
       lbl=tk.Label(root,text="Learn Vedam",font=('times',35))
       lbl.place(x=30,y=10)
       def ruca():
              global na
              te=open(r'files\rudrachamakam.txt',encoding='utf8')
              t=te.read()
              na=ttk.Label(scrollable_frame, text=t,width=400,font=('times',12),wraplength=300)
              na.pack()
       btn=tk.Button(root,text="Rudram Namakam",font=('times',15),command=runa)
       btn.place(x=50,y=130)
       btn=tk.Button(root,text="Rudram Chamakam",font=('times',15),command=ruca)
       btn.place(x=50,y=180)
       def ss():
              global na
              te=open(r'files\srisuktam.txt',encoding='utf8')
              t=te.read()
              na=ttk.Label(scrollable_frame, text=t,font=('times',12),wraplength=300)
              na.pack()
       btn=tk.Button(root,text="Sri Suktam",font=('times',15),command=ss)
       btn.place(x=50,y=230)
       def ds():
              global na
              te=open(r'files\durgasuktam.txt',encoding='utf8')
              t=te.read()
              na=ttk.Label(scrollable_frame, text=t,font=('times',12),wraplength=300)
              na.pack()
       btn=tk.Button(root,text="Durga Suktam",font=('times',15),command=ds)
       btn.place(x=50,y=280)
       canvas.configure(yscrollcommand=scrollbar.set)

       btn=tk.Button(root,text='Close',font=('times',15),command=close)
       btn.place(x=370,y=450)


       container.place(x=300,y=100)
       canvas.pack(side="left", fill="both", expand=True)
       scrollbar.pack(side="right", fill="y")

       root.mainloop()

