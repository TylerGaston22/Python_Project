# for loops = execute a block of code a fixed number of times.
 #            You can iterate over a range, string, sequence, etc.






# credit_card = "1234-5678-9012-3456"
# for x in credit_card:             #can add reverse function, can do , range function
#     print(x)


for x in range (1, 21):             #this works for skipping over a number, can also break instead of continue
    if x == 13:
        continue
    else:
        print(x)