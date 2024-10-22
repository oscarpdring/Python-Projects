'''
Oscar Dring
CS021
Homework #10
'''

#global variable
QUALITY_VALUES = {'A+': 4.00,
'A': 4.00,'A-': 3.67,
'B+': 3.33,'B': 3.00,'B-': 2.67,
'C+': 2.33,'C': 2.00,'C-': 1.67,
'D+': 1.33,'D': 1.00,'D-': 0.67,
'F': 0.00}





def main():
    display_title()
    course_info = get_courses()
    results_gpa = calculate_gpa(course_info)
    display_transcript(course_info, results_gpa)

def display_title():
    print('-----------------')
    print('GPA Calculator')
    print('-----------------')
    
def get_courses():
    course_dictionary = {}

    another = 'y'
    
    print('Submit the course information below:')

    while another.lower() == 'y':
        course_name = input('\tEnter the course ID (eg. CS021): ')
        number_credits = input('How many credits is '+ course_name+ '?: ')
        grade = input('What letter grade did you get in'+ course_name +'? ')
        number_credits = float(number_credits)
    
        course_dictionary[course_name] = [number_credits , grade]
 
        another = input('Would you like to submit another course? (y/n)')
    

    return course_dictionary
        
        
def calculate_quality_points(number_credits, grade):


    return QUALITY_VALUES[grade] * number_credits


def calculate_gpa(courses):
    counter = 0
    total_credits = 0

    for course in courses:
        number_credits = courses[course][0]
        grade = courses[course][1]
        counter += calculate_quality_points(number_credits, grade)
        total_credits += number_credits
    try:
        gpa = counter/total_credits
    except ZeroDivisionError:
        gpa = 0
        
    
    return gpa

def display_transcript(courses, calculated_gpa):

    print('For the following courses:')
    print('Course\t\tCredits\t\tGrade')
    print('----------------------------------')

    for i in courses:
        print((i),'\t\t',(courses[i][0]),'\t\t',courses[i][1])
    

    print('----------------------------------')
    gpa = format(calculated_gpa,".2f")
    print('\tYour GPA is',gpa)
    print('----------------------------------')


main()


