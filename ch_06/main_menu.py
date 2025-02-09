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


def get_order():
    order = {}
    order['name'] = input("What's your name: ")
    return order


def print_order(order):
    print(order)
    return


def save_order(order):
    print("Saving order...")
    return

main_menu()

