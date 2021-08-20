import mysql.connector
import sqlite3


def create_table():
    conn = sqlite3.connect("lopa.db")
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS Event (
                event_id INT AUTO_INCREMENT PRIMARY KEY,
                description TEXT,
                target_frequency REAL)
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
