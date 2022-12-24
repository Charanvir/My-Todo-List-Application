FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, "r") as file_open:
        todos_function = file_open.readlines()
    return todos_function


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write a to-do item list in the text file. """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello from todo_functions.py")
    print(get_todos())
