'''
Write a function that takes in an array of integers 
and returns a sorted array of the three largest integers 
in the input array. Note that the function should return duplicate 
integers if necessary; for example, 
it should return [10, 10, 12] for an input array of [10, 5, 9, 10, 12].
Sample input: [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
Sample output: [18, 141, 541]
'''

def findThreeLargest(array):
	threeLargest = [None, None, None]
	for num in array:
		if threeLargest[2] is None or num > threeLargest[2]:
			threeLargest = shiftAndUpdate(threeLargest, num, 2)
		elif threeLargest[1] is None or num > threeLargest[1]:
			threeLargest = shiftAndUpdate(threeLargest, num, 1)
		elif threeLargest[0] is None or num > threeLargest[0]:
			threeLargest = shiftAndUpdate(threeLargest, num, 0)
	return threeLargest		

def shiftAndUpdate(array, num, idx):
	for i in range(idx + 1):
		if i == idx:
			array[i] = num
		else:
			array[i] = array[i + 1]
	return array

array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
result = findThreeLargest(array)
print(result)	