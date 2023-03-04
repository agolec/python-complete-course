# this program gets employee data from the user and saves it as records in the employee.txt file.

def main():
    # Get the number of employee records to create.
    number_of_employees = int(
        input('How many employees do you want to create records for?'))

    # Open a file for writing
    employee_file = open('employee.txt', 'w')

    # Get each employee's data and write it to the file.

    for count in range(1, number_of_employees + 1):
        # Get the data for the employee.
        print("Enter the data for employee #", count, sep='')
        name = input('Name: ')
        id_number = input('ID Number')
        department = input('Department: ')

        # Write the data as a record to the file.
        employee_file.write(name + '\n')
        employee_file.write(id_number + '\n')
        employee_file.write(department + '\n')

        print()

    employee_file.close()
    print('Employee records written to file employee.txt.')


main()
