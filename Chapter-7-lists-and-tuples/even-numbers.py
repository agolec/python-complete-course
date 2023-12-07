def main():
    list_of_numbers = [1,2,3,4,5,6,7,8,9,10]
    print_list(list_of_numbers)
    odd_number_list = filter_out_even_numbers(list_of_numbers)
    print_list(odd_number_list)

def filter_out_even_numbers(origin_list: list[int])-> list[int]:
    desired_list: list[int] = []
    for entry in origin_list:
        if entry % 2 != 0:
            desired_list.append(entry)
    # return desired_list

def print_list(input_list):
    for entry in input_list:
        print(entry)

main()