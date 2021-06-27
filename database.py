import sqlite3

def start():
    global conn
    conn = sqlite3.connect('library.db')
    return conn
conn = start()
conn.execute('''CREATE TABLE IF NOT EXISTS Book(
    id INTEGER PRIMARY KEY, name text, quantity integer,author text,price real,
    class text,image_file text);''')

conn.execute('''CREATE TABLE IF NOT EXISTS Issues_book(
    issue_id INTEGER PRIMARY KEY, book_id INTEGER, stud_name text, 
    stud_class text,issue_date text,return_date text);''')

conn.close()
#
#query = 'drop table Book'
#
#conn.execute(query)
#conn.commit()
#
#query = 'select * from Book;'
#a = conn.execute(query)
#for i in a:
#    print(i[6])


#query = 'INSERT INTO Book(id,name,quantity,author,price,class,image_file) VALUES(101,"Applied Physics",4,"Pradeep Chaudhary",699,11,"physics.png");'
#conn.execute(query)
#conn.commit()
#
#query = 'INSERT INTO Book(id,name,quantity,author,price,class,image_file) VALUES(102,"Applied Maths",8,"R. D Sharma",499,11,"maths.jpg");'
#conn.execute(query)
#conn.commit()
#
#query = 'INSERT INTO Book(id,name,quantity,author,price,class,image_file) VALUES(103,"Surface Chemistry",2,"Vikas Ahuja",599,12,"chem.jpg");'
#conn.execute(query)
#conn.commit()
#
#query = 'INSERT INTO Book(id,name,quantity,author,price,class,image_file) VALUES(104,"Informatics Practices",6,"Sumita Arora",699,11, "IT.jpg" );'
#conn.execute(query)
#conn.commit()
#
#query = 'INSERT INTO Book(id,name,quantity,author,price,class,image_file) VALUES(105,"Fundamentals of Biology",10,"Meenakshi Agrawal",699,12,"Biology.jpg");'
#conn.execute(query)
#conn.commit()

#query = 'INSERT INTO Book(id,name,quantity,author,price,class,image_file) VALUES(106,"English Literature",5,"Shakespear",299,10,"eng.jpg");'
#conn.execute(query)
#conn.commit()
#
#query = 'INSERT INTO Book(id,name,quantity,author,price,class,image_file) VALUES(107,"Hindi Vyakaran",10,"Munshi Premchand",199,10,"hindi.jpg");'
#conn.execute(query)
#conn.commit()
#
#query = 'INSERT INTO Book(id,name,quantity,author,price,class,image_file) VALUES(108,"Basic Maths",8,"B. S Grewal",499,12,"maths.jpg");'
#conn.execute(query)
#conn.commit()

def close_database_conn():
    global conn
    conn.close()

def fetch():
    global conn
    conn = start()
    query = "SELECT * FROM Book;"
    result= conn.execute(query)
    #for r in result:
    #    print(r[0],r[1],r[2])    
    return result
#fetch()
#conn.close()
    
def update_book_on_issue(book_id,count):
    global conn
    conn = start()
    query = 'Update Book set quantity= quantity-:c where id=:new_id'
    conn.execute(query,{'new_id':book_id,'c':count})
    conn.commit()
    print('updated')

#def update_book_on_issue(book_id,new_class):
#    global conn
#    conn = start()
#    query = 'Update Book set class = :c where id=:new_id'
#    conn.execute(query,{'new_id':book_id,'c':new_class})
#    conn.commit()
#    print('updated')

#update_book_on_issue(263,6)
#conn.close()
#fetch()
#conn.close()
    
def add_book(b_id,name,quantity,author,price,book_class,filename):
    global conn
    conn = start()
    print(b_id,name,quantity,author,price,book_class,filename)
    conn = start()
    query = "INSERT INTO Book(id,name,quantity,author,price,class,image_file) VALUES(?,?,?,?,?,?,?);"
    conn.execute(query,(b_id,name,quantity,author,price,book_class,filename,))
    conn.commit()
    return 1
    
def delete_book():
    global conn
    conn = start()
    pass

def insert_issue(is_id,b_id,name,cl,iss_dt,ret_dt):
    global conn
    conn = start()
    #print(b_id,name,quantity,author,price,book_class,filename)
    query = """INSERT INTO Issues_book(issue_id, book_id, stud_name, 
    stud_class,issue_date,return_date ) VALUES(?,?,?,?,?,?);"""
    conn.execute(query,(is_id,b_id,name,cl,iss_dt,ret_dt,))
    conn.commit()
    
    return

def fetch_issues():
    global conn
    conn = start()
    query = "SELECT * FROM Issues_book;"
    #result = conn.execute(query)
    #for r in result:
    #    print(r[0],r[1],r[2])    
    result = conn.execute(query)
    return result
#fetch_issues()
#conn.close()
#update_book_on_issue(106)
print('DB Connected') 
 