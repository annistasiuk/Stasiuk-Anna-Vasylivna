import sqlite3

# підключення до бази даних
conn = sqlite3.connect("trains.db")
cursor = conn.cursor()

# отримання списку всіх таблиць у базі
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# виведення даних кожної таблиці
for table in tables:
    table_name = table[0]
    print(f"Вміст таблиці: {table_name}")

    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    print("-" * 40)

# Закриття з'єднання з базою даних
conn.close()
