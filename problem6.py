# This is intended to be a solution to problem 6 on Project EUler
# https://projecteuler.net/problem=6
# Toomas Liiv 2016-10-30

# We wish to calculate (1^2+2^2+...+100^2)-(1+2+...+100)
# For this we use that both are polygonal numbers, 
# https://en.wikipedia.org/wiki/Polygonal_number

def sum_of_nums(n):
	return n * (n + 1) // 2

def sum_of_square_of_nums(n):
	return n * (n + 1) * (2*n + 1) // 6

def main():
	print(sum_of_nums(100)*sum_of_nums(100)-sum_of_square_of_nums(100))

main()