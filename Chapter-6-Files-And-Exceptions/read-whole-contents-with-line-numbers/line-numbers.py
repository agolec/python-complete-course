# Write a program that asks the user to enter the name of a file.

# The program should then display the first five lines of the record's contents.

# If the file contains less than 5 lines, it should display the entire file.

import os


def main():
    try:
        filename = input(
            'Enter the name of a file and I will prefix the line number and a colon, followed by the contents')

        currentworkingdirectory = os.getcwd(
        ) + r'\Chapter-6-Files-And-Exceptions\read-whole-contents-with-line-numbers' + '\\'

        print('trying to open directory: ' +
              currentworkingdirectory + filename)

        inputfile = open(currentworkingdirectory + filename, 'r')

        line = inputfile.readline()
        line = line.rstrip('\n')

        count = 0
        while line != '':
            count = count+1
            print(count, ' : ', line)
            line = inputfile.readline()
            line = line.rstrip('\n')
        else:
            print('file done being read?')
        print('closing file')
        inputfile.close()
    except IOError:
        print("An error occurred trying to read the file.")


main()
