import os

# this program allows the user to modify the quantity
# in a record in the coffee.txt file.


def main():
    # Create a bool variable to use as a flag.
    found = False
    print('current working directory: ', os.getcwd())

    # Get the search value and a new quantity value.
    search = input('Enter a description to search for: ')
    new_quantity = int(input('Enter a new quantity: '))

    # Open the original coffee.txt file
    coffee_file = open(
        'coffee.txt', 'r')

    # Open a temporary file.
    temporary_file = open('temp.txt', 'w')

    # Read the first record's description field.
    description = coffee_file.readline()

    while description != '':
        # Read the quantity field.
        quantity = float(coffee_file.readline())

        # strip the \n from the description
        description = description.rstrip('\n')

        # Write either this record to the temporary file
        # or a new record if this is the one that is
        # to be modified.
        if description == search:

            # Write the modified record to the temp file.
            temporary_file.write(description + '\n')
            temporary_file.write(str(new_quantity) + '\n')

            # set the found flag to True
            found = True
        else:
            # Write the original record to the temp file.
            temporary_file.write(description + '\n')
            temporary_file.write(str(quantity) + '\n')

        # Read the next description
        description = coffee_file.readline()

    # Close the coffee.txt file and the temporary file.
    coffee_file.close()
    temporary_file.close()

    # Delete the original coffee.txt file.
    os.remove('coffee.txt')

    # Rename the temp.txt file to coffee.txt
    os.rename('temp.txt', 'coffee.txt')

    # if the search value was found in the original file,
    # display a message.
    if found:
        print('The file was updated.')
    else:
        print('The item was not found in the file.')


# Call main.
main()
