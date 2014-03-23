from examples_4 import todo

todo.add('Sandwich')
todo.add('Learn some python')
todo.add('Sleep')
_todos = todo.items()


def next_pending():
    return [task[0] for task in _todos if task[1] == 'pending'][0]

print next_pending()