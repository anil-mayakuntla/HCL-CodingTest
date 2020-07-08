class Node():
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

def traverseLeaves(base):
    if base==None:
        return
    if base.left==None and base.right==None:
        print (base.data)
        return
    if base.right:
        traverseLeaves(base.right)
    if base.left:
        traverseLeaves(base.left)

n1=Node(8)
n1.left=Node(3)
n1.left.left=Node(1)
n1.left.right=Node(6)
n1.left.right.left=Node(4)
n1.left.right.right=Node(7)
n1.right=Node(10)
n1.right.right=Node(14)
n1.right.right.left=Node(13)

traverseLeaves(n1)