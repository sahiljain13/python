from Tkinter import *
import os
root=Tk()
def p():
    root.destroy()
def o():
    print"welcome"
root.configure(bg='lightgrey')
Label(root,text='We Welcome you to our family, as our Customer',font='Times 45',fg='white',bg='black').grid(row=1,column=0,columnspan=5)
Label(root,text='Your Booked car will be at your home in 2-3 days',font='Times 30 bold',fg='red',bg='yellow').grid(row=9,column=0,columnspan=5)
Button(root,text='EXIT',font='Times 18 bold',command=p).grid(row=10,column=2)
root.mainloop()
