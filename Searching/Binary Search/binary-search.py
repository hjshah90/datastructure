def BinarySearch(array, target):
	left = 0
	right = len(array) - 1

	while left <= right:
		middle = (left + right) / 2
		value = array[middle]
		if value == target:
			return middle
		elif target < value:
			right = middle - 1
		else:
			left = middle + 1
	return -1
	
array = [0,1,21,33,45,45,61,71,72,73]
target = 33
position = BinarySearch(array, target)
print(position)
