# DataStorageManager.py
# This script contains the DataStorageManager class responsible for storing and retrieving market data
# using a SQLite database. It interacts with the MarketDataCollector class, which provides the market data
# to be stored. It is used in main.py to save the collected data and load it when needed.

import sqlite3
import pandas as pd

class DataStorageManager:

    def __init__(self, config):
        self.config = config
        self.db_name = "market_data.db"
        self._initialize_db()

    def _initialize_db(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS market_data (
                    id INTEGER PRIMARY KEY,
                    symbol TEXT NOT NULL,
                    date DATE NOT NULL,
                    open FLOAT NOT NULL,
                    high FLOAT NOT NULL,
                    low FLOAT NOT NULL,
                    close FLOAT NOT NULL,
                    volume INTEGER NOT NULL,
                    UNIQUE (symbol, date)
                )
            """)
            conn.commit()

    def store_data(self, symbol, data):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            for date, row in data.iterrows():
                cursor.execute("""
                    INSERT OR IGNORE INTO market_data (symbol, date, open, high, low, close, volume)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (symbol, date.strftime('%Y-%m-%d'), row["Open"], row["High"], row["Low"], row["Close"], row["Volume"]))
            conn.commit()
    
    def get_data(self, symbol, start_date, end_date):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT date, open, high, low, close, volume
                FROM market_data
                WHERE symbol = ? AND date >= ? AND date <= ?
                ORDER BY date
            """, (symbol, start_date, end_date))
            data = cursor.fetchall()
            
            # Create a DataFrame from the fetched data
            df = pd.DataFrame(data, columns=["Date", "Open", "High", "Low", "Close", "Volume"])
            df["Date"] = pd.to_datetime(df["Date"])
            df.set_index("Date", inplace=True)
            
            return df

