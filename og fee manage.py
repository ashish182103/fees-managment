from tkinter import *
from tkinter import ttk
from tkinter import Tk, Label, PhotoImage
from tkinter import Tk, Label, Button, PhotoImage
from PIL import Image, ImageTk
from PIL import ImageTk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import tkinter as tk
import sqlite3


# Define global variables
a1, b1, c1, d1, e1, f1, g1 = None, None, None, None, None, None, None
#h1, i1, j1, k1, l1, m1, n1 = None, None, None, None, None, None, None


# Function to handle database operations
def execute_query(query, data=None):
    mydb = mysql.connector.connect(host="localhost", user="root", password="loop", database="college")
    mycursor = mydb.cursor()
    try:
        if data:
            mycursor.execute(query, data)
        else:
            mycursor.execute(query)
        mydb.commit()
    except Exception as e:
        print(f"Error: {e}")
        mydb.rollback()
    finally:
        mydb.close()

# Functions for database operations
def on_insert_click():
    global a1, b1, c1, d1, e1, f1, g1
    a = a1.get()
    b = b1.get()
    c = c1.get()
    d = d1.get()
    e = e1.get()
    f = f1.get()
    g = g1.get()

    if a == "" or b == "" or c == "" or d == "" or e == "" or f == "" or g == "":
        messagebox.showinfo("Insert status", "All Fields are required")
    else:
        query = "INSERT INTO student_pro VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (a, b, c, d, e, f, g)
        execute_query(query, data)

        # Clear entry fields
        for entry in [a1, b1, c1, d1, e1, f1, g1]:
            entry.delete(0, 'end')

        messagebox.showinfo("Insert status", "Inserted Successfully")

def on_delete_click():
    global a1, b1, c1, d1, e1, f1, g1
    if a1.get() == "":
        messagebox.showinfo("Delete status", "Id is compulsory for delete")
    else:
        query = "DELETE FROM student_pro WHERE std_id = %s"
        data = (a1.get(),)
        execute_query(query, data)

        # Clear entry fields
        for entry in [a1, b1, c1, d1, e1, f1, g1]:
            entry.delete(0, 'end')

        messagebox.showinfo("Delete status", "Deleted Successfully")


def search_stdid():
    if(a1.get() == "" ):
        messagebox.showinfo("search status","student Id is compulsory for search")
    else:
        mydb = mysql.connector.connect(host="localhost", user="root", password="loop", database="college")
        mycursor = mydb.cursor()
        a = a1.get()
        mycursor.execute("SELECT * FROM student_pro WHERE std_id = %s", (a,))
        rows = mycursor.fetchall()
        if len(rows) != 0:
                # Display the first row's data in the respective Entry widgets
                data = rows[0]
                b1.delete(0, 'end')
                b1.insert(0, data[1])  # Assuming std_name is in the second column
                c1.delete(0, 'end')
                c1.insert(0, data[2])  # Assuming class is in the third column
                d1.delete(0, 'end')
                d1.insert(0, data[3])  # Assuming div is in the fourth column
                e1.delete(0, 'end')
                e1.insert(0, data[4])  # Assuming dob is in the fifth column
                f1.delete(0, 'end')
                f1.insert(0, data[5])  # Assuming roll_no is in the sixth column
                g1.delete(0, 'end')
                g1.insert(0, data[6])  # Assuming gender is in the seventh column

                messagebox.showinfo("Search status", "Search successful")
        else:
                messagebox.showinfo("Search status", "No data found for the given student ID")

                mydb.commit()
#a1, b1, c1, d1, e1, f1, g1 = None, None, None, None, None, None, None
def execute_query(query, data=None):
    mydb = mysql.connector.connect(host="localhost", user="root", password="loop", database="college")
    mycursor = mydb.cursor()
    try:
        if data:
            mycursor.execute(query, data)
        else:
            mycursor.execute(query)
        mydb.commit()
    except Exception as e:
        print(f"Error: {e}")
        mydb.rollback()
    finally:
        mydb.close()



                
    
def open_fee_details():
    def on_insert_fee_details():
        #global h1, i1, j1, k1, l1, m1, n1
        h = h1.get()
        i = i1.get()
        j = j1.get()
        k = k1.get()
        l = l1.get()
        m = m1.get()
        n = n1.get()

        if h == "" or i == "" or j == "" or k == "" or l == "" or m == "" or n == "":
            messagebox.showinfo("Insert status", "All Fields are required")
        else:
            query = "INSERT INTO fee_detail VALUES (%s, %s, %s, %s, %s, %s, %s)"
            data = (h, i, j, k, l, m, n)
            execute_query(query, data)

            # Clear entry fields
            for entry in [h1, i1, j1, k1, l1, m1, n1]:
                entry.delete(0, 'end')

            messagebox.showinfo("Insert status", "Inserted Successfully")
    def on_delete_click():
        #global a1, b1, c1, d1, e1, f1, g1
        if h1.get() == "":
            messagebox.showinfo("Delete status", "Id is compulsory for delete")
        else:
            query = "DELETE FROM fee_detail  WHERE std_id = %s"
            data = (h1.get(),)
            execute_query(query, data)

            # Clear entry fields
            for entry in [h1, i1, j1, k1, l1, m1, n1]:
                entry.delete(0, 'end')

            messagebox.showinfo("Delete status", "Deleted Successfully")

    def update_on_click():
     h = h1.get();
     i = i1.get();
     j = j1.get();
     k = k1.get();
     l = l1.get();
     m = m1.get();
     n = n1.get();
    
     if(h=="" or i=="" or j=="" or k=="" or l=="" or m=="" or n==""):
        messagebox.showinfo("update status","All Fields are required")
     else:
        mydb = mysql.connector.connect(host="localhost", user="root", password="loop", database="college")
        mycursor = mydb.cursor()
        mycursor.execute("update fee_detail set std_name='"+ i +"', gender='"+ j +"', class='"+ k +"', total_Fee='"+ l +"', fee_Paid='"+ m +"', pending_Fee='"+ n +"' where std_id='"+ h +"'")
        mycursor.execute("commit");
        
        h1.delete(0, 'end')
        i1.delete(0, 'end')
        j1.delete(0, 'end')
        k1.delete(0, 'end')
        l1.delete(0, 'end')
        m1.delete(0, 'end')
        n1.delete(0, 'end')
        messagebox.showinfo("update status","update Succesfully");
        mydb.close();




    text_label=tk.Label(Frameone,text="Fee Details",fg="black",bg="light green",font=('Georgia',24,'bold'),width=40)
    text_label.place(x=0,y=0)
    h = Label(window,text="Student Id:",font=('Georgia',18,'bold'))
    h.place(x=700,y=120)
    i = Label(window,text = "Student Name:",font=('Georgia',18,'bold'))
    i.place(x=700,y=160)
    j = Label(window,text="Gender:                        ",font=('Georgia',18,'bold'))
    j.place(x=700,y=210)
    k = Label(window ,text = "Class:        ",font=('Georgia',18,'bold'))
    k.place(x=700,y=260)
    l = Label(window ,text = "Total Fees:       ",font=('Georgia',18,'bold'))
    l.place(x=700,y=310)
    m = Label(window ,text = "Fees Paid:                  ",font=('Georgia',18,'bold'))
    m.place(x=700,y=360)
    n = Label(window ,text = "Pending Fees:",font=('Georgia',18,'bold'))
    n.place(x=700,y=410)
    h1 = Entry(window )
    h1.place(x=900,y=120)
    i1 = Entry(window )
    i1.place(x=900,y=160)
    j1 = Entry(window)
    j1.place(x=900,y=210)
    k1 = Entry(window )
    k1.place(x=900,y=260)
    l1 = Entry(window)
    l1.place(x=900,y=310)
    m1 = Entry(window )
    m1.place(x=900,y=360)
    n1 = Entry(window )
    n1.place(x=900,y=410)

    insert = Button(window , text="Insert", font=('Georgia',18,'bold'),fg="black",bg="light green",command=on_insert_fee_details)
    insert.place(x=700,y=500)

    delete = Button(window , text="Delete",font=('Georgia',18,'bold'),fg="black",bg="light green", command=on_delete_click)
    delete.place(x=900,y=500)
    
    update = Button(window , text="Update", font=('Georgia',18,'bold'),fg="black",bg="light green", command=update_on_click)
    update.place(x=1100,y=500)

def open_payment():
    new_window = tk.Toplevel(window)
    new_window.title("payment window")
    #g = Label(new_window
    g = Label(new_window,text="QR Code",fg="black",bg="light green",font=('Georgia',18,'bold'),width=100)
    g.pack()
    image_0=Image.open(r"C:\Users\rohit\OneDrive\Pictures\og QR code.png")
    bck_end=ImageTk.PhotoImage(image_0)
    lbl=Label(new_window,image=bck_end)
    lbl.place(x=500,y=150)
    new_window.mainloop()


def open_transac():
    def on_insert_transac():
        
        #global h1, i1, j1, k1, l1, m1, n1
        o = o1.get()
        p = p1.get()
        q = q1.get()
        r = r1.get()
        s = s1.get()
        t = t1.get()
        u = u1.get()

        if o == "" or p == "" or q == "" or r == "" or s == "" or t == "" or u == "":
            messagebox.showinfo("Insert status", "All Fields are required")
        else:
            query = "INSERT INTO student_transactions VALUES (%s, %s, %s, %s, %s, %s, %s)"
            data = (o, p, q, r, s, t, u)
            execute_query(query, data)

            # Clear entry fields
            for entry in [o1, p1, q1, r1, s1, t1, u1]:
                entry.delete(0, 'end')
            messagebox.showinfo("Insert status", "Inserted Successfully")
    def search_transac():
        if(o1.get() == "" ):
            messagebox.showinfo("search status","student Id is compulsory for search")
        else:
            mydb = mysql.connector.connect(host="localhost", user="root", password="loop", database="college")
            mycursor = mydb.cursor()
            o = o1.get()
            mycursor.execute("SELECT * FROM student_transactions WHERE student_id = %s", (o,))
            rows = mycursor.fetchall()
            if len(rows) != 0:
                # Display the first row's data in the respective Entry widgets
                    data = rows[0]
                    p1.delete(0, 'end')
                    p1.insert(0, data[1])  # Assuming std_name is in the second column
                    q1.delete(0, 'end')
                    q1.insert(0, data[2])  # Assuming class is in the third column
                    r1.delete(0, 'end')
                    r1.insert(0, data[3])  # Assuming div is in the fourth column
                    s1.delete(0, 'end')
                    s1.insert(0, data[4])  # Assuming dob is in the fifth column
                    t1.delete(0, 'end')
                    t1.insert(0, data[5])  # Assuming roll_no is in the sixth column
                    u1.delete(0, 'end')
                    u1.insert(0, data[6])  # Assuming gender is in the seventh column

                    messagebox.showinfo("Search status", "Search successful")
            else:
                    messagebox.showinfo("Search status", "No data found for the given student ID")

                    mydb.commit()
    def on_delete_tran():
        #global a1, b1, c1, d1, e1, f1, g1
        if o1.get() == "":
            messagebox.showinfo("Delete status", "Id is compulsory for delete")
        else:
            query = "DELETE FROM student_transactions  WHERE student_id  = %s"
            data = (o1.get(),)
            execute_query(query, data)

            # Clear entry fields
            for entry in [o1, p1, q1, r1, s1, t1, u1]:
                entry.delete(0, 'end')

            messagebox.showinfo("Delete status", "Deleted Successfully")

        
    text_label=tk.Label(Frameone,text="Transaction Details",fg="black",bg="light green",font=('Georgia',24,'bold'),width=40)
    text_label.place(x=0,y=0)
    o = Label(window,text="Student Id:",font=('Georgia',18,'bold'))
    o.place(x=700,y=120)
    p = Label(window,text = "Student Name:",font=('Georgia',18,'bold'))
    p.place(x=700,y=160)
    q = Label(window,text="Transaction id: ",font=('Georgia',18,'bold'))
    q.place(x=700,y=210)
    r = Label(window ,text = "Date:         ",font=('Georgia',18,'bold'))
    r.place(x=700,y=260)
    s= Label(window ,text = "Amount:                ",font=('Georgia',18,'bold'))
    s.place(x=700,y=310)
    t = Label(window ,text = "Payment Mode:",font=('Georgia',18,'bold'))
    t.place(x=700,y=360)
    u = Label(window ,text = "Phone No:       ",font=('Georgia',18,'bold'))
    u.place(x=700,y=410)
    o1 = Entry(window )
    o1.place(x=900,y=120)
    p1 = Entry(window )
    p1.place(x=900,y=160)
    q1 = Entry(window)
    q1.place(x=900,y=210)
    r1 = Entry(window )
    r1.place(x=900,y=260)
    s1 = Entry(window)
    s1.place(x=900,y=310)
    t1 = Entry(window )
    t1.place(x=900,y=360)
    u1 = Entry(window )
    u1.place(x=900,y=410)
    insert = Button(window , text="Insert", font=('Georgia',18,'bold'),bg='light green',command=on_insert_transac)
    insert.place(x=700,y=500)

    delete = Button(window , text="Delete",font=('Georgia',18,'bold'),bg='light green', command=on_delete_tran)
    delete.place(x=900,y=500)

    search = Button(window , text="Search", font=('Georgia',18,'bold'),bg='light green',command=search_transac)
    search.place(x=1100,y=500)
    
def open_fee_management():
    text_label=tk.Label(Frameone,text="Student Profile",fg="black",bg="light green",font=('Georgia',24,'bold'),width=40)
    text_label.place(x=0,y=0)
    global a1, b1, c1, d1, e1, f1, g1
    
    h = Label(window,text="Student Id:",font=('Georgia',18,'bold'))
    h.place(x=700,y=120)
    i = Label(window,text ="Name Of Std:     ",font=('Georgia',18,'bold'))
    i.place(x=700,y=160)
    j = Label(window,text="Class:                   ",font=('Georgia',18,'bold'))
    j.place(x=700,y=210)
    k = Label(window ,text = "Division :",font=('Georgia',18,'bold'))
    k.place(x=700,y=260)
    l = Label(window ,text = "Date Of Birth:",font=('Georgia',18,'bold'))
    l.place(x=700,y=310)
    m = Label(window ,text = "Roll No:                ",font=('Georgia',18,'bold'))
    m.place(x=700,y=360)
    n = Label(window ,text = "Gender:             ",font=('Georgia',18,'bold'))
    n.place(x=700,y=410)
    h1 = Entry(window )
    h1.place(x=900,y=120)
    i1 = Entry(window )
    i1.place(x=900,y=160)
    j1 = Entry(window)
    j1.place(x=900,y=210)
    k1 = Entry(window )
    k1.place(x=900,y=260)
    l1 = Entry(window)
    l1.place(x=900,y=310)
    m1 = Entry(window )
    m1.place(x=900,y=360)
    n1 = Entry(window )
    n1.place(x=900,y=410)

    insert = Button(window , text="Insert", font=('Georgia',18,'bold'),bg='light green',command=on_insert_click)
    insert.place(x=700,y=500)

    delete = Button(window , text="Delete",font=('Georgia',18,'bold'),bg='light green', command=on_delete_click)
    delete.place(x=900,y=500)

    search = Button(window , text="Search", font=('Georgia',18,'bold'),bg='light green',command=search_stdid)
    search.place(x=1100,y=500)
window = Tk()
window.title("Fee Management")
window.geometry('600x600')
Frameone=Frame(window,bd=15,relief=RIDGE)
Frameone.place(x=500,y=50,width=860,height=650)
text_label=tk.Label(Frameone,text="WELCOME",fg="black",bg="light green",font=('Georgia',24,'bold'),width=40)
text_label.pack()
text_label=tk.Label(window,text="fee management",fg="black",bg="light green",font=('Georgia',24,'bold'),width=100)
text_label.pack()
Framedeatils=Frame(window,bd=15,relief=RIDGE)
Framedeatils.place(x=2,y=50,width=500,height=650)
text_label=tk.Label(Framedeatils,text="MENU",fg="black",bg="light green",font=('Georgia',24,'bold'),width=100)
text_label.pack()
student_details = Button(Framedeatils, text="STUDENT PROFILE", height=2, width=30,font=('Georgia',12,'bold'),command= open_fee_management)
student_details .place(x=40,y=90)

fee_details = Button(Framedeatils, text="FEE DETAILS", height=2, width=30,font=('Georgia',12,'bold'),command= open_fee_details)
fee_details .place(x=40,y=180)

payment = Button(Framedeatils, text="PAY HERE", height=2, width=30,font=('Georgia',12,'bold'),command= open_payment)
payment .place(x=40,y=270)

transac = Button(Framedeatils, text="TRANSACTION DETAILS", height=2, width=30,font=('Georgia',12,'bold'),command= open_transac)
transac .place(x=40,y=360)

#reciept = Button(Framedeatils, text="RECIEPT", height=2, width=30,font=('Georgia',12,'bold'),command= open_reciept)
#reciept .place(x=40,y=470)


window.mainloop()
