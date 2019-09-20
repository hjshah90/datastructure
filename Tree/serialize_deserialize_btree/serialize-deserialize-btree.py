'''
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
'''
serialize_list = []

class Node():
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

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

	def preorder(self):
		global serialize_list
		serialize_list.append(self.data) 	

		if self.left:
			self.left.preorder()

		if self.right:
			self.right.preorder()


class Tree():
	def create(self, data):		
		for i, x in enumerate(data):
			if i == 0:
				self.node = Node(x)
			else:
				self.node.insert(x) 

	def serialize(self):
		self.node.preorder()
		print(serialize_list)

	def deserialize(self, data):
		self.create(data)	


data = [20, 8, 4, 12, 10, 14, 22]
tree = Tree()
tree.create(data)
tree.serialize()
tree.deserialize(data)

		
									

