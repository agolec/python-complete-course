import random

def main():
    TOTAL_DIGITS = 7
    lottery_numbers = [0] * TOTAL_DIGITS
    print("This program will generate a seven digit lottery number.")
    generate_lottery_numbers(lottery_numbers)
    display_lottery_numbers(lottery_numbers)
    print("END PROGRAM")

def generate_lottery_numbers(lottery_numbers):
    for number in range(len(lottery_numbers)):
        lottery_numbers[number] = random.randint(0,9)

def display_lottery_numbers(lottery_numbers):
    print('We are printing the list. . .\n')
    if(not len(lottery_numbers)):
        print("list is empty")
    else: 
        index = 0
        LIST_LENGTH = len(lottery_numbers)
        lottery_number_display = ''
        while index < LIST_LENGTH:
            if not (index == LIST_LENGTH - 1):
                lottery_number_display += (str(lottery_numbers[index]) + " ")
            else:
                lottery_number_display += (str(lottery_numbers[index]))
            index += 1
        print(lottery_number_display)
main()