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

	def inorder(self):
		if self.left:
			self.left.inorder()

		print(self.data)

		if self.right:
			self.right.inorder()	

	def preorder(self):
		print(self.data)

		if self.left:
			self.left.preorder()

		if self.right:
			self.right.preorder()	

	def postorder(self):
		if self.left:
			self.left.postorder()

		if self.right:
			self.right.postorder()

		print(self.data)	

	def contains(self, value):
		if value == self.data:
			return 1
		else:
			if value < self.data:
				if self.left:
					return self.left.contains(value)

			if value > self.data:
				if self.right:
					return self.right.contains(value)

	def height(self):
		return 1 + max(self.left.height() if self.left else 0, self.right.height() if self.right else 0)			


class BinaryTree:
	def create(self, data):
		for i, x in enumerate(data):
			if i == 0:
				self.node = Node(x)
			else:
				self.node.insert(x)

	def traversal(self, way = None):
		if way == 'preorder':
			self.node.preorder()
		elif way == 'postorder':
			self.node.postorder()
		else:
			self.node.inorder()

	def contains(self, value):
		if self.node.contains(value) == 1:
			print("Found")
		else:
			print("Not Found")

	def height(self):
		height = self.node.height()	
		print(height)	



data = [20, 8, 4, 12, 10, 14, 22]
Btree = BinaryTree()
Btree.create(data)
print("Inorder Binary Tree Traversal")
Btree.traversal('inorder') 

print("Preorder Binary Tree Traversal")
Btree.traversal('preorder')  

print("Postorder Binary Tree Traversal")
Btree.traversal('postorder')   

print("Find 14 in Binary Tree")
Btree.contains(14)

print("Find 140 in Binary Tree")
Btree.contains(140)

print("Tree Height")
Btree.height()
					

