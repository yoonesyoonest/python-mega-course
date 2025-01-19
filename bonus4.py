date = input("Enter today's date: ")
mood = input("How do you rate your mood today from 1 to 10? ")
thoughts = input("Ley your thoughts flow: \n")

with open(f"{date}.txt", "w") as file:
    file.write(mood + 5 * "\n")
    file.write(thoughts)