def count_primes(num):
	primes = [2]
	x = 3 
	while x <= num:
		for y in range(3,x,2):
			if x % y == 0:
				x+=2 
				break
		else:
			primes.append(x)	
			x+=2
	return primes
print(count_primes(100))

def print_big(letter):
	patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])

