# 02 - Strings
# A string is a series of characters (text).
# A variable is a reusable container for a value.

first_name = "Jon"
food = "pizza"
email = "bro123@fake.com"

# Printing a variable directly (no quotes around the variable name)
print(first_name)

# If you put it in quotes you print the WORD, not the value
print("first_name")  # prints: first_name

# f-strings ("f" for format) let you insert variables into text
# Put the variable inside curly braces {}
print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is {email}")

# Strings can contain numbers, but they are treated as characters
zip_code = "90210"
print(f"Your zip code is {zip_code}")

# Adding strings together is called concatenation
full_name = first_name + " " + "Smith"
print(full_name)
