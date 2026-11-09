# 20 - while loops
# Execute some code WHILE some condition remains true.


# --- Example 1: keep asking until a name is entered ---
# name = input("Enter your name: ")
# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name: ")
# print(f"Hello {name}")


# --- Example 2: keep going until the user types q ---
# food = input("Enter a food you like (q to quit): ")
# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food you like (q to quit): ")
# print("bye")


# --- Example 3: keep asking until the number is in range ---
num = int(input("Enter a # between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10: "))

print(f"Your number is {num}")
