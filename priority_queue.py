#Priority Queue



priority = 0
ID = 1


# below is a binaryHeap class

class BHeap:

	def __init__(self, size):
		"""initialize binary heap to given number of elements"""
		self.size = size
		self.n = 0
		self.elements = [[0, None] for i in range(size+1)]
		self.positions = [0 for i in range(size+1)]

	def isEmpty(self):
		"""determine whether binary heap is empty"""
		return self.n == 0

	def smallest(self):
		"extract and return smallest element in heap"""
		id = self.element[1][ID]

		# heap will have one less entry, so place final one appropriately
		last = self.elements[self.n]
		self.n - = 1

		self.elements[1] = last
		pIdx = 1
		child = pIdx * 2
		while child < = self.n:
			# select smaller of two childre
			sm = self.elements[child]
			if child < self.n:
				if sm[PRIORITY] >self.elements[child+1][PRIORITY]:
					child += 1
					sm = self.elements[child]

			if last[PRIORITY] < = sm[PRIORITY]:
				break

			self.elements[pIdx] = sm
			self.positions[sm[ID]] = pIdx
			return id

    def insert(self, id, priority):
    	"""insert item into heap with given priority"""
    	self.n += 1
    	i = self.n
    	while i > 1:
    		pIdx = int(i/2)
    		p = self.elements[pIdx]

    		if priority > p[PRIORITY]:
    			break

    		self.elements[i][ID] = id
    		self.elements[i][PRIORITY] = priority
    		self.positions[id] = i

#decreasekey will find current location of a value, change it's priority to be smaller,
#because its priority has been decreased and then it will heapify (can perform in log n time)

    	def decreasekey(self, id, newPriority):
    		"""reduce the priority for the given item"""

    		size = self.n
    		self.n = self.positions[id] - 1

    		self.insert(id, newPriority)

