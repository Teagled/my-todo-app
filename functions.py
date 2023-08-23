def get_todos():
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
    return todos

def write_todos(newtodo):
    with open('todos.txt', 'w') as file:
        file.writelines(newtodo)