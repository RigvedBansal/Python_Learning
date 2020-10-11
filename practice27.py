for a in range(1,1000):
	for b in range(1,1000):
		for c in range(1,1000):
			d = a + b + c
			if d>1000:
				break
			if d == 1000:
				if a < b and b < c:
					if a**2 + b**2 == c**2:
						print(a,b,c)
						print(a*b*c)