# got source code from moodle provided by lecturer 
class BinTreeNode(object):
 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
     
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return(tree)
 
def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print(tree.value)
 
def in_order(tree): # in order none recursive 
    node = tree
    stack = []
    treeNode = []
    check = False
    while check == False:
        length = len(stack)
        if node != None:
            stack.append(node)
            node = node.left # traverses the node to the left subtree
        else:
            if length >0:
                node = stack.pop()
                treeNode.append(node.value)#adds the node to the list
                node = node.right# traverses the node to the right subtree
            else:
                check = True
    print(treeNode)
'''
stored the 'tree' into a variable node
empty stack and empty list
check is set to false
while check is false carry on looping
length will be the legth of the stack
if node is not none then append node to the satck
traverse the node to the left substree
else
if the length is greater than 0
pop the stack and this will be the new node
adds the new node to the list
then traverses the node to the right subtree
else
check is true
print the list
'''

 
if __name__ == '__main__':
   
  t=tree_insert(None,6);
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  in_order(t)
