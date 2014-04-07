import sqlite3

with sqlite3.connect(':memory:') as connection:
    # Add row factory
    connection.row_factory = sqlite3.Row

    connection.execute('CREATE TABLE students(name, pl)')
    students = [('Kolya', 'javascript'), ('Vasya', 'brainfuck')]
    connection.executemany('INSERT INTO students VALUES (?, ?)', students)

    for row in connection.execute('SELECT * from students'):
        print row[0], row['name']
