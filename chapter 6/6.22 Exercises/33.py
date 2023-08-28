from things import BinSearchMap, TreeDrawerNoBalance, TreeNode


def inorder_trav(root: TreeNode):
    if root is not None:
        inorder_trav(root.child_left)
        print(root.value, end=' ')
        inorder_trav(root.child_right)


def inorder_successor(root: TreeNode):
    while True:
        min_node = root.find_min(root)
        while min_node is not None and min_node != root:  # explore entire left tree
            print(min_node.value, end=' ')
            min_node = min_node.get_successor(suppress=True)

        print(root.value, end=' ')  # print root
        if root.child_right is None:
            break

        root = root.child_right  # set new root


my_tree = BinSearchMap()
my_tree[50] = "jumps"
my_tree[40] = "a"
my_tree[60] = "lazy"
my_tree[45] = "quick"
my_tree[47] = "fox"
my_tree[57] = "the"
my_tree[70] = "dog"
my_tree[54] = "over"
my_tree[46] = "brown"

print('Inorder recursive: ', end='')
inorder_trav(my_tree.root)
print('')

# draw = TreeDrawerNoBalance(my_tree)
# draw.drawtree()

print('Inorder successor: ', end='')
inorder_successor(my_tree.root)
print('')
