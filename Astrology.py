import tkinter as tk
from PIL import Image,ImageTk
from geopy.geocoders import Nominatim
from flatlib.geopos import GeoPos
from flatlib.datetime import Datetime
from flatlib.chart import Chart
from flatlib import const
tel=['మేషము','వృషభము','మిథునము','కర్కాటకము','సింహము','కన్యా','తుల','వృశ్చికము','ధనస్సు','మకరము','కుంభము','మీనము']
eng=['Aries','Taurus','Gemini','Cancer','Leo','Virgo','Libra','Scorpio','Sagittarius','Capricorn','Aquarius','Pisces']
gno=[[1,2,3,9],[5,6,8],[3,5,6,8],[2,3,9],[1,3,5,9],[3,5,6,8],[5,6,8],[1,2,3,9],[1,3,8,9],[5,6,8,4],[5,6,8,9],[1,3,8,9]]
gday=[['Sunday,Tuesday,Thursday'],['Wednesday,Friday,Saturday'],['Wednesday,Friday,Sunday'],['Monday,Tuesday,Thursday'],['Sunday,Monday,Tuesday,Thursday'],['Wednesday,Friday,Sunday'],['Wednesday,Friday,Saturday'],['Sunday,Tuesday,Thursday'],['Sunday,Tuesday,Thursday,Saturday'],['Wednesday,Friday,Saturday'],['Wednesday,Friday,Saturday'],['Sunday,Tuesday,Thursday,Saturday']]


root=tk.Tk()
root.title('User Friendly Framework')
root.geometry("750x500")
canvas1 = tk.Canvas(root,bg='grey',height=500,width=750)
canvas1.pack()
btn_img = ImageTk.PhotoImage(file=r"files\ast.jpg")
canvas = tk.Label(canvas1,bg='white',height=500,width=750,image=btn_img)
canvas.place(x=0,y=0)
lbl=tk.Label(canvas,text='Name',font=('calibri',25))
lbl.place(x=75,y=45)
etn=tk.Entry(canvas,font=('calibri',20))
etn.place(x=175,y=47)
lbl=tk.Label(canvas,text='Date of Birth',font=('calibri',25))
lbl.place(x=75,y=115)
etnd=tk.Entry(canvas,font=('calibri',20))
etnd.place(x=270,y=117)
lbl=tk.Label(canvas,text='Time of Birth',font=('calibri',25))
lbl.place(x=75,y=225)
lbl=tk.Label(canvas,text='Enter in the format YYYY/MM/DD . Eg : 2001/07/17',font=('times',10))
lbl.place(x=270,y=155)
etnt=tk.Entry(canvas,font=('calibri',20))
etnt.place(x=270,y=227)
lbl=tk.Label(canvas,text='Enter in 24 hour format . Eg : 18:12:01',font=('times',10))
lbl.place(x=270,y=265)
lbl=tk.Label(canvas,text='Place',font=('calibri',25))
lbl.place(x=75,y=315)
etnp=tk.Entry(canvas,font=('calibri',20))
etnp.place(x=170,y=317)
name=''
date=''
time=''
place=''
def con():
    global name,date,time,place,tel,eng,gno,gday
    name=etn.get()
    dat=etnd.get()
    time=etnt.get()
    place=etnp.get()
    utc='+05:30'
    date = Datetime(dat, time, utc)
    geolocator = Nominatim(user_agent='myapplication')
    location = geolocator.geocode(place)
    d=location.raw
    lat=float(d['lat'])
    lon=float(d['lon'])
    pos = GeoPos(lat,lon)
    chart = Chart(date, pos, hsys=const.HOUSES_REGIOMONTANUS)
    moon = str(chart.getObject(const.MOON))
    for i in range(0,len(eng)):
        if eng[i] in moon:
            x=i
    win=tk.Tk()
    tk.Label(win,text='Name : '+name+'\n'+'Date of Birth : '+dat+'\n'+'Local Time of Birth : '+time+'\n'+'Place : '+place+'\n'+'Raasi : '+eng[x]+'('+tel[x]+')'+'\n'+'Good Numbers : '+str(gno[x])+'\n'+'Good Days : '+str(gday[x]),font=('Calibri',30)).pack()
    
    
btn=tk.Button(canvas,text='Get Details',font=('calibri',20),command=con)
btn.place(x=340,y=400)

