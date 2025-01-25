import PySimpleGUI as sg

import functions

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos("todos.txt"), key="todos",
                      enable_events=True, size=[45,15])

window = sg.Window('My To-Do App', layout=[[label, input_box, add_button],[list_box]])
window.read()
print("hello")
window.close()