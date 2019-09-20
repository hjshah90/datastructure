class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

target = 7

def findClosest(root, diff = None, closest = None):
	global target
	
	gap = abs(target - root.value)
	if gap < diff or diff is None:
		closest = root.value
		diff = gap
	
	if target < root.value and root.left:
		closest = findClosest(root.left, diff, closest)
	elif target > root.value and root.right:
		closest = findClosest(root.right, diff, closest)
		
	return closest		



root = Node(10)  
root.left = Node(5)  
root.right = Node(15)  
root.left.left = Node(2)  
root.left.right = Node(5)  
root.right.left = Node(13) 
root.right.right = Node(22)  
root.left.left.left = Node(1)  
root.right.left.right = Node(14) 
result = findClosest(root)
print(result)
