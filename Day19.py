# Bug - Fixing Exercise 1
# The following get_maximum function is designed
# to return the maximum value of
# the Celsius list, while the last two lines of the code will convert
# the Celsius value to Fahrenheit and print it out.

# def get_maximum():
#     celsius = [14, 15.1, 12.3]
#     maximum = max(celsius)
#     return maximum
#
# celsius = get_maximum()
# fahrenheit = celsius * 1.8 + 32
#
# print(fahrenheit)

# However, when running
# the code, the following error is generated:
#
# TypeError: unsupported operand
# type(s)
# for *: 'NoneType' and 'float'
#
# Try to fix the problem so that the last two
# lines can correctly get the maximal Celsius value
# from the function definition and convert that value to Fahrenheit.

# def get_num():
#     celsius = [14, 15.1, 12.3]
#     num = 0
#     for item in celsius:
#         num = num +1
#     return num
#
# celsius = get_num()
# print(celsius)

import os # operation system

# create todos.txt file whatever doesn't exist
if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w'):
        pass

user_prompt = "Enter a todo: "
todos = []

def get_todos(filepath):
    with open(filepath, "r") as file:  # read
        todos = file.readlines()
    return todos

def write_todos(todos, filepath):
    with open(filepath, "w") as file:  # write
        file.writelines(todos)

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

            write_todos(todos=todos, filepath="todos.txt")
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