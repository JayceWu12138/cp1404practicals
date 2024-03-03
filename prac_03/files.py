# 1.
name = input("Enter your name: ")
with open('name.txt', 'w') as file:
    file.write(name)

# 2.
with open('name.txt', 'r') as file:
    name_read = file.read()
print(f"Your name is {name_read}")

# 3.
with open('numbers.txt', 'r') as file:
    first_number = int(file.readline())
    second_number = int(file.readline())
print(first_number + second_number)

# 4.
total = 0
with open('numbers.txt', 'r') as file:
    for line in file:
        total = total + int(line)
print(total)
