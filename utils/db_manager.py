import sqlite3
import json
import time
from config import DB_PATH

class Cache:
    def __init__(self):
        self.db_path = DB_PATH
        self._init_db()

    def _init_db(self) -> None:
        """
        Initializes the SQLite database and creates the cache table if it doesn't exist.
        NOTE: This is a class method and should not be called explicitly. If done, it can corrupt the cache.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_cache(
            city TEXT PRIMARY KEY,
            response_json TEXT NOT NULL,
            timestamp REAL NOT NULL
        )
        """)
        conn.commit()
        conn.close()
    
    def save_weather(self, city:str, data:dict) -> None:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        timestamp = time.time()
        data_json = json.dumps(data)
        cursor.execute("INSERT OR REPLACE INTO weather_cache VALUES(?,?,?)", (city.lower(), data_json, timestamp))
        conn.commit()
        conn.close()

    def get_cached_weather(self, city:str) -> dict | None:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM weather_cache WHERE city=?", (city.lower(),))
        row = cursor.fetchone()
        conn.close()

        if row == None:
            return None
        if time.time() - row[2] > 600:
            return None
        else:
            return json.loads(row[1])