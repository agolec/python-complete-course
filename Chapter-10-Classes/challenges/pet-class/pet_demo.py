import pet

def main():
    name = input('Tell me your pets name: ')
    type_of_pet = input('Tell me your pet type')
    is_numeric = False
    while not is_numeric:
        try:
            age = int(input('Tell me your pet age: '))
            is_numeric = True
        except ValueError:
            print('Error. Enter a number.')
    your_pet = pet.Pet(name,type_of_pet,age)

    print('Name of your pet: ' + your_pet.get_name())
    print('Type of pet: ' + your_pet.get_animal_type())
    print('Age of your pet: ' + str(your_pet.get_age()))

main()