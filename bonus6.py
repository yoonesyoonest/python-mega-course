try:
    width = float(input("Enter rectangle width: "))
    height = float(input("Enter rectangle height: "))

    if width == height:
        exit("That looks like a square.")
    area = width * height
    print("Area of rectangle is: ", area)
except ValueError:
    print("Please enter numeric values")