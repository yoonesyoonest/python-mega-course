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
            file = open("todos.txt", "r") # read
            todos = file.readlines()
            file.close()

            # List comprehension
            todos = [item.strip("\n") for item in todos]

            for index, item in enumerate(todos):
                item = item.strip("\n")
                # print(index+1,"-",item)
                print(f"{index+1}- {item.title()}")
        case "edit":
            file = open("todos.txt", "r") # read
            todos = file.readlines()
            file.close()

            number = input("Enter a todo number to edit: ")
            number = int(number) - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo+"\n"

            file = open("todos.txt", "w") # write
            file.writelines(todos)
            file.close()
        case "complete":
            file = open("todos.txt", "r") # read
            todos = file.readlines()
            file.close()

            number = int(input("Enter a todo number to remove: "))
            todos.pop(number-1)

            file = open("todos.txt", "w") # write
            file.writelines(todos)
            file.close()
        case "exit":
            break