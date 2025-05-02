import tkinter
from tkinter import ttk
from tkinter import messagebox
import sqlite3
con=sqlite3.connect("sjec.db")
cur = con.cursor()

#Create Department table
cur.execute('''
CREATE TABLE IF NOT EXISTS Department (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
 )
 ''')

# Create Employee table
cur.execute('''
 CREATE TABLE IF NOT EXISTS Employee (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    salary INTEGER,
    department TEXT
 )
 ''')

con.commit()



a=tkinter.Tk()
a.title("GUI")
a.resizable(False,False)

label=tkinter.Label(a,text="Login page",fg="orange",bg="red")
label.grid(column=0, row=0, columnspan=2, pady=10)

bt=tkinter.Label(a,text="Username : ",bg="orange",fg="red")
bt.grid(column=0, row=1, sticky="e", padx=5, pady=5)

bt1=tkinter.Label(a,text="Password : ",bg="orange",fg="red")
bt1.grid(column=0, row=2, sticky="e", padx=5, pady=5)

entry = tkinter.Entry(a, width=30)
entry.grid(column=1, row=1, padx=5, pady=5)

entry1=tkinter.Entry(a,width=30)
entry1.grid(column=1, row=2, padx=5, pady=5)

def login():
    
    b=entry.get().lower()
    c=entry1.get()
    
    if b == "" and c == "":
        label_button.configure(text="Enter the details!!")    
    
    elif b!="delson" :
        label_button.configure(text="Username is incorrect!!")
        entry.delete(0,tkinter.END)
    elif c!="39":
        label_button.configure(text="Password is incorrect!!")
        entry1.delete(0,tkinter.END)
     
    else:
       
         label_button.configure(text="Login successful!!",fg="green")        
         a.destroy()
         next()
         saveinfo()
         
def saveinfo():
     messagebox.showinfo('showinfo', "Login successfull")
        
label_button= tkinter.Label(a, text="", fg="red")
label_button.grid(column=0, row=4, columnspan=2, pady=5)                
       
login_button = tkinter.Button(a, text="Login",bg="orange",fg="red", command=login)
login_button.grid(column=0, row=3, padx=5, pady=5)

def cancel():
    entry.delete(0,tkinter.END)
    entry1.delete(0,tkinter.END)

cancel_button=tkinter.Button(a,text="Cancel",fg="red",bg="orange",command=cancel)
cancel_button.grid(column=1, row=3, padx=5, pady=5, sticky="w")




def canceld1(entry,entry1):
    entry.delete(0,tkinter.END)
    entry1.delete(0,tkinter.END)
     
def deptadd(window):
    window.destroy()
    a=tkinter.Tk()
    a.title("GUI")
    a.resizable(False,False)
    
    label=tkinter.Label(a,text="Department ID: ",fg="orange",bg="red")
    label.grid(column=0, row=0, sticky="e", padx=5, pady=5)
    
    entry = tkinter.Entry(a, width=30)
    entry.grid(column=1, row=0, padx=5, pady=5)
    
    
    bt=tkinter.Label(a,text="Name : ",fg="orange",bg="red")
    bt.grid(column=0, row=1, sticky="e", padx=5, pady=5)
    
    entry1=tkinter.Entry(a,width=30)
    entry1.grid(column=1, row=1, padx=5, pady=5)
    
    def saveinfo():
        messagebox.showinfo('showinfo',"Inserted successfully")
    
    def save():
        b=entry.get()
        c=entry1.get()
        if b == "" and c =="":
         label_button.configure(text="Enter the details!!") 
        
        elif b=="":
          label_button.configure(text="Enter id!!") 
        elif c=="":
          label_button.configure(text="Enter  department name!!") 
    
        else:
           try:
             cur.execute("SELECT 1 FROM Department WHERE id = ?", (b))
             if cur.fetchone() is not None:
                messagebox.showerror('Error', "ID already exists!")
                
             else:
                cur.execute("INSERT INTO Department(id, name) VALUES (?, ?)", (b, c))
                con.commit()
                saveinfo()
                
           except Exception as e:
             messagebox.showerror('Error', f"An error occurred: {e}")
            
            
    label_button= tkinter.Label(a, text="", fg="red")
    label_button.grid(column=0, row=3, columnspan=2, pady=5)
    
    back_button=tkinter.Button(a,text="Back",bg="orange",fg="red",command=lambda:department(a))
    back_button.grid(column=0,row=2,padx=5,pady=5)
    
    save_button=tkinter.Button(a,text="SAVE",bg="orange",fg="red",command=save)
    save_button.grid(column=1,row=2,padx=5,pady=5)
          
    cancel_button=tkinter.Button(a,text="Cancel",bg="orange",fg="red",command=lambda: canceld1(entry,entry1))
    cancel_button.grid(column=2,row=2,padx=5,pady=5)
     
    
    
    
def canceld2(entry):
     entry.delete(0,tkinter.END)         
     
def deptdelete(window):
    window.destroy()
    a=tkinter.Tk()
    a.title("GUI")
    a.resizable(False,False)
    label=tkinter.Label(a,text="Department ID: ",fg="orange",bg="red")
    label.grid(column=0, row=0, sticky="e", padx=5, pady=5)
    
    entry = tkinter.Entry(a, width=30)
    entry.grid(column=1, row=0, padx=5, pady=5)
    
    def saveinfo():
        messagebox.showinfo('showinfo', 'Deleted Successfully')
    def save():
        b=entry.get()
        if b=="":
            label_button.configure(text="Enter the id!!")
        else:  
            try:  
              cur.execute("SELECT 1 FROM Department WHERE id = ?", (b))
              if cur.fetchone() is None:
                  messagebox.showerror('Error', "ID does not exists!")
                  
              else: 
                  cur.execute("DELETE FROM Department WHERE id = ?", (b))
                  con.commit()
                  saveinfo()
            except Exception as e:
             messagebox.showerror('Error', f"An error occurred: {e}")
             
    label_button= tkinter.Label(a, text="", fg="red")
    label_button.grid(column=0, row=2, columnspan=2, pady=5)    

    back_button=tkinter.Button(a,text="Back",bg="orange",fg="red",command=lambda:department(a))
    back_button.grid(column=0,row=1,padx=5,pady=5)
    
    save_button=tkinter.Button(a,text="DELETE",bg="orange",fg="red",command=save)
    save_button.grid(column=1,row=1,padx=5,pady=5)
    
    cancel_button=tkinter.Button(a,text="Cancel",bg="orange",fg="red",command=lambda: canceld2(entry))
    cancel_button.grid(column=2,row=1,padx=5,pady=5)
    
  
    
def canceld3(entry,entry1):
     entry.delete(0,tkinter.END)
     entry1.delete(0,tkinter.END) 
       
def deptupdate(window): 
    window.destroy()    
    a=tkinter.Tk()
    a.title("GUI")
    a.resizable(False,False)
    label=tkinter.Label(a,text="Department ID: ",fg="orange",bg="red")
    label.grid(column=0, row=0, sticky="e", padx=5, pady=5)
    
    entry= tkinter.Entry(a, width=30)
    entry.grid(column=1, row=0, padx=5, pady=5)
    
    bt=tkinter.Label(a,text="Name : ",fg="orange",bg="red")
    bt.grid(column=0, row=1, sticky="e", padx=5, pady=5)
    
    entry1=tkinter.Entry(a,width=30)
    entry1.grid(column=1, row=1, padx=5, pady=5)
    
    def saveinfo():
      messagebox.showinfo('showinfo',"Updated Successfully")
    def save():
        b=entry1.get()
        c=entry.get()
        if b=="" and c=="":
            label_button.configure(text="Enter the updated details!!")
        elif b=="":
            label_button.configure(text="Enter the updated name!!")
        elif c=="":
            label_button.configure(text="Enter the updated id!!")    
        else:
            try:
                cur.execute("SELECT 1 FROM Department WHERE id = ?", (c))
                if cur.fetchone() is None:
                   messagebox.showerror('Error', "ID does not exists!")
                
                else:
                   cur.execute("UPDATE Department SET name=? WHERE id=?", (b, c))
                   con.commit()
                   saveinfo()
            except Exception as e:
               messagebox.showerror('Error', f"An error occurred: {e}")   
               
    back_button=tkinter.Button(a,text="Back",bg="orange",fg="red",command=lambda:department(a))
    back_button.grid(column=0,row=2,padx=5,pady=5)
               
    save_button=tkinter.Button(a,text="UPDATE",bg="orange",fg="red",command=save)
    save_button.grid(column=1,row=2,padx=5,pady=5)
    
    cancel_button=tkinter.Button(a,text="Cancel",bg="orange",fg="red",command=lambda: canceld3(entry,entry1))
    cancel_button.grid(column=2,row=2,padx=5,pady=5)
    
    label_button= tkinter.Label(a, text="", fg="red")
    label_button.grid(column=0, row=3, columnspan=2, pady=5)    
    


    
def department(window):
        window.destroy()
        a=tkinter.Tk()
        a.title("GUI")
        a.resizable(False,False)
        department_label=tkinter.Label(a,text="Department window",fg="orange",bg="red")
        department_label.grid(column=0, row=0, columnspan=4, pady=10)
        columns=("#1","#2")
        c=ttk.Treeview(a,columns=columns,show="headings")
        c.heading("#1",text="id")
        c.heading("#2",text="name")
        c.column("#1", width=100,anchor="center")
        c.column("#2", width=150,anchor="center")
    
        data=[]
        cur.execute("SELECT id,name FROM department")
        data.extend(cur.fetchall())
        
        for row in data:
          c.insert("", tkinter.END, values=row)
          
        c.grid(column=0,row=1,columnspan=4,sticky='nsew')
    
        a.grid_columnconfigure((0,1,2,3),weight=1)
        a.grid_rowconfigure(1,weight=1) 
  
        dadd=tkinter.Button(a,text="ADD",bg="orange",fg="red",command=lambda:deptadd(a))
        dadd.grid(column=0,row=2,padx=5,pady=5,sticky="ew")
        
        ddelete=tkinter.Button(a,text="DELETE",bg="orange",fg="red",command=lambda:deptdelete(a))
        ddelete.grid(column=1,row=2,padx=5,pady=5,sticky="ew")
        
        dupdate=tkinter.Button(a,text="UPDATE",bg="orange",fg="red",command=lambda:deptupdate(a))
        dupdate.grid(column=2,row=2,padx=5,pady=5,sticky="ew")
        
        back_button=tkinter.Button(a,text="BACK",bg="orange",fg="red",command=lambda:(a.destroy(),next()))
        back_button.grid(column=3,row=2,padx=5,pady=5,sticky="ew")
      
        
        
def cancele1(entry,entry1,entry2,entry3):
     entry.delete(0,tkinter.END)
     entry1.delete(0,tkinter.END)
     entry2.delete(0,tkinter.END)
     entry3.delete(0,tkinter.END) 
            
def empadd(window):
    window.destroy()
    a=tkinter.Tk()
    a.title("GUI")
    a.resizable(False,False)
    label=tkinter.Label(a,text="Employee ID: ",fg="orange",bg="red")
    label.grid(column=0, row=0, sticky="e", padx=5, pady=5)
    
    entry = tkinter.Entry(a, width=30)
    entry.grid(column=1, row=0, padx=5, pady=5)
    
    bt=tkinter.Label(a,text="Name : ",fg="orange",bg="red")
    bt.grid(column=0, row=1, sticky="e", padx=5, pady=5)
    
    entry1=tkinter.Entry(a,width=30)
    entry1.grid(column=1, row=1, padx=5, pady=5)
    
    bt1=tkinter.Label(a,text="Salary: ",fg="orange",bg="red")
    bt1.grid(column=0, row=2, sticky="e", padx=5, pady=5)
    
    entry2=tkinter.Entry(a,width=30)
    entry2.grid(column=1, row=2, padx=5, pady=5)
    
    bt2=tkinter.Label(a,text="Department: ",fg="orange",bg="red")
    bt2.grid(column=0, row=3, sticky="e", padx=5, pady=5)
    
    entry3=tkinter.Entry(a,width=30)
    entry3.grid(column=1, row=3, padx=5, pady=5)
    
   
    def saveinfo():
     messagebox.showinfo('showinfo', 'Inserted Successfully')

    def save():
        b=entry.get()
        c=entry1.get()
        d=entry2.get()
        e=entry3.get()
        if b=="" and c=="" and d=="" and e=="":
            label_button.configure(text="Enter the details!!")
        elif b=="":
            label_button.configure(text="Enter the id!!")
        elif c=="":   
            label_button.configure(text="Enter the name!!") 
        elif d=="":
            label_button.configure(text="Enter the salary!!") 
        elif e=="":
            label_button.configure(text="Enter the department!!") 
        else:
            try:           
                cur.execute("SELECT 1 from Employee where  id=?",(b))
                if cur.fetchone() is not None:
                  messagebox.showerror('Error',"Id already exists!")
                else:
                  cur.execute("INSERT INTO Employee(id, name,salary,department) VALUES (?,?,?,?)", (b,c,d,e))
                  con.commit()
                  saveinfo()
            except Exception as e:
               messagebox.showerror('Error', f"An error occurred: {e}")         
            
    back_button=tkinter.Button(a,text="Back",bg="orange",fg="red",command=lambda:employee(a))
    back_button.grid(column=0,row=4,padx=5,pady=5)  
              
    save_button=tkinter.Button(a,text="SAVE",bg="orange",fg="red",command=save)
    save_button.grid(column=1,row=4,padx=5,pady=5)
    
    label_button= tkinter.Label(a, text="", fg="red")
    label_button.grid(column=0, row=5, columnspan=2, pady=5)    
    
    cancel_button=tkinter.Button(a,text="Cancel",bg="orange",fg="red",command=lambda: cancele1(entry,entry1,entry2,entry3))
    cancel_button.grid(column=2,row=4,padx=5,pady=5)
    
    
    
def cancele2(entry):
    entry.delete(0,tkinter.END)
    
def empdelete(window):
    window.destroy()
    a=tkinter.Tk()
    a.title("GUI")
    a.resizable(False,False)
    label=tkinter.Label(a,text="Employee ID: ",fg="orange",bg="red")
    label.grid(column=0, row=0, sticky="e", padx=5, pady=5)
    
    entry = tkinter.Entry(a, width=30)
    entry.grid(column=1, row=0, padx=5, pady=5)
    
    def saveinfo():
     messagebox.showinfo('showinfo', 'Deleted Successfully')
        
    def save():
        b=entry.get()
        if b=="":
            label_button.configure(text="Enter the employee id!!")
        else:
            try:    
              cur.execute("SELECT 1 FROM Employee WHERE id = ?", (b))
              if cur.fetchone() is None:
                  messagebox.showerror('Error',"Id does not exists!")
              else:
                   cur.execute("DELETE FROM employee WHERE id = ?", (b))   
                   con.commit()
                   saveinfo()
            except Exception as e:
               messagebox.showerror('Error', f"An error occurred: {e}")         
                   
    
    label_button= tkinter.Label(a, text="", fg="red")
    label_button.grid(column=0, row=2, columnspan=2, pady=5)   
      
    back_button=tkinter.Button(a,text="Back",bg="orange",fg="red",command=lambda:employee(a))
    back_button.grid(column=0,row=1,padx=5,pady=5)  
      
    save_button=tkinter.Button(a,text="DELETE",bg="orange",fg="red",command=save)
    save_button.grid(column=1,row=1,padx=5,pady=5)
    
    cancel_button=tkinter.Button(a,text="Cancel",bg="orange",fg="red",command=lambda: cancele2(entry))
    cancel_button.grid(column=2,row=1,padx=5,pady=5)
    
   

def cancele3(entry,entry1,entry2,entry3):
     entry.delete(0,tkinter.END)
     entry1.delete(0,tkinter.END)
     entry2.delete(0,tkinter.END)
     entry3.delete(0,tkinter.END) 
      
def empupdate(window):  
    window.destroy()
    a=tkinter.Tk()
    a.title("GUI") 
    a.resizable(False,False)
    label=tkinter.Label(a,text="Employee ID: ",fg="orange",bg="red")
    label.grid(column=0, row=0, sticky="e", padx=5, pady=5)
    
    entry = tkinter.Entry(a, width=30)
    entry.grid(column=1, row=0, padx=5, pady=5)
    
    bt=tkinter.Label(a,text="Name : ",fg="orange",bg="red")
    bt.grid(column=0, row=1, sticky="e", padx=5, pady=5)
    
    entry1=tkinter.Entry(a,width=30)
    entry1.grid(column=1, row=1, padx=5, pady=5)
    
    bt1=tkinter.Label(a,text="Salary: ",fg="orange",bg="red")
    bt1.grid(column=0, row=2, sticky="e", padx=5, pady=5)
    
    entry2=tkinter.Entry(a,width=30)
    entry2.grid(column=1, row=2, padx=5, pady=5)
    
    bt2=tkinter.Label(a,text="Department: ",fg="orange",bg="red")
    bt2.grid(column=0, row=3, sticky="e", padx=5, pady=5)
    
    entry3=tkinter.Entry(a,width=30)
    entry3.grid(column=1, row=3, padx=5, pady=5)
    
    
    def saveinfo():
     messagebox.showinfo('showinfo', 'Updated Successfully')
                    
    def save():
        b=entry1.get()
        c=entry2.get()
        d=entry3.get()
        e=entry.get()
        
        if b=="" and c=="" and d=="" and e=="":
            label_button.configure(text="Enter the details!!")
        elif b=="":
            label_button.configure(text="Enter the updated name!!")
        elif c=="":   
            label_button.configure(text="Enter the updated salary!!") 
        elif d=="":
            label_button.configure(text="Enter the updated department!!") 
        elif e=="":
            label_button.configure(text="Enter the updated id!!") 
        else:
            try:
                cur.execute("SELECT 1 FROM employee WHERE id = ?", (e))
                if cur.fetchone() is None:
                   messagebox.showerror('Error', "ID does not exists!") 
                else:     
                   cur.execute("UPDATE Employee SET name=?,salary=?,department=? WHERE id=?", (b,c,d,e))
                   con.commit()
                   saveinfo()
            except Exception as e:
               messagebox.showerror('Error', f"An error occurred: {e}")    
                
    back_button=tkinter.Button(a,text="Back",bg="orange",fg="red",command=lambda:employee(a))
    back_button.grid(column=0,row=4,padx=5,pady=5)
                                    
    save_button=tkinter.Button(a,text="SAVE",bg="orange",fg="red",command=save)
    save_button.grid(column=1,row=4,padx=5,pady=5)
    
    cancel_button=tkinter.Button(a,text="Cancel",bg="orange",fg="red",command=lambda: cancele3(entry,entry1,entry2,entry3))
    cancel_button.grid(column=2,row=4,padx=5,pady=5)
    
    label_button= tkinter.Label(a, text="", fg="red")
    label_button.grid(column=0, row=5, columnspan=2, pady=5) 
    
    
def employee(window):
        window.destroy()
        a=tkinter.Tk()
        a.title("GUI")
        a.resizable(False,False)
        
        employee_label = tkinter.Label(a, text="Employee Window",fg="orange",bg="red")
        employee_label.grid(column=0, row=0, columnspan=4, pady=10)
        columns=("#1","#2","#3","#4")
        d=ttk.Treeview(a,columns=columns,show="headings")
        d.heading("#1",text="id")
        d.heading("#2",text="name")
        d.heading("#3",text="salary")
        d.heading("#4",text="department")
        d.column("#1", width=100,anchor="center")
        d.column("#2", width=100,anchor="center")
        d.column("#3",width=100,anchor="center")
        d.column("#4",width=100,anchor="center")
        
        data=[]
        
        cur.execute("SELECT id, name,salary,department FROM Employee")
        data.extend(cur.fetchall())
        
        
        for row in data:
          d.insert("", tkinter.END, values=row)
        
        d.grid(column=0,row=1,columnspan=4,sticky='nsew')
         
        a.grid_columnconfigure((0,1,2,3),weight=1)
        a.grid_rowconfigure(1,weight=1)  
        
        eadd=tkinter.Button(a,text="ADD",bg="orange",fg="red",command=lambda:empadd(a))
        eadd.grid(column=0,row=2,padx=5,pady=5,sticky="ew")
        
        edelete=tkinter.Button(a,text="DELETE",bg="orange",fg="red",command=lambda:empdelete(a))
        edelete.grid(column=1,row=2,padx=5,pady=5,sticky="ew")
        
        eupdate=tkinter.Button(a,text="UPDATE",bg="orange",fg="red",command=lambda:empupdate(a))
        eupdate.grid(column=2,row=2,padx=5,pady=5,sticky="ew")
         
        back_button=tkinter.Button(a,text="BACK",bg="orange",fg="red",command=lambda:(a.destroy(),next()))
        back_button.grid(column=3,row=2,padx=5,pady=5,sticky="ew")
               
def next():
    b=tkinter.Tk()
    b.resizable(False,False)
    b.title("GUI")
    label=tkinter.Label(b,text="Data base option",fg="orange",bg="red")
    label.grid(column=0, row=0, columnspan=2, pady=10)
    
    label1=tkinter.Label(b,text="Select a database given below",bg="red",fg="orange")
    label1.grid(column=0, row=1, columnspan=2, pady=10)
      
    button1=tkinter.Button(b,text="Department",bg="orange",fg="red",command=lambda:department(b))
    button1.grid(column=0, row=2, padx=20, pady=10)
       
    button2=tkinter.Button(b,text="Employee",bg="orange",fg="red",command=lambda:employee(b))
    button2.grid(column=1, row=2, padx=20, pady=10)
    
a.mainloop()
con.close()