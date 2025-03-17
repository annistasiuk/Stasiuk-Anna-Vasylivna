import sqlite3

# підключення до бази даних trains.db
conn = sqlite3.connect("trains.db")
cursor = conn.cursor()

# отримання списку всіх таблиць в базі даних
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Список таблиць у базі даних:")
for table in tables:
    print(table[0])

# виведення всіх записів з кожної таблиці
for table in tables:
    table_name = table[0]
    print(f"\nДані з таблиці {table_name}:")

    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

# закриття з'єднання після роботи з базою
conn.close()
