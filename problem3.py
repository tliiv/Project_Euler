# This is intended to be a solution to problem 3 on Project EUler
# https://projecteuler.net/problem=3
# Toomas Liiv 2016-10-29

# We wish to find the largest prime factor of 600851475143

import time

def factors(n):
	'''Factors the number n and returns a sorted list of the factors'''
    factor = 2
    factors = []
    while factor * factor <= n:
        if n % factor == 0:
            factors.append(factor)
            n = n // factor
        else:
            factor += 1
    factors.append(n)
    return factors

def main():
	start = time.time()
	ans = factors(600851475143)
	print(ans[-1])
	end = time.time()
	print(end-start)

main()