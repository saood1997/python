## IMPORTS GO HERE

## END OF IMPORTS

### YOUR CODE FOR output_prime_factors() FUNCTION GOES HERE ###
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
def output_prime_factors(a):
	if type(a)== float:
		a = fun(a)
	for f in range(1,a+1):
		if a%f == 0 and is_prime(f):
			print f
def fun(a):
	if a%1>= 0.5:
		x = a +1
		x = int(x)
		return x
	else:
		return int(a)
#### End OF MARKER


### YOUR CODE FOR get_nth_prime() FUNCTION GOES HERE ###
def get_nth_prime(a):
	z = 3
	prime = 2
	if a  == 1:
		return 2
	while prime < a:
		z = z + 2
		if is_prime(z):
			prime = prime + 1
		if type(a) == float:
			return None
	return z
#### End OF MARKER


if __name__ == '__main__':
    output_prime_factors(23)
    print get_nth_prime(4)
