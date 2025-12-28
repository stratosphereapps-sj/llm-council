import sqlite3
from datetime import datetime

DB_PATH = "db/council.db"

def get_connection():
    return sqlite3.connect(
        DB_PATH,
        check_same_thread=False  # important
    )

def save_response(agent_name, input_text, output_text):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO responses (agent_name, input_text, output_text, timestamp)
        VALUES (?, ?, ?, ?)
    """, (
        agent_name,
        input_text,
        output_text,
        datetime.utcnow().isoformat()
    ))

    conn.commit()
    conn.close()

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS responses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        agent_name TEXT,
        input_text TEXT,
        output_text TEXT,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()
