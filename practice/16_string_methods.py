#name  = input("Enter your full name: ")
phone_number = input("Enter your phone #: ")

#result = len(name)
# result = name.find(" ") #uses index of zero
# result = name.rfind("o") #finds the last occurabnce 
# name = name.capitalize()
#name = name.upper()
#name = name.lower()
#result = name.isdigit() # is the string all digits?
#result = name.isalpha() # is the string all alphabet characters?
#result = phone_number.count("-") # counts how many times a character shows up in a string
phone_number = phone_number.replace("-", " ") # replace characters


print(phone_number)