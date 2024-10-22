'''
Oscar Dring
CS021
Homework #08
10-30-22
'''


def main():
    read_grocery_list()
    view_grocery()
    get_menu_options()


def read_grocery_list():
    infile = open('groceries.txt', 'a')   
