class Node:
	def __init__(self, data):
		self.data = data
		self.next = None					

class SLinkList:
	def __init__(self):
		self.head = None

	def addLast(self, data):
		newNode = Node(data)
		if self.head is None:
			self.head = Node(data)
		else:
			current = self.head
			while current.next:
				current = current.next
			current.next = newNode
			
	def addBegin(self, data):
		newNode = Node(data)
		newNode.next = self.head
		self.head = newNode	

	def printList(self):
		printNode = self.head
		while printNode is not None:
			print(printNode.data)
			printNode = printNode.next							

l = SLinkList()
l.addLast(10)
l.addLast(20)
l.addLast(30)
l.addBegin(5)
l.printList()