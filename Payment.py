from Tkinter import *
import os
root=Tk()
def pp():
    root.destroy()
def o():
    os.startfile("Debit.py")
    root.destroy()
def h():
    os.startfile("Thanks2.py")
    root.destroy()
#Label(root,text='Your Payment options',font='Times 50',bg='royalblue1',fg='yellow').grid(row=0,column=0,columnspan=5)
Label(root,text='Your Payment Options',font='airal 30 bold',fg='red',bg='yellow').grid(row=0,column=0,columnspan=5)

Button(root,text='Cash on Delivery',font='Times 15',command=h,fg='royalblue1',bg='white',bd=8).grid(row=1,column=0)
Button(root,text='Cancel Your Booking',font='Times 15',command=pp,fg='royalblue1',bg='white',bd=7).grid(row=1,column=2)
Button(root,text='Pay From Card',font='Times 15',command=o,fg='royalblue1',bg='white',bd=8).grid(row=1,column=4)
root.mainloop()
