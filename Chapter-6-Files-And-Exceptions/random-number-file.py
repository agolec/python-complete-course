# Write a program that lets the user determine how many numbers to write to a file.

# For each entry the user said they want, generate a random number between 1-500 and

# write that number to the file.

import random


def main():
    user_entered_quantity_of_numbers = 0
    MINUMUM_RANDOM_NUMBER = 1
    MAXIMUM_RANDOM_NUMBER = 500

    user_entered_quantity_of_numbers = input(
        'How many random numbers do you want to write to the file?')

    random_number_file = open('random_number_file.txt', 'w')

    for numbers in range(1, int(user_entered_quantity_of_numbers) + 1):
        print('writing number #' + str(numbers) + ' to file.')
        random_number_file.write(
            str(random.randint(MINUMUM_RANDOM_NUMBER, MAXIMUM_RANDOM_NUMBER)) + '\n')
    print('closing the file...')
    random_number_file.close()


main()
