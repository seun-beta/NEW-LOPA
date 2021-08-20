from tkinter import *
from PIL import ImageTk, Image
import sqlite3
from datetime import *
import mysql.connector
import tkinter.ttk

from db import create_table

# Initialize db table creation 
create_table()

# Connection to MySQL Database hosted on Azure 
def db_conn():
    global conn 
    global cur
    conn = sqlite3.connect("lopa.db")

    cur = conn.cursor()
    
    return conn, cur

db_conn()

root = Tk()
root.title(f"{datetime.now():%a, %b %d %Y} | Layer of Protection Analysis")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry("1200x700")
root.config(background='#394867')


def new_event():
    
    global save_event
    top = Toplevel(bg="orange")
    top.title(f"{datetime.now():%a, %b %d %Y} | Layer of Protection Analysis ")
    top.geometry("900x500")

    event_label = Label(top, text="CREATE EVENT", font=('serif', 14, 'bold'))
    event_label.grid(row=0, column=1, columnspan=2)

    # --------------Input UI----------------------------
    event_description_label = Label(top, text="Description:")
    event_description_label.grid(row=1, column=0, padx=10, pady=10)

    event_description = Entry(top, width=30)
    event_description.grid(row=1, column=1, padx=10, pady=10)

    
    event_target_freq_label = Label(top, text="Target Frequency: ")
    event_target_freq_label.grid(row=2, column=0, padx=10, pady=10)

    event_target_freq = Entry(top, width=30)
    event_target_freq.grid(row=2, column=1, padx=10, pady=10)

    
    def save_event():

        cur.execute("INSERT INTO Event VALUES (null, ?, ?)",(
                    event_description.get(),
                    event_target_freq.get()))

        success = Label(top, text="Added record successfully", fg="green")
        success.grid(row=4, column=1)
        conn.commit()
        event_description.delete(0, END)
    

    save_event = Button(top, text="Save", width=20, command=save_event)
    save_event.grid(row=3, column=1)
    


def new_cause():
    top = Toplevel(bg="blue")
    top.title(f"{datetime.now():%a, %b %d %Y} | Layer of Protection Analysis ")
    top.geometry("900x500")

    cause_label = Label(top, text="CREATE CAUSE", font=('serif', 14, 'bold'))
    cause_label.grid(row=0, column=2, columnspan=2)

    cause_description_label = Label(top, text="Description:")
    cause_description_label.grid(row=1, column=0, padx=10, pady=10)
    cause_description = Entry(top, width=30)
    cause_description.grid(row=1, column=1, padx=10, pady=10)

    cause_initial_frequency_label = Label(top, text="Initial Frequency:")
    cause_initial_frequency_label.grid(row=2, column=0, padx=10, pady=10)
    cause_initial_frequency = Entry(top, width=30)
    cause_initial_frequency.grid(row=2, column=1, padx=10, pady=10)

    # --------------------------------EVENT ID Dropdown-------------------
    event_id_label = Label(top, text="Event ID:")
    event_id_label.grid(row=1, column=3, padx=20, pady=20)
    cur.execute("""
            SELECT event_id, description FROM Event;
                """)

    event_id_data = cur.fetchall()
    event_id_list = list()

    for i in event_id_data:
        data = list(i)
        event_id_list.append(data[1])

    clicked_event = StringVar()
    if len(event_id_list) < 1:
        clicked_event.set("Create Event First")
        event_id_list = ["Create Event First"]
        
    else:
        clicked_event.set(event_id_list[0])

        
    event_id_drop = OptionMenu(top, clicked_event, *event_id_list)
    event_id_drop.grid(row=1, column=4, pady=10, padx=40)


    # ---------------Save CAUSE-------------------
    def save_cause():

        cur.execute("INSERT INTO Cause VALUES (null, ?, ?, ?)",(
            cause_description.get(),
            cause_initial_frequency.get(),
            clicked_event.get())
        )

        success = Label(top, text="Added record successfully", fg="green")
        success.grid(row=4, column=2, columnspan=2)
        conn.commit()

        cause_description.delete(0, END)
        cause_initial_frequency.delete(0, END)

        

    save_cause = Button(top, text="Save", width=20, command=save_cause)
    save_cause.grid(row=3, column=2, columnspan=2)




def new_cause_barrier():
    top = Toplevel()
    top.title(f"{datetime.now():%a, %b %d %Y} | Layer of Protection Analysis ")
    top.geometry("900x500")


    label = Label(top, text="CAUSE BARRIER", font=('serif', 14, 'bold'))
    label.grid(row=0, column=2, columnspan=2)



    cause_barrier_description_label = Label(top, text="Description")
    cause_barrier_description_label.grid(row=1, column=0, padx=10, pady=10)
    cause_barrier_description = Entry(top, width=30)
    cause_barrier_description.grid(row=1, column=1, padx=10, pady=10)

    cause_barrier_pfd_label = Label(top, text="PFD")
    cause_barrier_pfd_label.grid(row=2, column=0, padx=10, pady=10)
    cause_barrier_pfd = Entry(top, width=30)
    cause_barrier_pfd.grid(row=2, column=1, padx=10, pady=10)


    # -------------CAUSE ID Dropdown----------------------
    cur.execute("""
            SELECT cause_id, description FROM Cause;
                """)

    cause_id_data = cur.fetchall()
    cause_id_list = list()

    for i in cause_id_data:
        data = list(i)
        cause_id_list.append(data[0])

    clicked_cause = StringVar()
    if len(cause_id_list) < 1:
        clicked_cause.set("Create Cause First")
        cause_id_list = ["Create Cause First"]
        
    else:
        clicked_cause.set(cause_id_list[0])

    cause_id = Label(top, text="Cause ID:")
    cause_id.grid(row=1, column=2, padx=10, pady=10)
        
    cause_id_drop = OptionMenu(top, clicked_cause, *cause_id_list)
    cause_id_drop.grid(row=1, column=3, pady=10, padx=40)


    def save_cause_barrier():
    
        cur.execute("INSERT INTO Cause_Barrier VALUES (null, ?, ?, ?)",(
            cause_barrier_description.get(),
            cause_barrier_pfd.get(),
            clicked_cause.get())
        )

        success = Label(top, text="Added record successfully", fg="green")
        success.grid(row=4, column=1, columnspan=2)
        conn.commit()

        cause_barrier_description.delete(0, END)
        cause_barrier_pfd.delete(0, END)



    save_cause_barrier = Button(top, text="Save", width=20, command=save_cause_barrier)
    save_cause_barrier.grid(row=3, column=1, columnspan=2)


def new_consequence():
    top = Toplevel(bg="red")
    top.title(f"{datetime.now():%a, %b %d %Y} | Layer of Protection Analysis ")

    event_label = Label(top, text="CONSEQUENCE")
    event_label.grid(row=0, column=0, columnspan=2)


    consequence_description_label = Label(top, text="Description:")
    consequence_description_label.grid(row=1, column=0, padx=10, pady=10)
    consequence_description = Entry(top, width=30)
    consequence_description.grid(row=1, column=1, padx=10, pady=10)

    consequence_initial_frequency_label = Label(top, text="Initial Frequency:")
    consequence_initial_frequency_label.grid(row=2, column=0, padx=10, pady=10)
    consequence_initial_frequency = Entry(top, width=30)
    consequence_initial_frequency.grid(row=2, column=1, padx=10, pady=10)
    
    consequence_target_frequency_label = Label(top, text="Target Frequency:")
    consequence_target_frequency_label.grid(row=3, column=0, padx=10, pady=10)
    consequence_target_frequency = Entry(top, width=30)
    consequence_target_frequency.grid(row=3, column=1, padx=10, pady=10)


    def save_consequence():

        cur.execute("INSERT INTO Consequence VALUES (null,?, ?, ?)",(
            consequence_description.get(),
            consequence_initial_frequency.get(),
            consequence_target_frequency.get()
        )
        )

        success = Label(top, text="Added record successfully", fg="green")
        success.grid(row=5, column=1, columnspan=2)
        conn.commit()


        consequence_description.delete(0, END)
        consequence_initial_frequency.delete(0, END)
        consequence_target_frequency.delete(0, END)


    save_consequence = Button(top, text="Save", width=20, command=save_consequence)
    save_consequence.grid(row=4, column=1, columnspan=2)

def new_consequence_barrier():
    top = Toplevel()
    top.title(f"{datetime.now():%a, %b %d %Y} | Layer of Protection Analysis ")

    event_label = Label(top, text="CONSEQUENCE BARRIER")
    event_label.grid(row=0, column=0, columnspan=2)


    consequence_barrier_description_label = Label(top, text="Description:")
    consequence_barrier_description_label.grid(row=1, column=0, padx=10, pady=10)
    consequence_barrier_description = Entry(top, width=30)
    consequence_barrier_description.grid(row=1, column=1, padx=10, pady=10)


    consequence_barrier_pfd_label = Label(top, text="PFD:")
    consequence_barrier_pfd_label.grid(row=2, column=0, padx=10, pady=10)
    consequence_barrier_pfd = Entry(top, width=30)
    consequence_barrier_pfd.grid(row=2, column=1, padx=10, pady=10)

    cur.execute("""
            SELECT consequence_id, description FROM Consequence;
                """)

    consequence_id_data = cur.fetchall()
    consequence_id_list = list()

    for i in consequence_id_data:
        data = list(i)
        consequence_id_list.append(data[0])

    clicked_consequence = StringVar()
    if len(consequence_id_list) < 1:
        clicked_consequence.set("Create Consequence First")
        consequence_id_list = ["Create Consequence First"]
    else:
        clicked_consequence.set(consequence_id_list[0])

    consequence_id = Label(top, text="Consequence ID:")
    consequence_id.grid(row=1, column=2, padx=10, pady=10)
        
    consequence_id_drop = OptionMenu(top, clicked_consequence, *consequence_id_list)
    consequence_id_drop.grid(row=1, column=3, pady=10, padx=40)


    def save_consequence_barrier():
        
        cur.execute("INSERT INTO Consequence_Barrier VALUES (null, ?, ?, ?)",(
           consequence_barrier_description.get(),
           consequence_barrier_pfd.get(),
           clicked_consequence.get())
        )

        success = Label(top, text="Added record successfully", fg="green")
        success.grid(row=4, column=1, columnspan=2)
        conn.commit()

        consequence_barrier_description.delete(0, END)
        consequence_barrier_pfd.delete(0, END)

    save_consequence_barrier = Button(top, text="Save", width=20, command=save_consequence_barrier)
    save_consequence_barrier.grid(row=3, column=1, columnspan=2)

def delete():
    global clicked
    global entry



    gotten_id = clicked.get().lower() + "_id"
    print(gotten_id)


    cur.execute("DELETE FROM "+clicked.get()+ " WHERE " + gotten_id + " = " + entry.get())

    conn.commit()


    delete_success = Label(root, text=clicked.get() + " Item  with ID " + entry.get() + " sucessfully deleted", fg="green")
    delete_success.grid(row=3, column=2)

def query():
    top = Toplevel()
    top.title(clicked_query.get())

    cur.execute("SELECT * FROM " + clicked_query.get())
    records = cur.fetchall()

    print_records = ""
    if len(records) < 1:
            records_label = Label(top, text="No Data is present in the "+ clicked_query.get() + " Table", font=('serif', 14, 'bold'))
            records_label.grid(row=5, column=2, columnspan=2)
    else:
        for record in records:
            print_records += str(record[0]) +" "+ str(record[1]) + "       "+ "\t" + str(record[2]) +"\n"
            records_label = Label(top, text=print_records)
            records_label.grid(row=5, column=2, columnspan=2)

    conn.commit()



def update():


    if clicked.get() == "Event":


        cur.execute(""" UPDATE Event
              SET description = ? ,
                  cause_id = ? ,
                  consequence_id = ?
              WHERE event_id = ? """, (
            event_description_editor.get(),
            clicked_cause_editor.get(),
            clicked_consequence_editor.get(),
            entry.get()
            ))
        conn.commit() 
    elif clicked.get() == "Cause":
        cur.execute(""" UPDATE Cause
              SET description = ? ,
                  initial_frequency = ? ,
                  target_frequency = ?
              WHERE cause_id = ? """, (
        cause_description_editor.get(),
        cause_initial_frequency_editor.get(),
        cause_target_frequency_editor.get(),
        entry.get()
        ))

        conn.commit()

    elif clicked.get() == "Cause_Barrier":

        cur.execute(""" UPDATE Cause_Barrier
              SET description = ? ,
                  pfd = ? ,
                  cause_id = ?
              WHERE cause_barrier_id = ? """, (
        cause_barrier_description_editor.get(),
        cause_barrier_pfd_editor.get(),
        clicked_cause_editor.get(),
        entry.get()
        ))

        conn.commit()

    elif clicked.get() == "Consequence":

        cur.execute(""" UPDATE Consequence
              SET description = ? ,
                  initial_frequency = ? ,
                  target_frequency = ?
              WHERE consequence_id = ? """, (
        consequence_description_editor.get(),
        consequence_initial_frequency_editor.get(),
        consequence_target_frequency_editor.get(),
        entry.get()
        ))

        conn.commit()

    elif clicked.get() == "Consequence_Barrier":

        cur.execute(""" UPDATE Consequence_Barrier
              SET description = ? ,
                  pfd = ? ,
                  consequence_id = ?
              WHERE consequence_barrier_id = ? """, (
        consequence_barrier_description_editor.get(),
        consequence_barrier_pfd_editor.get(),
        clicked_consequence_editor.get(),
        entry.get()
        ))

        conn.commit()
    top.destroy()


def edit():
    global editor
    global top

    global clicked_cause_editor
    global clicked_consequence_editor
    global event_description_editor

    global cause_initial_frequency_editor
    global cause_description_editor
    global cause_target_frequency_editor

    global cause_barrier_description_editor
    global cause_barrier_pfd_editor
    global clicked_cause_editor

    global consequence_description_editor
    global consequence_initial_frequency_editor
    global consequence_target_frequency_editor

    global consequence_barrier_description_editor
    global consequence_barrier_pfd_editor
    global clicked_consequence_editor

    top = Toplevel()
    top.title("Edit " + clicked.get())

    if clicked.get() == "Event":

        event_description_editor = Entry(top, width=30)
        event_description_editor.grid(row=1, column=1, padx=20)

    # --------------------------------CAUSE ID Dropdown-------------------
        cur.execute("""
            SELECT cause_id, description FROM Cause;
                """)

        cause_id_data_editor = cur.fetchall()
        cause_id_list_editor = list()

        for i in cause_id_data_editor:
            data = list(i)
            cause_id_list_editor.append(data[0])

        clicked_cause_editor = StringVar()
        if len(cause_id_list_editor) < 1:
            clicked_cause_editor.set("Create Cause First")
            cause_id_list_editor = ["Create Cause First"]
            
        else:
            cur.execute("SELECT cause_id FROM Event WHERE event_id = " + entry.get())
            cause = cur.fetchone()
 
            clicked_cause_editor.set(cause[0])

        cause_id_editor = Label(top, text="Cause ID:")
        cause_id_editor.grid(row=1, column=2, padx=10, pady=10)
            
        cause_id_drop_editor = OptionMenu(top, clicked_cause_editor, *cause_id_list_editor)
        cause_id_drop_editor.grid(row=1, column=3, pady=10, padx=40)


        # --------------------------------CONSEQUENCE ID Dropdown-------------------
        cur.execute("""SELECT consequence_id, description FROM Consequence;
                    """)
        consequence_id_data_editor = cur.fetchall()

        consequence_id_list_editor = list()
        for i in consequence_id_data_editor:
            data = list(i)
            consequence_id_list_editor.append(data[0])


        clicked_consequence_editor = StringVar()
        if len(consequence_id_list_editor) < 1:
            clicked_consequence_editor.set("Create Consequence First")
            consequence_id_list_editor = ["Create Consequence First"]
            
        else:
            cur.execute("SELECT consequence_id FROM Event WHERE event_id = " + entry.get())
            consequence = cur.fetchone()
 
            clicked_consequence_editor.set(consequence[0])

        consequence_id_editor = Label(top, text="Consequence ID:")
        consequence_id_editor.grid(row=1, column=4, pady=10)
        
        consequence_id_drop_editor = OptionMenu(top, clicked_consequence_editor, *consequence_id_list_editor)
        consequence_id_drop_editor.grid(row=1, column=5, pady=10, padx=40)

        # Create labels
        event_description_label_editor = Label(top, text="Description:")
        event_description_label_editor.grid(row=1, column=0)


        cur.execute("SELECT description FROM Event WHERE event_id = " + entry.get())
        records = cur.fetchall()

        for record in records:
            if len(record) < 1:
                event_description_editor.insert(0, "No Record  with id= "+ entry.get() +" in Database, please create one")
            else:
                event_description_editor.insert(0, record[0])

    elif clicked.get() == "Cause":
        
        cause_description_label_editor = Label(top, text="Description:")
        cause_description_label_editor.grid(row=0, column=0, padx=10, pady=10)
        cause_description_editor = Entry(top, width=30)
        cause_description_editor.grid(row=0, column=1, padx=10, pady=10)

        cause_initial_frequency_label_editor = Label(top, text="Initial Frequency:")
        cause_initial_frequency_label_editor.grid(row=1, column=0, padx=10, pady=10)
        cause_initial_frequency_editor = Entry(top, width=30)
        cause_initial_frequency_editor.grid(row=1, column=1, padx=10, pady=10)

        cause_target_frequency_label_editor = Label(top, text="Target Frequency:")
        cause_target_frequency_label_editor.grid(row=2, column=0, padx=10, pady=10)
        cause_target_frequency_editor = Entry(top, width=30)
        cause_target_frequency_editor.grid(row=2, column=1, padx=10, pady=10)
        event_id_label_editor = Label(top, text="Event ID:")

        """
        event_id_label_editor.grid(row=3, column=0, padx=10, pady=10)
        event_id_editor = Entry(top, width=30)
        event_id_editor.insert(0, 1)
        event_id_editor.grid(row=3, column=1, padx=10, pady=10)
        """
        

        cur.execute("SELECT description, initial_frequency, target_frequency FROM Cause WHERE cause_id = " + entry.get())
        records = cur.fetchall()
        for record in records:
            cause_description_editor.insert(0, record[0])
            cause_initial_frequency_editor.insert(0, record[1])
            cause_target_frequency_editor.insert(0, record[2])
            # event_id_editor.insert(0, record[3])


    elif clicked.get() == "Cause_Barrier":

        cause_barrier_description_editor_label = Label(top, text="Description")
        cause_barrier_description_editor_label.grid(row=0, column=0, padx=10, pady=10)
        cause_barrier_description_editor = Entry(top, width=30)
        cause_barrier_description_editor.grid(row=0, column=1, padx=10, pady=10)

        cause_barrier_pfd_label_editor = Label(top, text="PFD")
        cause_barrier_pfd_label_editor.grid(row=1, column=0, padx=10, pady=10)
        cause_barrier_pfd_editor = Entry(top, width=30)
        cause_barrier_pfd_editor.grid(row=1, column=1, padx=10, pady=10)


    # --------------------------------CAUSE ID Dropdown-------------------
        cur.execute("""
            SELECT cause_id, description FROM Cause;
                """)

        cause_id_data_editor = cur.fetchall()
        cause_id_list_editor = list()

        for i in cause_id_data_editor:
            data = list(i)
            cause_id_list_editor.append(data[0])

        clicked_cause_editor = StringVar()
        if len(cause_id_list_editor) < 1:
            clicked_cause_editor.set("Create Cause First")
            cause_id_list_editor = ["Create Cause First"]
            
        else:
            cur.execute("SELECT cause_id FROM Event WHERE event_id = " + entry.get())
            cause = cur.fetchone()
 
            clicked_cause_editor.set(cause[0])

        cause_id_editor = Label(top, text="Cause ID:")
        cause_id_editor.grid(row=1, column=2, padx=10, pady=10)
            
        cause_id_drop_editor = OptionMenu(top, clicked_cause_editor, *cause_id_list_editor)
        cause_id_drop_editor.grid(row=1, column=3, pady=10, padx=40)

        cur.execute("SELECT description, pfd FROM Cause_Barrier WHERE cause_barrier_id = " + entry.get())
        records = cur.fetchall()

        for record in records:
            cause_barrier_description_editor.insert(0, record[0])
            cause_barrier_pfd_editor.insert(0, record[1])

    elif clicked.get() == "Consequence": 

        consequence_description_label_editor = Label(top, text="Description:")
        consequence_description_label_editor.grid(row=0, column=0, padx=10, pady=10)
        consequence_description_editor = Entry(top, width=30)
        consequence_description_editor.grid(row=0, column=1, padx=10, pady=10)

        consequence_initial_frequency_label_editor = Label(top, text="Initial Frequency:")
        consequence_initial_frequency_label_editor.grid(row=1, column=0, padx=10, pady=10)
        consequence_initial_frequency_editor = Entry(top, width=30)
        consequence_initial_frequency_editor.grid(row=1, column=1, padx=10, pady=10)

        consequence_target_frequency_label_editor = Label(top, text="Target Frequency:")
        consequence_target_frequency_label_editor.grid(row=2, column=0, padx=10, pady=10)
        consequence_target_frequency_editor = Entry(top, width=30)
        consequence_target_frequency_editor.grid(row=2, column=1, padx=10, pady=10) 

        cur.execute("SELECT description, initial_frequency, target_frequency FROM Consequence WHERE consequence_id = " + entry.get())
        records = cur.fetchall()
        for record in records:
            consequence_description_editor.insert(0, record[0])
            consequence_initial_frequency_editor.insert(0, record[1])
            consequence_target_frequency_editor.insert(0, record[2])  


    elif clicked.get() == "Consequence_Barrier": 

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

        for i in consequence_id_data_editor:
            data = list(i)
            consequence_id_list_editor.append(data[0])

        clicked_consequence_editor = StringVar()
        if len(consequence_id_list_editor) < 1:
            clicked_consequence_editor.set("Create Consequence First")
            consequence_id_list_editor = ["Create Consequence First"]
            
        else:
            cur.execute("SELECT consequence_id FROM Consequence_Barrier WHERE consequence_barrier_id = " + entry.get())
            consequence = cur.fetchone()
 
            clicked_consequence_editor.set(consequence[0])

        consequence_id_editor = Label(top, text="Consequence ID:")
        consequence_id_editor.grid(row=1, column=2, padx=10, pady=10)
            
        consequence_id_drop_editor = OptionMenu(top, clicked_consequence_editor, *consequence_id_list_editor)
        consequence_id_drop_editor.grid(row=1, column=3, pady=10, padx=40)

        cur.execute("SELECT description, pfd FROM Consequence_Barrier WHERE consequence_barrier_id = " + entry.get())
        records = cur.fetchall()

        for record in records:
            consequence_barrier_description_editor.insert(0, record[0])
            consequence_barrier_pfd_editor.insert(0, record[1])



    edit_button = Button(top, text="Save Record", command=update)
    edit_button.grid(row=5, column=2, columnspan=2, ipadx=100, padx=10, pady=10)  

    conn.commit()
    conn.close()


# Query, Delete and Edit

lopa_list = ["Event", "Cause", "Cause_Barrier", "Consequence", "Consequence_Barrier"]
clicked = StringVar(root)
clicked.set(lopa_list[0])
drop = OptionMenu(root, clicked, *lopa_list)
drop.grid(row=1, column=1, padx=20, pady=20)


entry = Entry(root, width=30)
entry.grid(row=1, column=2)

edit = Button(root, text="Edit Entry", command=edit, height = 2, width = 23)
edit.grid(row=2, column=2, padx=20, pady=20)

delete = Button(root, text="Delete Entry", bg="red", command=delete, height = 2, width = 23)
delete.grid(row=3, column=2, padx=20, pady=20)


query_list = ["Event", "Cause", "Cause_Barrier", "Consequence", "Consequence_Barrier"]
clicked_query = StringVar(root)
clicked_query.set(query_list[0])

query_drop = OptionMenu(root, clicked_query, *query_list)
query_drop.grid(row=5, column=1, padx=20, pady=20)

query = Button(root, text="Query", fg="blue", command=query, height = 2, width = 23)
query.grid(row=5, column=2, padx=20, pady=20)


# Buttons for inputing data
event = Button(root, text="Create Event", bg="orange", command=new_event, height = 2, width = 23)
event.grid(row=1, column=0, padx=(20,60), pady=20)

cause = Button(root, text="Create Cause", bg="blue",fg="white", command=new_cause, height = 2, width = 23)
cause.grid(row=2, column=0, padx=(20,60), pady=20)

consequence = Button(root, text="Create Consequence", bg="red", fg="white", command=new_consequence, height = 2, width = 23)
consequence.grid(row=3, column=0, padx=(20,60), pady=20)

cause_barrier = Button(root, text="Create Cause Barrier", command=new_cause_barrier, height = 2, width = 23)
cause_barrier.grid(row=4, column=0, padx=(20,60), pady=20)

consequence_barrier = Button(root, text="Create Consequence Barrier", command=new_consequence_barrier, height = 2, width = 23)
consequence_barrier.grid(row=5, column=0, padx=(20,60), pady=20)

# Add vertical lines 

mainloop()
