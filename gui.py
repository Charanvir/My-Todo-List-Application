import todo_functions
import PySimpleGUI as sg
import time

sg.theme("DarkBlue13")

clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button(size=2, tooltip="Add", image_source="assets/add.png", mouseover_colors="LightBlue2", key="Add")
todos = todo_functions.get_todos()
list_box = sg.Listbox(values=todos,
                      key="todos",
                      enable_events=True,
                      size=(45, 10))
edit_button = sg.Button("Edit", mouseover_colors="LightBlue2")
complete_button = sg.Button(image_source="assets/complete.png", key="Complete", mouseover_colors="LightBlue2",
                            tooltip="Complete")

exit_button = sg.Button("Exit")
error_message = sg.Text("", key="error")

layout = [
    # Row 1
    [clock],
    # Row 2
    [label],
    # Row 3
    [input_box, add_button],
    # Row 4
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
    event, values = window.read(timeout=500)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            if values["todo"] == "":
                window["error"].update("Please enter an item to add")
            else:
                todos = todo_functions.get_todos()
                new_todo = values["todo"] + "\n"
                todos.append(new_todo)
                todo_functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["error"].update("")
                window["todo"].update("")
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
