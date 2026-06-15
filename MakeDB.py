# Data Base
import sqlite3

conn = sqlite3.connect("scraper.db")
cursor = conn.cursor()

# programs
cursor.execute("""
CREATE TABLE IF NOT EXISTS programs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    url TEXT NULL,
)
""")

conn.commit()
conn.close()
print("SQLite database and tables created")