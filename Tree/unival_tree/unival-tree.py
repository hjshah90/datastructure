'''
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
'''

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

count = 0
def countUnivalTree(root):
	global count
	left = False
	right = False
	
	if root.data is None:
		pass

	if (root.left and root.data == root.left.data) or root.left is None:
		left = True

	if (root.right and root.data == root.right.data) or root.right is None:
		right = True	

	if left == True and right == True:
		count += 1	

	if root.left:
		countUnivalTree(root.left)

	if root.right:
		countUnivalTree(root.right)	
			

root = Node(1)
root.left = Node(1)
root.right = Node(1)

'''
root = Node(0)
root.left = Node(1)
root.right = Node(0)
root.right.left = Node(1)
root.right.right = Node(0)
root.right.left.left = Node (1)
root.right.left.right = Node(1)

root = Node(5) 
root.left = Node(4) 
root.right = Node(5) 
root.left.left = Node(4) 
root.left.right = Node(4) 
root.right.right = Node(5) 
'''
countUnivalTree(root)
print(count)