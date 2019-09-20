'''
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

def solutionWithDivision(data):
	result = []
	total = 1
	for x in data:
		total = total * x

	for x in data:
		result.append(total / x)

	return result	

def solutionWithoutDivision(data):
	result = []
	total = 1

	for x in data:
		for y in data:
			if x == y:
				pass
			else:
				total = total * y 

		result.append(total)

	return result	
			
data = [1, 2, 3, 4, 5]

print("Result with Division :: ")
result = solutionWithDivision(data)
print(result)

print("Result without Division :: ")
result = solutionWithDivision(data)
print(result)