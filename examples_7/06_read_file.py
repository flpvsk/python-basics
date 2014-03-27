import sys

text_file = open('text_file.txt', 'r')

try:
    print('First 4 bytes: %r' % text_file.read(4))
    print('Rest of the line: %r' % text_file.readline())
    print('** Iterate over all lines: **')
    for line in text_file:
        sys.stdout.write(line)
finally:
    text_file.close()
