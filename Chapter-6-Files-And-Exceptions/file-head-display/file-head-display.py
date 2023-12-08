'''
Write a program that asks the user to enter the name of a file.
The program should then display the first five lines of the record's contents.
If the file contains less than 5 lines, it should display the entire file.
'''

import os


def main():
    try:
        NUMBER_OF_LINES_TO_DISPLAY = 5
        filename = input(
            'Enter the name of a file and I will show the first 5 records of it.')

        currentworkingdirectory = os.getcwd(
        ) + r'\Chapter-6-Files-And-Exceptions\file-head-display' + '\\'

        print('trying to open directory: ' +
              currentworkingdirectory + filename)
        file_path = currentworkingdirectory + filename

        inputfile = open(file_path, 'r')

        line_count = open(file_path, 'r')
        line_count = len(line_count.readlines())

        line = inputfile.readline()
        line = line.rstrip('\n')

        if(line_count > 5):

            for count in range(1, NUMBER_OF_LINES_TO_DISPLAY + 1):
                if not line.isspace():
                    print(line)
                    line = inputfile.readline()
                    line = line.rstrip('\n')
                else:
                    inputfile.readline()
                    continue
        else:
            for count in range(1,line_count + 1):
                if not line.isspace():
                    print(line)
                    line = inputfile.readline()
                    line = line.rstrip('\n')
                else:
                    inputfile.readline()
                    continue
        print('closing file')
        inputfile.close()
    except IOError:
        print("An error occurred trying to read the file.")




main()
