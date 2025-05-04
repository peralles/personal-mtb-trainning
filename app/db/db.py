import sqlite3
import pandas as pd

DB_PATH = "treinos.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS activities (
            id INTEGER PRIMARY KEY,
            name TEXT,
            distance REAL,
            moving_time INTEGER,
            elapsed_time INTEGER,
            total_elevation_gain REAL,
            start_date TEXT
        )
    ''')
    conn.commit()
    conn.close()


def save_activity(activity):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR IGNORE INTO activities 
        (id, name, distance, moving_time, elapsed_time, total_elevation_gain, start_date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        activity["id"],
        activity["name"],
        activity["distance"],
        activity["moving_time"],
        activity["elapsed_time"],
        activity["total_elevation_gain"],
        activity["start_date"]
    ))
    conn.commit()
    conn.close()


def save_activities(activities):
    for act in activities:
        save_activity(act)


def load_activities_from_db():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(
        "SELECT * FROM activities ORDER BY start_date ASC", conn)
    conn.close()
    return df
