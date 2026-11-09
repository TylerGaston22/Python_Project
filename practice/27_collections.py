# ==========================================================
# 2D Collections (collections inside of collections)
# ==========================================================


# ----------------------------------------------------------
# Example 1: 2D list built from separate lists
# ----------------------------------------------------------

# fruits     = ["apple", "oranges", "banana", "coconut"]
# vegetables = ["celery", "carrots", "potatoes"]
# meats      = ["chicken", "fish", "turkey"]

# groceries = [fruits, vegetables, meats]

# # groceries[0] is the fruits list, then [1] is "oranges"
# print(groceries[0][1])


# ----------------------------------------------------------
# Example 2: 2D list written inline + nested loop to print it
# ----------------------------------------------------------

# groceries = [["apple", "oranges", "banana", "coconut"],
#              ["celery", "carrots", "potatoes"],
#              ["chicken", "fish", "turkey"]]

# for collection in groceries:
#     for food in collection:
#         print(food, end=" ")
#     print()


# ----------------------------------------------------------
# Example 3: 2D tuple (phone number pad)
# ----------------------------------------------------------

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()
