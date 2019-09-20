class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def insert(self, value):
		if value < self.data:
			if self.left is None:
				self.left = Node(value)
			else:
				self.left.insert(value)

		if value > self.data:
			if self.right is None:
				self.right = Node(value)
			else:
				self.right.insert(value)

	



Tree = Node(10)
Tree.insert(5)
Tree.insert(15)
Tree.insert(5)
Tree.insert(2)
Tree.insert(1)
Tree.insert(22)
Tree.insert(13)
Tree.insert(14)
Tree.insert(3)
	

def inOrderTraverse(tree):
	global array
	if tree.left:
		inOrderTraverse(tree.left)

	array.append(tree.data)
	
	if tree.right:
		inOrderTraverse(tree.right)	

def checkSort():
	global array
	for i, x in enumerate(array):
		if i < (len(array) - 1) and x > array[i+1]:
			return False
	return True		



array = []
inOrderTraverse(Tree)
print(array)
out = checkSort()
print(out)

