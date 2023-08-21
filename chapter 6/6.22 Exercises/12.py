class binary_treeNAR():
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def get_root_val(self):
        return self.value

    def set_root_val(self, val):
        self.value = val

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def insert_left(self, val):
        child = self.left
        if self.left is None:
            self.left = binary_treeNAR(val)
        else:
            self.left = binary_treeNAR(val)
            self.left.left = child

    def insert_right(self, val):
        child = self.right
        if self.right is None:
            self.right = binary_treeNAR(val)
        else:
            self.right = binary_treeNAR(val)
            self.right.right = child




tree = binary_treeNAR()

tree.insert_left('c')
tree.insert_left('compiled')

child = tree.get_left_child()
child.insert_right('Java')

tree.insert_right('Scheme')
tree.insert_right('interpreted')

child = tree.get_right_child()
child.insert_left('Python')

print(tree)