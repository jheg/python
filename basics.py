# Lesson 1 Introduction to Python
users_name = input("What's your name? ").strip()
print(f"Hello, {users_name}!")

# Lesson 2 Basic Operations and Control Flow
users_age = int(input("How old are you? "))
if users_age < 18:
    print("You are underage")
elif 18 <= users_age <= 65:
    print("You are an adult.")      
else:
    print("You are a senior citizen")

# Lesson 3 Loops
number_to_multiply = int(input("What number do you want to see the 10 times table for? "))

for number in range(1,11):
    print(f"{number} * {number_to_multiply} = {number * number_to_multiply}")

# Lesson 4 Functions
def calculate_average(my_numbers):
    total = sum(my_numbers)
    count = len(my_numbers)
    average = total / count
    return average

result = calculate_average([234, 23, 234, 56, 44, 12, 1, 99])
print(result)

# Lesson 5 Lists
fruits = ["apple", "banana", "cherry", "date"]
fruits.append("elderberry")

fruits.insert(2,"grape")

fruits.remove("cherry")
print(fruits)

# Lesson 6 While Loops
your_number = int(input("Enter a number ").strip())

while your_number >= 0:
    your_number = int(input("Enter a number ").strip())

print("You have finished the lesson!")

# visitors_name = input('please tell us your name ')
# print(f"Hello {visitors_name}")

# Lesson 7: Functions (Part 2)
def calculate_power(base, exponent):
    result = base ** exponent
    print(result)

calculate_power(2,3)

# Lesson 8: Lists
numbers = [1,2,3]
print(numbers[1])
numbers[0] = 4
numbers.append(5)
print(numbers)
