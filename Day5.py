# The code below has two bugs. Hunt them down and fix them.

# while True:
#     print("Hello")

# The programmer here is trying to convert the string "hello" to "HELLO" by using the upper() method:

# greeting = "hello"
# print(greeting.upper())
# However, the program returns an error. Can you help fix the code, so it prints out HELLO?

# A programmer wrote the following program:

# countries = []
#
# while True:
#     country = input("Enter the country: ")
#     countries.append(country)
#     print(countries)
# However, the code returns an error instead of the expected output. Fix the code, so it produces the expected output.

# The programmer is trying to loop over the buttons list and print out each item with the first letter capitalized. However, the programmer has done something wrong. Try to find and fix the issue.

# buttons = ["cancel", "reply", "submit"]
#
# for i in buttons:
#     print(i.capitalize())

# The programmer is again missing something in the code. Try to find what it is and fix it.

# buttons = ["cancel", "reply", "submit"]
#
# for i in buttons:
#     print(i.capitalize())

# The code below is supposed to print out the items of the list with the first character of each item capitalized. However, the code contains two errors. Try to find and fix the errors.

# for item in ["sandals", "glasses", "trousers"]:
#     print(item.capitalize())

# The programmer is trying to extract and print out 'b' using list indexing, but there is an error. Try to fix it.

# elements = ['a', 'b', 'c']
# print(elements[1])

# The code below aims to replace 'b' with 'x' in the list elements.

# However, the output of the code is still ['a', 'b', 'c'].

# Try to fix the code so 'b' is replaced with 'x'.

# elements = ['a', 'b', 'c']
# new = 'x'
# elements[1] = new
# print(elements)

# i=5
# while i < 10:
#     i+=1
#     print("*")

# for i in range(5, 10):
#     print("*")

# -------------------------------------------------------------------------------

user_prompt = "Enter a todo: "
todos = []

while True:
    user_action = input("Type add, show, or exit:")
    match user_action:
        case "add":
            todo = input(user_prompt)
            todos.append(todo)
        case "show":
            for item in todos:
                print(item)
        case "exit":
            break






