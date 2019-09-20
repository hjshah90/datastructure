
'''
The Fibonacci sequence is defined as follows: the first number of the sequence is 0, 
the second number is 1, and the nth number is the sum of the (n - 1)th and (n - 2)th 
numbers. Write a function that takes in an integer n and returns the nth Fibonacci 
number.
Sample input: 6
Sample output: 5 (0, 1, 1, 2, 3, 5)
'''

def getNthFib(n):
	x = 0
	y = 1

	i = 3
	while i <= n:
		z = x + y
		x = y
		y = z
		i += 1

	return z	


result = getNthFib(25);
print(result)