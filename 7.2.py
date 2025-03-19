import sqlite3

def create_table():
    conn = sqlite3.connect("articles.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            author TEXT UNIQUE
        )
    """)
    conn.commit()
    conn.close()

def add_article(title, content, author):
    conn = sqlite3.connect("articles.db")
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO Articles (title, content, author) 
            VALUES (?, ?, ?)
        """, (title, content, author))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Error: Author must be unique.")
    conn.close()

def delete_article(article_id):
    conn = sqlite3.connect("articles.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Articles WHERE id = ?", (article_id,))
    conn.commit()
    conn.close()

def view_articles():
    conn = sqlite3.connect("articles.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Articles")
    articles = cursor.fetchall()
    conn.close()
    for article in articles:
        print(f"ID: {article[0]}, Title: {article[1]}, Author: {article[3]}\nContent: {article[2]}\n")

if __name__ == "__main__":
    create_table()
    add_article("First Article", "This is the content of the first article.", "John Doe")
    add_article("Second Article", "This is the content of the second article.", "Jane Doe")
    view_articles()
    delete_article(1)
    view_articles()
