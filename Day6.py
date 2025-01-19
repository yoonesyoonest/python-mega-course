# meals = ['pasta', 'pizza', 'salad']
#
# for meal in meals:
#     print(meal.capitalize())

user_prompt = "Enter a todo: "
todos = []

while True:
    user_action = input("Type add, show, or exit: ")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input(user_prompt)
            todos.append(todo)
        case "show":
            for item in todos:
                print(item)
        case "edit":
            number = input("Enter a todo number to edit: ")
            number = int(number) - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case "exit":
            break






