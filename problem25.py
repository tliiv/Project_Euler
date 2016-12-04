# This is intended to be a solution to problem 15 on Project EUler
# https://projecteuler.net/problem=15
# Toomas Liiv 2016-12-04

# We want to find which fibonacci nr is the first to have 
# 1000 digits
# Can also be solved by pen and paper by using
# http://mathworld.wolfram.com/BinetsFibonacciNumberFormula.html

import time

def first_fibonacci_n_digits(n):
	count = 2
	f1 = 1
	f2 = 1
	while f2 < 10**(n-1):
		tmp = f2
		f2 = f1+f2
		f1 = tmp
		count += 1
	return count

def main():
	start = time.time()
	print(first_fibonacci_n_digits(1000))
	end = time.time()
	print(end-start)

main()