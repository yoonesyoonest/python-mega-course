# Bug-Fixing Exercise 1
# The following formula calculates the free-fall time of an object.
#
#
# h is the free-fall distance and g is the gravity. On Earth, gravity is 9.80665 m/s2.
#
# Given the above information, we have created a program that calculates the free-fall time given
# the free-fall distance h and the gravity g
# which will be a default parameter with a value of 9.80665:

# def calculate_time(h, g=9.80665):
#     t = (2 * h / g) ** 0.5
#     return t
#
# time = calculate_time(100)
# print(time)

# However, the script produces an error.
# Try running the script in your IDE and then fix the error
# so the program successfully calculates the free-fall time.

import os # operation system
from functions import get_todos, write_todos
# import functions

# create todos.txt file whatever doesn't exist
if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w'):
        pass

user_prompt = "Enter a todo: "
todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[3:].strip()

        todos = get_todos("todos.txt")

        todos.append(todo+"\n")

        write_todos(todos, "todos.txt")
    elif user_action.startswith("show"):
        todos = get_todos("todos.txt")

        # List comprehension
        todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(todos):
            # item = item.strip("\n")
            # print(index+1,"-",item)
            print(f"{index+1}- {item.title()}")
    elif user_action.startswith("edit"):
        try:
            number = user_action[4:].strip()

            todos = get_todos("todos.txt")

            new_todo = input("Enter new todo: ")
            todos[int(number) - 1] = new_todo+"\n"

            write_todos(filepath="todos.txt", todos=todos)
        except IndexError:
            print("Please enter a valid number.")
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[8:].strip())

            todos = get_todos("todos.txt")

            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            write_todos(todos, "todos.txt")

            message = f"Todo {todo_to_remove} was removed from the List."
            print(message)
        except IndexError:
            print("Please enter a valid number.")
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")

print("Bye")