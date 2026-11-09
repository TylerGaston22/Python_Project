# 19 - Format specifiers
# {value:flags} formats a value based on what flags are inserted

price1 = 3000000000.14159
price2 = -9870.65
price3 = 1200.34

print(f"Price 1 is ${price1:,.2f}")
print(f"Price 2 is ${price2:,}")
print(f"Price 3 is ${price3:,}")


# --- Notes ---
# .2f   - decimal places for a floating point number
# 10    - spaces before the value
# 010   - zero pads the numbers
# <10   - left justifies a value and puts the space after
# >10   - right justified (default)
# ^10   - centers the numbers
# +     - precedes numbers with their positive or negative sign
#       - a single space puts a space before positive numbers
# ,     - a thousands separator
# ,.2f  - thousands separator with 2 decimal places
#
# You can add any combination of these flags
