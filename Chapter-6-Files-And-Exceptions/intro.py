READ_MODE = 'r'
WRITE_MODE = 'w'
OPEN_FILE = 'a'

# this program writes three lines of data to a file.


def main():
    # open a file named 'Philosopers.txt'.
    outfile = open('philosophers.txt', WRITE_MODE)

    # Write the names of three philosophers to the file
    outfile.write('Rene Decartes' + '\n')
    outfile.write('Plato\n')
    outfile.write('Edmund Burke\n')

    outfile.close()


# Call the main function.
main()
