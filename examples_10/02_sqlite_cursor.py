import sqlite3

with sqlite3.connect(':memory:') as connection:
    cursor = connection.cursor()
    result = cursor.execute('CREATE TABLE students(name, pl)')
    print "Create rowcount %r" % result.rowcount


    cursor.execute('INSERT INTO students VALUES (?, ?)',
                   ('Andrey', 'python'))
    print "Insert rowcount %r" % result.rowcount

    cursor.execute('SELECT * FROM students')
    print "students: %r" % cursor.fetchall()
    print "cursor.description: %r" % (cursor.description,)

# According to PEP 249, description contains columns escriptions:
#   name
#   type_code
#   display_size
#   internal_size
#   precision
#   scale
#   null_ok
#
# http://legacy.python.org/dev/peps/pep-0249/
