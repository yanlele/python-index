a = 7


def make_pizza(size, *toppings):
    print('\n披萨的大小为： ' + str(size))
    for topping in toppings:
        print('- ' + topping)