def main():
    number_of_records = int(input('How many records do you want to enter?'))
    # Open a file for writing.
    employee_file = open('employees.txt', 'w')

    print('Enter the employee name and number for each record.')
    # using the range method to enter data for one whole record.
    for count in range(1, number_of_records + 1):
        employee_name = input(
            'Employee Name for employee #' + str(count) + ':')
        # Add the employee name to the file + a new line.
        employee_file.write(employee_name + '\n')
        # Prompt user to enter employee number and then write employee number by converting it into
        # a string and adding a newline
        employee_number = int(input('Enter an employee number: '))
        employee_file.write(str(employee_number) + '\n')

        employee_department = input('Enter a department: ')
        employee_file.write(employee_department + '\n')

    # close the file.
    print('closing the file.')
    employee_file.close()
    print('Employee names and numbers have been saved as records to the file.')


main()
