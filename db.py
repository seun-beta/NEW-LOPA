import sqlite3

def create_table():

    
    conn = sqlite3.connect("lopa.db")
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS "Event" (
        "event_id"	INTEGER NOT NULL UNIQUE PRIMARY KEY,
        "description"	TEXT,
        "cause_id"	INTEGER,
        "consequence_id" INTEGER,
        FOREIGN KEY("cause_id" ) REFERENCES "Cause"("cause_id")
        );
    """)

    cur.execute("""CREATE TABLE IF NOT EXISTS "Cause" 
        (
        "cause_id"	INTEGER NOT NULL UNIQUE PRIMARY KEY,
        "description"	TEXT,
        "initial_frequency"	REAL,
        "event_id"	INTEGER,
        "target_frequency"	REAL

        );
    """)

    cur.execute("""CREATE TABLE IF NOT EXISTS "Cause_Barrier" 
        (
        "cause_barrier_id"	INTEGER NOT NULL UNIQUE PRIMARY KEY,
        "description"	TEXT,
        "pfd"	REAL,
        "cause_id"	INTEGER,
        FOREIGN KEY("cause_id") REFERENCES "Cause"("cause_id")
        );
    """)

    cur.execute("""CREATE TABLE IF NOT EXISTS "Consequence"
        (
        "consequence_id"	INTEGER NOT NULL UNIQUE PRIMARY KEY,
        "description"	TEXT,
        "initial_frequency"	REAL,
        "target_frequency"	REAL
        );
    """)

    cur.execute("""CREATE TABLE IF NOT EXISTS "Consequence_Barrier" 
        (
        "consequence_barrier_id" INTEGER NOT NULL UNIQUE PRIMARY KEY,
        "description"	TEXT,
        "pfd"	REAL,
        "consequence_id"	INTEGER
        );
    """)

    conn.commit()
    conn.close()
