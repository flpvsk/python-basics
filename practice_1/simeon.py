import sha

name = raw_input("What's your second name? > ")
name = name.lower()
file_name = '{}.txt'.format(name)

with open(file_name, 'w') as f:
 name_hash = sha.new(name).hexdigest()
 f.write(name_hash)

print('Hash saved to {}.'.format(file_name))