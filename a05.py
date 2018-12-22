## IMPORTS GO HERE

## END OF IMPORTS

#### YOUR CODE FOR is_prime() FUNCTION GOES HERE ####

def is_prime(a):
    a = int(a)
    if a < 2:
        return False
    elif a == 2:
        return True
    else:
        for z in range(2, a - 1):
            if (a % z) == 0:
                return False
        return True
		
#### End OF MARKER


#### YOUR CODE FOR output_factors() FUNCTION GOES HERE ####
def output_factors(x):

	for factors_for_z in range(1, x):
		
		a = x % factors_for_z
		
		factors = factors_for_z
		
		if a == 0:
			print factors
		factors = factors + 1
		if factors == x:
			print x
			break
			
		else:
			None
			
			
			
			
			
			
#### End OF MARKER

#### YOUR CODE FOR get_largest_prime() FUNCTION GOES HERE ####
def get_largest_prime(z):
	if z == 0:
		return None
	for x in range(1,z):
		if is_prime(x):
			largest = x
	return largest
	
#### End OF MARKER



if __name__ == '__main__':
    print is_prime(499)  # should return True

    print get_largest_prime(10)  # should return 7
    # print get_largest_prime(100000)  # bonus, try with 100k

    output_factors(10)  # should output -- 1 2 5 10 -- one on each line
