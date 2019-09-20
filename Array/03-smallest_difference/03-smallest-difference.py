def smallestDifference(array1, array2):
	array1.sort()
	array2.sort()

	idx1 = 0
	idx2 = 0
	smallest = float("inf")

	while idx1 < len(array1) and idx2 < len(array2):
		value1 = array1[idx1]
		value2 = array2[idx2]
		if value1 < value2:
			current = value2 - value1
			idx1 += 1
		elif value2 < value1:
			current = value1 - value2
			idx2 += 1
		else:
			return [value1, value2]

		if smallest > current:
			smallest = current
			currentPair = [value1, value2]
	
	return currentPair				

array1 = [-1, 5, 10, 20, 28, 3]
array2 = [26, 134, 135, 15, 17]
result = smallestDifference(array1, array2)
print(result)