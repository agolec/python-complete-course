phonebook = {'chris':'555-2334','Link':'555-2211','Saria':'555-2213'}

keepGoing = True
optionsForContinue = ['Y','y']
while keepGoing:
    try:
        userKeyInput = input('Enter a key and I will try to find it')
        if(userKeyInput not in phonebook):
            print('key \'' + userKeyInput + '\' not found in dictionary')
        else:
            print(phonebook[userKeyInput])
        charInput = input('Keep going? y/n: ')
        if(charInput not in optionsForContinue):
            keepGoing = False
    except KeyError:
        print('Key does not exist.')

