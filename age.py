from tkinter import *
from datetime import date

today = date.today()
window = Tk()
window.geometry("400x300")
window.config(bg="#F7DC6F")
window.resizable(width=False,height=False)
window.title('Age Calculator!')
 
def exit():
    window.destroy()
def get_age():
    d = int(e1.get())
    m = int(e2.get())
    y = int(e3.get())
    age = today.year - y -((today.month, today.day)<(m,d))
    t1.config(state='normal')
    t1.delete('1.0', END)
    t1.insert(END,age)
    t1.config(state='disabled')
 
l1 = Label(window,text="The Age Calculator!",font=("Arial", 20),fg="black",bg="#F7DC6F")
l1.place(x=70,y=5)
l2 = Label(window,font=("Arial",12),text="Enter your birthday which includes the day-month-year.",fg="black",bg="#F7DC6F")
l2.place(x=10,y=40)

l_d= Label(window,text="Date: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
l_d.place(x=100,y=70)
l_m= Label(window,text="Month: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
l_m.place(x=100,y=95)
l_y= Label(window,text="Year: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
l_y.place(x=100,y=120)

e1=Entry(window,width=5)
e1.place(x=180,y=70)
e2=Entry(window,width=5)
e2.place(x=180,y=95)
e3=Entry(window,width=5)
e3.place(x=180,y=120)
 
b1=Button(window,text="Calculate Age!",font=("Arial",13),command=get_age)
b1.place(x=100,y=150)

l3 = Label(window,text="The Calculated Age is: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
l3.place(x=50,y=200)
t1=Text(window,width=5,height=0,state="disabled")
t1.place(x=240,y=203)
b2=Button(window,text="Exit Application!",font=("Arial",13),command=exit)
b2.place(x=100,y=230)
 
window.mainloop()