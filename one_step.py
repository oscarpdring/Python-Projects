'''
Oscar Dring
CS021
11-10-22
Lab 10
'''
#global dictionary 
ROUTES = {'Swanton' : ['St. Albans'],
          'St. Albans' : ['Swanton', 'Burlington'],
          'Burlington' : ['Montpelier', 'St. Albans' , 'Middlebury'],
          'Middlebury' : ['Burlington', 'Rutland'],
          'Rutland' : ['Middlebury'],
          'Montpelier' : ['Burlington', 'White River Junction'],
          'St. Jonhsbury' : ['White River Junction'],
          'White River Junction' : ['Montpelier', 'St. Jonhsbury', 'Brattleboro'],
          'Brattleboro' : ['White River Junction' ]}

#main sets up the program calls one_step
def main():
    one_step()

#asks the user for input and does logic to see if the origin is one step away from the destination 
def one_step():
    origin = input(str('Enter Origin: '))
    destination = input(str('Enter Destination: '))
    

    if origin in ROUTES[destination]:
        print('A one-step route exisits between',origin,'and',destination )
    elif origin not in ROUTES:
        print('Sorry. Town not found: ', origin)

    elif origin not in ROUTES[destination]:
        print('No one-step route exisits between',origin,'and',destination)

    else:
        print('Sorry. Town not found: ', origin)
main()
