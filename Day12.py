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
            with open("todos.txt", "r") as file: # read
                todos = file.readlines()

            todo = input(user_prompt)
            todos.append(todo+"\n")

            with open("todos.txt", "w") as file: # write
                file.writelines(todos)
        case "show":
            with open("todos.txt", "r") as file: # read
                todos = file.readlines()

            # List comprehension
            todos = [item.strip("\n") for item in todos]

            for index, item in enumerate(todos):
                item = item.strip("\n")
                # print(index+1,"-",item)
                print(f"{index+1}- {item.title()}")
        case "edit":
            with open("todos.txt", "r") as file: # read
                todos = file.readlines()

            number = input("Enter a todo number to edit: ")
            number = int(number) - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo+"\n"

            with open("todos.txt", "w") as file: # write
                file.writelines(todos)
        case "complete":
            with open("todos.txt", "r") as file: # read
                todos = file.readlines()

            number = int(input("Enter a todo number to remove: "))
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            with open("todos.txt", "w") as file: # write
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the List."
            print(message)
        case "exit":
            break