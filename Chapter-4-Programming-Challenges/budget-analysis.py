'''
Write a program that asks the user to enter the amount that he or she has 
budgeted for a month.

A loop should then prompt the user to enter each of their expenses for the 
month and keep a RUNNING TOTAL.

When the loop finishes, the program should display the amount the user is over or under budget.

Design considerations: prompt once for total budget allotted.

Unknown number of times user will need to loop through. 
    Can't use Sentinal, as 0 dollars or 999 dollars would be reasonable?
    Ask them to enter Q for quit?
'''
runningTotal = 0
expenseChar = '0'
totalBudgetAllowed = 0
continueLoop = True

print('I will ask you for your budget.')
print('Then I will ask you to enter the value of each of your expenses, or Q to quit.')
print('Then I will add up your expenses and tell you whether you are under or over budget')

print('BEGIN PROGRAM!')

totalBudgetAllowed = float(input('Enter your total budget allowed'))
print('Your total budget allowed is: $' +
      format(totalBudgetAllowed, format(',.2f')))

loopCount = 0
while continueLoop:
    expenseChar = input('Enter expense #' +
                        str(loopCount + 1) + ' for me, or Q to quit.')
    if (expenseChar.isnumeric() == True):
        runningTotal += float(expenseChar)
        loopCount += 1
    elif (expenseChar == 'Q'):
        continueLoop = False

print('I am outside the loop again.')
if (runningTotal > totalBudgetAllowed):
    amountOverBudget = runningTotal - totalBudgetAllowed
    print('total budget allowed is : $' + str(totalBudgetAllowed) + '\n' +
          'Your expenses were outside of/greater than your budget.\n')
    print('Total Expenses were $' + str(runningTotal))
    print('Overbudget by $' + str(amountOverBudget))
elif (runningTotal < totalBudgetAllowed):
    amountUnderBudget = totalBudgetAllowed - runningTotal
    print('total budget allowed is : $' + str(totalBudgetAllowed) + '\n' +
          'Your expenses were within budget.\n')
    print('Total Expenses were $' + str(runningTotal))
    print('Amount under budget is $' + str(amountUnderBudget))
