# collection = single "variable" used to store multiple values
#   List    = [] ordered and changeable. Duplicates OK
#   Set     = {} unordered and unchangeable items, but Add/Remove OK. NO duplicates
#   Tuple   = () ordered and unchangeable. Duplicates OK. FASTER


# ============================================================
# LISTS  []  ordered, changeable, duplicates OK
# ============================================================
print("----- LISTS -----")

fruits = ["apple", "orange", "banana", "coconut"]

print(fruits)                      # ['apple', 'orange', 'banana', 'coconut']
print(fruits[0])                   # apple        (access by index)
print(fruits[-1])                  # coconut      (last item)
print(fruits[1:3])                 # ['orange', 'banana']   (slicing)
print(fruits[::-1])                # reversed copy
print(len(fruits))                 # 4
print("pineapple" in fruits)       # False        (find if something is in a list)

fruits[0] = "pineapple"            # change an item
fruits.append("mango")             # add to the end
fruits.insert(0, "grape")          # add at a specific index
fruits.remove("orange")            # remove by value
fruits.append("banana")            # duplicates are OK
print(fruits)

print(fruits.index("banana"))      # index of the FIRST match
print(fruits.count("banana"))      # 2

fruits.sort()                      # sort alphabetically
print(fruits)
fruits.reverse()                   # reverse the order
print(fruits)

for fruit in fruits:               # loop through a list
    print(fruit)

# fruits.clear()                   # removes everything
# print(dir(fruits))               # see all list methods
# print(help(fruits))              # documentation for lists


# ============================================================
# SETS  {}  unordered, NO duplicates, add/remove OK
# ============================================================
print("\n----- SETS -----")

veggies = {"carrot", "potato", "onion", "carrot"}   # duplicate "carrot" is dropped

print(veggies)                     # order may be different every run!
print(len(veggies))                # 3
print("onion" in veggies)          # True

veggies.add("pepper")              # add an item
veggies.remove("potato")           # remove an item (error if it's not there)
veggies.discard("celery")          # remove an item (NO error if it's not there)
print(veggies)

# print(veggies[0])                # ERROR - sets have no index (unordered)
# print(veggies.count("onion"))    # ERROR - sets have no count() (no duplicates!)

# Handy trick: remove duplicates from a list
numbers = [1, 2, 2, 3, 3, 3]
print(set(numbers))                # {1, 2, 3}

# Set math
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)                       # union        {1, 2, 3, 4, 5}
print(a & b)                       # intersection {3}
print(a - b)                       # difference   {1, 2}

for veggie in veggies:             # loop through a set
    print(veggie)


# ============================================================
# TUPLES  ()  ordered, unchangeable, duplicates OK, FASTER
# ============================================================
print("\n----- TUPLES -----")

colors = ("red", "green", "blue", "red")

print(colors)                      # ('red', 'green', 'blue', 'red')
print(colors[0])                   # red          (access by index)
print(colors[1:3])                 # ('green', 'blue')
print(len(colors))                 # 4
print("blue" in colors)            # True
print(colors.index("green"))       # 1
print(colors.count("red"))         # 2            (duplicates OK)

# colors[0] = "yellow"             # ERROR - tuples can't be changed
# colors.append("yellow")          # ERROR - no append/remove either

# Good for data that should never change, like coordinates
point = (10, 20)
x, y = point                       # "unpacking" a tuple
print(f"x = {x}, y = {y}")

for color in colors:               # loop through a tuple
    print(color)
