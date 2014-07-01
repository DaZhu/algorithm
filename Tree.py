
class TreeNode:
	p = None
	l = None
	r = None
	k = None
	v = None 
	info = {}



class Tree:
	root = None
	def make_search_tree(self, kv_list):
		for item in kv_list:
			k = item
			self.insert_searchTree(k)

	def insert_searchTree(self, k, v=None):
		a = TreeNode()
		a.k = k
		a.v = v
		if self.root == None:
			self.root = a
		else:
			node = self.root
			while True:
				if node.k > k:
					if node.l == None:
						node.l = a
						a.p = node
						break
					else:
						node = node.l
				else:
					if node.r == None:
						node.r = a
						a.p = node
						break
					else:
						node = node.r

	def make_tree_bypremidorder(self, prelist, midlist, root):
		if len(prelist) == 0:
			root = None
			return
		k = prelist[0]
		pos = 0

		root.k = k 

		for i in range(0, len(midlist)):
			if midlist[i] == k:
				pos = i

		if pos > 0:
			left = TreeNode()
			root.l = left
			self.make_tree_bypremidorder(prelist[1: pos+1], midlist[0: pos], left)
		if pos < len(midlist):
			right = TreeNode()
			root.r = right
			self.make_tree_bypremidorder(prelist[pos + 1:], midlist[pos+1:], right)

			





	def preorder(self, node):
		if node:
			print(node.k)
			self.preorder(node.l)
			self.preorder(node.r)

	def inoreder(self, node):
		if node:
			self.inoreder(node.l)
			print(node.k)
			self.inoreder(node.r)	

	def backoreder(self, node):
		if node:
			self.backoreder(node.l)
			self.backoreder(node.r)		
			print(node.k)


if __name__ == '__main__':
	one = Tree()
	one.make_search_tree([5,3,7,2,5,8])

	two = Tree()
	two.root = TreeNode()
	two.make_tree_bypremidorder([5,3,2,7,6,8],[2,3,5,6,7,8],two.root )
	print(two.root)
	two.preorder(two.root)

