## IMPORTS GO HERE

## END OF IMPORTS

#### YOUR CODE FOR get_grade() FUNCTION GOES HERE ####
def get_grade(x):
    if x in range(90,101):
        return "A+"
		
    elif x in range(86,90):
        return "A"
		
    elif x in range(82,86):
        return "A-"
		
    elif x in range(78,82):			 
        return "B+"
		
    elif x in range(74,78):
        return "B"
		
    elif x in range(70,74):
        return "B-"
		
    elif x in range(66,70):
        return "C+"
		
    elif x in range(62,66):
        return "C"
		
    elif x in range(58,62):
        return "C-"
		
    elif x in range(54,58):
        return "D+"
		
    elif x in range(50,54):
        return "D"
		
    else:
	    return "F"		
#### End OF MARKER

#### YOUR CODE FOR calculate_sgpa() FUNCTION GOES HERE ####
def point_Equivalent(t):
    if t == 'A+':
        return 4.00
    elif t == 'A':
        return 4.00
    elif t == 'A-':
        return 3.67
    elif t == 'B+':
        return 3.33
    elif t == 'B':
        return 3.00
    elif t == 'B-':
        return 2.67
    elif t == 'C+':
        return 2.33
    elif t == 'C':
        return 2.00
    elif t == 'C-':
        return 1.67
    elif t == 'D+':
        return 1.33
    elif t == 'D':
        return 1.00
    elif t == 'F':
        return 0.00 
def calculate_sgpa(x,y,z):
    total_marks = 0
    total_number_of_subjects = 0
    if not x == 'nothing':
        total_number_of_subjects = total_number_of_subjects + 1
        total_marks = total_marks + point_Equivalent(x)
    if not y == 'nothing':
        total_number_of_subjects = total_number_of_subjects + 1
        total_marks = total_marks + point_Equivalent(y)
    if not z == 'nothing':
        total_number_of_subjects = total_number_of_subjects + 1
        total_marks = total_marks + point_Equivalent(z)
    if total_number_of_subjects is 0:
        return 0
    sgpa = total_marks / total_number_of_subjects
    return sgpa
#### End OF MARKER




if __name__ == '__main__':
    print get_grade(50)
    print calculate_sgpa('A', 'B', 'nothing')
