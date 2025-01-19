# Bug-Fixing Exercise 1
# Have a look at the program below:
#
waiting_list = ["john", "marry"]
name = input("Enter name: ")
try:
    number = waiting_list.index(name)
    print(f"{name}'s turn is {number}")
except ValueError:
     print(f"{name} is not in the list")
# When the user enters the name of one of the waiting_list members,
# the program returns the index of that name.
# For example, when the user enters "john", 0 is printed out.

# If the user enters a name that is not in the list, such as "zen", the program throws an error.

# Change the program, so it prints out "zen is not in the list" instead of returning an error
# when the user enters "zen" or any other name that is not in the list.