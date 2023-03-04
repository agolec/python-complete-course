# this program displays the contents of a file.

def main():
    # get the name of a file.
    filename = input('enter a file name: ')

    try:
        # open the file
        infile = open(filename, 'r')

        # read the file's contents.
        contents = infile.read()

        # Display the file's contents
        print(contents)

        # close the file
        infile.close()

    except IOError:
        print('an error has occurred trying to read')
        print('the file', filename)


main()
