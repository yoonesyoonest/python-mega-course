# Bug-Fixing Exercise 1
# with open("file.txt", 'r') as file:
#     content = file.read()
#     print(content)
#     print(len(content))
# The Python script above is in the same directory with a file named file.txt whose content is:
#
# Hello You
#
# The Python script should print out the content of the file and the number of characters of the text inside file.txt. So, the expected output would be:
#
# Hello You
# 9
# However, the script prints out this:
#
# Hello You
# 0
# Can you fix the program so it prints out the expected output?

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
        with open("todos.txt", "r") as file: # read
            todos = file.readlines()

        todo = user_action[3:].strip()
        todos.append(todo+"\n")

        with open("todos.txt", "w") as file: # write
            file.writelines(todos)
    elif "show" in user_action:
        with open("todos.txt", "r") as file: # read
            todos = file.readlines()

        # List comprehension
        todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(todos):
            item = item.strip("\n")
            # print(index+1,"-",item)
            print(f"{index+1}- {item.title()}")
    elif "edit" in user_action:
        with open("todos.txt", "r") as file: # read
            todos = file.readlines()

        number = user_action[4:].strip()
        number = int(number) - 1
        new_todo = input("Enter new todo: ")
        todos[number] = new_todo+"\n"

        with open("todos.txt", "w") as file: # write
            file.writelines(todos)
    elif "complete" in user_action:
        with open("todos.txt", "r") as file: # read
            todos = file.readlines()

        number = int(user_action[8:].strip())
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