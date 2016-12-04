# This is intended to be a solution to problem 20 on Project EUler
# https://projecteuler.net/problem=20
# Toomas Liiv 2016-12-04

# We wish to find the digits sum of 100!

import time

def sum_of_digits(n):
	'''Outputs sum of digits of a number'''

	digit_sum = 0
	while n > 0:
		digit_sum += n % 10
		n = n // 10

	return(digit_sum)

def factorial(n):
	'''Outputs the factorial of a number, 5! = 5*4*3*2*1'''
	prod = 1
	for i in range(1, n+1):
		prod *= i
	return prod

def main():
	start = time.time()
	print(sum_of_digits(factorial(100)))
	end = time.time()
	print(end-start)

main()