class Node():
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

def breadthFirstOrderTraversal(base):
    if base==None:
        return
    temp=[]
    temp.append(base)

    while(len(temp)!=0):
        print(temp[0].data)
        
        if temp[0].left!=None:
            temp.append(temp[0].left)
        if temp[0].right!=None:
            temp.append(temp[0].right)
        temp.pop(0)

n2=Node(1)
n2.right=Node(2)
n2.right.right=Node(5)
n2.right.right.left=Node(3)
n2.right.right.right=Node(6)
n2.right.right.left.right=Node(4)

breadthFirstOrderTraversal(n2)