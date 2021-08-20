import mysql.connector

def create_table():
    conn = mysql.connector.connect(
        host="lopasvr.mysql.database.azure.com",
        user="lopasvr_user@lopasvr",
        password="l0p@$vr_u$er",
    )



    cur = conn.cursor()
    
    cur.execute("CREATE DATABASE lopaproject")

create_table()

