import PySimpleGUI as sg

import functions

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos("todos.txt"), key="todos",
                      enable_events=True, size=[45,15])

edit_button = sg.Button("Edit")

button_labels = ["Close", "Apply"]

window = sg.Window('My To-Do App', layout=[[label, input_box, add_button],[list_box,edit_button]])

while True:
    event, values = window.read()
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos("todos.txt")
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos, "todos.txt")
        case WIN_CLOSED:
            break
    window.close()