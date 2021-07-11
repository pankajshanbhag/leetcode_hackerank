class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key

#  O (N) time | O (N) space -  where n is the number of nodes in a Binary Tree

def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key :
            root.right = insert(root.right,key)
        else:
            root.left = insert(root.left,key)
    return root



def branchsum(root):
    sums=[]
    calculatebs(root,0,sums)
    return sums
def calculatebs(node,runningsum,sums):
    if node is None:
        return
    newrunningsum = runningsum + node.val
    if node.left is None and node.right is None:
        sums.append(newrunningsum)
        return
    calculatebs(node.left,newrunningsum,sums)
    calculatebs(node.right,newrunningsum,sums)

r1=Node(50)
insert(r1,30)
insert(r1,40)
insert(r1,80)
bs=branchsum(r1)
print(bs)
