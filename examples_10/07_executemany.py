import sqlite3

with sqlite3.connect(':memory:') as connection:
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE students(name, pl)')
    students = [('Kolya', 'javascript'), ('Vasya', 'brainfuck')]
    cursor.executemany('INSERT INTO students VALUES (?, ?)', students)

    cursor.execute('SELECT * from students')
    print cursor.fetchall()
