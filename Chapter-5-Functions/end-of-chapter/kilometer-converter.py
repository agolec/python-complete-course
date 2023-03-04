def convertToMiles(kilometers):
    return format(kilometers * 0.6214, ',.2f')


user_input_for_kilometers = 0

while user_input_for_kilometers == 0:
    user_input_for_kilometers = float(
        input('Enter a kilometer numeric value: '))
    if user_input_for_kilometers > 0:
        print('Error. value is 0 or negative.')

print('Kilometer value is: ', str(user_input_for_kilometers))
print('Miles value is: ', str(convertToMiles(user_input_for_kilometers)))
