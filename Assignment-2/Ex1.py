class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root=None):
        self.root = root

def printTree(tree=None):
    if not tree: 
        print()
        return

    def printTreeHelper(treeNode):
        if not treeNode.left and not treeNode.right:
            print(treeNode.data, ' ', end='')
        else:
            printTreeHelper(treeNode.left)
            print(treeNode.data, ' ', end='')
            printTreeHelper(treeNode.right)
        

    printTreeHelper(tree.root)
    print()

# example case
leftChild = TreeNode(6)
rightChild = TreeNode(3)
left = TreeNode(7)
right = TreeNode(17, leftChild, rightChild)
root = TreeNode(1, left, right)
tree = Tree(root)

print('Example case: ')
printTree(tree)

# null case
print('Null case: ')
printTree()

# single-value case
root = TreeNode(1)
tree = Tree(root)

print('Single-value case: ')
printTree(tree)