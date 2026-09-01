# 06 - Type casting
# Type casting is converting a variable from one data type to another.
# The functions: str()  int()  float()  bool()

name = "Jon"
age = 25
gpa = 3.2
is_student = True

# type() tells you the data type of a value or variable
print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(gpa))         # <class 'float'>
print(type(is_student))  # <class 'bool'>

# float -> int (the decimal portion is truncated, not rounded)
gpa_int = int(gpa)
print(gpa_int)  # 3

# int -> float
age_float = float(age)
print(age_float)  # 25.0

# int -> str
age_str = str(age)
print(age_str)        # 25 (looks the same)
print(type(age_str))  # <class 'str'>

# Now that age is a string, "+" concatenates instead of adding
print(age_str + "1")  # 251, not 26

# str -> bool
# Any non-empty string is True. An empty string is False.
print(bool(name))  # True
print(bool("B"))   # True
print(bool(""))    # False  <- useful for checking if the user typed anything
