DAYS_IN_PROGRAM = 5
daysInput = 0
running_total = 0
totalBugsCollected = 0


print("I will ask you to enter 5 different sets of numbers.")
for days in range (DAYS_IN_PROGRAM):
    daysInput = int(input("Enter the total of bugs collected for day" + str(days + 1)))
    running_total += daysInput
totalBugsCollected = running_total
print('The total number of bugs collected is: ' + str(totalBugsCollected))