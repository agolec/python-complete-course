# simulate dice roll of two die.
import random
# Constants for the minimum and maximum random numbers
MINIMUM_DICE_NUMBER = 1
MAXIMUM_DICE_NUMBER = 20


def main():
    # Create a variable to control the loop
    again = 'y'

    # simulate the rolling of a dice.
    while again == 'y' or again == 'Y':
        print('Rolling the dice . . .')
        print('Their values are. . .:')
        print(random.randint(MINIMUM_DICE_NUMBER, MAXIMUM_DICE_NUMBER))
        print(random.randint(MINIMUM_DICE_NUMBER, MAXIMUM_DICE_NUMBER))

        # Ask if they want to roll another dice.
        again = input('Roll the dice again? (y = yes):')


# Call the main function
main()
