import sqlite3

with sqlite3.connect(':memory:') as connection:
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE students(name, pl)')

    cursor.execute('INSERT INTO students VALUES (:name, :pl)',
                   {'name': 'Andrey', 'pl': 'python'})

    cursor.execute('SELECT * FROM students')
    print cursor.fetchall()
