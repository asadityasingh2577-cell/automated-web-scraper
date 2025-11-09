import sqlite3
from config import DATABASE_PATH

def insert_quote(text, author, tags):
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute('''
        INSERT INTO quotes (text, author, tags)
        VALUES (?, ?, ?)
    ''', (text, author, tags))
    conn.commit()
    conn.close()

def get_all_quotes(limit=None):
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    query = 'SELECT id, text, author, tags, scraped_at FROM quotes ORDER BY scraped_at DESC'
    if limit:
        query += f' LIMIT {int(limit)}'
    c.execute(query)
    rows = c.fetchall()
    conn.close()
    return rows
