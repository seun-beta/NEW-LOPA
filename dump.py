



# EVENT INFORMATION

    
    cause_id = Label(top, text="Cause ID:")
    cause_id.grid(row=1, column=2, padx=10, pady=10)

    consequence_id = Label(top, text="Consequence ID:")
    consequence_id.grid(row=1, column=4, pady=10)


# --------------------------------CAUSE ID Dropdown-------------------

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

        
    cause_id_drop = OptionMenu(top, clicked_cause, *cause_id_list)
    cause_id_drop.grid(row=1, column=3, pady=10, padx=40)


  # --------------------------------CONSEQUENCE ID Dropdown-------------------
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

   
    consequence_id_drop = OptionMenu(top, clicked_consequence, *consequence_id_list)
    consequence_id_drop.grid(row=1, column=5, pady=10, padx=40)

