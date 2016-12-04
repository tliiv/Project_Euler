# This is intended to be a solution to problem 9 on Project EUler
# https://projecteuler.net/problem=9
# Toomas Liiv 2016-12-04

# Given a pythagorean triple a^2+b^2 = c^2 and a<b<c and a+b+c = n
# we want to find a*b*c

import time


def prod_pyth_trip_sum_n(n):
	''' Given that a^2+b^2 = c^2 and a+b+c = n, we find a*b*c '''

	for a in range(1, n - 1):
		for b in range(a, n - 1):
			c = 1000 - a - b
			if(a*a + b*b == c*c):
				return(a*b*c)
				
	return 0
				

def main():

	start = time.time()
	print(prod_pyth_trip_sum_n(1000))
	end = time.time()
	print(end-start)

main()