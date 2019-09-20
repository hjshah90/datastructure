class DoublyLinkList:
	def __init__(self):
		self.head = None
		self.tail = None 

	def setHead(self, node):
		if self.head is None:
			self.head = node
			self.tail = node
			return
		self.insertBefore(self.head, node)	

	def setTail(self, node):
		if self.tail is None:
			self.tail = node 
			return
		self.insertAfter(self.tail, node)		

	def insertBefore(self, node, nodeToInsert):
		if nodeToInsert == self.head and nodeToInsert == self.tail:
			return
		self.remove(nodeToInsert)
		nodeToInsert.next = node
		nodeToInsert.prev = node.prev 
		if node.prev is None:
			self.head = nodeToInsert
		else:
			node.prev.next = nodeToInsert
		node.prev = nodeToInsert	

	def insertAfter(self, node, nodeToInsert):
		if nodeToInsert == self.head and nodeToInsert == self.tail:
			return
		self.remove(nodeToInsert)
		nodeToInsert.prev = node 
		nodeToInsert.next = node.next 
		if node.next is None:
			self.tail = nodeToInsert
		else:
			node.next.prev = nodeToInsert
		node.next = nodeToInsert		

	def insertPosition(self, position, nodeToInsert):
		if position == 1:
			self.setHead(nodeToInsert)
		node = self.head 
		currentPosition = 1	
		while node.next is not None and currentPosition != position:
			node = node.next
			currentPosition += 1
		if node is not None:
			self.insertBefore(node, nodeToInsert)
		else:
			self.setTail(nodeToInsert)	

	def remove(self, node):
		if node == self.head:
			self.head = node.next
		if node == self.tail:
			self.tail = node.prev

		if node.prev is not None:
			node.prev.next = node.next 
		if node.next is not None:
			node.next.prev = node.prev 
		node.prev = None
		node.next = None 