# http://xkcd.com/327/
import sqlite3

def select_student(cursor, name):
    cursor.execute("SELECT * FROM students where name = '" + name + "'")
    return cursor.fetchall()

with sqlite3.connect(':memory:') as connection:
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE students(name, pl)')

    cursor.execute('INSERT INTO students VALUES (?, ?)',
                   ('Andrey', 'python'))

    cursor.execute('INSERT INTO students VALUES (?, ?)',
                   ('Vsevolod', 'java'))

    print 'Andreys: %r' % (select_student(cursor, 'Andrey'),)
    print 'Roberts: %r' % select_student(cursor, "Robert' or ''='")

