sales_for_week = []
DAYS_IN_WEEK = 7
sales_for_day = 0
total_sales = 0
positive_input = True


print("Enter the number of sales for the week")
for day in range(DAYS_IN_WEEK):
    sales_for_day = int(input("Enter sales for day " + str(day + 1) + ": "))
    if(sales_for_day < 0):
        positive_input = False
    while not positive_input:
        sales_for_day = int(input("Invalid input. sales for the day cannot be negative. Re-enter sales for day " + str(day +1) + ": "))
        if(sales_for_day >= 0):
            positive_input = True
    else:
        sales_for_week.append(sales_for_day)

print("sales total being calculated. . .")
for sales_for_day in range(DAYS_IN_WEEK):
    total_sales += sales_for_week[sales_for_day]
    print("day :" + str(sales_for_day + 1) + ": " + str(total_sales))
print("total sales for week are $" + str(total_sales))



