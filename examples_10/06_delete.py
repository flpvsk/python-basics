import sqlite3

with sqlite3.connect(':memory:') as connection:
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE students(name, pl)')
    cursor.execute('INSERT INTO students VALUES ("Kolya", "javascript")')
    cursor.execute('INSERT INTO students VALUES ("Vasya", "brainfuck")')
    cursor.execute('DELETE FROM students')
    print 'Rows affected: %s' % cursor.rowcount

    cursor.execute('SELECT * from students')
    print cursor.fetchall()
