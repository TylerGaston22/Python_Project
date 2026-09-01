# 10 - if statements
# Run some code ONLY if a condition is true. Otherwise do something else.
# Watch the colon at the end of the line, and the indentation underneath.

age = int(input("Enter your age: "))

if age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet")
else:
    print("You must be 18+ to sign up")


# Comparison operators you can use in a condition:
#   ==  equal to
#   !=  not equal to
#   >   greater than
#   <   less than
#   >=  greater than or equal to
#   <=  less than or equal to

response = input("Would you like food? (Y/N): ")

if response == "Y":
    print("Have some food!")
elif response == "N":
    print("No food for you!")
else:
    print(f"{response} is not a valid response")


# A boolean variable can be the condition all by itself
for_sale = True

if for_sale:
    print("That item is for sale")
else:
    print("That item is not available")
