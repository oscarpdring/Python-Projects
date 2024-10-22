'''
Oscar Dring
CS021
11-3-22
Lab 8
'''

def main():
    user = input(str('Please enter a word:'))
    
    is_palindrome(user)
    if (is_palindrome(user) == True):
        print('You have a palindrome')
    else:
        print('You do not have a palindrome')

def is_palindrome(user):
    word1 = user.replace('','').lower()
    word2 = word1[::-1]

    if word1 == word2:
        return True
    else:
        return False

main()
