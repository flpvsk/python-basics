# available in python 2.6 onwards
with open('text_file.txt', 'r') as text_file:
    print('Lines reversed:')
    for line in text_file:
        print(line[:-1][::-1])
