# This is intended to be a solution to problem 7 on Project EUler
#https://projecteuler.net/problem=7
# Toomas Liiv 2016-12-04

# We wish to determine the nth prime number, specificlaly the 10001nth

import time
from math import floor, sqrt


def is_prime(nr):
	'''Takes an int nr and check if it is prime or not'''
	if nr <= 1:
		return False

	# We only need to check factor up to sqrt(nr) + 1
	for div in range(2, floor(sqrt(nr)) + 1):
		if nr % div == 0:
			return False

	return True

def nth_prime(n):
	"Outputs the nth prime number"

	count = 1
	nr = 3
	while count < n:
		if is_prime(nr):
			count += 1
		nr += 2
		
	return nr - 2

def main():

	start = time.time()
	print(nth_prime(10001))
	end = time.time()
	print(end-start)

main()