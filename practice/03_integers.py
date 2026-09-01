# 03 - Integers
# An integer is a whole number. No decimal portion.
# Do NOT put them in quotes, or they become strings.

age = 25
quantity = 3
num_of_students = 30

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

# Integers can be used in arithmetic expressions (strings can't)
next_year = age + 1
print(f"Next year you will be {next_year}")

total_desks = num_of_students * 1
print(f"You need {total_desks} desks")

# Notice the difference:
print(25 + 1)      # 26   <- integer math
print("25" + "1")  # 251  <- string concatenation
