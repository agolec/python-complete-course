'''
For every 112 square feet of wall space, one gallon of paint and eight hours of labor are needed.

A company charges $35 per hour of labor.

Write a program that asks the user to enter the number of square feet of wall space to be painted and

and the price of paint per gallon.

the program should output the following: 

The number of gallons of paint required.

The hours of labor required.

The cost of the paint.

The labor charges.

The total cost of the paint job.
'''

# calculate_gallons_of_paint_for_job takes in the total_wall_space parameter provided elsewhere
# in the code and uses that to return the value of the calculation total_wall_space divided by
# the 112 constant that is meant to represent the number of square feet one gallon of paint can cover.


def calculate_gallons_of_paint_for_job(total_wall_space):
    # constant for the square footage a company has determined one
    # gallon of paint can cover
    SQUARE_FOOTAGE_OF_WALL_SPACE_PER_GALLON_OF_PAINT = 112
    return total_wall_space / SQUARE_FOOTAGE_OF_WALL_SPACE_PER_GALLON_OF_PAINT

# calculate_total_job_hours takes in the gallons_of_paint_necessary argument and
# returns the value of that variable, multiplied by 8, which is how many hours
# it takes a worker to use one gallon of paint.


def calculate_job_hours_required(gallons_of_paint_necessary):
    # constant for hours of labor per gallon of paint used in job.
    HOURS_OF_LABOR_PER_GALLON_OF_PAINT = 8
    return gallons_of_paint_necessary * HOURS_OF_LABOR_PER_GALLON_OF_PAINT


def calculate_total_cost_of_paint(total_gallons_of_paint, price_of_paint_per_gallon):
    return total_gallons_of_paint * price_of_paint_per_gallon


def calculate_labor_charges(total_job_hours):
    COMPANY_PAINT_LABOR_HOURLY_RATE = 35
    return total_job_hours * COMPANY_PAINT_LABOR_HOURLY_RATE


def calculate_total_cost_of_job(labor_charges, total_paint_cost):
    return labor_charges + total_paint_cost
