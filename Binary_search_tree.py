import collections

class BinarySearchTree:

    Node = collections.namedtuple('Node', ['left', 'right', 'value'])
    
    @staticmethod
    def contains(root, value):
        while root:
        	if root.value == value:
        		return True
        	elif root.value > value:
        		root = root.left
        	else:
        		root = root.right
        return False



n1 = BinarySearchTree.Node(value=1, left=None, right=None)
n3 = BinarySearchTree.Node(value=3, left=None, right=None)
n2 = BinarySearchTree.Node(value=2, left=n1, right=n3)

print(BinarySearchTree.contains(n2, 3))