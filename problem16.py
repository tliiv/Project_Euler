# This is intended to be a solution to problem 16 on Project EUler
# https://projecteuler.net/problem=16
# Toomas Liiv 2016-12-04

# We wish to find the sum of digits in 2^1000

import time

def sum_of_digits(n):
	'''Outputs sum of digits of a number'''

	digit_sum = 0
	while n > 0:
		digit_sum += n % 10
		n = n // 10

	return(digit_sum)

def main():

	start = time.time()
	print(sum_of_digits(2**1000))
	end = time.time()
	print(end-start)

main()