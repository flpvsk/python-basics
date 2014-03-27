import os

cur_path = os.path.abspath('.')
print('Interpreter was started at: %r' % cur_path)

up_one_level = os.path.join(cur_path, '..')
up_one_level_abs = os.path.abspath(up_one_level)
dir_name = os.path.basename(up_one_level_abs)
print('One level up is a dir called: %r' % dir_name)

print('Current directory contains: %r' % os.listdir('.'))
