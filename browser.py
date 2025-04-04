#web browser
from tkinterweb import HtmlFrame
import tkinter as tk
def br():
    root=tk.Tk()
    root.title('WEB Browser')
    frame=HtmlFrame(root)
    frame.load_website("http://www.google.co.in")
    frame.pack(fill='both',expand=True)
    root.mainloop()
