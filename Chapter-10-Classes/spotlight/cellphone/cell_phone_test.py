# This program  tests the cellphone class
import cellphone


def main():
    # get the cellphone data
    model = input('Enter a model: ')
    manufacturer = input('Enter a manufacturer: ')
    retail_price = float(input('Enter a price'))

    phone = cellphone.Cellphone(model, manufacturer, retail_price)

    #   Display the data entered:
    print('The model name you entered was: ' + phone.get_model())
    print('The manufacturer name you entered was: ' + phone.get_manufacturer())
    print('The price is : $' + str(phone.get_retail_price()))


main()
