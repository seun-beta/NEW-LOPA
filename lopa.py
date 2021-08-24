import tkinter as tk
from tkinter import *
from datetime import *
from tkinter.ttk import Style, Treeview
import mysql.connector
import webbrowser



# Create Tables 

conn = mysql.connector.connect(
    host="lopasvr.mysql.database.azure.com",
    user="lopasvr_user@lopasvr",
    password="l0p@$vr_u$er",
    database="lopaproject"
)
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Event (
            event_id INT AUTO_INCREMENT PRIMARY KEY,
            description TEXT,
            target_frequency REAL);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS Cause (
            cause_id INT AUTO_INCREMENT PRIMARY KEY,
            description TEXT,
            initial_frequency REAL,
            event_id INT)
""")

cur.execute("""CREATE TABLE IF NOT EXISTS Cause_Barrier (
            cause_barrier_id INT AUTO_INCREMENT PRIMARY KEY,
            description TEXT,
            pfd REAL,
            cause_id INT)
""")

cur.execute("""CREATE TABLE IF NOT EXISTS Consequence (
            consequence_id INT AUTO_INCREMENT PRIMARY KEY,
            description TEXT,
            target_frequency REAL,
            event_id INT)
""")

cur.execute("""CREATE TABLE IF NOT EXISTS Consequence_Barrier (
            consequence_barrier_id INT AUTO_INCREMENT PRIMARY KEY,
            description TEXT,
            pfd REAL,
            consequence_id INT)
""")

conn.commit()




# Connection to MySQL Database hosted on Azure 
def db_conn():
    global conn 
    global cur
    conn = mysql.connector.connect(
        host="lopasvr.mysql.database.azure.com",
        user="lopasvr_user@lopasvr",
        password="l0p@$vr_u$er",
        database="lopaproject"
    )
    cur = conn.cursor()
    
    return conn, cur

def add_scrollable(widgetFrame: Toplevel, height:int, width:int, color= "white"):
    widgetFrame.title("Layer of Protection Analysis")
    scrollcanvas = Canvas(widgetFrame, bg=color, height=height, width=width)
    scrollbar = Scrollbar(widgetFrame, orient="horizontal", width=18, command=canvas.xview)
    scrollcanvas.configure(scrollregion=(0,0,width,height), xscrollcommand=scrollbar.set)
    scrollcanvas.grid(column=0, row=0, sticky="nsew")
    scrollbar.grid(row=1, column=0, sticky="ew")
    for x in range(0, 2001, 100):
        scrollanchor = "sw" if x < 100 else ("se" if x==2000 else "s")
        canvas.create_line(x, 700, x, 690, fill="red")
        canvas.create_text(x, 680, text=x, anchor=scrollanchor)
    return scrollcanvas

root = Tk()
root.title("Layer of Protection Analysis")
tkintercolor = '#394867'
global presentTop
canvas = Canvas(root, bg=tkintercolor, height=700, width=500)
scrollbar = Scrollbar(root, orient="horizontal", width=18, command=canvas.xview)
canvas.configure(scrollregion=(0,0,700,700), xscrollcommand=scrollbar.set)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

canvas.grid(column=0, row=0, sticky="nsew")
scrollbar.grid(row=1, column=0, sticky="ew")

# this adds tick-marks every 100 pixels so that you can
# see the canvas scroll
for x in range(0, 2001, 100):
    anchor = "sw" if x < 100 else ("se" if x==2000 else "s")
    canvas.create_line(x, 700, x, 690, fill="red")
    canvas.create_text(x, 680, text=x, anchor=anchor)

def new_event():
    
    global save_event
    color = 'orange'
    top = Toplevel(bg=color)
    top.title("Layer of Protection Analysis ")
    cv = add_scrollable(widgetFrame=top, height=400, width=400, color=color)
    newentrylabelframe = LabelFrame(cv, text="Create Event", background=color, foreground="white")
    newentrylabelframe.grid(row=0, column=0, columnspan=2, rowspan=5, padx=20, pady=20)
    
    # --------------Input UI----------------------------
    event_description_label = Label(newentrylabelframe, text="Description:", background=color, foreground='white')
    event_description_label.grid(row=1, column=0, padx=10, pady=10)

    event_description = Entry(newentrylabelframe, width=30)
    event_description.grid(row=1, column=1, padx=10, pady=10)

    
    event_target_freq_label = Label(newentrylabelframe, text="Target Frequency: ", background=color, foreground='white')
    event_target_freq_label.grid(row=2, column=0, padx=10, pady=10)

    event_target_freq = Entry(newentrylabelframe, width=30)
    event_target_freq.grid(row=2, column=1, padx=10, pady=10)

    
    def save_event():
        db_conn()
        cur.execute("INSERT INTO Event VALUES (null, %s, %s)",(
                    event_description.get(),
                    event_target_freq.get()))

        success = Label(newentrylabelframe, text="Added record successfully", fg="green")
        success.grid(row=4, column=1)
        conn.commit()
        event_description.delete(0, END)
        event_target_freq.delete(0, END)
    

    save_event = Button(newentrylabelframe, text="Save", width=20, command=save_event)
    save_event.grid(row=3, column=1)
    


def new_cause():
    db_conn()
    color ='blue'
    top = Toplevel(bg=color)
    cv = add_scrollable(widgetFrame=top, height=400, width=400, color=color)
    newentrylabelframe = LabelFrame(cv, text="Create Cause", background=color, foreground="white")
    newentrylabelframe.grid(row=0, column=0, columnspan=2, rowspan=6, padx=20, pady=20)
    top.title("Layer of Protection Analysis ")

    cause_description_label = Label(newentrylabelframe, text="Description:", background=color, foreground='white')
    cause_description_label.grid(row=2, column=0, padx=10, pady=10)
    cause_description = Entry(newentrylabelframe, width=30)
    cause_description.grid(row=2, column=1, padx=10, pady=10)

    cause_initial_frequency_label = Label(newentrylabelframe, text="Initial Frequency:", background=color, foreground='white')
    cause_initial_frequency_label.grid(row=3, column=0, padx=10, pady=10)
    cause_initial_frequency = Entry(newentrylabelframe, width=30)
    cause_initial_frequency.grid(row=3, column=1, padx=10, pady=10)

    # --------------------------------EVENT ID Dropdown-------------------
    event_id_label = Label(newentrylabelframe, text="Event:", background=color, foreground='white')
    event_id_label.grid(row=1, column=0, padx=10, pady=10)
    cur.execute("""
            SELECT event_id, description FROM Event;
                """)

    event_id_data = cur.fetchall()
    event_id_list = list()
    event_name_list = list()


    for i in event_id_data:
        data = list(i)
        event_id_list.append(data[0])
        event_name_list.append(data[1])
    event_dict = dict(zip(event_name_list, event_id_list))
    
    # dict.fromkeys(event_id_list, "In stock")
    clicked_event = StringVar()
    if len(event_id_list) < 1:
        clicked_event.set("Create Event First")
        event_id_list = ["Create Event First"]
        
    else:
        clicked_event.set(event_name_list[0])

        
    event_id_drop = OptionMenu(newentrylabelframe, clicked_event, *event_name_list)
    event_id_drop.grid(row=1, column=1, pady=10, padx=5)

    # ---------------Save CAUSE-------------------
    def save_cause():
        db_conn()
        cur.execute("INSERT INTO Cause VALUES (null, %s, %s, %s)",(
            cause_description.get(),
            cause_initial_frequency.get(),
            event_dict[clicked_event.get()]
        ))

        success = Label(newentrylabelframe, text="Added record successfully", fg="green")
        success.grid(row=6, column=1, columnspan=2, pady=10)
        conn.commit()
        success.after(5000, success.destroy)
        cause_description.delete(0, END)
        cause_initial_frequency.delete(0, END)

    save_cause = Button(newentrylabelframe, text="Save", width=20, command=save_cause)
    save_cause.grid(row=5, column=1, columnspan=2, pady=10)


def new_cause_barrier():
    top = Toplevel()
    top.title("Layer of Protection Analysis ")
    cv = add_scrollable(widgetFrame=top, height=400, width=400)
    newentrylabelframe = LabelFrame(cv, text="Create Cause Barrier")
    newentrylabelframe.grid(row=0, column=0, columnspan=2, rowspan=6, padx=20, pady=20)





    cause_barrier_description_label = Label(newentrylabelframe, text="Description")
    cause_barrier_description_label.grid(row=2, column=0, padx=10, pady=10)
    cause_barrier_description = Entry(newentrylabelframe, width=30)
    cause_barrier_description.grid(row=2, column=1, padx=10, pady=10)

    cause_barrier_pfd_label = Label(newentrylabelframe, text="PFD")
    cause_barrier_pfd_label.grid(row=3, column=0, padx=10, pady=10)
    cause_barrier_pfd = Entry(newentrylabelframe, width=30)
    cause_barrier_pfd.grid(row=3, column=1, padx=10, pady=10)


    db_conn()
    # -------------CAUSE ID Dropdown----------------------
    cur.execute("""
            SELECT cause_id, description FROM Cause;
                """)

    cause_id_data = cur.fetchall()
    cause_id_list = list()
    cause_name_list = list()

    for i in cause_id_data:
        data = list(i)
        cause_id_list.append(data[0])
        cause_name_list.append(data[1])

    clicked_cause = StringVar()
    cause_dict = dict(zip(cause_name_list, cause_id_list))
    if len(cause_id_list) < 1:
        clicked_cause.set("Create Cause First")
        cause_id_list = ["Create Cause First"]
        
    else:
        clicked_cause.set(cause_name_list[0])

    cause_id = Label(newentrylabelframe, text="Cause:")
    cause_id.grid(row=1, column=0, padx=10, pady=10)
        
    cause_id_drop = OptionMenu(newentrylabelframe, clicked_cause, *cause_name_list)
    cause_id_drop.grid(row=1, column=1, pady=10, padx=40)


    def save_cause_barrier():
        db_conn()
        cur.execute("""INSERT INTO Cause_Barrier VALUES (null, %s, %s, %s)""",(
            cause_barrier_description.get(),
            cause_barrier_pfd.get(),
            cause_dict[clicked_cause.get()])
        )

        success = Label(newentrylabelframe, text="Added record successfully", fg="green")
        success.grid(row=5, column=1, columnspan=2, pady=10)
        conn.commit()

        success.after(5000, success.destroy)
        cause_barrier_description.delete(0, END)
        cause_barrier_pfd.delete(0, END)



    save_cause_barrier = Button(newentrylabelframe, text="Save", width=20, command=save_cause_barrier)
    save_cause_barrier.grid(row=4, column=1, columnspan=2, pady=10)


def new_consequence():
    db_conn()
    color="red"
    top = Toplevel(bg=color)
    top.title("Layer of Protection Analysis ")
    cv = add_scrollable(widgetFrame=top, height=400, width=400, color=color)
    newentrylabelframe = LabelFrame(cv, text="Create Consequence", background=color, foreground="white")
    newentrylabelframe.grid(row=0, column=0, columnspan=2, rowspan=6, padx=20, pady=20)


    consequence_description_label = Label(newentrylabelframe, text="Description:", background=color, foreground='white')
    consequence_description_label.grid(row=2, column=0, padx=10, pady=10)
    consequence_description = Entry(newentrylabelframe, width=30)
    consequence_description.grid(row=2, column=1, padx=10, pady=10)
    
    consequence_target_frequency_label = Label(newentrylabelframe, text="Target Frequency:", background=color, foreground='white')
    consequence_target_frequency_label.grid(row=3, column=0, padx=10, pady=10)
    consequence_target_frequency = Entry(newentrylabelframe, width=30)
    consequence_target_frequency.grid(row=3, column=1, padx=10, pady=10)


    # --------------------------------EVENT ID Dropdown-------------------
    event_id_label = Label(newentrylabelframe, text="Event:", background=color, foreground='white')
    event_id_label.grid(row=1, column=0, padx=20, pady=20)
    cur.execute("""
            SELECT event_id, description FROM Event;
                """)

    event_id_data = cur.fetchall()
    event_id_list = list()
    event_name_list = list()

    for i in event_id_data:
        data = list(i)
        event_id_list.append(data[0])
        event_name_list.append(data[1])

    event_dict = dict(zip(event_name_list, event_id_list))
    clicked_event = StringVar()
    if len(event_id_list) < 1:
        clicked_event.set("Create Event First")
        event_id_list = ["Create Event First"]
        
    else:
        clicked_event.set(event_name_list[0])

        
    event_id_drop = OptionMenu(newentrylabelframe, clicked_event, *event_name_list)
    event_id_drop.grid(row=1, column=1, pady=10, padx=40)

    # ---------------Save CONSEQUENCE-------------------
    def save_consequence():

        cur.execute("""INSERT INTO Consequence VALUES (null,%s, %s, %s)""",(
            consequence_description.get(),
            consequence_target_frequency.get(),
            event_dict[clicked_event.get()])
        )


        success = Label(newentrylabelframe, text="Added record successfully", fg="green")
        success.grid(row=5, column=1, columnspan=2, pady=10)
        conn.commit()

        success.after(5000, success.destroy)
        consequence_description.delete(0, END)
        consequence_target_frequency.delete(0, END)


    save_consequence = Button(newentrylabelframe, text="Save", width=20, command=save_consequence)
    save_consequence.grid(row=4, column=1, columnspan=2, pady=10)



def new_consequence_barrier():
    db_conn()
    top = Toplevel()
    top.title("Layer of Protection Analysis ")
    cv = add_scrollable(widgetFrame=top, height=400, width=400)
    newentrylabelframe = LabelFrame(cv, text="Create Consequence Barrier")
    newentrylabelframe.grid(row=0, column=0, columnspan=2, rowspan=6, padx=20, pady=20)


    consequence_barrier_description_label = Label(newentrylabelframe, text="Description:")
    consequence_barrier_description_label.grid(row=2, column=0, padx=10, pady=10)
    consequence_barrier_description = Entry(newentrylabelframe, width=30)
    consequence_barrier_description.grid(row=2, column=1, padx=10, pady=10)


    consequence_barrier_pfd_label = Label(newentrylabelframe, text="PFD:")
    consequence_barrier_pfd_label.grid(row=3, column=0, padx=10, pady=10)
    consequence_barrier_pfd = Entry(newentrylabelframe, width=30)
    consequence_barrier_pfd.grid(row=3, column=1, padx=10, pady=10)


    # ------------- CONSEQUENCE ID Dropdown---------------------------
    cur.execute("""
            SELECT consequence_id, description FROM Consequence;
                """)

    consequence_id_data = cur.fetchall()
    consequence_id_list = list()
    consequence_name_list = list()

    for i in consequence_id_data:
        data = list(i)
        consequence_id_list.append(data[0])
        consequence_name_list.append(data[1])

    consequence_dict = dict(zip(consequence_name_list, consequence_id_list))
    clicked_consequence = StringVar()
    if len(consequence_id_list) < 1:
        clicked_consequence.set("Create Consequence First")
        consequence_id_list = ["Create Consequence First"]
    else:
        clicked_consequence.set(consequence_name_list[0])

    consequence_id = Label(newentrylabelframe, text="Consequence:")
    consequence_id.grid(row=1, column=0, padx=10, pady=10)
        
    consequence_id_drop = OptionMenu(newentrylabelframe, clicked_consequence, *consequence_name_list)
    consequence_id_drop.grid(row=1, column=1, pady=10, padx=10)


    def save_consequence_barrier():
        
        cur.execute("""INSERT INTO Consequence_Barrier VALUES (null, %s, %s, %s)""",(
           consequence_barrier_description.get(),
           consequence_barrier_pfd.get(),
           consequence_dict[clicked_consequence.get()])
        )

        success = Label(newentrylabelframe, text="Added record successfully", fg="green")
        success.grid(row=4, column=1, columnspan=2, pady=10)
        conn.commit()
        success.after(5000, success.destroy)
        consequence_barrier_description.delete(0, END)
        consequence_barrier_pfd.delete(0, END)

    save_consequence_barrier = Button(newentrylabelframe, text="Save", width=20, command=save_consequence_barrier)
    save_consequence_barrier.grid(row=4, column=1, columnspan=2)

def delete():
    global clicked
    global entry
    db_conn()
    gotten_id = clicked.get().lower() + "_id"
    print(gotten_id)


    cur.execute("DELETE FROM "+clicked.get()+ " WHERE " + gotten_id + " = " + str(entry_dict[clicked_entry.get()]))

    conn.commit()


    delete_success = Label(canvas, text=clicked.get() + " Item  with ID " + str(entry_dict[clicked_entry.get()]) + " sucessfully deleted", fg="green")
    delete_success.grid(row=4, column=2)

def query():
    db_conn()
    top = Toplevel()
    top.title("Layer of Protection Analysis ")
    top.geometry("900x500")
    tree = Treeview(top, column=("#1", "#2", "#3"), show='headings')
    tree.heading("#1", text="s/n")
    tree.heading("#2", text="Description")
    if clicked_query.get() == 'Event' or clicked_query.get() == 'Consequence':
        tree.heading("#3", text="Target Frequency")
    elif clicked_query.get() == 'Cause':
        tree.heading("#3", text="Initial Frequency")
    else:
        tree.heading("#3", text="PFD")
    tree.grid(row=1)

    label = Label(top, text="Data from " + clicked_query.get() + " Table", font=("serif", 14, "bold"))
    label.grid(row=0)


    cur.execute("SELECT * FROM " + clicked_query.get())
    records = cur.fetchall()

    print_records = ""
    if len(records) < 1:
        count =0
        records_label = Label(top, text="No Data is present in the "+ clicked_query.get() + " Table", font=('serif', 14, 'bold'))
        records_label.grid(row=5, column=2, columnspan=2)
    else:
        count = 0
        for record in records:
            count += 1
            tree.insert('', END, values=(str(count), str(record[1]), str(record[2])))
            # print_records += str(record[0]) + "       |        "+ str(record[1]) + "      |       "+ "" + str(record[2]) +"\n"
            # records_label = Label(top, text=print_records)
            # records_label.grid(row=5, column=2, columnspan=2)



def update():
    db_conn()
    successlabel = Label(presentTop, text="Data updated successfully", font=('serif', 14, 'bold'), foreground='green')
    if clicked.get() == "Event":

        cur.execute(""" UPDATE Event
              SET description = %s ,
                  target_frequency = %s
              WHERE event_id = %s """, (
            event_description_editor.get(),
            event_target_frequency_editor.get(),
            str(entry_dict[clicked_entry.get()])
            ))
        conn.commit() 

    
    elif clicked.get() == "Cause":
        cur.execute(""" UPDATE Cause
              SET description = %s ,
                  initial_frequency = %s ,
                  event_id = %s
              WHERE cause_id = %s """, (
        cause_description_editor.get(),
        cause_initial_frequency_editor.get(),
        str(event_dict1[clicked_event_editor1.get()]),
        str(entry_dict[clicked_entry.get()])
        ))
        successlabel.grid(row=4, column=1)
        conn.commit()
        successlabel.after(5000, successlabel.master)

    elif clicked.get() == "Cause_Barrier":

        cur.execute(""" UPDATE Cause_Barrier
              SET description = %s ,
                  pfd = %s ,
                  cause_id = %s
              WHERE cause_barrier_id = %s """, (
        cause_barrier_description_editor.get(),
        cause_barrier_pfd_editor.get(),
        str(cause_dict[clicked_cause_editor.get()]),
        str(entry_dict[clicked_entry.get()])
        ))
        successlabel.grid(row=4, column=1)
        conn.commit()
        successlabel.after(5000, successlabel.master)
    elif clicked.get() == "Consequence":

        cur.execute(""" UPDATE Consequence
              SET description = %s ,
                  target_frequency = %s,
                  event_id = %s
              WHERE consequence_id = %s """, (
        consequence_description_editor.get(),
        consequence_target_frequency_editor.get(),
        str(event_dict2[clicked_event_editor2.get()]),
        str(entry_dict[clicked_entry.get()])
        ))

        conn.commit()

    elif clicked.get() == "Consequence_Barrier":

        cur.execute(""" UPDATE Consequence_Barrier
              SET description = %s ,
                  pfd = %s ,
                  consequence_id = %s
              WHERE consequence_barrier_id = %s """, (
        consequence_barrier_description_editor.get(),
        consequence_barrier_pfd_editor.get(),
        str(consequence_dict[clicked_consequence_editor.get()]),
        str(entry_dict[clicked_entry.get()])
        ))

        conn.commit()


def edit_entry():
    global editor
    global topx
    global presentTop

    global event_target_frequency_editor
    global event_description_editor


    global cause_description_editor
    global cause_initial_frequency_editor
    global clicked_event_editor1
    global event_dict1

    global cause_barrier_description_editor
    global cause_barrier_pfd_editor
    global clicked_cause_editor
    global cause_dict

    global consequence_description_editor
    global consequence_target_frequency_editor
    global clicked_event_editor2
    global event_dict2

    global consequence_barrier_description_editor
    global consequence_barrier_pfd_editor
    global clicked_consequence_editor
    global consequence_dict

    db_conn()

    print(entry_dict)
    print(clicked_entry.get())
    print(clicked_entry.get()+": "+str(entry_dict[clicked_entry.get()]))


    if clicked.get() == "Event":
        top = Toplevel(bg="orange")
        presentTop = top
        print(presentTop)
        top.title("Layer of Protection Analysis ")
        top.geometry("900x500")
        label = Label(top, text="Edit " + clicked.get(), font=("serif", 14, "bold"), background='orange', foreground='white')
        label.grid(row=0, column=1)

        event_description_label_editor = Label(top, text="Description:", background='orange', foreground='white')
        event_description_label_editor.grid(row=1, column=0)

        event_description_editor = Entry(top, width=30)
        event_description_editor.grid(row=1, column=1, padx=20)


        event_target_frequency_label_editor = Label(top, text="Target Frequency:", background='orange', foreground='white')
        event_target_frequency_label_editor.grid(row=2, column=0, padx=20)

        event_target_frequency_editor = Entry(top, width=30)
        event_target_frequency_editor.grid(row=2, column=1, padx=20)


        cur.execute("SELECT description, target_frequency FROM Event WHERE event_id = " + str(entry_dict[clicked_entry.get()]))
        records = cur.fetchall()

        for record in records:
            event_description_editor.insert(0, record[0])
            event_target_frequency_editor.insert(0, record[1])


    elif clicked.get() == "Cause":

        top = Toplevel(bg="blue")
        presentTop = top
        print(presentTop)
        top.title("Layer of Protection Analysis ")
        top.geometry("900x500")
        label = Label(top, text="Edit " + clicked.get(), font=("serif", 14, "bold"), background='blue', foreground='white')
        label.grid(row=0, column=1)

        cause_description_label_editor = Label(top, text="Description:", background='blue', foreground='white')
        cause_description_label_editor.grid(row=1, column=0, padx=10, pady=10)
        cause_description_editor = Entry(top, width=30)
        cause_description_editor.grid(row=1, column=1, padx=10, pady=10)

        cause_initial_frequency_label_editor = Label(top, text="Initial Frequency:", background='blue', foreground='white')
        cause_initial_frequency_label_editor.grid(row=2, column=0, padx=10, pady=10)
        cause_initial_frequency_editor = Entry(top, width=30)
        cause_initial_frequency_editor.grid(row=2, column=1, padx=10, pady=10)

        cause_event_id_label_editor = Label(top, text="Event:", background='blue', foreground='white')
        cause_event_id_label_editor.grid(row=1, column=2, padx=10, pady=10)

    

        #-------------Event Dropdown------------------
        cur.execute("""
                SELECT event_id, description FROM Event;
                    """)

        event_id_data_editor1 = cur.fetchall()
        event_id_list_editor1 = list()
        event_name_list_editor1 = list()

        for i in event_id_data_editor1:
            data1 = list(i)
            event_id_list_editor1.append(data1[0])
            event_name_list_editor1.append(data1[1])

        clicked_event_editor1 = StringVar()
        event_dict1 = dict(zip(event_name_list_editor1, event_id_list_editor1))
        if len(event_id_list_editor1) < 1:
            clicked_event_editor1.set("Create Event First")
            event_name_list_editor1 = ["Create Event First"]
            
        else:
            cur.execute("SELECT E.event_id, E.description FROM Cause as C INNER JOIN Event as E ON C.event_id = E.event_id WHERE C.cause_id = " + str(entry_dict[clicked_entry.get()]))
            event1 = cur.fetchone()
            clicked_event_editor1.set(event1[1])

            
        event_id_drop_editor1 = OptionMenu(top, clicked_event_editor1, *event_name_list_editor1)
        event_id_drop_editor1.grid(row=1, column=3, pady=10, padx=40)


        cur.execute("SELECT description, initial_frequency FROM Cause WHERE cause_id = " + str(entry_dict[clicked_entry.get()]))
        records = cur.fetchall()
        for record in records:
            cause_description_editor.insert(0, record[0])
            cause_initial_frequency_editor.insert(0, record[1])



    elif clicked.get() == "Cause_Barrier":

        top = Toplevel()
        presentTop = top
        print(presentTop)
        top.title("Layer of Protection Analysis ")
        top.geometry("900x500")
        label = Label(top, text="Edit " + clicked.get(), font=("serif", 14, "bold"))
        label.grid(row=0, column=1)

        cause_barrier_description_editor_label = Label(top, text="Description")
        cause_barrier_description_editor_label.grid(row=1, column=0, padx=10, pady=10)
        cause_barrier_description_editor = Entry(top, width=30)
        cause_barrier_description_editor.grid(row=1, column=1, padx=10, pady=10)

        cause_barrier_pfd_label_editor = Label(top, text="PFD")
        cause_barrier_pfd_label_editor.grid(row=2, column=0, padx=10, pady=10)
        cause_barrier_pfd_editor = Entry(top, width=30)
        cause_barrier_pfd_editor.grid(row=2, column=1, padx=10, pady=10)


    # --------------------------------CAUSE ID Dropdown-------------------
        cur.execute("""
            SELECT cause_id, description FROM Cause;
                """)

        cause_id_data_editor = cur.fetchall()
        cause_id_list_editor = list()
        cause_name_list_editor = list()

        for i in cause_id_data_editor:
            data = list(i)
            cause_id_list_editor.append(data[0])
            cause_name_list_editor.append(data[1])

        clicked_cause_editor = StringVar()
        cause_dict = dict(zip(cause_name_list_editor, cause_id_list_editor))
        if len(cause_id_list_editor) < 1:
            clicked_cause_editor.set("Create Cause First")
            cause_name_list_editor = ["Create Cause First"]
            
        else:
            cur.execute("SELECT C.cause_id, C.description FROM Cause_Barrier as Cb INNER JOIN Cause as C ON Cb.cause_id = C.cause_id WHERE Cb.cause_barrier_id = " + str(entry_dict[clicked_entry.get()]))
            cause1 = cur.fetchone()
            clicked_cause_editor.set(cause1[1])

        cause_id_editor = Label(top, text="Cause")
        cause_id_editor.grid(row=1, column=2, padx=10, pady=10)
            
        cause_id_drop_editor = OptionMenu(top, clicked_cause_editor, *cause_name_list_editor)
        cause_id_drop_editor.grid(row=1, column=3, pady=10, padx=40)

        cur.execute("""SELECT description, pfd FROM Cause_Barrier WHERE cause_barrier_id = """ + str(entry_dict[clicked_entry.get()]))
        records = cur.fetchall()

        for record in records:
            cause_barrier_description_editor.insert(0, record[0])
            cause_barrier_pfd_editor.insert(0, record[1])

    elif clicked.get() == "Consequence": 

        top = Toplevel(bg="red")
        presentTop = top
        print(presentTop)
        top.title("Layer of Protection Analysis ")
        top.geometry("900x500")
        label = Label(top, text="Edit " + clicked.get(), font=("serif", 14, "bold"), background='red', foreground='white')
        label.grid(row=0, column=1)

        consequence_description_label_editor = Label(top, text="Description:", background='red', foreground='white')
        consequence_description_label_editor.grid(row=1, column=0, padx=10, pady=10)
        consequence_description_editor = Entry(top, width=30)
        consequence_description_editor.grid(row=1, column=1, padx=10, pady=10)

        consequence_target_frequency_label_editor = Label(top, text="Target Frequency:", background='red', foreground='white')
        consequence_target_frequency_label_editor.grid(row=2, column=0, padx=10, pady=10)
        consequence_target_frequency_editor = Entry(top, width=30)
        consequence_target_frequency_editor.grid(row=2, column=1, padx=10, pady=10)

        consequence_event_id_label_editor = Label(top, text="Event", background='red', foreground='white')
        consequence_event_id_label_editor.grid(row=1, column=2, padx=10, pady=10)

    


        #-------------Event Dropdown------------------
        cur.execute("""
                SELECT event_id, description FROM Event;
                    """)

        event_id_data_editor2 = cur.fetchall()
        event_id_list_editor2 = list()
        event_name_list_editor2 = list()

        for i in event_id_data_editor2:
            data2 = list(i)
            event_id_list_editor2.append(data2[0])
            event_name_list_editor2.append(data2[1])

        clicked_event_editor2 = StringVar()
        event_dict2 = dict(zip(event_name_list_editor2, event_id_list_editor2))
        if len(event_id_list_editor2) < 1:
            clicked_event_editor2.set("Create Event First")
            event_name_list_editor2 = ["Create Event First"]
            
        else:
            cur.execute("SELECT E.event_id, E.description FROM Consequence as Co INNER JOIN Event as E ON Co.event_id = E.event_id WHERE Co.consequence_id = " + str(entry_dict[clicked_entry.get()]))
            event2 = cur.fetchone()
            clicked_event_editor2.set(event2[1])


            
        event_id_drop_editor2 = OptionMenu(top, clicked_event_editor2, *event_name_list_editor2)
        event_id_drop_editor2.grid(row=1, column=3, pady=10, padx=40)


        cur.execute("SELECT description, target_frequency FROM Consequence WHERE consequence_id = " + str(entry_dict[clicked_entry.get()]))
        records = cur.fetchall()
        for record in records:
            consequence_description_editor.insert(0, record[0])
            consequence_target_frequency_editor.insert(0, record[1])


    elif clicked.get() == "Consequence_Barrier": 
        top = Toplevel()
        presentTop = top
        print(presentTop)
        top.title("Layer of Protection Analysis ")
        top.geometry("900x500")
        label = Label(top, text="Edit " + clicked.get(), font=("serif", 14, "bold"))
        label.grid(row=0, column=1)

        consequence_barrier_description_label_editor = Label(top, text="Description:")
        consequence_barrier_description_label_editor.grid(row=1, column=0, padx=10, pady=10)
        consequence_barrier_description_editor = Entry(top, width=30)
        consequence_barrier_description_editor.grid(row=1, column=1, padx=10, pady=10)


        consequence_barrier_pfd_label_editor = Label(top, text="PFD:")
        consequence_barrier_pfd_label_editor.grid(row=2, column=0, padx=10, pady=10)
        consequence_barrier_pfd_editor = Entry(top, width=30)
        consequence_barrier_pfd_editor.grid(row=2, column=1, padx=10, pady=10)
    

    # --------------------------------CONSEQUENCE ID Dropdown-------------------
        cur.execute("""
            SELECT consequence_id, description FROM Consequence;
                """)

        consequence_id_data_editor = cur.fetchall()
        consequence_id_list_editor = list()
        consequence_name_list_editor = list()

        for i in consequence_id_data_editor:
            data = list(i)
            consequence_id_list_editor.append(data[0])
            consequence_name_list_editor.append(data[1])

        clicked_consequence_editor = StringVar()
        consequence_dict = dict(zip(consequence_name_list_editor, consequence_id_list_editor))
        if len(consequence_id_list_editor) < 1:
            clicked_consequence_editor.set("Create Consequence First")
            consequence_name_list_editor = ["Create Consequence First"]
            
        else:
            cur.execute("SELECT Con.consequence_id, Con.description FROM Consequence_Barrier as ConB INNER JOIN Consequence as Con ON ConB.consequence_id = Con.consequence_id WHERE ConB.consequence_barrier_id = " + str(entry_dict[clicked_entry.get()]))
            consequence1 = cur.fetchone()
            clicked_consequence_editor.set(consequence1[1])

        consequence_id_editor = Label(top, text="Consequence")
        consequence_id_editor.grid(row=1, column=2, padx=10, pady=10)
            
        consequence_id_drop_editor = OptionMenu(top, clicked_consequence_editor, *consequence_name_list_editor)
        consequence_id_drop_editor.grid(row=1, column=3, pady=10, padx=40)

        cur.execute("""SELECT description, pfd FROM Consequence_Barrier WHERE consequence_barrier_id = """ + str(entry_dict[clicked_entry.get()]))
        records = cur.fetchall()

        for record in records:
            consequence_barrier_description_editor.insert(0, record[0])
            consequence_barrier_pfd_editor.insert(0, record[1])



    edit_button = Button(top, text="Save Record", command=update)
    edit_button.grid(row=5, column=1, columnspan=2, ipadx=100, padx=10, pady=10)  

    conn.commit()


def view_dropdown(event):
    db_conn()
    global entry_dict
    cur.execute("""
            SELECT """+clicked.get().lower() +"""_id, description FROM """+clicked.get())

    entry_id_data = cur.fetchall()
    # print(entry_id_data)

    entry_id_list = list()
    entry_name_list = list()
    clicked_entry.set("")
    entry_select_drop['menu'].delete(0, 'end')
    for i in entry_id_data:
        data = list(i)
        entry_id_list.append(data[0])
        entry_name_list.append(data[1])
        entry_select_drop['menu'].add_command(label=data[1], command=tk._setit(clicked_entry, data[1],))
    clicked_entry.set(entry_name_list[0])
    entry_dict = dict(zip(entry_name_list, entry_id_list))
    print(entry_dict)
    # dict.fromkeys(event_id_list, "In stock")
    
    if len(entry_id_list) < 1:
        clicked_entry.set("Create Event First")
        event_id_list = ["Create Event First"]

        
    else:
        clicked_entry.set(entry_name_list[0])
    
    # entry_select_drop = OptionMenu(editlabelframe, clicked_event, *entry_dict.keys())
    # entry_select_drop.grid(row=2, column=2)


def load_initial_entry():
    db_conn()
    global entry_select_drop
    global entry_dict
    global drop
    global clicked
    global clicked_entry

    cur.execute("""
            SELECT event_id, description FROM """+ clicked.get())

    entry_id_data = cur.fetchall()
    entry_id_list = list()
    entry_name_list = list()

    clicked_entry = StringVar(editlabelframe)

    for i in entry_id_data:
        data = list(i)
        entry_id_list.append(data[0])
        entry_name_list.append(data[1])
    entry_dict = dict(zip(entry_name_list, entry_id_list))
    
    # dict.fromkeys(event_id_list, "In stock")
    if len(entry_id_list) < 1:
        clicked_entry.set("Create Event First")
        entry_name_list = ["Create Event First"]
        
    else:
        clicked_entry.set(entry_name_list[0])
    print(entry_dict)
    entry_select_drop = OptionMenu(editlabelframe, clicked_entry, *entry_name_list)
    entry_select_drop.grid(row=2, column=2)
# Query, Delete and Edit


global editlabelframe

editlabelframe = LabelFrame(canvas, text="Edit/Delete existing entries", background=tkintercolor, foreground="white")
editlabelframe.grid(row=1, column=1, columnspan=3, rowspan=4, padx=20, pady=20)

clicked_entry = StringVar(editlabelframe)
lopa_list = ["Event", "Cause", "Cause_Barrier", "Consequence", "Consequence_Barrier"]

clicked = StringVar(editlabelframe)
clicked.set(lopa_list[0])
drop = OptionMenu(editlabelframe, clicked, *lopa_list, command=view_dropdown)
drop.grid(row=2, column=1, padx=20, pady=20)


load_initial_entry()

edit = Button(editlabelframe, text="Edit Entry", command=edit_entry, height = 2, width = 23)
edit.grid(row=3, column=2, padx=80, pady=20)

delete = Button(editlabelframe, text="Delete Entry", bg="red", command=delete, height = 2, width = 23)
delete.grid(row=4, column=2, padx=80, pady=20)

querylabelframe = LabelFrame(canvas, text="View previous entries", background=tkintercolor, foreground="white")
querylabelframe.grid(row=5, column=1, columnspan=3, padx=20, pady=20)
query_list = ["Event", "Cause", "Cause_Barrier", "Consequence", "Consequence_Barrier"]
clicked_query = StringVar(querylabelframe)
clicked_query.set(query_list[0])

query_drop = OptionMenu(querylabelframe, clicked_query, *query_list)
query_drop.grid(row=5, column=2, padx=20, pady=20)

query = Button(querylabelframe, text="Query", fg="blue", command=query, height = 2, width = 23)
query.grid(row=5, column=3, padx=80, pady=20)


createlabelframe = LabelFrame(canvas, text="Create new Entries", background=tkintercolor, foreground="white")
createlabelframe.grid(row=0, column=0, rowspan=6, padx=20)
# Buttons for inputing data
event = Button(createlabelframe, text="Create Event", background="orange", foreground="white", command=new_event, height = 2, width = 23)
event.grid(row=2, column=0, padx=(20,60), pady=20)

cause = Button(createlabelframe, text="Create Cause", background="blue",foreground="white", command=new_cause, height = 2, width = 23)
cause.grid(row=3, column=0, padx=(20,60), pady=20)

consequence = Button(createlabelframe, text="Create Consequence", bg="red", fg="white", command=new_consequence, height = 2, width = 23)
consequence.grid(row=4, column=0, padx=(20,60), pady=20)

cause_barrier = Button(createlabelframe, text="Create Cause Barrier", command=new_cause_barrier, height = 2, width = 23)
cause_barrier.grid(row=5, column=0, padx=(20,60), pady=20)

consequence_barrier = Button(createlabelframe, text="Create Consequence Barrier", command=new_consequence_barrier, height = 2, width = 23)
consequence_barrier.grid(row=6, column=0, padx=(20,60), pady=20)

# Open Bowtie Diagram  


weblabelframe = LabelFrame(canvas, text="View all entries on the web", background=tkintercolor, foreground="white")
weblabelframe.grid(row=7, column=0, padx=20, pady=20)

new = 1
url = "https://lopa-web-bow-tie.azurewebsites.net/"

def openweb():
    webbrowser.open(url,new=new)

bowtie = Button(weblabelframe, text = "Draw Bowtie Diagram",command=openweb, height = 2, width = 23, bg="green")
bowtie.grid(row=7, column=0, padx=(20,60), pady=20)

mainloop()
