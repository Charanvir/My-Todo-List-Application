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
complete_button = sg.Button("Complete")

exit_button = sg.Button("Exit")
error_message = sg.Text("", key="error")

layout = [
    # Row 1
    [label],
    # Row 2
    [input_box, add_button],
    # Row 3
    [list_box, edit_button, complete_button],
    # Exit Row
    [exit_button, error_message]
]

window = sg.Window(
    "My To-Do App",
    layout=layout,
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
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"] + "\n"

                todos = todo_functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                todo_functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["error"].update("")
            except IndexError:
                window["error"].update("Please select an item to edit")
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = todo_functions.get_todos()
                todos.remove(todo_to_complete)
                todo_functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
                window["error"].update("")
            except IndexError:
                window["error"].update("Please select an item to complete")
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case sg.WINDOW_CLOSED:
            break
        case "Exit":
            break
window.close()
