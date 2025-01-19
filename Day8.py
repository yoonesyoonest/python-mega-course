# Bug-Fixing Exercise 1
# Supposedly, the following program should:
#
# 1. Prompt the user to input an index (e.g., 0, 1, or 2).
#
# 2. Print out the item with that index.
#
# However, there is a bug with the program which you should try to fix.
#
#
#
# menu = ["pasta", "pizza", "salad"]
#
# user_choice = input("Enter the index of the item: ")
#
# message = f"You chose {menu[int(user_choice)]}""."
# print(message)
#
#
#
# Bug-Fixing Exercise 2
# Here is another piece of buggy code:
#
# menu = ["pasta", "pizza", "salad"]
#
# for i, j in enumerate(menu):
#     print(f"{i+1}.{j}")
# Fix the code, so it prints out the output below:
#
# 0.pasta
# 1.pizza
# 2.salad
#
#
#
# Bug-Fixing Exercise 3
# Here is another piece of code that contains a bug:
#
# menu = ["pasta", "pizza", "salad"]
#
# for i, j in enumerate(menu):
#     print(f"{i}.{j}")
# The expected output is this:
#
# 0.pasta
# 1.pizza
# 2.salad
# Fix the bug so the program prints out the above output.

# -----------------------------
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w'):
        pass

user_prompt = "Enter a todo: "
todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    match user_action:
        case "add":
            file = open("todos.txt", "r") # read
            todos = file.readlines()
            file.close()

            todo = input(user_prompt)
            todos.append(todo+"\n")

            file = open("todos.txt", "w") # write
            file.writelines(todos)
            file.close()
        case "show":
            for index, item in enumerate(todos):
                # print(index+1,"-",item)
                print(f"{index+1}- {item.title()}")
        case "edit":
            number = input("Enter a todo number to edit: ")
            number = int(number) - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case "complete":
            number = int(input("Enter a todo number to remove: "))
            todos.pop(number-1)
        case "exit":
            break