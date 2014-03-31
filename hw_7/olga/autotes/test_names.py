#example C:\Users\Olga\git\python-basics\hw_7\olga\autotes>C:\Python27\python test_names.py
import os

log_dir = "C:\\test-results\\"
tests = []
for file in os.listdir(os.path.dirname(log_dir)):
    f = open(log_dir + file, 'r')
    data = f.read()
    if data:
        data = data.split("Started test ")
        for x in data:
            if x:
                tests.append( x[1: x.find("'",2)])
    f.close()

for test in list(set(tests)):
    print test
