courses = {'CS 020': {'title': 'MATLAB',
                  'prereqs': []},
           'CS 021': {'title': 'Introduction to programming',
                  'prereqs': []},
           'CS 064': {'title': 'Discrete structures',
                  'prereqs': ['MATH 021']},
           'CS 110': {'title': 'Intermediate programming',
                  'prereqs': ['CS 020']},
         'CS 124': {'title': 'Data structures and algorithms',
                  'prereqs': ['CS 110', 'CS 064']}}

#"CS 121 Computer organization" to the "courses" dictionary with prerequisites
#of CS 020 and CS 110 (a list):

courses["CS 121"] = {"title" : "Computer organization", "prereqs": ("CS 020", "CS 110")}

courses.pop("CS 020")

#if "CS 020" in courses["CS 110"]["prereqs"] or  courses["CS 121"]["prereqs"]:
 #   courses.pop("CS 020")
courses["CS 110"] = {"title" : "Intermediate programming", "prereqs": ( "CS 021")}
courses["CS 121"] = {"title" : "Computer organization", "prereqs": ( "CS 021, CS 110")}
    
print(courses)                     
