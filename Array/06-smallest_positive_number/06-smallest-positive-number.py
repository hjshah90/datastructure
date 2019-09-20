'''
Given an array of integers, find the first missing positive integer in 
linear time and constant space. In other words, find the lowest positive 
integer that does not exist in the array. The array can contain duplicates 
and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. 
The input [1, 2, 0] should give 3.
'''

def solution(data):
	m = max(data)
	l = len(data)

	if(m < 1):
		return 0

	if(l == 1):
		if(data[0] == 1):
			return 2
		else:
			return 1

	temp = [0] * m	
	
	for i in data:
		if(i > 0):
			temp[i-1] = 1

	for index, value in enumerate(temp):
		if(value == 0):
			return index + 1

	return len(temp) + 1


data = [1, 2, 0]
result = solution(data)
print(result)