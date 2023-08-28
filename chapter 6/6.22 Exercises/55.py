from things import BinSearchMap, TreeDrawerNoBalance, TreeNode

class DupBinSearchMap(BinSearchMap):
    def __init__(self):
        super().__init__()

    def _put(self, key, val, node):
        if key == node.key:
            node.replace_value(value = val)
        elif key >= node.key:
            if node.child_right:
                self._put(key, val, node.child_right)
            else:
                node.child_right = TreeNode(key, val, parent=node)
        else:
            if node.child_left:
                self._put(key, val, node.child_left)
            else:
                node.child_left = TreeNode(key, val, parent=node)



my_tree = DupBinSearchMap()
my_tree[50] = "jumps"
my_tree[40] = "a"
my_tree[60] = "lazy"
my_tree[45] = "quick"
my_tree[47] = "fox"
my_tree[57] = "the"
my_tree[70] = "dog"
my_tree[54] = "over"
my_tree[46] = "brown"
my_tree[57] = "the uhh uh the uhh"

draw = TreeDrawerNoBalance(my_tree)
draw.drawtree()