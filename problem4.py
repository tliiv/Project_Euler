# This is intended to be a solution to problem 4 on Project EUler
#https://projecteuler.net/problem=4
# Toomas Liiv 2016-12-04

# We wish to find the largest palindrome made from the product of two 3-digit numbers

import time


def is_palindrome(nr):
	'''Takes an int (nr) and outputs true if it is palindrome'''
	nr = str(nr)
	for i in range(0, len(nr)//2):
		if nr[i] != nr[len(nr) - i - 1]:
			return False

	return True

def palindrome_search(start, end):
	''' Searches for the largest palindrome product of nrs betwwen start
	    and end, inclusive 
	'''

	max_palindrome = 0
	for i in range(start, end + 1):
		for j in range(i, end +1):
			if is_palindrome(i*j) and i*j > max_palindrome:
				max_palindrome = i*j

	return max_palindrome

def main():

	start = time.time()
	print(palindrome_search(100,999))
	end = time.time()
	print(end-start)

main()