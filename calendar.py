from tkinter import *
#from tkcalendar import *
from datetime import datetime
root= Tk()
root.geometry('600x400')

#pip install tkcalendar

cal = Calendar(root,selectmode='day',year=2020,month=10,day=9)
cal.pack(pady=20)
def get_date():
    d = cal.get_date()
    a = d.split('/')
    day = a[1]
    mon = a[0]
    year = a[2]
    d = a[1]+'/'+a[0]+'/'+a[2]
    my_lab.config(text=d)

my_but = Button(root,text='Get date',command=get_date)
my_but.pack(pady=20)
my_lab = Label(root,text='')
my_lab.pack(pady=20)
root.mainloop()