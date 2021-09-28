import mysql.connector

def create_table():
    conn = mysql.connector.connect(
        host="HOST",
        user="USER",
        password="PASSWORD",
        database="DATABASE"
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
    conn.close()
