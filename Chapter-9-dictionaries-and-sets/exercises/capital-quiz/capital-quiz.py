'''
Write a program that creates a dictionary using the countries as keys
and their capitals of those countries as values.

The program should randomly quiz the user by displaying the name of a country,

and asking them to enter the capital.

The program should keep track of the number of correct and incorrect responses.
'''
import random 

def main():
    countries_dictionary = set_countries_and_capitals_dictionary()
    number_of_questions = set_number_of_questions()
    display_quiz_question(countries_dictionary,number_of_questions)
    
def set_countries_and_capitals_dictionary():
    countries_and_capitals = {
    'Afghanistan': 'Kabul',
    'Albania': 'Tirana',
    'Algeria': 'Algiers',
    'Andorra': 'Andorra la Vella',
    'Angola': 'Luanda',
    'Argentina': 'Buenos Aires',
    'Armenia': 'Yerevan',
    'Australia': 'Canberra',
    'Austria': 'Vienna',
    'Bangladesh': 'Dhaka',
    'Belgium': 'Brussels',
    'Brazil': 'Brasília',
    'Canada': 'Ottawa',
    'China': 'Beijing',
    'Colombia': 'Bogotá',
    'Czech Republic': 'Prague',
    'Denmark': 'Copenhagen',
    'Egypt': 'Cairo',
    'Finland': 'Helsinki',
    'France': 'Paris',
    'Germany': 'Berlin',
    'Greece': 'Athens',
    'India': 'New Delhi',
    'Indonesia': 'Jakarta',
    'Iran': 'Tehran',
    'Iraq': 'Baghdad',
    'Italy': 'Rome',
    'Japan': 'Tokyo',
    'Mexico': 'Mexico City',
    'Netherlands': 'Amsterdam',
    'Nigeria': 'Abuja',
    'Norway': 'Oslo',
    'Pakistan': 'Islamabad',
    'Peru': 'Lima',
    'Philippines': 'Manila',
    'Poland': 'Warsaw',
    'Russia': 'Moscow',
    'Saudi Arabia': 'Riyadh',
    'South Africa': 'Pretoria',
    'South Korea': 'Seoul',
    'Spain': 'Madrid',
    'Sweden': 'Stockholm',
    'Switzerland': 'Bern',
    'Turkey': 'Ankara',
    'United Kingdom': 'London',
    'United States': 'Washington, D.C.'}
    return countries_and_capitals

def set_number_of_questions():
    NUMBER_OF_QUESTIONS_PROMPT = 'Enter the number of questions you want to be quizzed on: '
    number_of_questions = ''
    while True:
        try:
            number_of_questions = int(input(NUMBER_OF_QUESTIONS_PROMPT))
            return number_of_questions
        except ValueError:
            print('ERROR. Unable to parse integer from prompt answer.')

def display_quiz_question(countries,number_of_questions):
    count = 1
    questions_correct = 0
    questions_incorrect = 0
    if(number_of_questions > len(countries)):
        number_of_questions = len(countries)

    for country in range(number_of_questions):
        country, capital = shuffle_dictionary_items(countries)
        del countries[country]
        print('Question #' + str(count) +':')
        answer = input('What is the capital of ' + country + '?')
        count += 1
        
        if(answer == capital):
            questions_correct += int(1)
        else:
            questions_incorrect += int(1)
    print('Finished. Your score is: ' + str(questions_correct) + ' correct answers and ' 
          + str(questions_incorrect) + ' incorrect answers.')
    
def shuffle_dictionary_items(dictionary):
    return random.choice(list(dictionary.items()))

main()