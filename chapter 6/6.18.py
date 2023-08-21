from stuff import BinSearchMap, TreeNode, TreeDrawer


class TreeNodeAVL(TreeNode):
    def __init__(self, key, value, child_left=None, child_right=None, parent=None):
        super().__init__(key, value, child_left, child_right, parent)
        self.balance_factor = 0


class BinAVLMap(BinSearchMap):
    def __init__(self):
        super().__init__()

    def put(self, key, val):
        if not self.root:
            self.root = TreeNodeAVL(key, val)
        else:
            self._put(key, val, self.root)
        self.size += 1

    def _put(self, key, val, node):
        if key >= node.key:
            if node.child_right:
                self._put(key, val, node.child_right)
            else:
                node.child_right = TreeNodeAVL(key, val, parent=node)
                self.update_balance(node.child_right)
        else:
            if node.child_left:
                self._put(key, val, node.child_left)
            else:
                node.child_left = TreeNodeAVL(key, val, parent=node)
                self.update_balance(node.child_left)

    def update_balance(self, node: TreeNodeAVL):
        if node.balance_factor > 1 or node.balance_factor < - 1:
            self.rebalance_node(node)
            return

        if node.parent:
            if node.is_child_left():
                node.parent.balance_factor += 1
            elif node.is_child_right():
                node.parent.balance_factor -= 1

            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)

    def rebalance_node(self, node=None):
        if node is None:
            node = self.root

        if node.balance_factor == 0:
            return

        elif node.balance_factor > 0:
            self.rotate_tree(node, left=False)

        elif node.balance_factor < 0:
            self.rotate_tree(node, left=True)

    def rotate_tree(self, oldroot, left=True):
        if left:
            childleft = 'child_left'
            childright = 'child_right'
        else:
            childleft = 'child_right'
            childright = 'child_left'

        new_root = getattr(oldroot,childright)
        setattr(oldroot,childright,getattr(new_root,childleft))

        if getattr(new_root,childright):
            child = getattr(new_root,childright)
            child.parent = oldroot

        new_root.parent = oldroot.parent
        if new_root.is_root():
            self.root = new_root

        setattr(new_root,childleft, oldroot)

        oldroot.parent = new_root


        if left:
            oldroot.balance_factor = (
                    oldroot.balance_factor + 1 - min(new_root.balance_factor, 0)
            )
            new_root.balance_factor = (
                    new_root.balance_factor + 1 + max(oldroot.balance_factor, 0)
            )
        else:
            oldroot.balance_factor = (
                    oldroot.balance_factor - 1 - max(new_root.balance_factor, 0)
            )
            new_root.balance_factor = (
                    new_root.balance_factor - 1 + min(oldroot.balance_factor, 0)
            )


tree = BinAVLMap()
# tree.put(8, 80)
# tree.put(4, 40)
# tree.put(10, 100)
# tree.put(3, 30)
# tree.put(7, 60)
# tree.put(9, 90)
# tree.put(5, 50)
# tree.put(6, 60)

# tree.put(40, 'E')
# tree.put(50, 'F')
# tree.put(30, 'C')
# tree.put(35, 'D')
# tree.put(20, 'B')
# tree.put(10, 'A')

tree.put(10, 'A')
tree.put(20, 'B')
tree.put(30, 'C')

draw = TreeDrawer(tree)


draw.drawtree(verticaloffset=0, rebuildcoordinates=True)

