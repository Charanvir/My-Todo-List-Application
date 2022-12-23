import todo_functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App", layout=[
    # Row 1
    [label],
    # Row 2
    [input_box, add_button]
])
window.read()
window.close()
