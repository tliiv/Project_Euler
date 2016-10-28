# This is intended to be a solution to problem 1 on Project EUler
# https://projecteuler.net/problem=1
# Toomas Liiv 2016-10-28

# This is a brute force solution.
# However, for fun, we implement it generally, for an upper limit n and 
# a list of factors instead of just 3 and 5.

import time

def multiple_sum(n, factors):
	'''Computes the sum of all numbers below n which are divisible by
	   at least one element in the list factors. 

	   Args: 
	   		n (int)        : upper limit
	   		factors (list) : list of factors

	   Returns:
	   		ans (int)      : sum of all numbers below n divisible by at 
	   						 at least one element in factors

	   Example:

	   		>> multiple_sum(1000, [3, 5])
	   		233168
	'''
	ans = 0
	for i in range(n):
		for el in factors:
			if i%el == 0:
				ans += i
				break
	return ans

def main():
	start = time.time()
	print(multiple_sum(1000,[3, 5]))
	end = time.time()
	print(end-start)

main()
