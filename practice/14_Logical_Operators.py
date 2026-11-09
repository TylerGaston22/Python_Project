# 14 - Logical operators
# Logical operators evaluate multiple conditions (or, and, not)
#   or  = at least one condition must be True
#   and = both conditions must be True
#   not = inverts the condition (not False, not True)


# --- Example 1: or ---
# temp = 35
# is_raining = False

# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled")


# --- Example 2: and ---
temp = 20
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT outside")
    print("It is SUNNY")
elif temp <= 0 and is_sunny:
    print("It is COLD outside")
    print("It is SUNNY")
elif temp < 28 and temp > 0 and is_sunny:
    print("It is WARM outside")
    print("It is SUNNY")
