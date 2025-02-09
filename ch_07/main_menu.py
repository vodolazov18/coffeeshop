def main_menu():
    while True:
        order = get_order()
        print("Check your order:")
        print_order(order)
        confirm = input("Confirm? Press 'Yes' to confirm, 'No' to cancel: ")
        if confirm == 'Yes' or confirm == 'yes':
            save_order(order)
            print("Thanks for your order:")
            print_order(order)
        else:
            continue


def menu(choices, title="Andrey's Menu", prompt="Choose your item: "):
    print(title)
    print(len(title) * '-')
    number = 1
    for c in choices:
        print(number, c)
        number = number + 1
    while True:
        choice = input(prompt)
        allowed_answers = []
        for a in range(1, len(choices) + 1):
            allowed_answers.append(str(a))

        allowed_answers.append('X')
        allowed_answers.append('x')

        if choice in allowed_answers:
            if choice == 'X' or choice == 'x':
                answer = ''
                break
            else:
                answer = choices[int(choice) - 1]
                break
        else:
            print("Enter number from 1 to", len(choices))
            answer = ''

    return answer


def read_menu(filename):
    with open(filename) as file:
        temp = file.readlines()
        result = []
        for item in temp:
            new_item = item.strip()
            result.append(new_item)
    return result


def get_order():
    order = {}
    order['name'] = input("What's your name: ")
    drinks = read_menu("drinks.txt")
    flavors = read_menu("flavors.txt")
    toppings = read_menu("toppings.txt")
    order["drink"] = menu(drinks, "Andrey's drinks", "Choose your drink: ")
    order["flavor"] = menu(flavors, "Andrey's flavors", "Choose your flavors: ")
    order["toppings"] = menu(toppings, "Andrey's toppings", "Choose your toppings: ")
    return order


def print_order(order):
    print("Here is your order, ", order["name"])
    print("Main product: ", order["drink"])
    print("Flavor: ", order["flavor"])
    print("Toppings: ", order["toppings"])
    print("Thanks for your order!")
    return


def save_order(order):
    print("Saving order...")
    return

main_menu()
