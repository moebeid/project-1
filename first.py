def median(a,b,c):
	if a >= b:
		if a >= c:
			if c >=b:
				return c
			return b
		return a
	else:
		if b >= a:
			if b >= c:
				if c >=a:
					return c
				return a
			return b




print(median(-5,-3,0))
print(median(9,3,6))
print(median(7,8,7))