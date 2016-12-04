# This is intended to be a solution to problem 15 on Project EUler
# https://projecteuler.net/problem=15
# Toomas Liiv 2016-12-04

# We want to find the number of paths through a 20x20 grid
# The binomial coefficient can be implemented more efficiently
# but this suffices

import time

def binomial(n,k):
	'''Outputs n choose k'''

	return factorial(n)//(factorial(k)*factorial(n-k))

def factorial(n):
	'''Outputs the factorial of a number, 5! = 5*4*3*2*1'''
	prod = 1
	for i in range(1, n+1):
		prod *= i
	return prod

def main():
	start = time.time()
	print(binomial(40,20))
	end = time.time()
	print(end-start)

main()