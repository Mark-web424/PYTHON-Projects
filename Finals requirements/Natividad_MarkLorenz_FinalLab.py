#Natividad, Mark Lorenz P.
#WD-202
#Finals Laboratory Exam
#Part I - Basic Sorting Algorithms
#Part II - Binary Search Tree


#==========================================
#PART I - BASIC SORTING ALGORITHMS
#==========================================

def selection_sort(numbers):
	for i in range(len(numbers)):
		min_index = i

		for j in range(i + 1, len(numbers)):
			if numbers[j] < numbers[min_index]:
				min_index = j

		numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

	return numbers


def insertion_sort(numbers):
	for i in range(1, len(numbers)):
		key = numbers[i]
		j = i - 1

		while j >= 0 and numbers[j] > key:
			numbers[j + 1] = numbers[j]
			j = j - 1

		numbers[j + 1] = key

	return numbers


#==========================================
#PART II - BINARY SEARCH TREE
#==========================================

class Node:

	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None


class BST:

	def __init__(self):
		self.root = None

	def insert(self, key):
		self.root = self._insert(self.root, key)

	def _insert(self, root, key):

		if root is None:
			return Node(key)

		if key < root.key:
			root.left = self._insert(root.left, key)

		elif key > root.key:
			root.right = self._insert(root.right, key)

		return root

	def inorder(self, root):

		if root is not None:
			self.inorder(root.left)
			print(root.key, end=" ")
			self.inorder(root.right)

	def preorder(self, root):

		if root is not None:
			print(root.key, end=" ")
			self.preorder(root.left)
			self.preorder(root.right)

	def postorder(self, root):

		if root is not None:
			self.postorder(root.left)
			self.postorder(root.right)
			print(root.key, end=" ")

	def search(self, root, key):

		if root is None:
			return False

		if root.key == key:
			return True

		if key < root.key:
			return self.search(root.left, key)

		return self.search(root.right, key)


#==========================================
#MAIN PROGRAM
#==========================================

print("Enter 10 integers:")

numbers = list(map(int, input().split()))


#Make copies of the original list
selection_numbers = numbers.copy()
insertion_numbers = numbers.copy()


#==========================================
#SELECTION SORT
#==========================================

selection_sort(selection_numbers)

print("\nSelection Sort Result:")

for number in selection_numbers:
	print(number, end=" ")


#==========================================
#INSERTION SORT
#==========================================

insertion_sort(insertion_numbers)

print("\n\nInsertion Sort Result:")

for number in insertion_numbers:
	print(number, end=" ")


#==========================================
#PART II - BINARY SEARCH TREE
#==========================================

print("\n\nPart II - Binary Search Tree")


#Create BST
bst = BST()


#Insert the required values
values = [50, 30, 70, 20, 40, 60, 80, 10, 35]

for value in values:
	bst.insert(value)


#==========================================
#INORDER TRAVERSAL
#==========================================

print("\nInorder Traversal:")

bst.inorder(bst.root)


#==========================================
#PREORDER TRAVERSAL
#==========================================

print("\n\nPreorder Traversal:")

bst.preorder(bst.root)


#==========================================
#POSTORDER TRAVERSAL
#==========================================

print("\n\nPostorder Traversal:")

bst.postorder(bst.root)


#SEARCH FOR 35
search_value = 35

if bst.search(bst.root, search_value):
	print("\n\n35 found in the BST.")
else:
	print("\n\n35 not found in the BST.")