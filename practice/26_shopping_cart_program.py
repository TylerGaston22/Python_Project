# Shopping cart program

foods = []
prices =[]
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q": #makes the input lower case. so Q will quit also
        break
    else:
        price = float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")

for food in foods:
    print(food, end=" ")

    for price in prices:
        total += price
        
print()
print(f"Your total is: ${total}")

