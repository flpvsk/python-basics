''' Asks for name;
Calculates sha1-hash from it;
Writes hash to file.
'''

import sha

name = raw_input("What's your first name? > ")
name = name.lower()
file_name = '{}.txt'.format(name)

with open(file_name, 'w') as f:
    name_hash = sha.new(name).hexdigest()
    f.write(name_hash)

print('Hash to {}.'.format(file_name))