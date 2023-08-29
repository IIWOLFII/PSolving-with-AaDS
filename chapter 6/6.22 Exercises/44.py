from things import binary_treeNAR, NarDrawer

class Threaded_Binary_TreeNAR(binary_treeNAR):
    def __init__(self, value=None, parent = None):
        super().__init__(value)
        self.parent = parent

    def get_parent(self):
        return self.parent

    def find_left(self, tree):
        while tree.left:
            tree = tree.left
        return tree

    def find_successor(self,tree):
        succ = None
        # If the node has a right child, then the successor is the smallest key in the right subtree
        if tree.right:
            succ = self.find_left(tree.right)
        # If the node has no right child and is the left child of its parent, then the parent is the successor.
        elif tree.parent.left == tree:
            succ = tree.parent
        # If the node has no right child and is the right child of its parent,, then the successor to this node is the successor of its parent, excluding this node.
        elif tree.parent.right == tree:
            tree.parent.right = None
            succ = self.find_successor(tree.parent)
            tree.parent.right = tree
        return succ

    def insert_left(self, val):
        child = self.left
        if self.left is None:
            self.left = Threaded_Binary_TreeNAR(val,self)
        else:
            self.left = Threaded_Binary_TreeNAR(val,self)
            self.left.insert_left(child)

    def insert_right(self, val):
        child = self.right
        if self.right is None:
            self.right = Threaded_Binary_TreeNAR(val,self)
        else:
            self.right = Threaded_Binary_TreeNAR(val,self)
            self.right.insert_right(child)

def inorder_threaded(root):
    while True:
        leftmost = root.find_left(root)
        while leftmost is not None and leftmost != root:  # explore entire left tree
            print(leftmost.value, end=' ')
            leftmost = leftmost.find_successor(leftmost)

        print(root.value, end=' ')  # print root
        if root.right is None:
            break

        root = root.right  # set new root


a_tree = Threaded_Binary_TreeNAR("jumps")
a_tree.insert_left("a")
a_tree.get_left_child().insert_right('quick')
a_tree.get_left_child().get_right_child().insert_right('fox')
a_tree.get_left_child().get_right_child().get_right_child().insert_left('brown')
a_tree.insert_right("lazy")
a_tree.get_right_child().insert_right('dog')
a_tree.get_right_child().insert_left('the')
a_tree.get_right_child().get_left_child().insert_left('over')

draw = NarDrawer(a_tree)
draw.drawtree()

inorder_threaded(a_tree)
