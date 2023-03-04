"""
Write a program that displays a table of Celcius temperatures.

Starting from 0 degrees Celsius through 20 and write 
their Fahrenheit equivalents.

Formula for converting Celsius to Fahrenheit: F = ((9/5) * C) + 32
"""
STARTING_CELSIUS_TEMP = 0
ENDING_CELSIUS_TEMP = 21
FORMAT_TWO_DECIMALS = ',.2f'

print('~~~Celcius~~~\t\t\t~~~Fahrenheit~~~')
for temperature in range(STARTING_CELSIUS_TEMP, ENDING_CELSIUS_TEMP):
    fahrenheitConversion = ((9/5) * temperature) + 32
    print(temperature, '\t\t\t', format(
        fahrenheitConversion, FORMAT_TWO_DECIMALS))
