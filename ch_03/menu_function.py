def menu(choices, title="Andrey's Menu", prompt="Choose your item: "):
    print(title)
    print(len(title) * '-')
    number = 1
    for c in choices:
        print(number, c)
        number = number + 1
    choice = input(prompt)
    answer = choices[int(choice) -1]

    return answer

drinks = ["chocolate", "coffee", "decaf"]
flavors = ["caramel", "vanilla", "peppermint", "raspberry", "plain"]
toppings = ["chocolate", "cinnamon", "caramel"]
drink = menu(drinks)
flavor = menu(flavors, "Andrey's flavors", "Choose your flavor: ")
topping = menu(toppings, "Andrey's toppings", "Choose your topping: ")

print("Here is your order: ")
print("Main product: ", drink)
print("Flavor: ", flavor)
print("Topping: ", topping)
print("Thanks for your order!")
