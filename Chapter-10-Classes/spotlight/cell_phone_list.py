
from cellphone import cellphone


def main():
    phones = make_list()
    print('Here is the data you entered:')
    display_list(phones)


def make_list():
    # creates an empty list
    phone_list = []

    # add five Cellphone objects to the list.
    print('Enter data for five phones: ')
    for count in range(1, 6):
        manufacturer_name = input('Enter Manufacturer: ')
        model_name = input('Enter model name: ')
        retail_price = float(input('Enter retail price: '))
        print()

        phone = cellphone.Cellphone(
            manufacturer_name, model_name, retail_price)
        phone_list.append(phone)

    return phone_list


def display_list(phone_list):
    for item in phone_list:
        print(item.get_model())
        print(item.get_manufacturer())
        print(item.get_retail_price())
        print()


main()
