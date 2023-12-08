from random import randint

def main():
    number_input = ''
    SIZE_OF_LIST = ''
    number_list = []
    number_input = get_integer_input()
    SIZE_OF_LIST = enter_list_size()
    number_list = generate_random_numbers(SIZE_OF_LIST)
    display_larger_than_n(number_list,number_input)
    
def enter_list_size():
    size_variable = 0
    print('please enter size of list: ')
    size_variable = get_integer_input()
    return size_variable

def get_integer_input():
    user_variable = ''
    while True:
        try:
            user_variable = int(input('Enter a numeric value: '))
            return user_variable
        except ValueError:
            print('That was not a valid number. Try again. . .')
    
    
def generate_random_numbers(LIST_SIZE):
    numbers = []
    index = 0
    while index < LIST_SIZE:
        numbers.insert(index,randint(1,100))
        index += 1
    return numbers


def display_larger_than_n(number_list,user_number):
    output_list = []
    print('printing numbers larger than ' + str(user_number))
    string_of_numbers_larger_than_user_input = ''
    for number in number_list:
        if number > user_number:
            output_list.insert(number,str(number))
    print('original list is: ' + str(number_list))
    print('\n')
    print('now displaying all numbers larger in list: \n')
    print(str(output_list))


main()
