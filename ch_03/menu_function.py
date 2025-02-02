def menu(choices, title, prompt):
    print(title)
    print("-----------------------")
    number = 1
    for c in choices:
        print(number, c)
        number = number + 1
    choice = input(prompt)
    answer = choices[int(choice) -1]

    return answer

drinks = ["chocolate", "coffee", "decaf"]
flavors =["caramel", "vanilla", "peppermint", "raspberry", "plain"]
toppings = ["chocolate", "cinnamon", "caramel"]
choice = menu(drinks, "Erik's drinks", "Choose your drink: ")
print(choice)