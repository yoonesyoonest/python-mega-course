# user_prompt = "Enter a todo: "
# todo = input(user_prompt)
# print(todo)

# user_prompt = "Enter a todo: "
# todo1 = input(user_prompt)
# todo2 = input(user_prompt)
# todo3 = input(user_prompt)
# todo4 = input(user_prompt)
#
# todos = [todo1, todo2, todo3, todo4]
# print(todos)

text = input("Enter a title: ")

length = len(text)

if length <= 20:
    print("The length of the text is", length)
else:
    print("The length is more than 20")