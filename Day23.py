# Congratulations on coming this far! That is a BIG achievement!
#
#
# Throughout the next few days, we will gradually migrate from coding exercises
# to a new type of activity - projects.
# Projects will require you to code longer scripts.
# Projects will finally replace coding exercises on Day 20. Today,
# we will have a coding exercise that looks more like a (small) project.
# Please read the instructions below.
#
#
#
# Coding Exercise 1
# Your task is to create a program that generates a random whole number.
# Here is how the program should behave:
#
# Output
# Enter the lower bound: 1
# Enter the upper bound: 10
# >>> 7
# As you can see, the program first asks the user to enter a whole number.
# Then, once the user enters a number,
# the program asks the user again to enter another number.
#
# Then, the program returns a random number that falls between the two whole numbers.
# Here is another example:
#
# Output
# Enter the lower bound: 12
# Enter the upper bound: 15
# >>> 14
#
# Note: To create this program, you might need to do some internet research or use the Python module
# index to find out what module and what function of that module you can use to generate
# random numbers.
# While it is easy for me to provide some clues here on what module you should use,
# searching for information and becoming familiar with programming community sites
# such as Stackoverflow is part of the programming skillset you should acquire.
# Thus, it is essential to practice such skills as well
# so you are independent after you finish the course.

import random

num1 = int(input("Enter the lower bound: "))
num2 = int(input("Enter the upper bound: "))

random_num = random.randint(num1, num2)
print(random_num)

# Bug-Fixing Exercise 1
# Please have a look at the following scripts:
#
# parsers.py
#
# def parse(user_input):
#     """Extract the values split by a comma in a string
#     and return the two values via a dictionary.
#     """
#     # Get the two values in a list
#     parts = user_input.split(" ")
#
#     # Store the two values in variables
#     lower_bound = float(parts[0])
#     upper_bound = float(parts[1])
#
#     # Inject the values in a dictionary
#     return {"lower_bound": lower_bound, "upper_bound": upper_bound}
#
#
# main.py
#
# from parsers import parse
# import random
#
# # Ask the user to enter a lower and an upper bound divided by a comma
# user_input = input("Enter a lower bound and an uppwer bound divided a comma (e.g., 2,10)")
#
# # Parse the user string by calling the parse function
# parsed = parse(user_input)
#
# # Pick a random int between the two numbers
# rand = random.randint(parsed['lower_bound'], parsed['upper_bound'])
#
# print(rand)
# When the user executes main.py file, an error is produced.
# Place the two files in your IDE and try to debug the program.


