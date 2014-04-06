import sqlite3
from collections import namedtuple

Student = namedtuple('Student', ['name', 'pl'])

def student_factory(cursor, row):
    return Student(*row)


with sqlite3.connect(':memory:') as connection:
    # Add row factory
    connection.row_factory = student_factory

    connection.execute('CREATE TABLE students(name, pl)')
    students = [('Kolya', 'javascript'), ('Vasya', 'brainfuck')]
    connection.executemany('INSERT INTO students VALUES (?, ?)', students)

    for student in connection.execute('SELECT * from students'):
        print student.name
