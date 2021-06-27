import tkinter
import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import messagebox, Scrollbar,Canvas
from tkinter import Menu, filedialog
from PIL import ImageTk, Image
import database as db
#import tkinter as tk
from tkinter import ttk
from datetime import datetime
from datetime import timedelta
import random

# setting up the tkinter window
root = tkinter.Tk()
root.geometry("700x600")
root.resizable(0,0)
root.title("Library Management System")

main_menu_font = font.Font(family='Times New Roman', size=10, weight='bold')

############### MENUBAR 

menubar = Menu(root)  
file = Menu(menubar, tearoff=0)  
file.add_command(label="New")  
file.add_command(label="Open")  
file.add_command(label="Save")  
file.add_command(label="Save as...")  
file.add_command(label="Close")  
  
file.add_separator()  
  
file.add_command(label="Exit", command=root.destroy)  
  
menubar.add_cascade(label="File", menu=file) 

edit = Menu(menubar, tearoff=0)  
edit.add_command(label="Undo")  
edit.add_separator()    
edit.add_command(label="Cut")  
edit.add_command(label="Copy")  
edit.add_command(label="Paste")  
edit.add_command(label="Delete")  
edit.add_command(label="Select All")  
menubar.add_cascade(label="Edit", menu=edit)  

help = Menu(menubar, tearoff=0)  
help.add_command(label="About")  
menubar.add_cascade(label="Help", menu=help)  
  
root.config(menu=menubar)  

topframe = Frame(root, width=700, height=50,bg="#081838")  
topframe.pack(side = TOP) 
#photo = PhotoImage(file='library.png')
#photoimage1 = photo.subsample(1, 6)
photo = ImageTk.PhotoImage(Image.open("lib.jpg").resize((700,100)))  # PIL solution
label = Label(topframe,width=700, height=100,image=photo)  #relief=RAISED 
label.pack()

leftframe = Frame(root,width=103, height=550,bg="#4a88d9")  
leftframe.pack(side=LEFT)

rightframe = Frame(root,width=597, height=550,bg='#104cad')  
rightframe.pack(side=LEFT,expand = True, fill = "both")

#canvas = Canvas(rightframe,bg='#fff',width=597,height=550)

#scrollbar = ttk.Scrollbar(rightframe,orient="vertical",command=canvas.yview)
#canvas.pack(side=LEFT,expand=True, fill=BOTH)
#scrollbar.pack(side=RIGHT, fill=Y)
#canvas.config(yscrollcommand=scrollbar.set)
#scrollbar.config(command=canvas.yview)

#canvas_frame = ttk.Frame(canvas)
#canvas.pack(side=TOP)
#canvas.config(scrollregion=canvas.bbox(ALL))
#canvas.create_window((0, 0), window=canvas_frame, anchor="nw")

    
list_of_books =db.fetch()

def List_OF_BOOKS():
    global list_of_books
    list_of_books =db.fetch()
    return list_of_books

def List_OF_ISSUES():
    #global list_of_books
    list_of_issues = db.fetch_issues()
    return list_of_issues


count=0
li = []
f=0
def next_record(cur_id,s):
    #db.start()
    list_of_books_rec =db.fetch()
    global f
    #print('current;',cur_id)
    #print(list_of_books)
    for a in list_of_books_rec:
        #print('next',f)
        if f == 1:
            #print('inside')
#            s.id_la.configure(text='ID            :\t'+str(a[0]))
#            s.book_la.configure(text='Book Name  :\t'+a[1])
#            s.author_la.configure(text='Author Name:\t'+a[3])
#            s.quantity_la.configure(text='Quantity  :\t'+str(a[2]))
#            s.price_la.configure(text='Book Price :\t'+str(a[4]))
#            s.clas_la.configure(text='Class       :\t'+a[5])
#            s.profile_img_la = ImageTk.PhotoImage(Image.open(a[6]).resize((150,150)))
#            s.canvas.configure(image=s.profile_img_la)
            s.hide()
            new_det = Item_details(rightframe,a)
            #det = Item_details(rightframe,a)
            f=0
            db.close_database_conn()
            return
        if a[0] == cur_id:
            #print('id:',a[0])
            f = 1
    db.close_database_conn()
            
    
def prev_record(cur_id,s):
    #db.start()
    list_of_books_rec =db.fetch()
    global f
    prev = list_of_books_rec.fetchone()
    while True:
        current_record = list_of_books_rec.fetchone() 
        if prev[0] == cur_id:
            f=1
            l = list_of_books_rec.fetchall()  
            #print(len(l))
            prev = l[len(l)-1]               
        elif current_record[0] == cur_id:
            #print('id:',a[0])
            f = 1
        else:
            prev = current_record
        if f==1:
            s.hide()
            new_det = Item_details(rightframe,prev)
            #det = Item_details(rightframe,a)
            f=0
            db.close_database_conn() 
            return
    db.close_database_conn() 
        
def unpack_others():
    for a in rightframe.winfo_children():
        a.destroy()
        #a.pack_forget()   

def generate_random_issue_id():
    #db.start()
    is_id = random.randint(10000,100000)
    
    issues_List = List_OF_ISSUES() #call database to return with list of ids already present
    for i in issues_List:
        if is_id == i[0]:
            generate_random_issue_id()
    db.close_database_conn()
    return is_id

def select_book_picture(event):
    #db.start()
    global canvas_issue_img
    global issue_lbl_image
    global book_id_combo
    n = book_id_combo.get()
    b_list = List_OF_BOOKS()
    for b in b_list:
        if int(n) == b[0]:
            #print('MATCH',b[6])
            img = ImageTk.PhotoImage(Image.open(b[6]).resize((128,128))) 
            canvas_issue_img.image = img
            issue_lbl_image.config(image=img)
            return
        else:
            img = ImageTk.PhotoImage(Image.open('addbook.png').resize((128,128))) 
            canvas_issue_img.image = img
            issue_lbl_image.config(image=img)
    db.close_database_conn()
            
def issue_book_add_to_db(is_id,b_id,name,cl,iss_dt,ret_dt):
    #db.start()
    global response_lbl, issue_labelframe,book_id_combo
    global issuer_name_input_box,issuer_class_input,issuer_date_input,return_date_input
    if int(b_id) == -99:
        print('Sorry select an id')
        return
    db.insert_issue(is_id,int(b_id),name,cl,iss_dt,ret_dt)
    response_lbl.config(text='Successfully Issued')
    
    #Update the database i.e reduce the book quantity
    #db.update_book_on_issue(b_id)
    db.update_book_on_issue(b_id,1)
    #update book issue id and mpty fields
    new_issue_id = generate_random_issue_id()
    issue_labelframe.configure(text='Book Issue No: '+str(new_issue_id))
    
    for index, a in enumerate(book_id_combo['values']):
        if int(a) == -99:
            book_id_combo.current(index)
    issuer_name_input_box.delete(0,END)
    issuer_class_input.delete(0,END)
    todays_date = datetime.today()
    todays_date_str = todays_date.strftime('%d/%m/%y')
    issuer_date_input.config(state='normal')
    issuer_date_input.delete(0,END)
    issuer_date_input.config(text=todays_date_str)
    issuer_date_input.config(state='readonly')
    
    return_date = todays_date + timedelta(days=30)
    return_date_str = return_date.strftime("%d/%m/%Y")
    return_date_input.config(state='normal')
    return_date_input.delete(0,END)
    return_date_input.config(text=return_date_str)
    return_date_input.config(state='readonly')
    db.close_database_conn()
    
def issue_book_to_student(id_no):
    #db.start()
    number=''
    if id_no == -99:
        number = id_no
        pass
    else:
        for i in id_no:
            if (i >= '0' and i<='9'):
                number =  number + i
    
    id_no = number
    global issuer_name_input_box,issuer_class_input,issuer_date_input,return_date_input
    global issue_labelframe,hide1,hide,count,book_id_combo,canvas_issue_img,issue_lbl_image,response_lbl
    #print('List')
    add_new_book.configure(bg="#4a88d9",fg='#fff')
    list_stud.configure(bg="#4a88d9",fg='#fff')
    issue_book.configure(bg='#104cad',fg='#fff')
    #issue_book.configure(fg='#000')  
    #m1 = PanedWindow(rightframe,orient=HORIZONTAL)
    unpack_others()

    new_issue_id = generate_random_issue_id()

    issue_labelframe = LabelFrame(rightframe,text='Book Issue No: '+str(new_issue_id),font=('Times new Roman',16),bg='#104cad',fg='#fff')
    issue_labelframe.pack(pady=15,ipadx=50)
   
    b_list = List_OF_BOOKS()

    book_ids = [-99]
    for i in b_list:
        book_ids.append(i[0])
    
    #book_id_combo['values'] = book_ids
    book_id_combo = ttk.Combobox(issue_labelframe, values= book_ids) 
    for index, a in enumerate(book_id_combo['values']):
        if int(a) == int(id_no):
            #print('here')
            book_id_combo.current(index)
    
    book_id_combo.bind('<<ComboboxSelected>>',select_book_picture)
    book_id_combo.grid(row=0,column=0,columnspan=2,padx=20,pady=15)
    #n.set(102)
    
    issuer_name_lbl = Label(issue_labelframe,text= 'Enter students name :',bg='#104cad',fg='#fff')
    issuer_name_input_box = Entry(issue_labelframe)
    issuer_name_lbl.grid(row=1,column=0,padx=(10,5),pady=10,sticky='w')
    issuer_name_input_box.grid(row=1,column=1,padx=(5,10),pady=10)
    
    issuer_class_lbl = Label(issue_labelframe,text='Enter class :',bg='#104cad',fg='#fff')
    issuer_class_input = Entry(issue_labelframe)
    issuer_class_lbl.grid(row=2,column=0,padx=10,pady=10,sticky='w')
    issuer_class_input.grid(row=2,column=1,padx=10,pady=10)
    
    
    todays_date = datetime.today()
    todays_date_str = todays_date.strftime('%d/%m/%y')

    issuer_date_lbl = Label(issue_labelframe,text='Issue date :',bg='#104cad',fg='#fff')
    issuer_date_input = Entry(issue_labelframe)
    issuer_date_input.insert(0,todays_date_str)
    issuer_date_input.config(state='readonly')
    issuer_date_lbl.grid(row=3,column=0,padx=10,pady=10,sticky='w')
    issuer_date_input.grid(row=3,column=1,padx=10,pady=10)
    
    return_date = todays_date + timedelta(days=30)
    return_date_str = return_date.strftime("%d/%m/%Y")
    return_date_lbl = Label(issue_labelframe,text='Return date :',bg='#104cad',fg='#fff')
    return_date_input = Entry(issue_labelframe)
    return_date_input.insert(0,return_date_str)
    return_date_input.config(state='readonly')
    return_date_lbl.grid(row=4,column=0,padx=10,pady=10,sticky='w')
    return_date_input.grid(row=4,column=1,padx=10,pady=10)
    
    book_image = 'addbook.png'
    b_list = List_OF_BOOKS()
    for i in b_list:
        if i[0] == int(id_no):
            book_image = i[6]
            #print(book_image)
    
    canvas_issue_img = Canvas(issue_labelframe,width=128,height=128)
    issue_book_image = ImageTk.PhotoImage(Image.open(book_image).resize((128,128))) 
    canvas_issue_img.image = issue_book_image
    issue_lbl_image = Label(issue_labelframe,image=issue_book_image,
                        bg='#104cad')
                        
    canvas_issue_but_img = Canvas(issue_labelframe,width=64,height=64)
    issue_image = ImageTk.PhotoImage(Image.open('plus64.png').resize((64,64))) 
    canvas_issue_but_img.image = issue_image
    issue_button_image = Button(issue_labelframe,image=issue_image,
                relief=FLAT,bg='#104cad',
            command=lambda:issue_book_add_to_db(new_issue_id,book_id_combo.get(),
        issuer_name_input_box.get(),issuer_class_input.get(),issuer_date_input.get(),return_date_input.get()))
             
    issue_lbl_image.grid(row=0,padx=(20,0),column=2,rowspan=3)
    issue_button_image.grid(row=5,column=0)
    
    response_lbl = Label(issue_labelframe,text='',fg='#26ed0c',bg='#104cad',font=('Times new Roman',16))
    response_lbl.grid(row=5,column=1)  
    db.close_database_conn()
#    if hide1 == 0:
#        #l.pack_forget()
#        #canvas.pack_forget()
#        #scrollbar.pack_forget()
#        for a in range(count):
#            li[a].hide()
#        l1.pack(side=LEFT)
#        print('show')
#        hide1=1
#        hide=0


class Item_details:
    def __init__(self,rf,a):
        self.font = font.Font(family='Calibri Light', size=16, weight='bold')
        self.rf = rf
        self.id = a[0]
        self.book_name = a[1]
        self.author_name = a[3]
        self.quantity = a[2]
        self.price = a[4]
        self.clas = a[5]
        self.profile = a[6]
        #self.f = Frame(self.rf)
        self.canvas = Canvas(self.rf,bg="#fff",height=150,width=150)
        self.id_la = Label(self.rf,text='ID            :\t'+str(self.id),bg='#104cad',font=self.font,fg='#fff')
        self.book_la = Label(self.rf,text='Book Name  :\t'+self.book_name,bg='#104cad',font=self.font,fg='#fff')
        self.author_la = Label(self.rf,text='Author Name:\t'+self.author_name,bg='#104cad',font=self.font,fg='#fff')
        self.quantity_la = Label(self.rf,text='Quantity  :\t'+str(self.quantity),bg='#104cad',font=self.font,fg='#fff')
        self.price_la = Label(self.rf,text='Book Price :\t'+str(self.price),bg='#104cad',font=self.font,fg='#fff')
        self.clas_la = Label(self.rf,text='Class       :\t'+self.clas,bg='#104cad',font=self.font,fg='#fff')
        
        self.profile_img_la = ImageTk.PhotoImage(Image.open(self.profile).resize((150,150))) 
        #self.profile_icon_la = Label(self.rf,image=self.profile_img_la,bg='#4a88d9',relief=FLAT)
        self.canvas.image = self.profile_img_la
        self.canvas.create_image(0,0,anchor='nw',image=self.profile_img_la)
        
        self.prev = ImageTk.PhotoImage(Image.open('prev.png').resize((40,40))) 
        self.prev_icon= Button(self.rf,image=self.prev ,bg='#104cad',relief=FLAT)
        
        #prev_icon.grid(row=0,column=0)
        self.prev_canvas = Canvas(self.rf,border=0,height=40,width=40)
        self.prev_canvas.image = self.prev
        #self.prev_canvas.create_image(0,0,anchor='nw',image=self.prev)
        
        self.next = ImageTk.PhotoImage(Image.open('next.png').resize((40,40))) 
        self.next_icon= Button(self.rf,image=self.next,bg='#104cad',relief=FLAT)
        #next_icon.grid(row=0,column=3)
        self.next_canvas = Canvas(self.rf,height=40,width=40)
        self.next_canvas.image = self.next
      
        #self.issue_img = ImageTk.PhotoImage(Image.open('next.png').resize((40,40))) 
        self.issue_but = Button(self.rf,text='Issue Book',font=('Arial',16),
            bg='#104cad',fg='#fff',command=lambda:issue_book_to_student(self.id_la['text']))
        
        self.display()
        self.bind(a)
    
    def display(self):
        #self.profile_icon_la.grid(row=0,column=0,rowspan=3,padx=20)
        self.canvas.grid(row=0,column=1,columnspan=2,pady=10)
        #self.profile_icon_la.pack()
        #self.f.grid(row=0,column=0,pady=10)
        self.prev_icon.grid(row=0,column=0,padx=10)
        self.next_icon.grid(row=0,column=3)
        #self.profile_icon_la.pack()
        self.id_la.grid(row=1,column=1,pady=5,sticky=W)
        self.book_la.grid(row=2,column=1,pady=5,sticky=W)
        self.author_la.grid(row=3,column=1,pady=5,sticky=W)
        self.quantity_la.grid(row=4,column=1,pady=5,sticky=W)
        self.price_la.grid(row=5,column=1,pady=5,sticky=W)
        self.clas_la.grid(row=6,column=1,pady=5,sticky=W)
        
        self.issue_but.grid(row=7,column=1,pady=5)
        #self.profile_icon_la.grid(row=0,column=0,rowspan=3,columnspan=3,padx=20,pady=20)
            
    def bind(self,a):
        self.next_icon.bind("<Button-1>",lambda x:next_record(a[0],self))
        self.prev_icon.bind("<Button-1>",lambda x:prev_record(a[0],self))
        
    def hide(self):
        self.canvas.grid_forget()
        self.next_icon.grid_forget()
        self.prev_icon.grid_forget()
        self.id_la.grid_forget()
        self.book_la.grid_forget()
        self.author_la.grid_forget()
        self.quantity_la.grid_forget()
        self.price_la.grid_forget()
        self.clas_la.grid_forget()
        
def create(a):
    #print(a[1],a[2],a[5],a[6])
    for i in li:
        i.frame1.pack_forget()
    det = Item_details(rightframe,a)


class Item:
    def __init__(self,rf,a):
        self.f = font.Font(family='Bahnschrift Condensed', size=16, weight='bold')
        self.f1 = font.Font(family='Agency FB', size=11)
        self.heading = a[1]
        self.quantity = a[2]
        self.clas = a[5]
        self.rf = rf
        #self.cf = canvas_frame
        #self.canvas=canvas
        self.frame1 = Frame(self.rf,bg="#4a88d9",width=200)
        self.head = Label(self.frame1,text=self.heading,font=self.f,bg="#4a88d9",fg='#fff')
        self.quantity = Label(self.frame1,text='Quantity: ' + str(self.quantity),font=self.f1,bg="#4a88d9",fg='#fff')
        self.clas = Label(self.frame1,text='Class: '+ str(self.clas),font=self.f1,bg="#4a88d9",fg='#fff')
        self.arrow = ImageTk.PhotoImage(Image.open("arrow.png").resize((30,30))) 
        self.arrow_icon = Button(self.frame1,image=self.arrow,bg='#4a88d9',relief=FLAT)
        self.trash = ImageTk.PhotoImage(Image.open("trash.png").resize((30,30))) 
        self.trash_icon = Button(self.frame1,image=self.trash,bg='#4a88d9',relief=FLAT)
        self.profile = ImageTk.PhotoImage(Image.open(a[6]).resize((50,50))) 
        self.profile_icon = Label(self.frame1,image=self.profile,bg='#4a88d9',relief=FLAT)
        #self.show()
        self.bind(a)
    def show(self):
        #self.frame1.grid(row=self.row,column=self.column,padx=100,pady=10,ipadx=10)
        self.frame1.pack(side=TOP,padx=50,pady=10,ipadx=10,anchor='w') 
        self.profile_icon.grid(row=0,column=0,rowspan=2)
        self.head.grid(row=0,column=1,columnspan=2,ipady=2)
        self.quantity.grid(row=1,column=1,ipady=2)        
        self.clas.grid(row=1,column=2,ipady=2)
        self.arrow_icon.grid(row=0,column=3,rowspan=2,ipadx=10)
        self.trash_icon.grid(row=0,column=4,rowspan=2)
        
    def hide(self):
        self.frame1.pack_forget()

    def bind(self,a):
        self.arrow_icon.bind("<Button-1>",lambda x:create(a))
hide=0
hide1=0
l = Label(rightframe,text='Hello World')

#li = []

count=count+1


def list_books():
    #db.start()
    global hide,hide1,count
    #print('List')
    list_stud.configure(bg='#104cad',fg='#fff')
    issue_book.configure(bg='#4a88d9',fg='#fff')
    add_new_book.configure(bg='#4a88d9',fg='#fff')
    unpack_others()
    list_of_books = List_OF_BOOKS()
    for a in list_of_books:
        #print('boooks')
        i = Item(rightframe,a)   
        li.append(i)
        i.show()
    db.close_database_conn()
    #m1 = PanedWindow(rightframe,orient=HORIZONTAL)
#    if hide == 0:
#        l1.pack_forget()
#        print(count)
#        for a in range(count):
#            li[a].show()
#        #l.pack(side=LEFT)
#        print('show')
#        hide=1
#        hide1=0
    
def issue_book():
    pass
        
def openfile():
    global canvas_image
    global photo_frame,filename_upload,response_lbl
    filename_upload =  filedialog.askopenfilename(initialdir = "D://Tkinter//LMS",title = "Select file",filetypes = (("png files","*.png"),("all files","*.*")))
    book_upload_img = ImageTk.PhotoImage(Image.open(filename_upload).resize((128,128))) 
    canvas_image.image = book_upload_img
    photo_frame.configure(image =book_upload_img)    
    
def generate_random_id():
    #db.start()
    b_id = random.randint(100,1000)
    
    books_List = List_OF_BOOKS() #call databse to return with list of ids already present
    for b in books_List:
        if b_id == b[0]:
            generate_random_id()
    db.close_database_conn()
    return b_id

def empty_input_field():
    global canvas_image,labelframe
    global name_input_box,quant_input_box,authors_input,price_input,class_input,filename_upload,response_lbl
    
    name_var.set('')
    auth_var.set('')
    price_var.set(0)
    class_var.set('')
    
    book_dummy_img = ImageTk.PhotoImage(Image.open('addbook.png').resize((128,128))) 
    canvas_image.image = book_dummy_img
    photo_frame.configure(image=book_dummy_img)
    new_book_id = generate_random_id()
    labelframe.configure(text='Book Id: '+str(new_book_id))
    
    
def add_book_info_database(new_book_id):
    #db.start()
    global name_input_box,quant_input_box,authors_input,price_input,class_input,filename_upload
    name = name_input_box.get()
    quantity = int(quant_input_box.get())
    author = authors_input.get()
    price = int(price_input.get())
    book_class = class_input.get()
    
    #To extract only the name of the file from the pathname
    filename = filename_upload.split('/')[len(filename_upload.split('/'))-1]
    
    res = db.add_book(new_book_id,name,quantity,author,price,book_class,filename)
    if res:
        response_lbl.configure(text='Successfully Submitted')
    else:
        response_lbl.configure(text='Failed to submit. Try Again', fg='#f2400f')

    empty_input_field()
    db.close_database_conn()

name_var = tk.StringVar()
auth_var = tk.StringVar()
price_var = tk.IntVar()
class_var = tk.StringVar()

def add_book():
    global canvas_image
    global photo_frame,labelframe
    global hide
    global name_input_box,quant_input_box,authors_input,price_input,class_input,response_lbl
    unpack_others()
    list_stud.configure(bg="#4a88d9")
    list_stud.configure(fg='#fff')
    issue_book.configure(bg='#4a88d9')
    issue_book.configure(fg='#fff')
    add_new_book.configure(bg='#104cad',fg='#fff')
    hide=0

    new_book_id = generate_random_id()
    
    labelframe = LabelFrame(rightframe,text='Book Id: '+str(new_book_id),font=('Times new Roman',16),bg='#104cad',fg='#fff')
    labelframe.pack(pady=15,ipadx=70)
    name_lbl = Label(labelframe,text= 'Enter book name',bg='#104cad',fg='#fff')
    name_input_box = Entry(labelframe,textvariable=name_var)
    quant_lbl = Label(labelframe,text='Please select quantity',bg='#104cad',fg='#fff')
    #n = IntVar()
    quant_input_box = Spinbox(labelframe, from_=0, to=30)
    #quant_input_box = ttk.Combobox(rightframe,textvariable=n)
    #quant_input_box['values'] = (1,2,3,4)
    authors_lbl = Label(labelframe,text='Enter authors name',bg='#104cad',fg='#fff')
    authors_input = Entry(labelframe,textvariable=auth_var)
    price_lbl = Label(labelframe,text='Enter price of book',bg='#104cad',fg='#fff')
    price_input = Entry(labelframe,textvariable=price_var)
    class_lbl = Label(labelframe,text='Enter class',bg='#104cad',fg='#fff')
    class_input = Entry(labelframe,textvariable=class_var)
    canvas_image = Canvas(labelframe,width=128,height=128)
    book_dummy_img = ImageTk.PhotoImage(Image.open('addbook.png').resize((128,128))) 
    canvas_image.image = book_dummy_img
    photo_frame = Label(labelframe,image= book_dummy_img,bg='#104cad',fg='#fff')
    photo_frame.bind('<Button-1>',lambda x:openfile())

    canvas_but_image = Canvas(labelframe,width=64,height=64)
    but_image = ImageTk.PhotoImage(Image.open('plus64.png').resize((64,64))) 
    canvas_but_image.image = but_image
    add_button = Button(labelframe,image=but_image,relief=FLAT,
                        bg='#104cad',fg='#fff',command=lambda :add_book_info_database(new_book_id))

    response_lbl = Label(labelframe,text='',fg='#26ed0c',bg='#104cad')
    
    name_lbl.grid(row=0,column=0,padx=25,pady=20,sticky='w')
    name_input_box.grid(row=0,column=1,sticky='w')
    quant_lbl.grid(row=1,column=0,padx=25,sticky='w')
    quant_input_box.grid(row=1,column=1,sticky='w')
    authors_lbl.grid(row=2,column=0,padx=25,pady=20,sticky='w')
    authors_input.grid(row=2,column=1,stick='w')       
    price_lbl.grid(row=3,column=0,padx=25,stick='w')
    price_input.grid(row=3,column=1,sticky='w')
    class_lbl.grid(row=4,column=0,padx=25,pady=20,stick='w')
    class_input.grid(row=4,column=1,stick='w')
    photo_frame.grid(row=5,column=0,padx=25,stick='w')
    add_button.grid(row=6,column=0)
    response_lbl.grid(row=6,column=1)
    
    db.close_database_conn()

add_logo = ImageTk.PhotoImage(Image.open("add.png").resize((30,30))) 
add_new_book = Button(leftframe,font=main_menu_font,
                      text='Add New Book',width=103,height=20,
                      image=add_logo,compound= LEFT,
                      bg="#4a88d9",fg='#fff',relief=FLAT,command=add_book)
add_new_book.pack(side=TOP,pady=5)  

list_logo = ImageTk.PhotoImage(Image.open("list.png").resize((30,30))) 
list_stud = Button(leftframe,font=main_menu_font,text='List Of Books',
                   command=list_books,width=103,height=20,image=list_logo,
                   compound= LEFT,bg="#4a88d9",fg='#fff',relief=FLAT)
list_stud.pack(side=TOP,pady=5)

issue_logo = ImageTk.PhotoImage(Image.open("issue.png").resize((30,30))) 
issue_book = Button(leftframe,font=main_menu_font,text='Issue A Book',
                    command=lambda:issue_book_to_student(-99), width=103,height=20,image=issue_logo,compound= LEFT,
                    bg="#4a88d9",fg='#fff',relief=FLAT)
issue_book.pack(side=TOP,pady=5)

return_logo = ImageTk.PhotoImage(Image.open("return.png").resize((25,25))) 
return_book = Button(leftframe,font=main_menu_font,text='Return A Book', 
                     width=103,height=20,image=return_logo,compound= LEFT,
                     bg="#4a88d9",fg='#fff',relief=FLAT)
return_book.pack(side=TOP,pady=5)

label_space = Label(leftframe,height=29,width=15,bg="#4a88d9",)
label_space.pack(side=BOTTOM)
                    



#btn = tkinter.Button(root,text='Python',image=photoimage1,compound= LEFT,)
#btn.pack()
root.mainloop()
