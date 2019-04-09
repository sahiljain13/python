from Tkinter import *
from tkMessageBox import *
import os
import time
import random
root=Tk()
def pp():
    r=random.randint(56546,79899)
    showinfo('Time','Wait for 3 seconds')
    time.sleep(3)
    showinfo('YOUR OTP',r)
    h(r)
Label(root,text='Debit Card',font='airal 30 bold',fg='red',bg='yellow',bd=5).grid(row=0,column=0,columnspan=7)

Label(root,text='Card No.',font='airal 18',fg='blue',bg='pink').grid(row=1,column=0)
e=Entry(root,bd=5)
e.grid(row=1,column=1)
Label(root,text='CVV No.(3)',font='airal 18',fg='royalblue1',bg='white').grid(row=2,column=0)
e1=Entry(root,show='X',bd=5)
e1.grid(row=2,column=1)
Label(root,text='Amount',font='airal 18',fg='yellow',bg='royalblue1').grid(row=3,column=0)
e2=Entry(root,bd=7)
e2.grid(row=3,column=1)

Button(root,text='Generate your OTP',font='airal 12',bd=20,fg='white',bg='black',command=pp).grid(row=4,column=1,columnspan=1)
def h(x):
    root1=Tk()
    Label(root1,text='Enter OTP',font='airal 22 bold').grid(row=0,column=0,columnspan=3)
    e2=Entry(root1)
    e2.grid(row=1,column=1)
    def uu():
        y=e2.get()
        print 'x:',x,'y:',y
        if int(y)==x:
            showinfo('Time','Wait for Processing...')
            time.sleep(3)
            showinfo('Confirmation','Payment Succesfull')
            root.destroy()
            root1.destroy()
            
        else:
            showinfo('Time','Wait for Processing...')
            time.sleep(3)
            showerror('Error',"Wrong OTP, Generate it again")
    Button(root1,text='Pay',font='Times 12',bd=8,command=uu).grid(row=2,column=1)
root.mainloop()
