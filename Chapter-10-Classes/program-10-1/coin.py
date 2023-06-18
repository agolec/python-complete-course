import random

#   The Coin class simulates a
#   coin that can be flipped.


class Coin:

    # The __init__ method initializes the sideup attribute with the value 'Heads'.
    def __init__(self):
        self.__sideup = 'Heads'
        self.__number_of_tosses = 0

    #   The toss method generates a number (either 0 or 1), and
    #   assigns the sideup attribute with 'Heads' or 'Tails' respectively.
    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    def increment(self):
        self.__number_of_tosses += 1

    def get_sideup(self):
        return self.__sideup

    def get_number_of_tosses(self):
        return self.__number_of_tosses
