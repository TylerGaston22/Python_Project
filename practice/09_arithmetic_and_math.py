# 09 - Arithmetic operators and math functions
import math

# --- Arithmetic operators ---
friends = 10

print(friends + 2)   # addition
print(friends - 2)   # subtraction
print(friends * 2)   # multiplication
print(friends / 2)   # division (always gives a float)
print(friends ** 2)  # exponent (10 to the power of 2)
print(friends % 3)   # modulus = the remainder of a division

# --- Augmented assignment operators (shorthand) ---
friends += 1   # same as: friends = friends + 1
friends -= 1
friends *= 2
friends /= 2
friends **= 2
print(friends)

# Modulus is often used to check if a number is even or odd
number = 7
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")


# --- Built-in math functions ---
x = 3.14
y = -4
z = 5

print(round(x))        # 3    round to the nearest whole number
print(abs(y))          # 4    absolute value (distance from zero)
print(pow(4, 3))       # 64   base to the power of an exponent
print(max(x, y, z))    # 5    largest value
print(min(x, y, z))    # -4   smallest value


# --- The math module ---
print(math.pi)         # 3.141592653589793
print(math.e)          # 2.718281828459045
print(math.sqrt(9))    # 3.0  square root
print(math.ceil(9.1))  # 10   always rounds UP
print(math.floor(9.9)) # 9    always rounds DOWN


# --- Exercise 1: circumference of a circle ---
radius = float(input("Enter the radius of a circle: "))
circumference = 2 * math.pi * radius
print(f"The circumference is {round(circumference, 2)}cm")


# --- Exercise 2: area of a circle ---
area = math.pi * pow(radius, 2)
print(f"The area of the circle is {round(area, 2)}cm²")


# --- Exercise 3: hypotenuse of a right triangle ---
# c = square root of (a squared + b squared)
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Side C = {c}")
