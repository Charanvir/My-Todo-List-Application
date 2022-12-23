import todo_functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
todos = todo_functions.get_todos()
list_box = sg.Listbox(values=todos,
                      key="todos",
                      enable_events=True,
                      size=(45, 10))
edit_button = sg.Button("Edit")

exit_button = sg.Button("Exit")

window = sg.Window(
    "My To-Do App",
    layout=[
        # Row 1
        [label],
        # Row 2
        [input_box, add_button],
        # Row 3
        [list_box, edit_button],
        # Exit Row
        [exit_button]
    ],
    font=('Helvetica', 20)
)
while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = todo_functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            todo_functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"] + "\n"

            todos = todo_functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            todo_functions.write_todos(todos)
            window["todos"].update(values=todos)
        case sg.WINDOW_CLOSED:
            break
        case "Exit":
            window.close()
            break
