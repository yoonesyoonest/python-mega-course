# Please code this exercise in your computer IDE. For this exercise,
# download the members.txt file attached to the resources. Then, create a program that:
#
# 1. prompts the user to enter a new member.
#
# 2. adds that member to members.txt at the end of the existing members.
# For example, the user here has entered the member Solomon Right.
#
#
# In the above example, Solomon Right will be added to members.txt updating the content of the file to:
#
# John Smith
#
# Sen Lakmi
#
# Sono Octonot
#
# Solomon Right

user_prompt = input("Enter a new member name: ")
members_list = []

file = open("members.txt", "r") # r= read mode
members_list = file.readlines()
file.close()

members_list.append(user_prompt+"\n")

file = open("members.txt", "w") # w= write mode
file.writelines(members_list)
file.close()

print(members_list)

# Open your computer IDE and place the following in a Python file:
#

#
# Then, create a program that:
#
# 1. generates multiple text files by iterating over the filenames list,
#
# 2. and writes the text Hello  inside each generated text file.

# file = open('doc.txt', "w")
# file.writelines('Hello')
# file.close()

# file = open('report.txt', "w")
# file.writelines("Hello")
# file.close()
filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
    file = open(filename, "w")
    file.writelines("Hello Again!")
    file.close()

# Please download the three text files a.txt, b.txt, and c.txt from the resources and place them in your computer IDE.
#
# Then, create a program that:
#
# 1. reads each text file and
#
# 2. prints out the content of each file in the command line.
#
# The expected output would be like the following:

filenames = ['a.txt', 'b.txt', 'c.txt']

for filename in filenames:
    file = open(filename, "r")
    print(file.readline())

# Bug-Fixing Exercise 1: Take a look at the code below:
#
file = open("data.txt", 'w')

file.write("100.12\n")
file.write("111.23")

file.close()
# The code creates a text file which contains the following content:
#
# 100.12111.23
#
# However, the correct content should be:
#
# 100.12
#
# 111.23
#
# Please fix the code so it creates the file with the correct content.

# Bug-Fixing Exercise 2:
# The code below tries to write the string "100.2" to the text file. However,
# there is an error. Try to fix the error.

file = open("data.txt", 'w')
file.write("100.12")
file.close()