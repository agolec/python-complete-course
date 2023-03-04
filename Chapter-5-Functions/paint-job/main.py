import paint_job_estimator
total_square_feet_of_job = 0
total_gallons_of_paint_for_job = 0
total_job_hours = 0
total_cost_of_paint = 0
cost_of_paint_per_gallon = 0
total_cost_of_paint_for_job = 0
total_labor_charges = 0
total_cost_of_job = 0

total_square_feet_of_job = int(input(
    'enter the total square footage needed for the job.'))
cost_of_paint_per_gallon = int(
    input('What is the total cost of paint per gallon?'))

total_gallons_of_paint_for_job = paint_job_estimator.calculate_gallons_of_paint_for_job(
    total_square_feet_of_job)

total_job_hours = paint_job_estimator.calculate_job_hours_required(
    total_gallons_of_paint_for_job)

total_cost_of_paint_for_job = paint_job_estimator.calculate_total_cost_of_paint(
    total_gallons_of_paint_for_job, cost_of_paint_per_gallon)

total_labor_charges = paint_job_estimator.calculate_labor_charges(
    total_job_hours)

total_cost_of_job = paint_job_estimator.calculate_total_cost_of_job(
    total_labor_charges, total_cost_of_paint_for_job)
print('\n\n')
print("Your job information is the following. . .")
print('Number of gallons of paint required: ', total_gallons_of_paint_for_job)
print('Hours of labor required: ', total_job_hours)
print('Cost per gallon of paint: $', cost_of_paint_per_gallon)
print('Labor cost for the job: $', total_labor_charges)
print('Cost of the paint for the job: $', total_cost_of_paint_for_job)
print('Total cost of the job is: $', total_cost_of_job)
print('END')
