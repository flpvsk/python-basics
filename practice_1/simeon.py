import sha

name = raw_input("What's your first name? > ")
name = name.lower()
surname = raw_input("What's your second name? > ")
surname = surname.lower()

#file_name = '{}.txt'.format(name)

# with open(file_name, 'w') as f:
#  name_hash = sha.new(name).hexdigest()
#  f.write(name_hash)

print('Hi, {} {}!'.format(name,surname))
