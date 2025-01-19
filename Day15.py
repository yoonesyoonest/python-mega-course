# Bug-Fixing Exercise 1: The program below intends to find out how many items have at least one underscore ("_") character in them.  However, there is an error with the code. Try to find and fix it.
#
# ids = ["XF345_89", "XER76849", "XA454_55"]
#
# x = 0
#
# for id in ids:
#
#    if '_' in id:
#     x = x + 1
# print(x)

# Solution
#
#
#
# Bug-Fixing Exercise 2: This program also intends to find out how many items have an underscore in them. However, the program has a bug. It doesn't return an error message, but it returns:
#
# 1
#
# 1
#
# 2
#
# Instead, the expected output is:
#
# 2

# Try to fix the program so it returns the expected output. Here is the buggy program:

# ids = ["XF345_89", "XER76849", "XA454_55"]
#
# x = 0
#
# for id in ids:
#    if '_' in id:
#      x = x + 1
# print(x)
#
# Solution
#
#
#
# Bug-Fixing Exercise 3: Fix the program below so it prints out "OK" when the perimeter is less than 14 and the area is less than 8.
#
# length = float(input("Enter length: "))
#
# width = float(input("Enter width: "))
#
#
# perimeter = (length + width) * 2
#
# area = length * width
#
#
# print("Perimeter is", perimeter)
#
# print("Area is", area)
#
#
# if perimeter < 14 or area < 8:
#    print("OK")
# else:
#    print("NOT OK")
#
# Solution

import os

# create todos.txt file whatever doesn't exist
if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w'):
        pass

user_prompt = "Enter a todo: "
todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if "add" in user_action:
        todo = user_action[3:].strip()

        with open("todos.txt", "r") as file: # read
            todos = file.readlines()

        todos.append(todo+"\n")

        with open("todos.txt", "w") as file: # write
            file.writelines(todos)
    elif "show" in user_action:
        with open("todos.txt", "r") as file: # read
            todos = file.readlines()

        # List comprehension
        todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(todos):
            # item = item.strip("\n")
            # print(index+1,"-",item)
            print(f"{index+1}- {item.title()}")
    elif "edit" in user_action:
        number = user_action[4:].strip()

        with open("todos.txt", "r") as file: # read
            todos = file.readlines()

        new_todo = input("Enter new todo: ")
        todos[int(number) - 1] = new_todo+"\n"

        with open("todos.txt", "w") as file: # write
            file.writelines(todos)
    elif "complete" in user_action:
        number = int(user_action[8:].strip())

        with open("todos.txt", "r") as file: # read
            todos = file.readlines()

        index = number - 1
        todo_to_remove = todos[index].strip("\n")
        todos.pop(index)

        with open("todos.txt", "w") as file: # write
            file.writelines(todos)

        message = f"Todo {todo_to_remove} was removed from the List."
        print(message)
    elif "exit" in user_action:
        break
    else:
        print("Command is not valid.")

print("Bye")