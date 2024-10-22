'''
Oscar Dring
CS021
11-4-22
Homework 9
'''
#global variables
A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
B = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
C = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
D = ['.', ',', '?', '!', '\'', '"', '-','(', ')', '[', ']', '{', '}', '@','#', '$', '%', '^', '&', '*', '/','\\', '|', '<', '>', ':', ';', ' ']

#starting function case code
def main():
    display_title()

def display_title():
    print('-------------------')
    print('Secret Message')
    print('-------------------')
    get_menu_options()


# This function promts the user to select a menu option which then sends the user to the next section 
def get_menu_options():

    
    print('\t1. Encrypt Message ')
    print('\t2. Decrypt Message')
    print('\t3. Quit \n')
   
    
    number = int(input('Please select from the following options:'))
    


    if number == 1:
       encode()
    elif number == 2:
        decode()
    elif number == 3:
        program_exit()
    else:
        number = int('Please select from the following options:')
        print('\t1. Encrypt Message ')
        print('\t2. Decrypt Message')
        print('\t3. Quit \n')
   

    return number

#the encode function gets a input from the user that they want to encrypt and does just that!
#using the newly learned string minipulators we are able to find and clasify a string
def encode():
    code = input(('Enter a message to encrypt:'))
    private_message = ''

    
    for i in code:
        if i.islower():
            new_code = 'A:'+ str(A.index(i))
        elif i.isupper():
            new_code = 'B:'+ str(B.index(i))
        elif i.isdigit():
            new_code = 'C:'+ str(C.index(i))
        elif i in D:
            new_code = 'D:'+ str(D.index(i))
        else:
            print('Can not encrypt your message')

        #private_message = '-'.join(message)

        private_message += new_code + '-'
    private_message = private_message.rstrip('-')

        
    print('The encrypted message is,', private_message, '\n')

    
    program_exit()
#this function decodes a message that has been encryped.
#taking the user input and giving back the original message that was entered before encryption 
def decode():
    encoder = input(str('Enter a message:'))

    
    encoded = encoder.split('-')
    
    message = ''

    
    for thing in encoded:
        if thing.startswith('A'):
            find_thing = A[int(thing[2:])]
        elif thing.startswith('B'):
            find_thing = B[int(thing[2:])]
            
        elif thing.startswith('C'):
            find_thing = C[int(thing[2:])]
            
        elif thing.startswith('D'):
            find_thing = D[int(thing[2:])]
            
        else:
            print('Can not encrypt your message')
        message += find_thing
            
            
            
        
    print(message)
    
    program_exit()
#this is a reused function that asks the user if they want to leave the script and then either continues or leaves
def program_exit():
    leave = input(str('Are you sure you want to leave? (y/n)'))
    
    
    if leave == 'y':
        bye()
    elif leave == 'n':
        display_title()
    else:
        leave = input(str('Are you sure you want to leave? (y/n)'))
        
def bye():
        print('Thank you for using Secret Message!')
main()


    

    
