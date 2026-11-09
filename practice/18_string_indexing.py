# 18 - String indexing
# Indexing = accessing elements of a sequence using [] (indexing operator)
#   [start : end : step]

credit_number = "1234-5678-9012-3456"

# print(credit_number[0])
# print(credit_number[0:4])     # if you leave out the 0, Python assumes the starting position is 0
# print(credit_number[5:9])
# print(credit_number[5:])      # if you leave out the end, Python assumes you want everything until the end of the string
# print(credit_number[-1])      # starts from the end of the string
# print(credit_number[::3])     # step counts every 3 characters here
credit_number = credit_number[::-1]   # this will print the number backwards

# last_digits = credit_number[-4:]
# print(f"XXXX-XXXX-XXXX-{last_digits}")

print(credit_number)
