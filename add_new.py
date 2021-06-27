import tkinter
from tkinter import *
from tkinter import font
from PIL import ImageTk, Image

def add_comp():
    print('Added')
    
def book_list(rf):
    #print('List')
    m1 = PanedWindow(rf,orient=HORIZONTAL)
    m1.pack()
    
    add_logo = ImageTk.PhotoImage(Image.open("add.png").resize((70,70))) 
    #label = Label(m1,image=add_logo)  #relief=RAISED 
    list_stud = Button(m1,image=add_logo,border=1)
    m1.add(list_stud)
    
    m2 = PanedWindow(m1, orient=VERTICAL)        
    m1.add(m2)

    label2 = Label(m2,text='Informatics Practices')  #relief=RAISED 
    m2.add(label2)
    label3 = Label(m2,text='Informatics Practices')  #relief=RAISED 
    m2.add(label3)



def issue_book():
    print('Issued')
    
def return_book():
    print('returned')