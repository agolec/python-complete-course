'''
Running on a particular treadmill will burn 4.2 calories per minute.

Write a program that uses a loop to display the number of calories burned
after 10, 15, 20, 25, and 30 minutes.

pseudocode:
Calculate how many calories are burned on a treadmill after 10 minutes.
Output the amount of calories burned after 10 minutes.
Calculate how many calories are burned on a treadmill after running 15 minutes.
Output the amount of calories burned after 15 minutes.
Calculate how many calories are burned on a treadmill after running 20 minutes.
Output the amount of calories burned after 20 minutes.
Calculate the amount of calories burned after 25 minutes.
Output the amount of calories burned after 25 minutes.
Calculate the amount of calories burned after 30 minutes of running.
Output the amount of calories burned after running for 30 minutes.

Calories burned calories_burned = 4.2 * <integer_number_of_minutes>
'''

CALORIES_BURNED_PER_MINUTE = 4.2

print('Running on a particular treadmill will burn 4.2 calories per minute.')
print('I will calculate how many calories are burned after running for 10, 15, 20, 25, and 30 minutes on this treadmill.')
print('I will print \'Done!\' when I finish.')

for minutes in [10,15,20,25,30]:
    print(format(minutes * CALORIES_BURNED_PER_MINUTE, ',.2f'))
print('Done!')