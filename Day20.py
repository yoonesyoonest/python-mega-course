import os # operation system

# create todos.txt file whatever doesn't exist
if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w'):
        pass

user_prompt = "Enter a todo: "
todos = []

def get_todos(filepath):
    """
    Read a text file and return the list of to-do items.
    :param filepath:
    """
    with open(filepath, "r") as file:  # read
        todos = file.readlines()
    return todos

def write_todos(todos, filepath):
    """
    Write the to-do items list in the next file.
    :param todos:
    :param filepath:
    """
    with open(filepath, "w") as file:  # write
        file.writelines(todos)

text = "\n\
Principles of productivity:\n\
Managing you inflow.\n\
Systemizing everything that repeats.\n\
"

print(text)

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