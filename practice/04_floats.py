# 04 - Floats
# "Float" is short for floating-point number.
# It's a number that contains a decimal portion.

price = 10.99
gpa = 3.2
distance = 5.5

print(f"The price is ${price}")
print(f"Your GPA is {gpa}")
print(f"You ran {distance} km")

# Floats work in arithmetic too
subtotal = price * 3
print(f"Three of them cost ${subtotal}")

# Dividing two integers always gives you a float
print(10 / 2)   # 5.0, not 5

# Floats can be rounded
print(round(subtotal, 2))
