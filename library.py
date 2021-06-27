#library management system
from os import system
from datetime import datetime,timedelta
#from datetime import datetime
import random


book_list = [{'Id':101,'Name':'Informatics Practices','Quantity':4,'Author':'Sumita Arora','Price':450,
             'Class':'11','Issue_date':['23/08/2020'],'Return_date':['22/09/2020'],
             'Issued_by':['steve samson'], 'Returned':['No']}]

Student_list = []

def check_available_id():
    id = random.randint(100,500)
    for a in book_list:
        if id == a['Id']:
            break
    else:
        return id
    check_available_id()
system('cls')
ch=''     
def main_menu():
    print('1. New Book')
    print('2. List of Students')
    print('3. Issue Book')
    print('4. Return Book')
    print('5. List of books')
    print('0.  EXIT')
    ch = input('Enter the number to continue')
    return ch

while ch!='0':
    ch = main_menu()
    
    if ch == '1':
        system('cls')
        name = input('Enter name of the book\t')
        author = input('Enter name of the author\t')
        price = float(input('Enter price\t'))
        cl = input('Enter class\t')
        quantity = int(input('Enter no of books\t'))
        iss_date = list()
        issued_by = list()
        return_date=list()
        id = check_available_id()        
        returned = list()
        book_dict={'Id':id,'Name':name,'Quantity':quantity,'Author':author,'Price':price,'Class':cl,
                   'Issue_date':iss_date,'Return_date':return_date
                   ,'Issued_by':issued_by,'Returned':returned}
        book_list.insert(0,book_dict)
        
        choice = input('Press 9 to go back to the Main Menu\n 0 to Exit')
        if choice=='9':
            system('cls')
        else:
            break
    elif ch == '2':
        for book in book_list:
            print('------------------------------------------------------------')
            print(book['Issued_by'],'\t',book['Name'],'\t',book['Issue_date'])
        choice = input('Press 9 to go back to the Main Menu\n 0 to Exit')
        if choice=='9':
            system('cls')
        else:
            break
            
    elif ch == '3':
        for book in book_list:
            print('------------------------------------------------------------')
            print(book['Id'],'\t',book['Name'],'\t\t',book['Quantity'],'\t',book['Class'])
            
        book_id = int(input('Enter Id of the book to issue\t'))
        issuer = input('Enter Students name\t\t')
        today = datetime.today()
        #time = datetime.now()
        d1 = today.strftime("%d/%m/%Y")
        return_date = today + timedelta(days=30)
        return_date = return_date.strftime("%d/%m/%Y")
        for book in book_list:
            if book_id == book['Id'] and book['Quantity']>0:
                book['Quantity'] = book['Quantity'] - 1
                book['Issued_by'].insert(0,issuer)                
                book['Issue_date'].insert(0,d1)
                book['Return_date'].insert(0,return_date) 
                book['Returned'].insert(0,'No')
                print('******Thankyou Book has been issued successfully******') 
                break
            else:
                print('*****Sorry the book you are looking for is not avialable*****')                
        
        choice = input('Press 9 to go back to the Main Menu\n 0 to Exit')
        if choice=='9':
            system('cls')
        else:
            break
    elif ch == '4':
        for book in book_list:
            print('------------------------------------------------------------')
            print(book['Id'],'\t',book['Name'],'\t\t',book['Quantity'],'\t',book['Issued_by'])
        book_id = int(input('Enter Id of the book to return\t'))
        returnee = input('Enter Students name\t\t')
        today = datetime.today()
        d1 = today.strftime("%d/%m/%Y")
        for book in book_list:
            if book['Id'] == book_id and len(book['Issued_by']) >0 :
                index = book['Issued_by'].index(returnee)
                #book['Issued_by'].remove(returnee)
                #book['Issue_date'].pop(index)
                book['Quantity'] = book['Quantity'] + 1
                book['Return_date'][index] = d1
                book['Returned'][index] = 'Yes'
                print('******Thankyou Book has been returned successfully******')
                break
            else:
                print('****** Sorry Nothing to return*****')
        
        choice = input('Press 9 to go back to the Main Menu\n 0 to Exit')
        if choice=='9':
            system('cls')
        else:
            break 
        
    elif ch == '5':
        system('cls')
        for book in book_list:
            print('*************************************************************')
            print('Id of the book\t\t\t',book['Id'])
            print('Name of the book\t\t',book['Name'])
            print('Author Name\t\t\t',book['Author'])
            print('Price of the book\t\t',book['Price'])
            print('Class \t\t\t\t',book['Class'])
            print('Issue Date\t\t\t',book['Issue_date'])
            print('Issue by\t\t\t',book['Issued_by'])
            print('Books in store\t\t\t',book['Quantity'])
            print('Return Date\t\t\t',book['Return_date'])
            print('Returned or not\t\t\t', book['Returned'])
            print('*************************************************************')
        
        choice = input('Press 9 to go back to the Main Menu\n 0 to Exit')
        if choice=='9':
            system('cls')
        else:
            break
            
    elif ch == '0':
        pass
    else:  
        ch = input('Please Enter any number between 1 to 5')
        