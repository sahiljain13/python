from Tkinter import *

root1=Tk()
root1.geometry("1920x1080")

def fun(e):
    root1.destroy()
    import sahiljain

photo=PhotoImage(file='sahil.gif')
l=Label(root1,image=photo)
l.bind('<Motion>',fun)
l.place(x=0,y=0)

Label(root1,text='Car Booking System',font='times 40 bold',bg='black',fg='white').place(x=280,y=300)
Label(root1,text='Sahil Jain  \n171B106 \n Batch:B3 \n Email: sahil13jain@gmail.com' ,font='times 42 bold',bg='black',fg='white').place(x=400,y=400)
root1.mainloop()
