# Write a program that asks the user to enter the name of a file.

# The program should then display the first five lines of the record's contents.

# If the file contains less than 5 lines, it should display the entire file.

import os


def main():
    try:
        number_of_lines_to_display = 5
        filename = input(
            'Enter the name of a file and I will show the first 5 records of it.')

        currentworkingdirectory = os.getcwd(
        ) + r'\Chapter-6-Files-And-Exceptions\file-head-display' + '\\'

        print('trying to open directory: ' +
              currentworkingdirectory + filename)

        inputfile = open(currentworkingdirectory + filename, 'r')

        line = inputfile.readline()
        line = line.rstrip('\n')

        for count in range(1, number_of_lines_to_display + 1):
            if line != '':
                print(line)
                line = inputfile.readline()
                line = line.rstrip('\n')
            else:
                break
    except IOError:
        print("An error occurred trying to read the file.")
    print('closing file')
    inputfile.close()


main()
