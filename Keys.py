import tkinter as tk
from tkinter import messagebox as mb

#main window
def mai():
    mai.root=tk.Tk()
    mai.root.title('Keyboard')
    mai.root.geometry("700x350")
    mai.root.resizable(False,False)
    mai.etn=tk.Entry(mai.root,width=40,borderwidth=3,font=('calibri',20))
    mai.etn.pack()
    mai.end=mai.etn.get()
    mai.c=''
def one():
    global c
    mai.c=mai.c+'1'
    mai.etn.delete(0,'end')
    mai.etn.insert(0,mai.c)
def two():
    global c
    mai.c=mai.c+'2'
    mai.etn.delete(0,'end')
    mai.etn.insert(0,mai.c)
def three():
    global c
    mai.c=mai.c+'3'
    mai.etn.delete(0,'end')
    mai.etn.insert(0,mai.c)
def four():
    global c
    mai.c=mai.c+'4'
    mai.etn.delete(0,'end')
    mai.etn.insert(0,mai.c)
def five():
    global c
    mai.c=mai.c+'5'
    mai.etn.delete(0,'end')
    mai.etn.insert(0,mai.c)
def six():
    global c
    mai.c=mai.c+'6'
    mai.etn.delete(0,'end')
    mai.etn.insert(0,mai.c)
def seven():
    global c
    mai.c=mai.c+'7'
    mai.etn.delete(0,'end')
    mai.etn.insert(0,mai.c)
def eight():
    global c
    mai.c=mai.c+'8'
    mai.etn.delete(0,'end')
    mai.etn.insert(0,mai.c)
def nine():
    global c
    mai.c=mai.c+'9'
    mai.etn.delete(0,'end')
    mai.etn.insert(0,mai.c)
def zero():
    global c
    mai.c=mai.c+'0'
    mai.etn.delete(0,'end')
    mai.etn.insert(0,mai.c)
def exc():
    global c
    mai.c=mai.c+'!'
    mai.etn.delete(0,'end')
    mai.etn.insert(0,mai.c)
def clbr():
    global c
    mai.c=mai.c+')'
    mai.etn.delete(0,'end')
    mai.etn.insert(0,mai.c)
def at():
    global c
    mai.c=mai.c+'@'
    mai.etn.delete(0,'end')
    mai.etn.insert(0,mai.c)
def has():
    global c
    mai.c=mai.c+'#'
    mai.etn.delete(0,'end')
    mai.etn.insert(0,mai.c)
def dolar():
    global c
    mai.c=mai.c+'$'
    mai.etn.delete(0,'end')
    mai.etn.insert(0,mai.c)
def ad():
    global c
    mai.c=mai.c+'&'
    mai.etn.delete(0,'end')
    mai.etn.insert(0,mai.c)
def percent():
    global c
    mai.c=mai.c+'%'
    mai.etn.delete(0,'end')
    mai.etn.insert(0,mai.c)
def copyrigh():
    global c
    mai.c=mai.c+'©'
    mai.etn.delete(0,'end')
    mai.etn.insert(0,mai.c)
def opbr():
    global c
    mai.c=mai.c+'('
    mai.etn.delete(0,'end')
    mai.etn.insert(0,mai.c) 
def add():
    global c
    mai.c=mai.c+'+'
    mai.etn.delete(0,'end')
    mai.etn.insert(0,mai.c)
def dash():
    global c
    mai.c=mai.c+'-'
    mai.etn.delete(0,'end')
    mai.etn.insert(0,mai.c)
def dndash():
    global c
    mai.c=mai.c+'_'
    mai.etn.delete(0,'end')
    mai.etn.insert(0,mai.c)
def eq():
    global c
    try:
        d=str(eval(mai.c))
        print(d)
        mai.etn.delete(0,'end')
        mai.etn.insert(0,d)
    except (ValueError,NameError,SyntaxError):
        mai.c=mai.c+'='
        mai.etn.delete(0,'end')
        mai.etn.insert(0,mai.c)
def did():
    global c
    mai.c=mai.c+'/'
    mai.etn.delete(0,'end')
    mai.etn.insert(0,mai.c)
def docom():
    global c
    mai.c=mai.c+';'
    mai.etn.delete(0,'end')
    mai.etn.insert(0,mai.c)
def tdot():
    global c
    mai.c=mai.c+':'
    mai.etn.delete(0,'end')
    mai.etn.insert(0,mai.c)
def quo():
    global c
    mai.c=mai.c+'"'
    mai.etn.delete(0,'end')
    mai.etn.insert(0,mai.c)
def star():
    global c
    mai.c=mai.c+'*'
    mai.etn.delete(0,'end')
    mai.etn.insert(0,mai.c)
def slash():
    global c
    mai.c=mai.c+"'\'"
    mai.etn.delete(0,'end')
    mai.etn.insert(0,mai.c)
def les():
    global c
    mai.c=mai.c+'<'
    mai.etn.delete(0,'end')
    mai.etn.insert(0,mai.c)
def grt():
    global c
    mai.c=mai.c+'>'
    mai.etn.delete(0,'end')
    mai.etn.insert(0,mai.c)
def spc():
    global c
    mai.c=mai.c+' '
    mai.etn.delete(0,'end')
    mai.etn.insert(0,mai.c)

def alpha():
    
    #1st row
    def q():
        global c
        mai.c=mai.c+'Q'
        mai.etn.delete(0,'end')
        mai.etn.insert(0,mai.c)
    btn_q = tk.Button(mai.root, text = 'Q',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=q)
    btn_q.place(x=5,y=55)
    def w():
        global c
        mai.c=mai.c+'W'
        mai.etn.delete(0,'end')
        mai.etn.insert(0,mai.c)
    btn_w = tk.Button(mai.root, text = 'W',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=w)
    btn_w.place(x=60,y=55)
    def e():
        global c
        mai.c=mai.c+'E'
        mai.etn.delete(0,'end')
        mai.etn.insert(0,mai.c)
    btn_e = tk.Button(mai.root, text = 'E',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=e)
    btn_e.place(x=115,y=55)
    def r():
        global c
        mai.c=mai.c+'R'
        mai.etn.delete(0,'end')
        mai.etn.insert(0,mai.c)
    btn_r = tk.Button(mai.root, text = 'R',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=r)
    btn_r.place(x=170,y=55)
    def t():
        global c
        mai.c=mai.c+'T'
        mai.etn.delete(0,'end')
        mai.etn.insert(0,mai.c)
    btn_t = tk.Button(mai.root, text = 'T',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=t)
    btn_t.place(x=225,y=55)
    def y():
        global c
        mai.c=mai.c+'Y'
        mai.etn.delete(0,'end')
        mai.etn.insert(0,mai.c)
    btn_y = tk.Button(mai.root, text = 'Y',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=y)
    btn_y.place(x=280,y=55)
    def u():
        global c
        mai.c=mai.c+'U'
        mai.etn.delete(0,'end')
        mai.etn.insert(0,mai.c)
    btn_u = tk.Button(mai.root, text = 'U',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=u)
    btn_u.place(x=335,y=55)
    def i():
        global c
        mai.c=mai.c+'I'
        mai.etn.delete(0,'end')
        mai.etn.insert(0,mai.c)
    btn_i = tk.Button(mai.root, text = 'I',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=i)
    btn_i.place(x=390,y=55)
    def o():
        global c
        mai.c=mai.c+'O'
        mai.etn.delete(0,'end')
        mai.etn.insert(0,mai.c)
    btn_o = tk.Button(mai.root, text = 'O',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=o)
    btn_o.place(x=445,y=55)
    def p():
        global c
        mai.c=mai.c+'P'
        mai.etn.delete(0,'end')
        mai.etn.insert(0,mai.c)
    btn_p = tk.Button(mai.root, text = 'P',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=p)
    btn_p.place(x=500,y=55)
    def backsp():
        global c
        mai.c=mai.c[:-1]
        mai.etn.delete(0,'end')
        mai.etn.insert(0,mai.c)
    btn_backsp = tk.Button(mai.root, text = 'Backspace\n<-',font = ("Calibri",15), activebackground = "GREY", state = "normal",command=backsp)
    btn_backsp.place(x=555,y=55)

    #2nd row
    def a():
        global c
        mai.c=mai.c+'A'
        mai.etn.delete(0,'end')
        mai.etn.insert(0,mai.c)
    btn_a = tk.Button(mai.root, text = 'A',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=a)
    btn_a.place(x=25,y=125)
    def s():
        global c
        mai.c=mai.c+'S'
        mai.etn.delete(0,'end')
        mai.etn.insert(0,mai.c)     
    btn_s = tk.Button(mai.root, text = 'S',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=s)
    btn_s.place(x=80,y=125)
    def d():
        global c
        mai.c=mai.c+'D'
        mai.etn.delete(0,'end')
        mai.etn.insert(0,mai.c)     
    btn_d = tk.Button(mai.root, text = 'D',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=d)
    btn_d.place(x=135,y=125)
    def f():
        global c
        mai.c=mai.c+'F'
        mai.etn.delete(0,'end')
        mai.etn.insert(0,mai.c)
    btn_f = tk.Button(mai.root, text = 'F',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=f)
    btn_f.place(x=190,y=125)
    def g():
        global c
        mai.c=mai.c+'G'
        mai.etn.delete(0,'end')
        mai.etn.insert(0,mai.c)
    btn_g = tk.Button(mai.root, text = 'G',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=g)
    btn_g.place(x=245,y=125)
    def h():
        global c
        mai.c=mai.c+'H'
        mai.etn.delete(0,'end')
        mai.etn.insert(0,mai.c)     
    btn_h = tk.Button(mai.root, text = 'H',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=h)
    btn_h.place(x=300,y=125)
    def j():
        global c
        mai.c=mai.c+'J'
        mai.etn.delete(0,'end')
        mai.etn.insert(0,mai.c)     
    btn_j = tk.Button(mai.root, text = 'J',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=j)
    btn_j.place(x=355,y=125)
    def k():
        global c
        mai.c=mai.c+'Q'
        mai.etn.delete(0,'end')
        mai.etn.insert(0,mai.c)     
    btn_k = tk.Button(mai.root, text = 'K',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=k)
    btn_k.place(x=410,y=125)
    def l():
        global c
        mai.c=mai.c+'L'
        mai.etn.delete(0,'end')
        mai.etn.insert(0,mai.c)     
    btn_l = tk.Button(mai.root, text = 'L',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=l)
    btn_l.place(x=465,y=125)
    def etr():
        global c
        print(mai.c)
        mai.etn.delete(0,'end')
        #mai.etn.insert(0,mai.c)
        mai.c=''
    btn_etr = tk.Button(mai.root, text = 'Enter',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=8,height=1,command=etr)
    btn_etr.place(x=520,y=125)


    #3rd row
    def lower():
        btn_lower.destroy()
        btn_q.destroy()
        btn_w.destroy()
        btn_e.destroy()
        btn_r.destroy()
        btn_t.destroy()
        btn_y.destroy()
        btn_u.destroy()
        btn_i.destroy()
        btn_o.destroy()
        btn_p.destroy()
        btn_a.destroy()
        btn_s.destroy()
        btn_d.destroy()
        btn_f.destroy()
        btn_g.destroy()
        btn_h.destroy()
        btn_j.destroy()
        btn_k.destroy()
        btn_l.destroy()
        btn_z.destroy()
        btn_x.destroy()
        btn_c.destroy()
        btn_v.destroy()
        btn_b.destroy()
        btn_n.destroy()
        btn_m.destroy()
        def q1():
            global c
            mai.c=mai.c+'q'
            mai.etn.delete(0,'end')
            mai.etn.insert(0,mai.c)
        btn_q1 = tk.Button(mai.root, text = 'q',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=q1)
        btn_q1.place(x=5,y=55)
        def upper():
            btn_upper.destroy()
            btn_q1.destroy()
            btn_w1.destroy()
            btn_e1.destroy()
            btn_r1.destroy()
            btn_t1.destroy()
            btn_y1.destroy()
            btn_u1.destroy()
            btn_i1.destroy()
            btn_o1.destroy()
            btn_p1.destroy()
            btn_a1.destroy()
            btn_s1.destroy()
            btn_d1.destroy()
            btn_f1.destroy()
            btn_g1.destroy()
            btn_h1.destroy()
            btn_j1.destroy()
            btn_k1.destroy()
            btn_l1.destroy()
            btn_z1.destroy()
            btn_x1.destroy()
            btn_c1.destroy()
            btn_v1.destroy()
            btn_b1.destroy()
            btn_n1.destroy()
            btn_m1.destroy()
            btn_lower=tk.Button(mai.root,text='Lower\ncase',font = ("Calibri",10), activebackground = "GREY", state = "normal",padx=5,pady=10,command=lower)
            btn_lower.place(x=5,y=195)
            btn_q = tk.Button(mai.root, text = 'Q',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=q)
            btn_q.place(x=5,y=55)

            btn_w = tk.Button(mai.root, text = 'W',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=w)
            btn_w.place(x=60,y=55)

            btn_e = tk.Button(mai.root, text = 'E',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=e)
            btn_e.place(x=115,y=55)

            btn_r = tk.Button(mai.root, text = 'R',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=r)
            btn_r.place(x=170,y=55)

            btn_t = tk.Button(mai.root, text = 'T',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=t)
            btn_t.place(x=225,y=55)

            btn_y = tk.Button(mai.root, text = 'Y',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=y)
            btn_y.place(x=280,y=55)

            btn_u = tk.Button(mai.root, text = 'U',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=u)
            btn_u.place(x=335,y=55)

            btn_i = tk.Button(mai.root, text = 'I',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=i)
            btn_i.place(x=390,y=55)

            btn_o = tk.Button(mai.root, text = 'O',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=o)
            btn_o.place(x=445,y=55)

            btn_p = tk.Button(mai.root, text = 'P',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=p)
            btn_p.place(x=500,y=55)

            #2nd row

            btn_a = tk.Button(mai.root, text = 'A',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=a)
            btn_a.place(x=25,y=125)

            btn_s = tk.Button(mai.root, text = 'S',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=s)
            btn_s.place(x=80,y=125)

            btn_d = tk.Button(mai.root, text = 'D',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=d)
            btn_d.place(x=135,y=125)

            btn_f = tk.Button(mai.root, text = 'F',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=f)
            btn_f.place(x=190,y=125)

            btn_g = tk.Button(mai.root, text = 'G',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=g)
            btn_g.place(x=245,y=125)
           
            btn_h = tk.Button(mai.root, text = 'H',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=h)
            btn_h.place(x=300,y=125)

            btn_j = tk.Button(mai.root, text = 'J',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=j)
            btn_j.place(x=355,y=125)

            btn_k = tk.Button(mai.root, text = 'K',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=k)
            btn_k.place(x=410,y=125)
             
            btn_l = tk.Button(mai.root, text = 'L',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=l)
            btn_l.place(x=465,y=125)


            btn_z = tk.Button(mai.root, text = 'Z',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=z)
            btn_z.place(x=60,y=195)

            btn_x = tk.Button(mai.root, text = 'X',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=x)
            btn_x.place(x=115,y=195)
              
            btn_c = tk.Button(mai.root, text = 'C',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=c)
            btn_c.place(x=170,y=195)
           
            btn_v = tk.Button(mai.root, text = 'V',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=v)
            btn_v.place(x=225,y=195)
          
            btn_b = tk.Button(mai.root, text = 'B',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=b)
            btn_b.place(x=280,y=195)
           
            btn_n = tk.Button(mai.root, text = 'N',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=n)
            btn_n.place(x=335,y=195)
               
            btn_m = tk.Button(mai.root, text = 'M',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=m)
            btn_m.place(x=390,y=195)

        btn_upper=tk.Button(mai.root,text='Upper\ncase',font = ("Calibri",10), activebackground = "GREY", state = "normal",padx=5,pady=10,command=upper)
        btn_upper.place(x=5,y=195)
        def w1():
            global c
            mai.c=mai.c+'w'
            mai.etn.delete(0,'end')
            mai.etn.insert(0,mai.c)
        btn_w1 = tk.Button(mai.root, text = 'w',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=w1)
        btn_w1.place(x=60,y=55)
        def e1():
            global c
            mai.c=mai.c+'e'
            mai.etn.delete(0,'end')
            mai.etn.insert(0,mai.c)
        btn_e1 = tk.Button(mai.root, text = 'e',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=e1)
        btn_e1.place(x=115,y=55)
        def r1():
            global c
            mai.c=mai.c+'r'
            mai.etn.delete(0,'end')
            mai.etn.insert(0,mai.c)
        btn_r1 = tk.Button(mai.root, text = 'r',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=r1)
        btn_r1.place(x=170,y=55)
        def t1():
            global c
            mai.c=mai.c+'t'
            mai.etn.delete(0,'end')
            mai.etn.insert(0,mai.c)
        btn_t1 = tk.Button(mai.root, text = 't',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=t1)
        btn_t1.place(x=225,y=55)
        def y1():
            global c
            mai.c=mai.c+'y'
            mai.etn.delete(0,'end')
            mai.etn.insert(0,mai.c)
        btn_y1 = tk.Button(mai.root, text = 'y',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=y1)
        btn_y1.place(x=280,y=55)
        def u1():
            global c
            mai.c=mai.c+'u'
            mai.etn.delete(0,'end')
            mai.etn.insert(0,mai.c)
        btn_u1 = tk.Button(mai.root, text = 'u',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=u1)
        btn_u1.place(x=335,y=55)
        def i1():
            global c
            mai.c=mai.c+'i'
            mai.etn.delete(0,'end')
            mai.etn.insert(0,mai.c)
        btn_i1 = tk.Button(mai.root, text = 'i',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=i1)
        btn_i1.place(x=390,y=55)
        def o1():
            global c
            mai.c=mai.c+'o'
            mai.etn.delete(0,'end')
            mai.etn.insert(0,mai.c)
        btn_o1 = tk.Button(mai.root, text = 'o',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=o1)
        btn_o1.place(x=445,y=55)
        def p1():
            global c
            mai.c=mai.c+'p'
            mai.etn.delete(0,'end')
            mai.etn.insert(0,mai.c)
        btn_p1 = tk.Button(mai.root, text = 'p',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=p1)
        btn_p1.place(x=500,y=55)
        def a1():
            global c
            mai.c=mai.c+'a'
            mai.etn.delete(0,'end')
            mai.etn.insert(0,mai.c)
        btn_a1 = tk.Button(mai.root, text = 'a',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=a1)
        btn_a1.place(x=25,y=125)
        def s1():
            global c
            mai.c=mai.c+'s'
            mai.etn.delete(0,'end')
            mai.etn.insert(0,mai.c)     
        btn_s1 = tk.Button(mai.root, text = 's',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=s1)
        btn_s1.place(x=80,y=125)
        def d1():
            global c
            mai.c=mai.c+'d'
            mai.etn.delete(0,'end')
            mai.etn.insert(0,mai.c)     
        btn_d1 = tk.Button(mai.root, text = 'd',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=d1)
        btn_d1.place(x=135,y=125)
        def f1():
            global c
            mai.c=mai.c+'f'
            mai.etn.delete(0,'end')
            mai.etn.insert(0,mai.c)
        btn_f1 = tk.Button(mai.root, text = 'f',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=f1)
        btn_f1.place(x=190,y=125)
        def g1():
            global c
            mai.c=mai.c+'g'
            mai.etn.delete(0,'end')
            mai.etn.insert(0,mai.c)
        btn_g1 = tk.Button(mai.root, text = 'g',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=g1)
        btn_g1.place(x=245,y=125)
        def h1():
            global c
            mai.c=mai.c+'h'
            mai.etn.delete(0,'end')
            mai.etn.insert(0,mai.c)     
        btn_h1 = tk.Button(mai.root, text = 'h',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=h1)
        btn_h1.place(x=300,y=125)
        def j1():
            global c
            mai.c=mai.c+'j'
            mai.etn.delete(0,'end')
            mai.etn.insert(0,mai.c)     
        btn_j1 = tk.Button(mai.root, text = 'j',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=j1)
        btn_j1.place(x=355,y=125)
        def k1():
            global c
            mai.c=mai.c+'k'
            mai.etn.delete(0,'end')
            mai.etn.insert(0,mai.c)     
        btn_k1 = tk.Button(mai.root, text = 'k',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=k1)
        btn_k1.place(x=410,y=125)
        def l1():
            global c
            mai.c=mai.c+'l'
            mai.etn.delete(0,'end')
            mai.etn.insert(0,mai.c)     
        btn_l1 = tk.Button(mai.root, text = 'l',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=l1)
        btn_l1.place(x=465,y=125)
        def z1():
            global c
            mai.c=mai.c+'z'
            mai.etn.delete(0,'end')
            mai.etn.insert(0,mai.c)
        btn_z1 = tk.Button(mai.root, text = 'z',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=z1)
        btn_z1.place(x=60,y=195)
        def x1():
            global c
            mai.c=mai.c+'x'
            mai.etn.delete(0,'end')
            mai.etn.insert(0,mai.c)
        btn_x1 = tk.Button(mai.root, text = 'x',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=x1)
        btn_x1.place(x=115,y=195)
        def c1():
            global c
            mai.c=mai.c+'c'
            mai.etn.delete(0,'end')
            mai.etn.insert(0,mai.c)     
        btn_c1 = tk.Button(mai.root, text = 'c',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=c1)
        btn_c1.place(x=170,y=195)
        def v1():
            global c
            mai.c=mai.c+'v'
            mai.etn.delete(0,'end')
            mai.etn.insert(0,mai.c)     
        btn_v1 = tk.Button(mai.root, text = 'v',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=v1)
        btn_v1.place(x=225,y=195)
        def b1():
            global c
            mai.c=mai.c+'b'
            mai.etn.delete(0,'end')
            mai.etn.insert(0,mai.c)     
        btn_b1 = tk.Button(mai.root, text = 'b',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=b1)
        btn_b1.place(x=280,y=195)
        def n1():
            global c
            mai.c=mai.c+'n'
            mai.etn.delete(0,'end')
            mai.etn.insert(0,mai.c)     
        btn_n1 = tk.Button(mai.root, text = 'n',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=n1)
        btn_n1.place(x=335,y=195)
        def m1():
            global c
            mai.c=mai.c+'m'
            mai.etn.delete(0,'end')
            mai.etn.insert(0,mai.c)     
        btn_m1 = tk.Button(mai.root, text = 'm',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=m1)
        btn_m1.place(x=390,y=195)

    btn_lower=tk.Button(mai.root,text='Lower\ncase',font = ("Calibri",10), activebackground = "GREY", state = "normal",padx=5,pady=10,command=lower)
    btn_lower.place(x=5,y=195)
    
    def z():
        global c
        mai.c=mai.c+'Z'
        mai.etn.delete(0,'end')
        mai.etn.insert(0,mai.c)
    btn_z = tk.Button(mai.root, text = 'Z',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=z)
    btn_z.place(x=60,y=195)
    def x():
        global c
        mai.c=mai.c+'X'
        mai.etn.delete(0,'end')
        mai.etn.insert(0,mai.c)
    btn_x = tk.Button(mai.root, text = 'X',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=x)
    btn_x.place(x=115,y=195)
    def c():
        global mai.c
        c=mai.c+'mai.c'
        mai.etn.delete(0,'end')
        mai.etn.insert(0,mai.c)     
    btn_c = tk.Button(mai.root, text = 'C',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=c)
    btn_c.place(x=170,y=195)
    def v():
        global c
        mai.c=mai.c+'V'
        mai.etn.delete(0,'end')
        mai.etn.insert(0,mai.c)     
    btn_v = tk.Button(mai.root, text = 'V',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=v)
    btn_v.place(x=225,y=195)
    def b():
        global c
        mai.c=mai.c+'B'
        mai.etn.delete(0,'end')
        mai.etn.insert(0,mai.c)     
    btn_b = tk.Button(mai.root, text = 'B',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=b)
    btn_b.place(x=280,y=195)
    def n():
        global c
        mai.c=mai.c+'N'
        mai.etn.delete(0,'end')
        mai.etn.insert(0,mai.c)     
    btn_n = tk.Button(mai.root, text = 'N',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=n)
    btn_n.place(x=335,y=195)
    def m():
        global c
        mai.c=mai.c+'M'
        mai.etn.delete(0,'end')
        mai.etn.insert(0,mai.c)     
    btn_m = tk.Button(mai.root, text = 'M',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=m)
    btn_m.place(x=390,y=195)
    def com():
        global c
        mai.c=mai.c+','
        mai.etn.delete(0,'end')
        mai.etn.insert(0,mai.c)     
    btn_com = tk.Button(mai.root, text = ',',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=com)
    btn_com.place(x=445,y=195)
    def fst():
        global c
        mai.c=mai.c+'.'
        mai.etn.delete(0,'end')
        print(mai.c)
        mai.etn.insert(0,mai.c)     
    btn_fst = tk.Button(mai.root, text = '.',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=fst)
    btn_fst.place(x=500,y=195)
    def qmrk():
        global c
        mai.c=mai.c+'?'
        mai.etn.delete(0,'end')
        print(mai.c)
        mai.etn.insert(0,mai.c)     
    btn_qmrk = tk.Button(mai.root, text = '?',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=qmrk)
    btn_qmrk.place(x=555,y=195)
    def clear():
        global c
        mai.etn.delete(0,'end')
        print(mai.c)
        mai.c=''
    btn_clear=tk.Button(mai.root,text='Clear',font = ("Calibri",10), activebackground = "GREY", state = "normal",padx=5,pady=15,command=clear)
    btn_clear.place(x=610,y=195)



    #4th row
    def num():
        
        btn_num.destroy()
        btn_q.destroy()
        btn_w.destroy()
        btn_e.destroy()
        btn_r.destroy()
        btn_t.destroy()
        btn_y.destroy()
        btn_u.destroy()
        btn_i.destroy()
        btn_o.destroy()
        btn_p.destroy()
        btn_a.destroy()
        btn_s.destroy()
        btn_d.destroy()
        btn_f.destroy()
        btn_g.destroy()
        btn_h.destroy()
        btn_j.destroy()
        btn_k.destroy()
        btn_l.destroy()
        btn_z.destroy()
        btn_x.destroy()
        btn_c.destroy()
        btn_v.destroy()
        btn_b.destroy()
        btn_n.destroy()
        btn_m.destroy()
        btn_com.destroy()
        btn_fst.destroy()
        btn_qmrk.destroy()
        btn_etr.destroy()
        btn_backsp.destroy()
        btn_spc.destroy()
        btn_les.destroy()
        btn_grt.destroy()
        btn_ctr.destroy()
        lbl_eng.destroy()
        btn_abc=tk.Button(mai.root, text = 'abc',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=4,height=1,command=alpha)
        btn_abc.place(x=5,y=265)
        #1st row
   
        btn_1 = tk.Button(mai.root, text = '1',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=one)
        btn_1.place(x=5,y=55)
         
        btn_2 = tk.Button(mai.root, text = '2',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=two)
        btn_2.place(x=60,y=55)
        
        btn_3 = tk.Button(mai.root, text = '3',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=three)
        btn_3.place(x=115,y=55)
          
        btn_4 = tk.Button(mai.root, text = '4',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=four)
        btn_4.place(x=170,y=55)
         
        btn_5 = tk.Button(mai.root, text = '5',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=five)
        btn_5.place(x=225,y=55)
        
        btn_6 = tk.Button(mai.root, text = '6',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=six)
        btn_6.place(x=280,y=55)
             
        btn_7 = tk.Button(mai.root, text = '7',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=seven)
        btn_7.place(x=335,y=55)
          
        btn_8 = tk.Button(mai.root, text = '8',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=eight)
        btn_8.place(x=390,y=55)
        
        btn_9 = tk.Button(mai.root, text = '9',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=nine)
        btn_9.place(x=445,y=55)
          
        btn_0 = tk.Button(mai.root, text = '0',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=zero)
        btn_0.place(x=500,y=55)
          
        btn_backsp1 = tk.Button(mai.root, text = 'Backspace\n<-',font = ("Calibri",15), activebackground = "GREY", state = "normal",command=backsp)
        btn_backsp1.place(x=555,y=55)


        #2nd row
            
        btn_exc = tk.Button(mai.root, text = '!',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=exc)
        btn_exc.place(x=25,y=125)
            
        btn_at = tk.Button(mai.root, text = '@',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=at)
        btn_at.place(x=80,y=125)
            
        btn_hash = tk.Button(mai.root, text = '#',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=has)
        btn_hash.place(x=135,y=125)
            
        btn_dolar = tk.Button(mai.root, text = '$',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=dolar)
        btn_dolar.place(x=190,y=125)
         
        btn_and = tk.Button(mai.root, text = '&',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=ad)
        btn_and.place(x=245,y=125)
        
        btn_percent = tk.Button(mai.root, text = '%',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=percent)
        btn_percent.place(x=300,y=125)
          
        btn_copyright = tk.Button(mai.root, text = '©',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=copyrigh)
        btn_copyright.place(x=355,y=125)
        
        btn_opbr = tk.Button(mai.root, text = '(',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=opbr)
        btn_opbr.place(x=410,y=125)
        
        btn_clbr = tk.Button(mai.root, text = ')',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=clbr)
        btn_clbr.place(x=465,y=125)
        
        btn_etr1 = tk.Button(mai.root, text = 'Enter',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=8,height=1,command=etr)
        btn_etr1.place(x=520,y=125)


        #3rd row
           
        btn_dash = tk.Button(mai.root, text = '-',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=dash)
        btn_dash.place(x=60,y=195)
             
        btn_dndash = tk.Button(mai.root, text = '_',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=dndash)
        btn_dndash.place(x=115,y=195)
            
        btn_eq = tk.Button(mai.root, text = '=',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=eq)
        btn_eq.place(x=170,y=195)
             
        btn_add = tk.Button(mai.root, text = '+',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=add)
        btn_add.place(x=225,y=195)
           
        btn_did = tk.Button(mai.root, text = "'/'" ,font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=did)
        btn_did.place(x=280,y=195)
            
        btn_docom = tk.Button(mai.root, text = ';',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=docom)
        btn_docom.place(x=335,y=195)
          
        btn_tdot = tk.Button(mai.root, text = ':',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=tdot)
        btn_tdot.place(x=390,y=195)
           
        btn_quo = tk.Button(mai.root, text = '"',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=quo)
        btn_quo.place(x=445,y=195)
           
        btn_star = tk.Button(mai.root, text = '*',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=star)
        btn_star.place(x=500,y=195)
          
        btn_slash = tk.Button(mai.root, text = "'\'",font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=slash)
        btn_slash.place(x=555,y=195)
        
        #4th row
        
        btn_ctr1=tk.Button(mai.root, text = 'Ctrl',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1)
        btn_ctr1.place(x=70,y=265)
         
        btn_spc1=tk.Button(mai.root, text = 'Space',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=25,height=1,command=spc)
        btn_spc1.place(x=125,y=265)
          
        btn_les1=tk.Button(mai.root, text = '<',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=les)
        btn_les1.place(x=490,y=265)
           
        btn_grt1=tk.Button(mai.root, text = '>',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=grt)
        btn_grt1.place(x=545,y=265)
        lbl_eng1=tk.Label(mai.root,text='ENG',font=('calibri',20),activebackground = "GREY", state = "normal",width=3,height=1,anchor='ne')
        lbl_eng1.place(x=605,y=265)
        lbl_2=tk.Label(mai.root,text='Press = to get answer of your calculations',anchor='s',font=('calibri',20))






    #4th row
        
    btn_num=tk.Button(mai.root, text = '&123',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=4,height=1,command=num)
    btn_num.place(x=5,y=265)
    btn_ctr=tk.Button(mai.root, text = 'Ctrl',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1)
    btn_ctr.place(x=70,y=265)
    btn_spc=tk.Button(mai.root, text = 'Space',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=25,height=1,command=spc)
    btn_spc.place(x=125,y=265)
    btn_les=tk.Button(mai.root, text = '<',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=les)
    btn_les.place(x=490,y=265)
    btn_grt=tk.Button(mai.root, text = '>',font = ("Calibri",20), activebackground = "GREY", state = "normal",width=3,height=1,command=grt)
    btn_grt.place(x=545,y=265)
    lbl_eng=tk.Label(mai.root,text='ENG',font=('calibri',20),activebackground = "GREY", state = "normal",width=3,height=1,anchor='ne')
    lbl_eng.place(x=605,y=265)

