# This is intended to be a solution to problem 13 on Project EUler
# https://projecteuler.net/problem=13
# Toomas Liiv 2016-12-04

# We wish to find the sum of a number of integers, one per line,
# in the file problem13data.txt and display the 10 first of the sum

import time

def main():

	start = time.time()
	
	fid = open("problem13data.txt", 'r')
	lines = fid.readlines()
	fid.close()
	bigsum = 0
	for line in lines:
		bigsum += int(line)

	bigsum = str(bigsum)	
	print(bigsum[0:10])

	end = time.time()
	print(end-start)


main()