# 24 - Nested loops
# A loop within another loop (outer, inner)
#   outer loop:
#       inner loop:


# --- Example 1: print 1-9 three times ---
# for x in range(3):
#     for y in range(1, 10):
#         print(y, end="")
#     print()


# --- Example 2: draw a rectangle of symbols ---
rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()
