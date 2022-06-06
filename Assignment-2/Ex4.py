class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

class BinarySearchTree:

    def __init__(self, root=None):
        self.root = root

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
            return
        current = self.root
        while current:
            if key <= current.key:
                if not current.left:
                    current.left = Node(key)
                    break
                else:
                    current = current.left
            else:
                if not current.right:
                    current.right = Node(key) 
                    break
                else:
                    current = current.right
    
    def find(self, key):
        
        def findHelper(root, key):
            if not root: return False
            if key == root.key: 
                return True
            else:
                if key < root.key:
                    return findHelper(root.left, key)
                else:
                    return findHelper(root.right, key)

        return findHelper(self.root, key)

def printTree(tree=None):
    if not tree or not tree.root: 
        print()
        return

    def printTreeHelper(treeNode):
        if not treeNode: return
        printTreeHelper(treeNode.left)
        print(treeNode.key, ' ', end='')
        printTreeHelper(treeNode.right)

    printTreeHelper(tree.root)
    print()

tree = BinarySearchTree()
for num in [16, 10, 7, 13, 21, 18, 29, 99]:
    tree.insert(num)
printTree(tree)
tree.insert(11)
printTree(tree)
print(tree.find(18))
print(tree.find(28))