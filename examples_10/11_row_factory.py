import sqlite3

def dict_factory(cursor, row):
    print 'dict_factory called with %r' % (row,)
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

with sqlite3.connect(':memory:') as connection:
    # Add row factory
    connection.row_factory = dict_factory

    connection.execute('CREATE TABLE students(name, pl)')
    students = [('Kolya', 'javascript'), ('Vasya', 'brainfuck')]
    connection.executemany('INSERT INTO students VALUES (?, ?)', students)

    for row in connection.execute('SELECT * from students'):
        print row['name']
