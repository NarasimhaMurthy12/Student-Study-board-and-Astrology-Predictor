import tkinter as tk
from playsound import playsound
from pygame import mixer
def bha():
    root=tk.Tk()
    root.title('Learn Bhajans')
    root.geometry('750x500')
    lbl=tk.Label(root,text='Learn Bhajans',font=('times',25))
    lbl.place(x=10,y=10)

    mixer.init()

    def play_music():
        mixer.music.load(r"files\Gajanana.mp3")
        if btn["text"] == "Play":
            btn["text"] = "Pause"
            btn["bg"] = "red"
            mixer.music.play()
        else:
            btn["text"] = "Play"
            btn["bg"] = "green"
            mixer.music.pause()

    btn=tk.Button(root,text='Play',command=play_music)
    btn.place(x=450,y=85)

    lbl=tk.Label(root,text='1 . Gajanana Gajanana'+'\n'+'Prathama Pujana Ganaraya'+'\n'+ 'Prathama Prarthana Shri Ganaraya'+'\n'+ 'Lambodhara Ganaraya',font=('calibri',15),justify='left')
    lbl.place(x=25,y=65)

    def play_muic():
        mixer.music.load(r"files\HaraGanga.mp3")
        if btn1["text"] == "Play":
            btn1["text"] = "Pause"
            btn1["bg"] = "red"
            mixer.music.play()
        else:
            btn1["text"] = "Play"
            btn1["bg"] = "green"
            mixer.music.pause()

    btn1=tk.Button(root,text='Play',command=play_muic)
    btn1.place(x=650,y=175)
    lbl=tk.Label(root,text='2 . Ganga Jatadhara Gauri Shankara Girija Mana Ramana (Jaya)'+'\n'+'Mruthyunjaya Mahadeva Maheshwara Mangala Shubha Charana'+'\n'+ 'Nandhi Vahana Naga Bhushana'+'\n'+ 'Nirupama Guna Sadhana'+'\n'+'Natana Manohara Nilakantha Sai'+'\n'+'Niraja Dala Nayana'
    ,font=('calibri',15),justify='left')
    lbl.place(x=25,y=175)


    lbl=tk.Label(root,text='3 . Guruvayur Pura Shri Hari Krishna Narayana Gopal'+'\n'+'Mukunda Madhava Muralidhari Narayana Gopal'+'\n'+ 'Narayana Gopal Shri Hari Narayana Gopal(2)'+'\n'+ 'Mohana Muralidhari Shri Hari Narayana Gopal'+'\n'+'Govardhana Giridhari Murari Narayana Gopal',font=('calibri',15),justify='left')
    lbl.place(x=25,y=340)
