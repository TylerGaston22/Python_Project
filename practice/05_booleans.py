# 05 - Booleans
# A boolean is either True or False. Note the capital first letter.
# You usually don't print booleans directly - you use them in if statements.

is_student = True
for_sale = True
is_online = True

if is_student:
    print("You are a student")
else:
    print("You are not a student")

if for_sale:
    print("That item is for sale")
else:
    print("That item is not available")

if is_online:
    print("You are online")
else:
    print("You are offline")

# You can still print them if you want to see the value
print(f"Are you a student? {is_student}")

# Flipping a boolean
is_online = False
print(f"Now is_online is {is_online}")
