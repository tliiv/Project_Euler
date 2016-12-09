# This is intended to be a solution to problem 14 on Project EUler
# https://projecteuler.net/problem=14
# Toomas Liiv 2016-12-09

# The goal is to find the longest collatz sequence for a starting
# number below one million

import time

def longest_collatz_sequence(n):
	'''Provides the length of the longest collatz sequence
	   starting at n.

	   To speed it up, we use caching.
	'''

	cache = [-1]*1000000
	cache[1] = 1

	length = 0
	start = 0
	for i in range(2, n):
		count = 1
		current = i
		while current != 1:
			#print(current, end = " ")
			
			if current < 1000000 and cache[current] != -1:
				count += cache[current] - 1
				break
		
			if current % 2 == 0: 
				current //= 2
			else:
				current = current * 3 +1
			count += 1
		#print()

		cache[i] = count
		#print(i, cache[i])

		if count > length:
			length = count
			start = i

	return start

def main ():

	start = time.time()
	print(longest_collatz_sequence(1000000))
	end = time.time()
	print(end-start)

main()