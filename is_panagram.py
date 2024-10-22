'''
Oscar Dring
CS021
11-3-22
Lab 8
'''
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def main():
    user = input(str('Please enter a sentence:'))
    
    is_panagram(user)

    if (is_panagram(user) == True):
        print('You have a panagram')
    else:
        print('''You don't have a panagram''')
    


def is_panagram(user):
    counter = 1
    for char in ALPHABET:
        if char not in set(user):
            return False
    
    return True
    
    
main()

#how quickly daft jumping zebras vex
