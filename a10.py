## IMPORTS GO HERE
import os 
import sys
## END OF IMPORTS

### YOUR CODE FOR line_count() FUNCTION GOES HERE ###
def line_count(filename,a,z = False):
	f1 = os.path.join(filename,a)
	f = open(f1,'r')
	sum = 1
	for i in f:
		for seq in i:
			if seq == '\n':
				sum += 1
	
	f.close()
	if z == True:
		f = open(f1,'r')
		sum = 0
		for i in f:
			if i != '\n':
				sum += 1
					
	f.close()				
	return sum

#### End OF MARKER

### YOUR CODE FOR character_count() FUNCTION GOES HERE ###
def character_count(filename , a , parameter = False):
	f1 = os.path.join(filename,a)

	sum = 0
	f = open(f1,'r')
	for i in f:
		for seq in i:
			if seq != "" and seq !='\n':
				sum += 1
							
	f.close()			
		
	if parameter != True:
		f = open(f1,'r')	
		sum = 0
		for i in f:
			for seq in i:
				sum += 1
	f.close()					
	return sum

### YOUR CODE FOR move_lines() FUNCTION GOES HERE ###
def move_lines(file1,file2,parameter):
	a = " "
	b = 0
	
	with open(file1,'r') as f:
	
		for i in f:
			b = b + 1
			if b <= parameter:
				a += i
	with open (file2,'w') as f:
	
	
		for i in a.strip():
			f.write(i)
			if b == parameter:
				a += 1		
	
				
		return  a and b
		
	
	
			
			
	
#### End OF MARKER



if __name__ == '__main__':
    print line_count('.', 'essay.txt')
    print line_count('.', 'essay.txt', True)

    print character_count('.', 'essay.txt')
    print character_count('.', 'essay.txt', True)

    move_lines('essay.txt', 'out.txt', 3)

    pass
