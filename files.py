# Writing the user's name to "name.txt"
user_name = input("Enter your name: ")
with open("name.txt", "w") as file:
    file.write(user_name)

# Reading the name from "name.txt" and printing it
with open("name.txt", "r") as file:
    name = file.read()
    print(f"Your name is {name}")

# Opening "numbers.txt" and adding the first two numbers
with open("numbers.txt", "r") as file:
    lines = file.readlines()
    if len(lines) >= 2:
        num1 = int(lines[0])
        num2 = int(lines[1])
        result = num1 + num2
        print(f"The result of adding the first two numbers is: {result}")

# Printing the total for all lines in "numbers.txt"
with open("numbers.txt", "r") as file:
    lines = file.readlines()
    total = 0
    for line in lines:
        total += int(line)
    print(f"The total of all numbers in 'numbers.txt' is: {total}")
