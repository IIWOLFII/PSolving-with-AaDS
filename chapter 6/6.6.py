class binary_treeNAR():
    def __init__(self, value = None):
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
            self.left.insert_left(child)

    def insert_right(self, val):
        child = self.right
        if self.right is None:
            self.right = binary_treeNAR(val)
        else:
            self.right = binary_treeNAR(val)
            self.right.insert_right(child)


a_tree = binary_treeNAR("a")
print(a_tree.get_root_val())
print(a_tree.get_left_child())
a_tree.insert_left("b")
print(a_tree.get_left_child())
print(a_tree.get_left_child().get_root_val())
a_tree.insert_right("c")
print(a_tree.get_right_child())
print(a_tree.get_right_child().get_root_val())
a_tree.get_right_child().set_root_val("hello")
print(a_tree.get_right_child().get_root_val())
