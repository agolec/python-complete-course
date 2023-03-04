'''
Write a function named 'max' that accepts two intergers as arguments and returns the value that is the
greater of the two values.

for example if the user enters 2 and 5, they tell which of the two is larger.
'''


def print_max_number(firstNumber, secondNumber):
    if (firstNumber > secondNumber):
        return ('first number, ', str(firstNumber), ' is > than second number, ', str(secondNumber), '.')
    elif (secondNumber > firstNumber):
        return ('second number, ', str(secondNumber), ' is > than second number, ', str(firstNumber), '.')
    else:
        return ('both numbers are equal. ', str(firstNumber), ' is = to ', str(secondNumber))


userValueOne = 0
userValueTwo = 0

continueLoop = 'y'


while continueLoop == 'y' or continueLoop == 'Y':
    userValueOne = int(input('Enter first number:'))
    userValueTwo = int(input('Enter a second number:'))
    print(print_max_number(userValueOne, userValueTwo))

    continueLoop = str(input('Continue loop? Y/y'))
