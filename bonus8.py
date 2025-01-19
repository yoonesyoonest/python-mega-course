# def calc_sum(numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     return sum
#
# def calc_len(items):
#     count = 0
#     for item in items:
#         count = count + 1
#     return count

def get_average():
    with open("tempratures.txt", "r") as file:
        data = file.readlines()

    # print(data)
    data = data[1:]
    data = [float(i) for i in data]
    # print(data)
    average = sum(data) / len(data)
    return average

average = get_average()
print(average)