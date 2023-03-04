"""

Write a program asking the user to enter a number in the range of 1-7.

The program should display the corresponding day of the week.

KEY: 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, 7 = Sunday

The program should display an error message if the user enters a number outside the range.

PSEUDOCODE:

    print prompt asking user for number
    user inputs number
    program runs through if conditions for statement
    program outputs the day of the week, or error.
    program ends.

"""

user_input_month = 0

user_input_month = int(input(
    "Enter a number 1-7 and I will tell you the day of the week that corresponds to."))

if user_input_month == 1:
    print('Monday')
elif user_input_month == 2:
    print('Tuesday')
elif user_input_month == 3:
    print('Wednesday')
elif user_input_month == 4:
    print('Thursday')
elif user_input_month == 5:
    print('Friday')
elif user_input_month == 6:
    print('Saturday')
elif user_input_month == 7:
    print('Sunday')
else:
    print('Wrong input for day of the week')
