def main():
    try:
        # get the number of hours worked.
        hours = int(input('how many hours did you worked? '))

        # Get the hourly pay rate.
        pay_rate = float(input('Enter your hourly pay rate: '))

        # Calculate the gross pay.
        gross_pay = hours * pay_rate

        # Display the gross pay
        print('Gross pay: $', format(gross_pay, ',.2f', sep=''))
    except ValueError:
        print('Error: Hours worked and hourly pay rate must be numeric values')
        print('Do not enter string text values.')


main()
