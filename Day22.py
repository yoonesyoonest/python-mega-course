# The program depicted below consists of two Python files.
# The program tries to count and print out the number of periods in the "Trees are good.
# Grass is green." . However, running the main.py file returns an error. Please fix the error.
#
# main.py:
#
# import functions
#
# nr_of_periods = functions.count("Trees are good. Grass is green.....")
# print(nr_of_periods)
#
# functions.py
#
# def count(phrase):
#     return phrase.count('.')

# Bug-Fixing Exercise 2
# The same program as in exercise 1 now is throwing yet another error.
# Hunt the error down and fix it.
#
# main.py:
#
# import functions
#
# nr_of_periods = functions.count("Trees are good. Grass is green.")
# print(nr_of_periods)
#
#
# functions.py:
#
# def count(phrase):
#     return phrase.count('.')
#
# Bug-Fixing Exercise 3
# There is another error in the same program. Please fix the error.
#
# main.py:
#
# from functions import count
#
# nr_of_periods = count("Trees are good. Grass is green.")
# print(nr_of_periods)
#
#
# functions.py:
#
# def count(phrase):
#     return phrase.count('.')

import os # operation system
from functions import get_todos, write_todos
# import functions
import time

# create todos.txt file whatever doesn't exist
if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w'):
        pass

user_prompt = "Enter a todo: "
todos = []

now = time.strftime("%A %b %d, %Y %H:%M:%S")
print("It is", now)

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