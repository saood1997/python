## IMPORTS GO HERE

## END OF IMPORTS


### YOUR CODE FOR calculate_sgpa() FUNCTION GOES HERE ###
def get_grade(x):
    if x=='A+':
        return 4.00
    elif x=='A':
        return 4.00
    elif x=='A-':
        return 3.67
    elif x=='B+':
        return 3.33
    elif x=='B':
        return 3.00
    elif x=='B-':
        return 2.67
    elif x=='C+':
        return 2.33
    elif x=='C':
        return 2.00
    elif x=='C-':
        return 1.67
    elif x=='D+':
        return 1.33
    elif x=='D':
        return 1.00
    elif x=='F':
        return 0   
    else:
        return 0

def calculate_sgpa(x):
    if x==None:
        return None
    grade_list=[]
    for i in x:
        y=get_grade(i)
        if y==0:
            return None
        grade_list.append(y)
    
    total_marks=0
    total_number_of_subjects=len(x)
    
    
    for i in grade_list:
        total_marks=total_marks+i
    
    sgpa=total_marks/total_number_of_subjects
    return sgpa
#### End OF MARKER

### YOUR CODE FOR calculate_sgpa_weighted() FUNCTION GOES HERE ###
def calculate_sgpa_weighted(g,w):
    if not type(g)==list:
        y=get_grade(g)
        return (y*w)/w
	if g==None:
		return None
    
    
    add=0
    x=0
    p=[]
    if not len(g)==len(w):
        return None
    product_of_w_and_g=[]
    for i in g:
        y=get_grade(i)
        if y==0:
            return None
        p.append(y)
    
    for i in range(len(p)):
        y=p[i]*w[i]
        product_of_w_and_g.append(y)
    for i in product_of_w_and_g:
        x+=i
    for i in w:
        add+=i
    sgpa=x/add
    return sgpa

#### End OF MARKER


if __name__ == '__main__':
    print calculate_sgpa(['A+'])
    print calculate_sgpa_weighted(['A+'], [4])
