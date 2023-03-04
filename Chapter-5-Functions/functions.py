import random


def main():
    # get a random number from 1-10 and generate it.
    number = random.randint(1, 10)
    # Display the number
    print('the number is', number)


def end():
    print('END')


# Call the function
for iteratable in range(1, 10):
    main()
