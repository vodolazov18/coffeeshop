drinks = ["chocolate", "coffee", "decaf"]
flavors =["caramel", "vanilla", "peppermint", "raspberry", "plain"]
toppings = ["chocolate", "cinnamon", "caramel"]

print("Andrey's Coffee Shop drinks")

print("---------------------------")
number = 1
for d in drinks:
    print(number, d)
    number = number + 1
drink = input("Choose your drink: ")

print("Andrey's Coffee Shop flavors")
print("----------------------------")
number = 1
for f in flavors:
    print(number, f)
    number = number + 1
flavor = input("Choose your flavor: ")

print("Andrey's Coffee Shop toppings")
print("-----------------------------")
number = 1
for t in toppings:
    print(number, t)
    number = number + 1
topping = input("Choose your topping: ")

print("Here is your order: ")
print("Main product: ", drinks[int(drink) - 1])
print("Flavor: ", flavors[int(flavor) - 1])
print("Topping: ", toppings[int(topping) - 1])
print("Thanks for your order!")

