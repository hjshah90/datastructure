class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class BinaryTree:
	def __init__(self):
		self.root = None

	def create(self, data):
		for x in data:
			self.add(x)

	def add(self, value):
		if self.root is None:
			self.root = Node(value)
		else:
			current = self.root
			while 1==1:
				if value < current.value:
					if current.left is None:
						current.left = Node(value)
						break
					else:
						current = current.left
				elif value > current.value:
					if current.right is None:
						current.right = Node(value)
						break
					else:
						current = current.right	

	def traversal(self, traversalType = 'None'):
		if traversalType == 'preorder':
			self.preorderTraversal()
		elif traversalType == 'postorder':
			self.postorderTraversal()
		else:
			self.inorderTraversal()		

	# Left Root Right
	def inorderTraversal(self, data = None):
		if data is None:
			data = self.root

		if data.left:
			self.inorderTraversal(data.left)

		print(data.value)

		if data.right:
			self.inorderTraversal(data.right)	

	# Root Left Right
	def preorderTraversal(self, data = None):
		if data is None:
			data = self.root 

		print(data.value)
		
		if data.left:
			self.preorderTraversal(data.left)

		if data.right:
			self.preorderTraversal(data.right)

	# Left Right Root
	def postorderTraversal(self, data = None):
		if data is None:
			data = self.root 

		if data.left:
			self.postorderTraversal(data.left)

		if data.right:
			self.postorderTraversal(data.right)
			
		print(data.value)							




data = [12, 6, 14, 3]
Btree = BinaryTree()
Btree.create(data)
print("Inorder Binary Tree Traversal")
Btree.traversal('inorder') 

print("Preorder Binary Tree Traversal")
Btree.traversal('Preorder')  

print("Postorder Binary Tree Traversal")
Btree.traversal('postorder')            				

