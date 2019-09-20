'''
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

'''

def solution(data, k):
	result = []
	for x in data:
		if x <= k:
			remain = k - x
			found = data.index(remain)
			if found > 0:
				result.append(x)
				result.append(remain)
				return result
	return result

data = [10, 15, 3, 7]
k = 17
result = solution(data, k)
print(result)
