
def get_integer_input():
    user_variable = ''
    while True:
        try:
            user_variable = int(input('Enter a numeric value: '))
            return user_variable
        except ValueError:
            print('That was not a valid number. Try again. . .')