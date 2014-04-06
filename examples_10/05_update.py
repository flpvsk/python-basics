import sqlite3

with sqlite3.connect(':memory:') as connection:
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE students(name, pl)')
    cursor.execute('INSERT INTO students VALUES ("Andrey", "python")')
    cursor.execute('UPDATE students SET pl="Java" where name="Andrey"')
    print 'Rows affected: %s' % cursor.rowcount

    cursor.execute('SELECT * from students')
    print cursor.fetchall()
