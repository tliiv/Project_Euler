# This is intended to be a solution to problem 10 on Project EUler
# https://projecteuler.net/problem=10
# Toomas Liiv 2016-12-04

# We wish to find the sum of all primes below two million. 
# We do this by creating a sieve and summing stuff

from math import sqrt, floor
import time


def primes_below(n):
	'''Erathostenes sieve. Ouputs in format [True, True, False, True, ...]
	'''

	primes = [True] * n 
	for i in range(2, floor(sqrt(n)) + 1):
		if (primes[i]):
			for j in range(i*i, n, i):
				primes[j] = False

	return primes

def primes_below_n_sum(n):
	'''Sums all primes below n'''

	primesum  = 0
	primes = primes_below(n)
	for i in range(2, n):
		if(primes[i]):
			primesum += i	

	return primesum		


def main():

	start = time.time()
	print(primes_below_n_sum(2000000))
	end = time.time()
	print(end-start)

main()
