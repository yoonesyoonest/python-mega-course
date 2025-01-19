# filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]
#
# for filename in filenames:
#     print(filename.replace(".","-",1))

# -------------------

user_prompt = "Enter a todo: "
todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input(user_prompt)
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos):
                # print(index+1,"-",item)
                print(f"{index+1}- {item.title()}")
        case "edit":
            number = input("Enter a todo number to edit: ")
            number = int(number) - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case "exit":
            break