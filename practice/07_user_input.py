# 07 - User input
# input() prompts the user to type something.
# IMPORTANT: input() ALWAYS returns a string, even if you type a number.
# If you need to do math with it, type cast it to int() or float().

name = input("What is your name?: ")
print(f"Hello {name}")

# Type casting the input right away is the cleaner way to do it
age = int(input("How old are you?: "))
age = age + 1
print("Happy birthday!")
print(f"You are {age} years old")


# --- Exercise 1: area of a rectangle ---
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width
print(f"The area is {area}cm²")


# --- Exercise 2: shopping cart ---
item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is ${total}")
