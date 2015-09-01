# Binary search tree

class BinaryNode:

    def ___init__(self, value = None):
		"""Create binary node"""
		self.value = value
		self.left = None
		self.right = None
    
    def add(self, val):
    	"""Adds a new node to the tree containing this value"""
        if val <= self.value: 
        	if self.left:
                self.left.add(val)
            else:
        	    self.left = BinaryNode(Val)
        else:
        	if self.right:
        		self.right.add(val)
        	else:
        		self.right = BinaryNode(val)


class BinaryTree:
  
    def __init__(Self):
    	"""Create empty binary tree"""
    	self.root = None
    
    def add(self, value):
    	"""insert value into proper location in Binary Tree"""
    	if self.root is None:
    		self.root = BinaryNode(value)
    	else:
    		self.root.add(value)

    def contains(self, target):
    	"""Check whether BST contains target value"""

    	node = self.root
    	while node:
    		if target == node,value:
    			return True
    	    if target < node.value:
    	    	node = node.left
    	    else:
    	    	node = node.right
    	return False


import random
from time import time

def performance():
	"""Demonstrate execution performance"""
	n = 1024
	while n < = 65536:

		bt = BinaryTree()
		for i in range(n):
			bt.add(random.randint(1,n))

			now = time()
			bt.contains(random.randint(1,n))
			print n, (time()) - now)*1000
           
            n *= 2


performance()








