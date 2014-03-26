import sys

password = None

while password != 'tefteli\n':

    if password != None:
        sys.stdout.write('Wrong password!\n')

    sys.stdout.write('Your password, please >>> ')
    password = sys.stdin.readline()


sys.stdout.write("** All set! Now get to work! **\n")
