"""
The distance a vehicle travels over time can be expressed in the fillowing equation:

                    Distance = average speed x time

Ex: If a train travels 40 mph for three hours, the distance traveled over three hours is 120 miles total.

Write a program that asks the user for the speed of a vehicle (in miles per hour) and the number of hours it has traveled.

Input:  Speed of vehicle.
        Distance vehicle has traveled.

The program should then use a loop to display a table of all the distance it has traveled each hour of the
entire trip duration.

Ex:

[output] What is the speed of the vehicle in MPH? [input] 40 [ENTER]
[output] How many hours has it traveled? [input] 3 [ENTER]

Hour                Distance Traveled
-------------------------------------
1                   40
2                   80
3                  120

"""

"""
pseudocode:
print "What is the speed of the vehicle?"
input the vehicle speed
print "What is the duration of the trip?"
input the trip length/duration in hours.
PRINT TABLE HEADER
LOOP OVER EACH HOUR.
FOR EACH LOOP, PRINT HOUR NUMBER, THEN DISTANCE TRAVELED.

"""
print("START PROGRAM\n\n")
hoursTraveled = 0
speedOfVehicle = 0
NUMBER_TO_START_LOOP = 1
INCREMENT = 1


# Input hoursTraveled
hoursTraveled = int(input("Enter the number of hours traveled"))
# Pad output with two new lines.
print('\n\n')

# Input speedOfVehicle
speedOfVehicle = int(input("Enter the speed of the vehicle"))
# Pad output with two new lines.
print('\n\n')

"""
use a for loop with a range function to iterate over each hour traveled.

hourVehicleTraveled starts at 1 and implicitly iterates (++), so the next time
the loop executes, it's value is 2, etc.

in range, we're designating the number to start the range at as NUMBER_TO_START_LOOP, 
and the number to end the range at, as hoursTraveled + 1, since the end value is exclusive 
(will stop at n-1 of the user's input for hoursTraveled).

"""
print("Hour\t\t\tDistance Traveled")
for hourVehicleTraveled in range(NUMBER_TO_START_LOOP, hoursTraveled + 1):
    print(str(hourVehicleTraveled), '\t\t\t', str(
        hourVehicleTraveled * speedOfVehicle))
print("\n\nEND OF THE MPH PROGRAM")
