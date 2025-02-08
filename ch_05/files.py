# После работы с файлом его нужно закрыть, чтобы освободить ресурсы.
# Используем конструкцию with
def read_menu(filename):
    with open(filename) as file:
        temp = file.readlines()
        result = []
        for item in temp:
            new_item = item.strip()
            result.append(new_item)

    return result

drinks = read_menu("drinks.txt")
print(drinks)
flavors = read_menu("flavors.txt")
print(flavors)
toppings = read_menu("toppings.txt")
print(toppings)