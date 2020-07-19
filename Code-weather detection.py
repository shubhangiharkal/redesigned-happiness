import tkinter
from tkinter import messagebox
import requests
from PIL import ImageTk,Image
import json
from datetime import *

import mysql.connector
window1=None

window2=None
window3=None
winow4=None
window5=None
window6=None
window7=None
win=None

txt1var=None
txt2var=None
tx3var=None
txt4var=None
txt5var=None
txt6var=None
txt8var=None
txt9var=None
a=None

t1var=[]
t2var=[]
t3var=[]
t4var=[]
t5var=[]
t6var=[]

t1=[]
t2=[]
t3=[]
t4=[]
t5=[]
t6=[]
cityn=None
tempn=None
atpn=None
humn=None
desn=None
sub=None
cityf=None
tempf=None
atpf=None
humf=None
desf=None
cityname1=None
city1=None
lis1=[]
lis2=[]
lis4=[]
var1=[]
var2=[]
var4=[]
lis3=[]
var3=[]
lis5=[]
var5=[]

tvar=[]
t=[]

lis6=[]
var6=[]
lis=[]
var=[]

mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             passwd="",
                             database="weather")
mycursor=mydb.cursor()

def win1():
    global window1
    global txt1var
    global txt2var
    global txt8var
    window1=tkinter.Tk()
    
    window1.geometry("600x600+100+100")
    window1.config(bg="light pink")

    
    img=ImageTk.PhotoImage(file=r'weatherbg.jpg')
    window1.img=img
    tkinter.Label(window1,image=img).place(relwidth=1,relheight=1)
    

    txt1var=tkinter.StringVar(window1)
    txt2var=tkinter.StringVar(window1)
    txt8var=tkinter.StringVar(window1)
    frame=tkinter.Frame(window1)
    frame.pack(side=tkinter.TOP)
    
   
    
    
    lb1=tkinter.Label(frame,text="WEATHER  REPORTER",fg="black",font=("Helvetica",32),bg="teal")
    lb1.pack(side=tkinter.TOP)
    

    menubar=tkinter.Menu(window1)
    menubar.add_command(label="About",command=about)
    menubar.add_command(label="Help",command=h)

    window1.config(menu=menubar)

    username=tkinter.Label(window1,text="username",bg="teal",relief="ridge",bd=5)
    username.place(x=100,y=200,height=30,width=100)
    password=tkinter.Label(window1,text="password",bg="teal",relief="ridge",bd=5)
    password.place(x=100,y=240,height=30,width=100)
    usl=tkinter.Entry(window1,textvariable=txt1var,bd=5)
    usl.place(x=210,y=200,height=30,width=100)
    passl=tkinter.Entry(window1,textvariable=txt2var,bd=5)
    passl.place(x=210,y=240,height=30,width=100)
    mail=tkinter.Label(window1,text="mail",bg="teal",relief="ridge",bd=5)
    mail.place(x=100,y=280,height=30,width=100)
    mail1=tkinter.Entry(window1,textvariable=txt8var,bd=5)
    mail1.place(x=210,y=280,height=30,width=100)
    btn=tkinter.Button(window1,text="login",command=checker,bd=7,bg="teal")
    btn.place(x=210,y=320,height=30,width=100)
    
def about():
    wl=tkinter.Tk()
    var=tkinter.StringVar(wl)
    label=tkinter.Message(wl,textvariable=var,relief=tkinter.FLAT,bg="teal")
    var.set("It is a weather gui app.It will tell you about the current temperature,ATP,Humidity,description about the city of India.it is very helpful for searching weather condition")
    label.pack()
def h():
    wl=tkinter.Tk()
    var=tkinter.StringVar(wl)
    label=tkinter.Message(wl,textvariable=var,relief=tkinter.FLAT,bg="teal")
    var.set(" 1.You need to login first \n 2.If you are not registered than you need to contact the admin \n 3.You can search any city's temperature by entering the city name \n 4.You can update your info by clicking on view menu /n 5.You can search your history by clicking on search menu")
    label.pack()
    
    
def win2():
    global window2
    global txt3var
    global txt4var
    global txtvar
    window2=tkinter.Tk()
    txt3var=tkinter.StringVar(window2)
    txt4var=tkinter.StringVar(window2)
    txtvar=tkinter.StringVar(window2)
    window2.geometry("600x600+100+100")
    window2.config(bg="pink")
    img=ImageTk.PhotoImage(file=r"weatherbg.jpg")
    window2.img=img
    tkinter.Label(window2,image=img).place(relwidth=1,relheight=1)
    username=tkinter.Label(window2,text="username",bg="teal",relief="ridge",bd=5)
    username.place(x=100,y=200,height=30,width=100)
    password=tkinter.Label(window2,text="password",bg="teal",relief="ridge",bd=5)
    password.place(x=100,y=240,height=30,width=100)
    usl=tkinter.Entry(window2,textvariable=txt3var,bd=5)
    usl.place(x=210,y=200,height=30,width=100)
    passl=tkinter.Entry(window2,textvariable=txt4var,bd=5)
    passl.place(x=210,y=240,height=30,width=100)
    mail=tkinter.Label(window2,text="mail",relief="ridge",bg="teal",bd=5)
    mail.place(x=100,y=280,height=30,width=100)
    mail1=tkinter.Entry(window2,textvariable=txtvar,bd=5)
    mail1.place(x=210,y=280,height=30,width=100)
    btn1=tkinter.Button(window2,text="back",command=win2closer,bd=7,bg="teal")
    btn1.place(x=210,y=320,height=30,width=100)
    btn=tkinter.Button(window2,text="register",command=register,bd=7,bg="teal")
    btn.place(x=210,y=360,height=30,width=100)
def win3():
    global window3
    global tempn
    global atpn
    global humn
    global desn
    global cityn
    global sub
    global cityf
    global tempf
    global atpf
    global humf
    global desf
    global txt1var
    global txt2var
    
    window3=tkinter.Tk()
    window3.config(bg="pink")
    window3.geometry("600x600+100+100")
    window3.title("GUI APPLICATION")
    img=ImageTk.PhotoImage(file=r"weatherbg.jpg")
    window3.img=img
    tkinter.Label(window3,image=img).place(relwidth=1,relheight=1)
    win=tkinter.Label(window3,text="Weather Gui Application",relief="ridge",bg="teal",bd=5, font='bold')
    win.place(x=140,y=0,height=30,width=200)
    cityn=tkinter.StringVar(window3)
    tempn=tkinter.StringVar(window3)
    atpn=tkinter.StringVar(window3)
    humn=tkinter.StringVar(window3)
    desn=tkinter.StringVar(window3)
    city=tkinter.Label(window3,text="city name:",font="BOLD",relief="ridge",bg="teal",bd=5)
    city.place(x=20,y=30,height=30,width=100)
    cityf=tkinter.Entry(window3,textvariable=cityn,bd=5)
    cityf.place(x=130,y=30,height=30,width=300)
    sub=tkinter.Button(window3,text="submit",command=subb,bd=5,bg="teal")
    sub.place(x=210,y=80,height=20,width=100)
    temp=tkinter.Label(window3,text="Temperature:",relief="ridge",bg="teal",bd=5)
    temp.place(x=20,y=110,height=30,width=100)
    tempf=tkinter.Entry(window3,textvariable=tempn,bd=5)
    tempf.place(x=130,y=110,height=30,width=300)
    atp=tkinter.Label(window3,text="atm pressure:",relief="ridge",bg="teal",bd=5)
    atp.place(x=20,y=150,height=30,width=100)
    atpf=tkinter.Entry(window3,textvariable=atpn,bd=5)
    atpf.place(x=130,y=150,height=30,width=300)
    hum=tkinter.Label(window3,text="humidity:",relief="ridge",bg="teal",bd=5)
    hum.place(x=20,y=190,height=30,width=100)
    humf=tkinter.Entry(window3,textvariable=humn,bd=5)
    humf.place(x=130,y=190,height=30,width=300)
    des=tkinter.Label(window3,text="description:",relief="ridge",bg="teal",bd=5)
    des.place(x=20,y=230,height=30,width=100)
    desf=tkinter.Entry(window3,textvariable=desn,bd=5)
    desf.place(x=130,y=230,height=30,width=300)
    cc=tkinter.Button(window3,text="clear",command=cll,bd=7,bg="teal")
    cc.place(x=210,y=270,height=30,width=100)
    btn1=tkinter.Button(window3,text="back",command=win3closer,bd=7,bg="teal")
    btn1.place(x=20,y=320,height=30,width=100)
    menubar=tkinter.Menu(window3)
    menubar.add_command(label="search",command=winn)
    
    if txt1var.get()=="sima123" and txt2var.get()=="1234":
        menubar.add_command(label="register",command=win2opener)
        menubar.add_command(label="view",command=vie)
    else:
        menubar.add_command(label="view",command=viea)
    window3.config(menu=menubar)
        

def ss():
    global window4
    global city1
    global cityname1
    window4=tkinter.Tk()
    window4.geometry("600x600+100+100")
    window4.title("info")
    img=ImageTk.PhotoImage(file=r"weatherbg.jpg")
    window4.img=img
    tkinter.Label(window4,image=img).place(relwidth=1,relheight=1)
    
    cityname1=tkinter.StringVar(window4)
    city=tkinter.Label(window4,text="date:",bg="teal",relief="ridge",bd=5)
    city.place(x=20,y=30,height=30,width=100)
    city1=tkinter.Entry(window4,textvariable=cityname1,bd=5)
    city1.place(x=130,y=30,height=30,width=300)
    sub=tkinter.Button(window4,text="search",command=s1,bd=5,bg="teal")
    sub.place(x=140,y=80,height=20,width=100)
    btn1=tkinter.Button(window4,text="back",command=win4closer,bd=7,bg="teal")
    btn1.place(x=20,y=320,height=30,width=100)
def s1():
    global cityname1
    global mycursor
    global mydb
    global lis6
    global var6
    global t1var
    global t2var
    global t3var
    global t4var
    global t5var
    global t6var
    global txt1var
    global txt2var
    global txt8var


    global tvar
    global t
    global t1
    global t2
    global t3
    global t4
    global t5
    global t6

    t1var.clear()
    t2var.clear()
    t3var.clear()
    t4var.clear()
    t5var.clear()
    t6var.clear()

    tvar.clear()

    t.clear()
    t1.clear()
    t2.clear()
    t3.clear()
    t4.clear()
    t5.clear()
    t6.clear()

    lis6.clear()
    var6.clear()

    h=0

    if txt1var.get()=="sima123" and txt2var.get()=="1234":
        mycursor.execute("select * from info where weatherDate='"+cityname1.get()+"'")
        data=mycursor.fetchall()
    else:
        mycursor.execute("select * from info where weatherDate='"+cityname1.get()+"'and mail='"+txt8var.get()+"'")
        data=mycursor.fetchall()
    
    if len(data)==0:
        messagebox.showinfo("info","no data is there in ")
    else:
        i=0
        while i in range(len(data)):
            tvar.append(tkinter.IntVar(window4))
            t1var.append(tkinter.StringVar(window4))
            t2var.append(tkinter.StringVar(window4))
            t3var.append(tkinter.StringVar(window4))
            t4var.append(tkinter.StringVar(window4))
            t5var.append(tkinter.StringVar(window4))
            t6var.append(tkinter.StringVar(window4))
            var6.append(tkinter.IntVar(window4))
            t.append(tkinter.Entry(window4,textvariable=tvar[i]))
            t[i].place(x=10,y=100+h,height=30,width=30)
            
            t1.append(tkinter.Entry(window4,textvariable=t1var[i]))
            t1[i].place(x=40,y=100+h,height=30,width=80)
            t2.append(tkinter.Entry(window4,textvariable=t2var[i]))
            t2[i].place(x=120,y=100+h,height=30,width=80)
            t3.append(tkinter.Entry(window4,textvariable=t3var[i]))
            t3[i].place(x=200,y=100+h,height=30,width=80)
    
            t4.append(tkinter.Entry(window4,textvariable=t4var[i]))
            t4[i].place(x=280,y=100+h,height=30,width=100)
            t5.append(tkinter.Entry(window4,textvariable=t5var[i]))
            t5[i].place(x=380,y=100+h,height=30,width=80)
            t6.append(tkinter.Entry(window4,textvariable=t6var[i]))
            t6[i].place(x=460,y=100+h,height=30,width=80)

            lis6.append(tkinter.Checkbutton(window4,text="delete",onvalue=1,offvalue=0,variable=var6[i]))
            lis6[i].place(x=540,y=100+h,height=30,width=60)
            tvar[i].set(data[i][0])
            t1var[i].set(data[i][1])
            t2var[i].set(data[i][2])
            t3var[i].set(data[i][3])
            t4var[i].set(data[i][4])
            t5var[i].set(data[i][5])
            t6var[i].set(data[i][6])
            h=h+40
            i=i+1
        btn=tkinter.Button(window4,text="delete",command=dell,bd=7,bg="teal")
        btn.place(x=140,y=100+h,height=30,width=100)

def dell():
    global mydb
    global mycursor
    global lis6
    global var6
    global tvar
    i=0
    while i<len(lis6):
        if var6[i].get()==1:
            var=tvar[i].get()
            mycursor.execute("delete from info where id='"+str(var)+"'")
            mydb.commit()
        i=i+1
    window4.destroy()
    ss()



            
            





def win4opener():
    window3.destroy()
    win4()


def win4closer():
    window4.destroy()
    win3()

def win2opener():
    window3.destroy()
    win2()
def bb():
    window7.destroy()
    win3()
def vie():
    window3.destroy()
    vieal()
def viea():
    window3.destroy()
    vieall()

def win2closer():
    window2.destroy()
    win3()
def win3opener():
    window1.destroy()
    win3()
def win3closer():
    window3.destroy()
    win1()
def register():
    global mycursor
    global mydb
    global txt3var
    global txt4var
    global txtvar
    mycursor.execute("select * from admin where username='"+txt3var.get()+"'and password='"+txt4var.get()+"'")
    data=mycursor.fetchall()
    if len(data)>0:
        messagebox.showinfo("info","user is already registered")
    else:
        mycursor.execute("insert into admin(username,password,mail) values('"+txt3var.get()+"','"+txt4var.get()+"','"+txtvar.get()+"')")
        mydb.commit()
        messagebox.showinfo("info","user registered successfully ")
def checker():
    global mycursor
    global txt1var
    global txt2var
    global txt8var
    global a
    mycursor.execute("select * from admin where username='"+txt1var.get()+"'and password='"+txt2var.get()+"'")
    data=mycursor.fetchall()
    if len(data)>0:
        a=data[0][0]
        b=data[0][3]
        
        if txt8var.get()==b:
            win3opener()
        else:

            messagebox.showinfo("info","username or password or mail is error")
            
    else:
        messagebox.showinfo("info","username or password or mail is error")
def viewall():
    mycursor.execute("select * from admin ")
    data=mycursor.fetchall()
    b=tkinter.Label(window3,text="username",bg="teal",relief="ridge",bd=5)
    b.place(x=100,y=50,height=30,width=100)
    d=tkinter.Label(window3,text="password",bg="teal",relief="ridge",bd=5)
    d.place(x=210,y=50,height=30,width=100)

    
    h=0
    for datae in range(len(data)):
        t1var=tkinter.StringVar(window3)
        t2var=tkinter.StringVar(window3)
        t1=tkinter.Entry(window3,textvariable=t1var)
        t1.place(x=100,y=100+h,height=30,width=100)
        t2=tkinter.Entry(window3,textvariable=t2var)
        t2.place(x=210,y=100+h,height=30,width=100)
        t1var.set(data[datae][0])
        t2var.set(data[datae][1])
        h=h+40

def subb():
    
    global tempn
    global atpn
    global humn
    global desn
    global cityn
    global sub
    global cityf
    global mycursor
    global mydb

    global txt8var
    apikey="455e95078178ca854b277f7ba5b9ed9b"
    base="http://api.openweathermap.org/data/2.5/weather?"
    cityname=cityn.get()
    sub.config(state=tkinter.DISABLED)
    comple=base+"q="+cityname+"&APPID="+apikey
    response=requests.get(comple)
    x=response.json()
    if x["cod"]!="404":
        y=x["main"]
        t1=y["temp"]
        tempn.set(t1)
        t2=y["pressure"]
        atpn.set(t2)
        t3=y["humidity"]
        humn.set(t3)
        z=x["weather"]
        t4=z[0]["description"]
        desn.set(t4)
        date=datetime.date(datetime.now())
        date=str(date)
        t1=str(t1)
        t2=str(t2)
        t3=str(t3)
        t4=str(t4)
        mycursor.execute("insert into info(City,Temperature,ATP,Humidity,Description,weatherDate,mail) values('"+cityname+"','"+t1+"','"+t2+"','"+t3+"','"+t4+"','"+date+"','"+txt8var.get()+"')")
        mydb.commit()
        
    else:
        messagebox.showerror("error","city not found")
        cityf.delete(0,tkinter.END)
        cityf.focus_set()
def vieal():
    global lis1
    global lis2
    global lis3
    global lis4
    global var4
    global mydb
    global mycursor
    global window1
    global var1
    global var2
    global var3
    global lis5
    global var5
    global lis
    global var
    global win
    lis1.clear()
    lis2.clear()
    lis3.clear()
    lis5.clear()
    
    var1.clear()
    var2.clear()
    var3.clear()
    lis4.clear()
    var4.clear()
    var5.clear()

    lis.clear()
    var.clear()
    win=tkinter.Tk()
    win.geometry("600x600")
    img=ImageTk.PhotoImage(file=r"weatherbg.jpg")
    win.img=img
    tkinter.Label(win,image=img).place(relwidth=1,relheight=1)
    
    mycursor.execute("select * from admin ")
    data=mycursor.fetchall()
    i=0
    h=0
    while i in range(len(data)):
        var1.append(tkinter.IntVar(win))
        var2.append(tkinter.StringVar(win))
        var3.append(tkinter.StringVar(win))
        var.append(tkinter.StringVar(win))
   
        var4.append(tkinter.IntVar(win))
        var5.append(tkinter.IntVar(win))
        
        lis1.append(tkinter.Entry(win,textvariable=var1[i]))
        lis2.append(tkinter.Entry(win,textvariable=var2[i]))
        lis3.append(tkinter.Entry(win,textvariable=var3[i]))
        lis.append(tkinter.Entry(win,textvariable=var[i]))
        
        lis4.append(tkinter.Checkbutton(win,text="update",onvalue=1,offvalue=0,variable=var4[i]))
        lis5.append(tkinter.Checkbutton(win,text="delete",onvalue=1,offvalue=0,variable=var5[i]))

        lis1[i].place(x=50,y=50+h,height=30,width=100)
        lis2[i].place(x=160,y=50+h,height=30,width=100)
        lis3[i].place(x=270,y=50+h,height=30,width=100)
        lis[i].place(x=370,y=50+h,height=30,width=100)
        
        lis4[i].place(x=450,y=50+h,height=30,width=80)
        lis5[i].place(x=530,y=50+h,height=30,width=50)
        var1[i].set(data[i][0])
        var2[i].set(data[i][1])
        var3[i].set(data[i][2])
        var[i].set(data[i][3])
        i=i+1
        h=h+40
    btn=tkinter.Button(win,text="update",command=update,bg="teal",bd=7)
    btn.place(x=160,y=50+h,height=30,width=100)
    btn=tkinter.Button(win,text="delete",command=delete,bg="teal",bd=7)
    btn.place(x=270,y=50+h,height=30,width=100)
    btn=tkinter.Button(win,text="back",command=bb1,bg="teal",bd=7)
    btn.place(x=20,y=320,height=30,width=100)
def bb1():
    win.destroy()
    win3()
def update():
    global mydb
    global mycursor
    global lis1
    global lis2
    global lis
    global lis4
    global var1
    global var2
    global var3
    global var4
    global var
    global win

    i=0
    while i<len(lis4):
        if var4[i].get()==1:
            a=var1[i].get()
            mycursor.execute("update admin set username='"+var2[i].get()+"',password='"+var3[i].get()+"',mail='"+var[i].get()+"'where id='"+str(a)+"'")
            mydb.commit()
            
        
            
            
        i=i+1
    messagebox.showinfo("info","updated successfully")
    win.destroy()
    vieal()
def vieall():
    global window7
    global txt5var
    global txt6var
    global txt1var
    global txt2var
    global txt8var
    global txt9var
    global mycursor
    global mydb
    global a
    
    window7=tkinter.Tk()
    window7.geometry("600x600+100+100")
    window7.config(bg="pink")
    img=ImageTk.PhotoImage(file=r"weatherbg.jpg")
    window7.img=img
    tkinter.Label(window7,image=img).place(relwidth=1,relheight=1)
    
    txt5var=tkinter.StringVar(window7)
    txt6var=tkinter.StringVar(window7)
    txt9var=tkinter.StringVar(window7)
    username=tkinter.Label(window7,text="username",bg="teal",relief="ridge",bd=5)
    username.place(x=100,y=200,height=30,width=100)
    password=tkinter.Label(window7,text="password",bg="teal",relief="ridge",bd=5)
    password.place(x=100,y=240,height=30,width=100)
    mail=tkinter.Label(window7,text="mail",bg="teal",relief="ridge",bd=5)
    mail.place(x=100,y=280,height=30,width=100)
    usl=tkinter.Entry(window7,textvariable=txt5var,bd=5)
    usl.place(x=210,y=200,height=30,width=100)
    passl=tkinter.Entry(window7,textvariable=txt6var,bd=5)
    passl.place(x=210,y=240,height=30,width=100)
    mail=tkinter.Entry(window7,textvariable=txt9var,bd=5)
    mail.place(x=210,y=280,height=30,width=100)
    
    btn=tkinter.Button(window7,text="update",command=upd,bd=7,bg="teal")
    btn.place(x=210,y=320,height=30,width=100)
    btn=tkinter.Button(window7,text="Back",command=bb,bd=7,bg="teal")
    btn.place(x=210,y=360,height=30,width=100)
    a=str(a)
   
    mycursor.execute("select * from admin where id='"+a+"'")
    data=mycursor.fetchall()
    b=data[0][1]
    c=data[0][2]
    d=data[0][3]
    
    
    txt9var.set(d)
    txt5var.set(b)
    txt6var.set(c)
    
    
        
def delete():
    global mydb
    global mycursor
    global lis1
    global lis2
    global lis4
    global lis5
    global var5
    global var1
    global var2
    global var3
    global var4

    i=0
    while i<len(lis4):
        if var5[i].get()==1:
            var=var1[i].get()
            mycursor.execute("delete from admin where id='"+str(var)+"'")
            mydb.commit()
        i=i+1
def upd():
    global txt5var
    global txt6var
    global txt1var
    global txt2var
    global txt9var
    global mycursor
    global mydb

    mycursor.execute("select id from admin where username='"+txt1var.get()+"'and password='"+txt2var.get()+"'")
    a=mycursor.fetchall()
    b=a[0][0]
    b=str(b)
    
    mycursor.execute("update admin set username='"+txt5var.get()+"',password='"+txt6var.get()+"',mail='"+txt9var.get()+"'where id='"+b+"'")
    mydb.commit()
    messagebox.showinfo("info","updated successfully")
    

    
        
def cll():
    global cityf
    global tempf
    global atpf
    global humf
    global desf
    sub.config(state=tkinter.ACTIVE)
    cityf.delete(0,tkinter.END)
    tempf.delete(0,tkinter.END)
    atpf.delete(0,tkinter.END)
    humf.delete(0,tkinter.END)
    desf.delete(0,tkinter.END)
    cityf.focus_set()
def winn():
    window3.destroy()
    ss()

win1()

