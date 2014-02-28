import sha

name = raw_input("What's your first name? > ")
name = name.lower()

with open(name + '.txt', 'w') as f:
    name_hash = sha.new(name).hexdigest()
    f.write(name_hash)
    
print('Hash saved to {}.txt'.format(name))