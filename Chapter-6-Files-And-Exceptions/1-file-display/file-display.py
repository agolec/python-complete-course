def read_file_line(open_file):
    for line in open_file:
        line = line.rstrip('\n')
        print(line)

def main():
    file_directory = r"python-complete-course\Chapter-6-Files-And-Exceptions\1-file-display\numbers.txt"
    try:
        number_file = open(file_directory,'r')
        read_file_line(number_file)
    except FileNotFoundError:
        print('Error. Unable to open file; File not Found.')
    

main()
