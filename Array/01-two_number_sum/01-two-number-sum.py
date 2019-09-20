def twoNumbersum(data, total):
	for i in range(len(data)-1):
		for j in range(i+1, len(data)):
			if data[i] + data[j] == total:
				return sorted([data[i], data[j]])

data = [3, 5, -4, 8, 11, 1, -1, 6]
total = 10
result = twoNumbersum(data,total)	
print(result)