# Bug-Fixing Exercise 1
# The code below tries to write the items of temperatures each in one line in the file.txt list.
# However, the code has an error. Try to fix the error.
#
#
temperatures = [10, 12, 14]
temperatures = [str(tempreture)+"\n" for tempreture in temperatures]
file = open("file.txt", 'w')
file.writelines(temperatures)
#
#
#
# Bug-Fixing Exercise 2
# The code below tries to convert all the numbers to integers.
# However, the code has an error. Try to fix the error.
#
numbers = [10.1, 12.3, 14.7]
numbers = [int(number) for number in numbers]
print(numbers)