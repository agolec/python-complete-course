
def main():
    start_program()
    user_number = float(input('Enter a number and I will multiply it be 10: '))
    print(times_ten(user_number))
    end_program()
    
def times_ten(input):
    return input * 10

def start_program():
    print("START")
def end_program():
    print("END")

main()
