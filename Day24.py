# import os # operation system
# from functions import get_todos, write_todos
# # import functions
# import time
#
# # create todos.txt file whatever doesn't exist
# if not os.path.exists('todos.txt'):
#     with open('todos.txt', 'w'):
#         pass
#
# user_prompt = "Enter a todo: "
# todos = []
#
# now = time.strftime("%A %b %d, %Y %H:%M:%S")
# print("It is", now)
#
# while True:
#     user_action = input("Type add, show, edit, complete or exit: ")
#     user_action = user_action.strip()
#
#     if user_action.startswith("add"):
#         todo = user_action[4:]
#
#         todos = get_todos("todos.txt")
#
#         todos.append(todo+"\n")
#
#         write_todos(todos, "todos.txt")
#     elif user_action.startswith("show"):
#         todos = get_todos("todos.txt")
#
#         # List comprehension
#         todos = [item.strip("\n") for item in todos]
#
#         for index, item in enumerate(todos):
#             # item = item.strip("\n")
#             # print(index+1,"-",item)
#             print(f"{index+1}- {item.title()}")
#     elif user_action.startswith("edit"):
#         try:
#             number = user_action[5:]
#
#             todos = get_todos("todos.txt")
#
#             new_todo = input("Enter new todo: ")
#             todos[int(number) - 1] = new_todo+"\n"
#
#             write_todos(filepath="todos.txt", todos=todos)
#         except IndexError:
#             print("Please enter a valid number.")
#     elif user_action.startswith("complete"):
#         try:
#             number = int(user_action[9:])
#
#             todos = get_todos("todos.txt")
#
#             index = number - 1
#             todo_to_remove = todos[index].strip("\n")
#             todos.pop(index)
#
#             write_todos(todos, "todos.txt")
#
#             message = f"Todo {todo_to_remove} was removed from the List."
#             print(message)
#         except IndexError:
#             print("Please enter a valid number.")
#     elif user_action.startswith("exit"):
#         break
#     else:
#         print("Command is not valid.")
#
# print("Bye")

# import csv
#
# with open("weather.csv", "r") as file:
#     data = list(csv.reader(file))
#
# print(data[1:])
#
# city = input("Enter city: ")
#
# for row in data[1:]:
#     if row[0] == city:
#         print(row[1])

# import glob
#
# myfiles = glob.glob("*.txt")
#
# print(myfiles)
#
# for filepath in myfiles:
#     with open(filepath, "r") as file:
#         print(file.read())

# import shutil
#
# shutil.make_archive("output", "zip", "files")
