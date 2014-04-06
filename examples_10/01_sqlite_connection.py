import sqlite3

DB_NAME = 'students.db'

conn = sqlite3.connect(DB_NAME)
try:
    # sqlite supports auto (None), 'DEFERRED', 'IMMEDIATE' or 'EXCLUSIVE'
    print 'Isolation Level %r' % conn.isolation_level
finally:
    conn.close()


with sqlite3.connect(DB_NAME, isolation_level='EXCLUSIVE') as conn:
    print 'Isolation Level %r' % conn.isolation_level


# connect to in-memory db
with sqlite3.connect(':memory:') as conn:
    print 'Total changes %r' % conn.total_changes
