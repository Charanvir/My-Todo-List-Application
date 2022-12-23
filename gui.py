import todo_functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

exit_button = sg.Button("Exit")

window = sg.Window(
    "My To-Do App",
    layout=[
        # Row 1
        [label],
        # Row 2
        [input_box, add_button],
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
        case sg.WINDOW_CLOSED:
            break
        case "Exit":
            window.close()
            break
