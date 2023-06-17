import coin


def main():
    # Create an object of the coin class.
    # since we stored this in a module,

    # we need to quantify the Coin class by
    # calling it's module name, lowercase 'coin',
    # following with the . notation, and then upper case Coin(), the class name.
    first_coin = coin.Coin()
    print('This side is up after creation: ', first_coin.get_sideup())

    while (first_coin.get_sideup() == 'Heads'):
        first_coin.toss()
        first_coin.increment()
    print('This side up after while loop: ', first_coin.get_sideup())
    print('It took', first_coin.get_number_of_tosses(), " tosses.")


main()
