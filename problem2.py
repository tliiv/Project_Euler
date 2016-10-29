# This is intended to be a solution to problem 2 on Project EUler
# https://projecteuler.net/problem=2
# Toomas Liiv 2016-10-29

import time

def sum_even_fibonacci(n):
	'''Calculates the sum of the even fibonacci numbers below n'''
	num, prev = 1, 1
	mysum = 0
	while num < n:
		if num % 2 == 0:
			mysum += num
		tmp = num
		num = num + prev
		prev = tmp
	return(mysum)


def main():
	start = time.time()
	print(sum_even_fibonacci(4000000))
	end = time.time()
	print(end-start)
	
main()