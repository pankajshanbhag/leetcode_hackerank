class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key

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

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def findClosest(Node,target):
    return findclosehelp(Node,target,9999)

def findclosehelp(Node,target,closest):
    currentnode=Node
    while currentnode is not None:
        if abs(target - closest) > abs(target - currentnode.val):
            closest = currentnode.val
        if target < currentnode.val:
            currentnode=currentnode.left
        elif target > currentnode.val:
            currentnode=currentnode.right
        else:
            break
    return closest


r1=Node(50)
r=insert(r1,30)
#inorder(r)
closest=findClosest(r1,200)
print(closest)

