#pip install PyMySQL
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

#connection for phpmyadmin
def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root', 
        password='',
        db='database_employee',
    )
    return conn

def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)

    for array in read():
        my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
    my_tree.grid(row=8, column=0, columnspan=5, rowspan=11, padx=10, pady=20)

root = Tk()
root.title("Empployee Database Management System")
root.geometry("1080x720")
my_tree = ttk.Treeview(root)

#placeholders for entry
ph1 = tk.StringVar()
ph2 = tk.StringVar()
ph3 = tk.StringVar()
ph4 = tk.StringVar()

#placeholder set value function
def setph(word,num):
    if num ==1:
        ph1.set(word)
    if num ==2:
        ph2.set(word)
    if num ==3:
        ph3.set(word)
    if num ==4:
        ph4.set(word)
    if num ==5:
        ph5.set(word)

def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employee_table")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results

def add():
    id = str(idEntry.get())
    name = str(nameEntry.get())
    age = str(ageEntry.get())
    department = str(departmentEntry.get())
    

    if (id == "" or id == " ") or (name == "" or name == " ") or (age == "" or age == " ") or (department == "" or department == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO employee_table VALUES ('"+id+"','"+name+"','"+age+"','"+department+"') ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Stud ID already exist")
            return

    refreshTable()
    



def delete():
    decision = messagebox.askquestion("Warning!!", "Delete the selected data?")
    if decision != "yes":
        return 
    else:
        selected_item = my_tree.selection()[0]
        deleteData = str(my_tree.item(selected_item)['values'][0])
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM employee_table WHERE STUDID='"+str(deleteData)+"'")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

        refreshTable()

def select():
    try:
        selected_item = my_tree.selection()[0]
        id = str(my_tree.item(selected_item)['values'][0])
        name = str(my_tree.item(selected_item)['values'][1])
        age = str(my_tree.item(selected_item)['values'][2])
        department= str(my_tree.item(selected_item)['values'][3])
        

        setph(id,1)
        setph(name,2)
        setph(age,3)
        setph(department,4)
        
    except:
        messagebox.showinfo("Error", "Please select a data row")

def search():
    id = str(idEntry.get())
    name = str(nameEntry.get())
    age = str(ageEntry.get())
    department = str(departmentEntry.get())


    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data WHERE STUDID='"+
    id+"' or NAME='"+
    name+"' or AGE='"+
    age+"' or DEPARTMENT='")
    
    try:
        result = cursor.fetchall()

        for num in range(0,5):
            setph(result[0][num],(num+1))

        conn.commit()
        conn.close()
    except:
        messagebox.showinfo("Error", "No data found")

def update():
    selectedStudid = ""

    try:
        selected_item = my_tree.selection()[0]
        selectedStudid = str(my_tree.item(selected_item)['values'][0])
    except:
        messagebox.showinfo("Error", "Please select a data row")

    id = str(idEntry.get())
    name = str(nameEntry.get())
    age = str(ageEntry.get())
    department = str(departmentEntry.get())
    

    if (id == "" or id == " ") or (name == "" or name == " ") or (age == "" or age == " ") or (department == "" or department == " ") :
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE employee_table SET STUDID='"+
            name+"', NAME='"+
            age+"', AGE='"+
            department+"', DEPARTMENT='"+
            id+"' ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Employee ID already exist")
            return

    refreshTable()

label = Label(root, text="Employee Database Management System", font=('Arial Bold', 30))
label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=50, pady=40)

idLabel = Label(root, text="ID", font=('Arial', 15))
nameLabel = Label(root, text="Name", font=('Arial', 15))
ageLabel = Label(root, text="Age", font=('Arial', 15))
departmentLabel = Label(root, text="Department", font=('Arial', 15))

idLabel.grid(row=3, column=0, columnspan=1, padx=50, pady=5)
nameLabel.grid(row=4, column=0, columnspan=1, padx=50, pady=5)
ageLabel.grid(row=5, column=0, columnspan=1, padx=50, pady=5)
departmentLabel.grid(row=6, column=0, columnspan=1, padx=50, pady=5)


idEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph1)
nameEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph2)
ageEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph3)
departmentEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph4)

idEntry.grid(row=3, column=1, columnspan=4, padx=5, pady=0)
nameEntry.grid(row=4, column=1, columnspan=4, padx=5, pady=0)
ageEntry.grid(row=5, column=1, columnspan=4, padx=5, pady=0)
departmentEntry.grid(row=6, column=1, columnspan=4, padx=5, pady=0)


addBtn = Button(
    root, text="Add", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#84F894", command=add)
updateBtn = Button(
    root, text="Update", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#84E8F8", command=update)
deleteBtn = Button(
    root, text="Delete", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#FF9999", command=delete)
searchBtn = Button(
    root, text="Search", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#F4FE82", command=search)

selectBtn = Button(
    root, text="Select", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#EEEEEE", command=select)

addBtn.grid(row=3, column=5, columnspan=1, rowspan=2)
updateBtn.grid(row=5, column=5, columnspan=1, rowspan=2)
deleteBtn.grid(row=7, column=5, columnspan=1, rowspan=2)
searchBtn.grid(row=9, column=5, columnspan=1, rowspan=2)
selectBtn.grid(row=11, column=5, columnspan=1, rowspan=2)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial Bold', 13))

my_tree['columns'] = ("id","name","age","department")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("id", anchor=W, width=170)
my_tree.column("name", anchor=W, width=150)
my_tree.column("age", anchor=W, width=150)
my_tree.column("department", anchor=W, width=165)


my_tree.heading("id", text="Employee ID", anchor=W)
my_tree.heading("name", text="Employee_Name", anchor=W)
my_tree.heading("age", text="Employee_Age", anchor=W)
my_tree.heading("department", text="Employee_Dept", anchor=W)


refreshTable()

root.mainloop()