import sqlite3


with sqlite3.connect(':memory:') as connection:
    connection.execute('CREATE TABLE students(name, pl)')
    students = [('Kolya', 'javascript'), ('Vasya', 'brainfuck')]

    connection.execute('BEGIN DEFERRED')
    connection.executemany('INSERT INTO students VALUES (?, ?)', students)
    connection.execute('''
        UPDATE students
        SET name="Ninja"
        WHERE pl="javascript"''')
    connection.commit()

    for row in connection.execute('SELECT * from students'):
        print row
