class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.middle=None
        self.right=None
        
class Tree:
    def __init__(self,root,name=''):
        self.root=root
        self.name=name
        
node=Node(15)

Node.left=Node(4)
Node.middle=Node(6)
Node.right=Node(11)

Node.left.left=Node(9)
Node.left.right=Node(8)

Node.middle.left=Node(13)
Node.middle.right=Node(12)

Node.right.left=Node(10)
Node.right.right=Node(15)

myTree=Tree(Node,'basic BTS')

print(myTree.name)
print('Node.kiri:',myTree.root.left.data)
print('Node.tengah:',myTree.root.middle.right.data)
print('Node.kanan:',myTree.root.right.right.data)
