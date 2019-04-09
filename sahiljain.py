from Tkinter import *
from tkMessageBox import *
import os
import sqlite3
from PIL import Image,ImageTk
con=sqlite3.Connection("Booking")
cur=con.cursor()
cur.execute("create table if not exists staff(user varchar(10) primary key,password varchar(20),rpl number)")
#a=(('sahil','jain',1))
#cur.execute("insert into staff values(?,?,?)",a)
con.commit()
cur.execute("select * from staff")
qw=cur.fetchall()
print qw
cur.execute("create table if not exists Booking(fname varchar(20),lname varchar(20),dob number,cost number(8),model varchar(20),ragistration varchar2(10),address varchar(56),mob number(10),qty number(2))")

def st() : #STAFF Login
    sta=Tk()
    sta.title("Login")
    f=PhotoImage(file="rsz_baleno.gif")
    Label(sta,image=f,compound='right').grid(row=0,columnspan=4)
    Label(sta,text="Staff Login",font="arial 20 bold italic").grid(row=1)
    Label(sta,text="Login id:",font="castellar 16").grid(row=2)
    e=Entry(sta,)
    e.grid(row=3)
    Label(sta,text="Password:",font="castellar 16").grid(row=4)
    ps=Entry(sta,)
    hin=Label(sta,text="Hint")
    ao=hint=Label(sta,text=" username=sahil \n password=jain")
    ps.grid(row=5)
    hin.grid(row=6)
    ao.grid(row=7)
    def check(): #CHECKER
        ch=(str(e.get()),str(ps.get()))
        if e.get()=="" or ps.get()=="":
            showinfo("Missing","username/password not entered")
        cur.execute("select rpl from staff where user=? and password=?",ch)
        kk=cur.fetchone()
        if kk==True:
            if int(kk[0])==True:
                re=e.get()
                sta.destroy()
                rt=Tk()    
                Label(rt,text="Welcome to NEXA %s"%re).pack()
                f=PhotoImage(file="nexawp.gif")
                Label(rt,image=f,compound='right').pack()
                rt.mainloop()
        else :
            showinfo("Login","Incorect Username/password")
    Button(sta,text="log in",command=lambda: check()).grid(row=8)
def Buk(cost,model): #BOOK BUTTON
    root=Tk()
    x=IntVar()
    root.title("Car Booking System")
    Label(root,text="Car Booking Record Keeping System :",font="airal 15",bg="royalblue1").grid(row=0,column=0,columnspan=3)
    Label(root,text="Maruti Suzuki ",font="castellar 20").grid(row=1,column=0)
    Label(root,text=model,font="Castellar 20").grid(row=1,column=1)
    Label(root,text="Amount: %s"%cost,font="castellar 20").grid(row=13,column=0)
    Label(root,text="Enter First Name:").grid(row=2,column=0,sticky='w')
    f=Entry(root,)
    f.grid(row=2,column=1)
    cc=IntVar()
    mod=StringVar()
    cc=cost
    mod=model
    Label(root,text="Enter Last Name :").grid(row=3,column=0,sticky='W')
    l=Entry(root,)
    l.grid(row=3,column=1)
    Label(root,text="Enter DOB :").grid(row=4,column=0,sticky='w')
    d=Entry(root,)
    d.grid(row=4,column=1)
    Label(root,text="Enter registration date :").grid(row=8,column=0,sticky='w')
    re=Entry(root,)
    re.grid(row=8,column=1)
    Label(root,text="Enter Your Address :").grid(row=9,column=0,sticky='w')
    add=Entry(root,)
    add.grid(row=9,column=1)
    Label(root,text="Enter Your Mobile Number :").grid(row=10,column=0,sticky='w')
    mo=Entry(root,)
    mo.grid(row=10,column=1)
    Label(root,text="Enter no of cars to be booked :").grid(row=11,column=0,sticky='w')
    c=Entry(root,)
    c.grid(row=11,column=1)
    Label(root,text="Enter registration No. to fetch record:").grid(row=12,column=0,sticky='w')
    i=Entry(root,)
    i.grid(row=12,column=1)
    def insert(): #BOOK
        a=(f.get(),l.get(),d.get(),cc,mod,re.get(),add.get(),mo.get(),c.get())
        cur.execute("insert into Booking values(?,?,?,?,?,?,?,?,?)",a)
        con.commit()
        cur.execute("select * from Booking")
        a=cur.fetchall()
        ab=int(c.get())
        ac=ab*cost
        showinfo("Congratulation!!","Your bill is %s"%ac)
        os.startfile("Payment.py")
        print a
    def show(): #FIND
        q=int(i.get())
        cur.execute("select * from Booking where fname=(?)",(q,))
        a=cur.fetchall()
        showinfo('Find',a)
        print a
    def showall(): #ALL RECORDS
        cur.execute("select * from Booking")
        a=cur.fetchall()
        showinfo('All records',a)
        print a
    Button(root,text="Book",command=lambda:insert()).grid(row=14,column=0)
    Button(root,text="Find",command=lambda:show()).grid(row=14,column=1,sticky='w')
    Button(root,text="All Records",command=lambda:showall()).grid(row=14,column=2)
    root.mainloop()
        
def fun01(): #SWIFT
    master=Tk()
    master.title("Hondna bike")
    f=PhotoImage(file="swift.gif")
    Label(master,image=f,compound='right').grid(row=0,columnspan=4)
    Label(master,text="Hondna",font="arial 10").grid(row=1,columnspan=4)
    Label(master,text="One of the Best Premium bike.Comes in Two variant Diesel \n and petrol with Auto Breaking technology.").grid(row=2,columnspan=4)
    Label(master,text="RS 80000").grid(row=3,columnspan=8)
    model="Hondna";
    cost=80000
    def st():
        master.destroy()
        Buk(cost,model)

    Button(master,text="Book",command=lambda:st()).grid(row=4,column=1,columnspan=2)
               
    def fun11():
        master.destroy()
        fun02()
    Button(master,text='Previous',command=lambda:fun11()).grid(row=5,column=1,sticky=E)
    def fun12():
        master.destroy()
        fun05()
    Button(master,text='Next',command=lambda:fun12()).grid(row=5,column=2,sticky=W)  
    master.mainloop()
                
def fun02(): #BALENO
    bale = Tk()
    bale.title("Suzuki")
    f=PhotoImage(file="rsz_baleno.gif")
    Label(bale,image=f,compound='right').grid(row=0,columnspan=4)
    Label(bale,text="Baleno").grid(row=1,columnspan=4)
    Label(bale,text="One of the Best bike on road .Comes in Two variant Diesel \n and petrol with  ABS.Enjoy the Luxurious and roll with style.\nThe perfect Style andPower").grid(row=2,columnspan=4)
    Label(bale,text="RS 1200000").grid(row=3,columnspan=8)
    model="Baleno"
    cost=1200000
    def st():
        bale.destroy()
        Buk(cost,model)
           
    Button(bale,text="Book",command=lambda:st()).grid(row=4,column=1,columnspan=2)
        
    def fun21():
        bale.destroy()
        fun03()
    Button(bale,text='Previous',command=lambda:fun21()).grid(row=5,column=1,sticky=E)
    def fun22():
        bale.destroy()
        fun01()
    Button(bale,text='Next',command=lambda:fun22()).grid(row=5,column=2,sticky=W)
    bale.mainloop()

def fun03(): #BREZZA
    doc = Tk()
    doc.title("Maruti Suzuki-Brezza")
    f=PhotoImage(file="rsz_brezza.gif")
    Label(doc,image=f,compound='right').grid(row=0,columnspan=4)
    Label(doc,text="Brezaa",font="arial 10").grid(row=1,columnspan=4)
    Label(doc,text="One of the most Stylish SUV.Comes in Two variant Diesel \n and petrol with Auto Breaking technology.With child door Locks you can Drive freely \n and enjoy ofroading :)").grid(row=2,columnspan=4)
    Label(doc,text="RS 1400000").grid(row=3,columnspan=8)
    cost=1400000
    model="Brezza"
    def st():
        doc.destroy()
        Buk(cost,model)
           
    Button(doc,text="Book",command=st).grid(row=4,column=1,columnspan=2)
        
        
    def fun31():
        doc.destroy()
        fun04()
    Button(doc,text='Previous',command=lambda:fun31()).grid(row=5,column=1,sticky=E)
    def fun32():
        doc.destroy()
        fun02()
    Button(doc,text='Next',command=lambda:fun32()).grid(row=5,column=2,sticky=W)
    doc.mainloop()
def fun04(): #ERTIGA
    ertiga= Tk()
    ertiga.title("Hero")
    f=PhotoImage(file="rsz_ertiga.gif")
    Label(ertiga,image=f,compound='right').grid(row=0,columnspan=4)
    Label(ertiga,text="Hero",font="arial 10").grid(row=1,columnspan=4)
    Label(ertiga,text="Hero Comes in Two variant Diesel \n and petrol with Auto Breaking technology.you can Drive freely.Enjoy the ride \n to enjoy trips better/").grid(row=2,columnspan=4)
    Label(ertiga,text="RS 1800000").grid(row=3,columnspan=8)
    cost=1800000
    model="Hero"
    def st():
        ertiga.destroy()
        Buk(cost,model)
           
    Button(ertiga,text="Book",command=lambda:st()).grid(row=4,column=1,columnspan=2)
        
        
    def fun41():
        ertiga.destroy()
        fun05()
    Button(ertiga,text='Previous',command=lambda:fun41()).grid(row=5,column=1,sticky=E)
    def fun42():
        ertiga.destroy()
        fun03()
    Button(ertiga,text='Next',command=lambda:fun42()).grid(row=5,column=2,sticky=W)
    ertiga.mainloop()
def fun05(): #CIAZ
    ciaz= Tk()
    ciaz.title("Maruti Suzuki-Ciaz")
    f=PhotoImage(file="rsz_ciaz.gif")
    Label(ciaz,image=f,compound='right').grid(row=0,columnspan=4)
    Label(ciaz,text="Ciaz",font="arial 10").grid(row=1,columnspan=4)
    Label(ciaz,text="Enjoy the luxurious Ciaz with powerfull engine and sleek aerodynamics.Comes in Two variant Diesel \n and petrol with Auto Breaking technology.With child door Locks you can Drive freely \n and without any worries").grid(row=2,columnspan=4)
    Label(ciaz,text="RS 1400000").grid(row=3,columnspan=8)
    cost=1400000
    model="Ciaz"
    def st():
        ciaz.destroy()
        Buk(cost,model)
           
    Button(ciaz,text="Book",command=lambda:st()).grid(row=4,column=1,columnspan=2)
        
    def fun51():
        ciaz.destroy()
        fun01()
    Button(ciaz,text='Previous',command=lambda:fun51()).grid(row=5,column=1,sticky=E)
    def fun52():
        ciaz.destroy()
        fun04()
    Button(ciaz,text='Next',command=lambda:fun52()).grid(row=5,column=2,sticky=W)     
    ciaz.mainloop()
def abou():
    abo=Tk()
    Label(abo,text="Next Premium bike launch ",font="algerian 20").grid(row=0)
    i=PhotoImage(file="nexawp.gif")
    Label(abo,image=i,compound='right').grid(row=1)
    def ttt():
        abo.destroy()
    Label(abo,text="This bike is next big thing on the road this is by hondna this \n will be launched by 2020. \n For more details you can contact the nearest showroom ").grid(row=2)
    Button(abo,text="exit",command=lambda: ttt()).grid(row=3)
    abo.mainloop()
    
def menu(): #MAIN MENU
    
    menu=Tk()
    r=101
    menu.title("Menu")
    Label(menu,text="Cars and bike" , font=" algerian 30").grid(row=0,columnspan=5)
    def pr():
        br = Button(menu,)
        image = PhotoImage(file="about.gif")
        br.image=image
        def bbo():
            menu.destroy()
            abou()
        br.config(image=image,command=lambda:bbo())
        br.grid(row=1,column=3)
  
    def pp():
        b = Button(menu,)
        image = PhotoImage(file="rsz_images.gif")
        b.image=image
        def ti():
            menu.destroy()
            fun01()
        b.config(image=image,command=lambda:ti())
        b.grid(row=1,column=1)
  
        def gi():
            menu.destroy()
            st()
        bq.config(image=image,command=lambda:gi())
        bq.grid(row=1,column=2)
    
    
    pr()
    pp()
    pq()
    menu.mainloop()
re=Tk() #FRONT PAGE
re.configure(bg='midnight blue')
Button(re,text="Python Project",bd=-9.5,bg="Royalblue1",justify="left" ,width=444).pack()
image = PhotoImage(file="sahil.gif")
Button.image=image
Label(re,text="Python Project",font="TIMES",fg="pink").pack()
Label(re,text="Name:",font="code 20").pack()
Label(re,text="Sahil jain",font="algerian 20").pack()
Label(re,text="Enrollment Number :",font="algerian 20").pack()
Label(re,text="171B106:",font="arial 20").pack()
Label(re,text="Batch",font="algerian 20").pack()
Label(re,text="B3",font="arial 20").pack()
Label(re,text="Email id:",font="algerian 20").pack()
Label(re,text="sahil13jain@gmail.com",font="arial 20").pack()
Button(re,text="Project",command=lambda:(re.destroy(),menu()),bd=9.5,bg="Royalblue1",justify="right" ,width=444).pack()
re.mainloop()




