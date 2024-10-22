'''
Oscar Dring
CS021
11-3-22
Lab 8
'''

def main():
    in_both()

def in_both():
    word1 = input(str('Enter frist string:'))
    word2 = input(str('Enter second string:'))
    output = ''
    
    for char in set(word1):
        if char in word2:
            output += char


    print(output)        



    return output 

    

   
   

main()
