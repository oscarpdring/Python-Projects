'''
Oscar Dring
CS021
11-10-22
Lab 10
'''

#creates a global variable
ROUTES = {'Swanton' : ['St. Albans'],
          'St. Albans' : ['Swanton', 'Burlington'],
          'Burlington' : ['Montpelier', 'St. Albans' , 'Middlebury'],
          'Middlebury' : ['Burlington', 'Rutland'],
          'Rutland' : ['Middlebury'],
          'Montpelier' : ['Burlington', 'White River Junction'],
          'St. Jonhsbury' : ['White River Junction'],
          'White River Junction' : ['Montpelier', 'St. Jonhsbury', 'Brattleboro'],
          'Brattleboro' : ['White River Junction' ]}
