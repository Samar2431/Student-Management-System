import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import pymysql
from tkinter import messagebox
win=tk.Tk()
win.geometry("1350x900+0+0")
win.title("Student Management System")
title_label=tk.Label(win,text="Student Management System",font=("Arial",30,"bold"),border=12,relief=tk.GROOVE,bg="lightblue")
title_label.pack(side=tk.TOP,fill=tk.X)

detail_frame=tk.LabelFrame(win,text="Enter the Details",font=("Arial",20),bd=12,relief=tk.GROOVE,bg="lightblue")
detail_frame.place(x=30,y=90,width=420,height=650)

data_frame=tk.Frame(win,bd=12,bg="lightgray",relief=tk.GROOVE)
data_frame.place(x=515,y=90,width=1000,height=650)


#---------variables-------#


name=tk.StringVar()
rollno=tk.StringVar()
course=tk.StringVar()
sem=tk.StringVar()
tech=tk.StringVar()
contact=tk.StringVar()
college=tk.StringVar()
address=tk.StringVar()
gender=tk.StringVar()
dob=tk.StringVar()
search_by = tk.StringVar()
search_txt = tk.StringVar()







#---------------#
name_lbl=tk.Label(detail_frame,text="Name",font=("Arial",15),bg="lightblue")
name_lbl.grid(row=0,column=0,padx=2,pady=4)

name_ent=tk.Entry(detail_frame,bd=7,font=("Arial",15),textvariable=name)
name_ent.grid(row=0,column=1,padx=2,pady=4)

#----------------#


rollno_lbl=tk.Label(detail_frame,text="Roll No",font=("Arial",15),bg="lightblue")
rollno_lbl.grid(row=1,column=0,padx=2,pady=4)

rollno_ent=tk.Entry(detail_frame,bd=7,font=("Arial",15),textvariable=rollno)
rollno_ent.grid(row=1,column=1,padx=2,pady=4)


#---------------------#

course_lbl=tk.Label(detail_frame,text="Course",font=("Arial",15),bg="lightblue")
course_lbl.grid(row=2,column=0,padx=2,pady=4)

course_ent=tk.Entry(detail_frame,bd=7,font=("Arial",15),textvariable=course)
course_ent.grid(row=2,column=1,padx=2,pady=4)

#----------------------------#
sem_lbl=tk.Label(detail_frame,text="Semester",font=("Arial",15),bg="lightblue")
sem_lbl.grid(row=3,column=0,padx=2,pady=4)

sem_ent=tk.Entry(detail_frame,bd=7,font=("Arial",15),textvariable=sem)
sem_ent.grid(row=3,column=1,padx=2,pady=4)

#------------------------------#
technology_lbl=tk.Label(detail_frame,text="Technology",font=("Arial",15),bg="lightblue")
technology_lbl.grid(row=4,column=0,padx=2,pady=4)

technology_ent=tk.Entry(detail_frame,bd=7,font=("Arial",15),textvariable=tech)
technology_ent.grid(row=4,column=1,padx=2,pady=4)

#-----------------------#


contact_lbl=tk.Label(detail_frame,text="Contact",font=("Arial",15),bg="lightblue")
contact_lbl.grid(row=5,column=0,padx=2,pady=4)

contact_ent=tk.Entry(detail_frame,bd=7,font=("Arial",15),textvariable=contact)
contact_ent.grid(row=5,column=1,padx=2,pady=4)

#---------------------------------#
college_lbl=tk.Label(detail_frame,text="College",font=("Arial",15),bg="lightblue")
college_lbl.grid(row=6,column=0,padx=2,pady=4)

college_ent=tk.Entry(detail_frame,bd=7,font=("Arial",15),textvariable=college)
college_ent.grid(row=6,column=1,padx=2,pady=4)

#---------------------#

address_lbl=tk.Label(detail_frame,text="Address",font=("Arial",15),bg="lightblue")
address_lbl.grid(row=7,column=0,padx=2,pady=4)

address_ent=tk.Entry(detail_frame,bd=7,font=("Arial",15),textvariable=address)
address_ent.grid(row=7,column=1,padx=2,pady=4)


 #--------------------#
gender_lbl=tk.Label(detail_frame,text="Gender",font=("Arial",15),bg="lightblue")
gender_lbl.grid(row=8,column=0,padx=2,pady=4)

gender_ent=ttk.Combobox(detail_frame,text=("Arial",15),state="readonly",width=35,height=7,textvariable=gender)
gender_ent['values']=("Male","Female","Others")
gender_ent.grid(row=8,column=1,padx=2,pady=4)

#-----------------------#
dob_lbl = tk.Label(detail_frame, text="D.O.B", font=("Arial", 15), bg="lightblue")
dob_lbl.grid(row=9, column=0, padx=2, pady=4)

dob_ent = DateEntry(detail_frame, bd=7, font=("Arial", 15), date_pattern='dd/mm/yyyy',textvariable=dob)
dob_ent.grid(row=9, column=1, padx=2, pady=4)

#-----------functions---------#

def fetch_data():
    conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
    curr = conn.cursor()
    curr.execute("SELECT * FROM DATA")
    rows = curr.fetchall()
    if len(rows) != 0:
        student_table.delete(*student_table.get_children())  
        for row in rows:
            student_table.insert('', tk.END, values=row)
        conn.commit()
    conn.close()

def add_func():
    if name.get()==""or rollno.get()=="" or course.get()=="":
        messagebox.showerror("error","Please fill all the fileds!")
    else:
        conn=pymysql.connect(host="localhost", user="root", password="", database="sms1")   
        curr=conn.cursor()
        curr.execute("INSERT INTO data VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(name.get(),rollno.get(),course.get(),sem.get(),tech.get(),contact.get(),college.get(),address.get(),gender.get(),dob.get()))
        conn.commit()
        conn.close()

        fetch_data()
        


def get_cursor(event):
    cursor_row=student_table.focus()
    content=student_table.item(cursor_row)
    row=content['values']
    name.set(row[0])
    rollno.set(row[1])
    course.set(row[2])
    sem.set(row[3])
    tech.set(row[4])
    contact.set(row[5])
    college.set(row[6])
    address.set(row[7])
    gender.set(row[8])
    dob.set(row[9])

def update_func():
    selected_row = student_table.focus()
    content = student_table.item(selected_row)
    row = content['values']

    if not selected_row:
        messagebox.showerror("Error", "Please select a record to update.")
        return

    conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
    curr = conn.cursor()
    update_query = "UPDATE data SET name=%s, rollno=%s, course=%s, sem=%s, tech=%s, contact=%s, college=%s, address=%s, gender=%s, dob=%s WHERE rollno=%s"
    data = (name.get(), rollno.get(), course.get(), sem.get(), tech.get(), contact.get(), college.get(), address.get(), gender.get(), dob.get(), row[1])

    try:
        curr.execute(update_query, data)
        conn.commit()
        messagebox.showinfo("Success", "Record updated successfully.")
        fetch_data()
        clear_func()
    except Exception as e:
        messagebox.showerror("Error", f"Error updating record: {str(e)}")
    finally:
        conn.close()

def delete_func():
    selected_row = student_table.focus()
    content = student_table.item(selected_row)
    row = content['values']

    if not selected_row:
        messagebox.showerror("Error", "Please select a record to delete.")
        return

    conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
    curr = conn.cursor()
    delete_query = "DELETE FROM data WHERE rollno=%s"
    try:
        curr.execute(delete_query, (row[1],))
        conn.commit()
        messagebox.showinfo("Success", "Record deleted successfully.")
        fetch_data()
        clear_func()
    except Exception as e:
        messagebox.showerror("Error", f"Error deleting record: {str(e)}")
    finally:
        conn.close()



def clear_func():
    name.set("")
    rollno.set("")
    course.set("")
    sem.set("")
    tech.set("")
    contact.set("")
    college.set("")
    address.set("")
    gender.set("")
    dob.set("")  



def search_data():
    conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
    curr = conn.cursor()
    try:
        query = f"SELECT * FROM data WHERE {search_by.get()} LIKE %s"
        curr.execute(query, ('%' + search_txt.get() + '%',))
        rows = curr.fetchall()
        if rows:
            student_table.delete(*student_table.get_children())
            for row in rows:
                student_table.insert('', tk.END, values=row)
        conn.commit()
    except Exception as e:
        messagebox.showerror("Error", f"Error due to: {str(e)}")
    finally:
        conn.close()


         


    

    



#------------buttons----------------#

btn_frame=tk.Frame(detail_frame,bg="lightgray",bd=10,relief=tk.GROOVE)
btn_frame.place (x=20,y=469,width=345,height =120  )  

add_btn=tk.Button(btn_frame,bg="lightgrey",text="Add",bd=7,font=("Arial",13),width=15,command=add_func)
add_btn.grid(row=0,column=0,padx=2,pady=2)

add_btn=tk.Button(btn_frame,bg="lightgrey",text="Update",bd=7,font=("Arial",13),width=15,command=update_func)
add_btn.grid(row=0,column=1,padx=2,pady=2)

add_btn=tk.Button(btn_frame,bg="lightgrey",text="Delete",bd=7,font=("Arial",13),width=15,command=delete_func)
add_btn.grid(row=1,column=0,padx=2,pady=2)

add_btn=tk.Button(btn_frame,bg="lightgrey",text="Clear",bd=7,font=("Arial",13),width=15,command=clear_func)
add_btn.grid(row=1,column=1,padx=2,pady=2)

#--------------search Frame---------#

search_frame=tk.Frame(data_frame,bg="lightblue",bd=10,relief=tk.GROOVE)
search_frame.pack(side=tk.TOP ,fill=tk.X )

search_lbl=tk.Label(search_frame,text="Search",bg="lightblue",font=("Arial",14))
search_lbl.grid(row=0,column=0,padx=12,pady=2)

search_in = ttk.Combobox(search_frame, font=("Arial", 14), state="readonly", textvariable=search_by)
search_in['values'] = ('name', 'rollno', 'contact', 'college', 'dob')
search_in.grid(row=0, column=1, padx=12, pady=2)

search_txt = tk.Entry(search_frame, font=("Arial", 14), textvariable=search_txt)
search_txt.grid(row=0, column=2, padx=12, pady=2)

search_btn=tk.Button(search_frame,text="Search",font=("Arial",9),width=10,bg="lightgrey",command=search_data)
search_btn.grid(row=0,column=4,padx=12,pady=2)

ShowAll_btn=tk.Button(search_frame,text="Show All",font=("Arial",9),width=10,bg="lightgrey",command=fetch_data)
ShowAll_btn.grid(row=0,column=5,padx=12,pady=2)

#------------main frame------------#
main_frame=tk.Frame(data_frame,bg="lightgrey",bd=11,relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH,expand=True)


y_scroll=tk.Scrollbar(main_frame,orient=tk.VERTICAL)
x_scroll=tk.Scrollbar(main_frame,orient=tk.HORIZONTAL)

student_table=ttk.Treeview(main_frame,columns=("Name","Roll No.","Course","Semester","Technology","Contact","College","Address","Gender","D.O.B"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)


y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

student_table.heading("Name",text="Name")
student_table.heading("Roll No.",text="Roll No.")
student_table.heading("Course",text="Course")
student_table.heading("Semester",text="Semester")
student_table.heading("Technology",text="Technology")
student_table.heading("Contact",text="Contact")
student_table.heading("College",text="College")
student_table.heading("Address",text="Address")
student_table.heading("Gender",text="Gender")
student_table.heading("D.O.B",text="D.O.B")

student_table['show']='headings'

student_table.column("Name",width=150)
student_table.column("Roll No.",width=100)
student_table.column("Course",width=100)
student_table.column("Semester",width=100)
student_table.column("Technology",width=100)
student_table.column("Contact",width=100)
student_table.column("College",width=200)
student_table.column("Address",width=200)
student_table.column("Gender",width=100)
student_table.column("D.O.B",width=100)

student_table.pack(fill=tk.BOTH,expand=True)

fetch_data()
student_table.bind("<ButtonRelease-1>",get_cursor)


win.mainloop()
