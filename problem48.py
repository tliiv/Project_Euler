# This is intended to be a solution to problem 48 on Project EUler
# https://projecteuler.net/problem=48
# Toomas Liiv 2016-12-05

import time

def self_power_sum(n):
	bigsum = 0
	for i in range(1, n+1):
		bigsum += i**i

	return bigsum

def main():
	start = time.time()
	print(self_power_sum(1000)%10000000000)
	end = time.time()
	print(end-start)

main()