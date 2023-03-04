# this program reads the contents of text file 'philosophers.txt' in 'r' read mode and
# initializes line1, line2, and line3 variables with one line each from the file.
# it then prints out the variables line1, line2, and line3.
def main():
    aninputfile = open('philosophers.txt', 'r')

    # Read the first line from the file but don't do anything with it yet.
    line = stripnewline(aninputfile)

    # Check whether that line variable is an empty string.
    # If it is not, print the value and then read the next line, and evaluate whether line != '' again.
    while line != '':
        print(line)
        line = stripnewline(aninputfile)


def stripnewline(inputfile):
    return inputfile.readline().rstrip('\n')


# call main method
main()
