import PySimpleGUI as sg

import functions

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos("todos.txt"), key="todos",
                      enable_events=True, size=[45,15])

edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")

button_labels = ["Close", "Apply"]

window = sg.Window('My To-Do App', layout=[[label, input_box, add_button],[list_box,edit_button,complete_button]])

while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "Add":
            todos = functions.get_todos("todos.txt")
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos, "todos.txt")
            window["todos"].update(todos)
        case "todos":
            window["todo"].update(values["todos"][0])
        case "Edit":
            todos_to_edit = values["todos"][0]
            new_todo = values["todo"]

            todos = functions.get_todos("todos.txt")
            index = todos.index(todos_to_edit)
            todos[index] = new_todo + "\n"
            functions.write_todos(todos, "todos.txt")
            window["todos"].update(todos)
        case "Complete":
            todos_to_complete = values["todos"][0]
            todos = functions.get_todos("todos.txt")
            todos.remove(todos_to_complete)
            functions.write_todos(todos,filepath="todos.txt")
            window["todos"].update(todos)

