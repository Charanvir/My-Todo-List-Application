# from functions import get_todos, write_todos
import todo_functions
import time

now = time.strftime("%b %d %Y %H:%M:%S")
print(f"The current date and time is: {now}")

while True:
    user_action = input('Type add, show, edit, remove or exit: ').strip()

    if user_action.startswith("add"):
        # add a break line
        if len(user_action) == 3:
            todo = input("Please enter your new todo: ") + "\n"
        elif len(user_action) > 3:
            # Splicing out everything before index 4
            todo = user_action[4:] + "\n"

        # file_read = open("todos.txt", "r")
        # todos = file_read.readlines()
        # file_read.close()

        # Does the same as above, without the need to close the file
        todos = todo_functions.get_todos()

        todos.append(todo.capitalize())

        todo_functions.write_todos(todos)

        # The line below is the same as the line directly above, but using context manager
        # file_write = open("todos.txt", "w")
        # file_write.writelines(todos)
        # file_write.close()
    elif user_action.startswith("show"):
        # savedTodos = open("todos.txt", "r")
        # todos = savedTodos.readlines()
        # savedTodos.close()

        # Will accomplish the above code without the need to close()
        todos = todo_functions.get_todos()

        # new_todos = []
        # for item in todos:
        #     new_item = item.strip("\n")
        #     new_todos.append(new_item)

        # The list comprehension below will do the same as the for loop above
        # Don't have to define a new variable and create a new for loop
        new_todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(new_todos):
            print(f"{index + 1}. {item}")
    elif user_action.startswith("edit"):
        try:
            if len(user_action) == 4:
                number = int(input("Which item would you like to edit (select the item number) "))
            elif len(user_action) > 4:
                number = int(user_action[5:])
            number = number - 1
            newTodo = input("Enter the new item: ").capitalize() + "\n"

            todos = todo_functions.get_todos()

            todos[number] = newTodo

            todo_functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("remove"):

        try:
            if len(user_action) == 6:
                number = int(input("Which item would you like to remove (select the item number) "))
            elif len(user_action) > 6:
                number = int(user_action[7:])
            number = number - 1

            todos = todo_functions.get_todos()

            todosToPrint = [todo.strip("\n") for todo in todos]

            print(f"{todosToPrint[number]} was removed from the list")
            todos.pop(number)

            todo_functions.write_todos(todos)

        except IndexError:
            print("That item number does not exist.")
            continue
        except ValueError:
            print("Must select an item number to remove.")

    elif user_action.startswith("exit"):
        break

    else:
        print("That command was no valid, please enter a valid command")
# The below is for when an option is entered that does not match one of the cases defined above
# Similar to the else added above
# case _:
#     print("Please enter one of the options")

print("Bye!!!")
