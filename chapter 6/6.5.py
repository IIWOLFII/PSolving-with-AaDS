# BinaryTree() creates a new instance of a binary tree.
# get_root_val() returns the object stored in the current node.
# set_root_val(val) stores the object in parameter val in the current node.
# get_left_child() returns the binary tree corresponding to the left child of the current node.
# get_right_child() returns the binary tree corresponding to the right child of the current node.
# insert_left(val) creates a new binary tree and installs it as the left child of the current node.
# insert_right(val) creates a new binary tree and installs it as the right child of the current node.

def binary_treeLOL(root = None):
    if root is None:
        root = [None,[],[]]
    else:
        root = [root,[],[]]
    return root

def get_root_val(root):
    return root[0]

def set_root_val(root, val):
    root[0] = val

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]

def insert_left(root,val):
    insert(root, val,left = True)

def insert_right(root,val):
    insert(root, val, left = False)

def insert(root, val, left):
    pos = 2  # right
    if left:
        pos = 1
    if len(root[pos]) != 0:
        if pos == 1:
            root[pos] = [val, root[pos], []]
        else:
            root[pos] = [val, [], root[pos]]
    else:
        root[pos] = [val,[],[]]

a_tree = binary_treeLOL(3)
insert_left(a_tree,4)
insert_left(a_tree,5)
insert_right(a_tree,6)
insert_right(a_tree,7)
left_child = get_left_child(a_tree)
print(left_child)

set_root_val(left_child, 9)
print(a_tree)
insert_left(left_child, 11)
print(a_tree)
print(get_right_child(get_right_child(a_tree)))

print('===' * 15)

x = binary_treeLOL("a")
insert_left(x, "b")
insert_right(x, "c")
insert_right(get_right_child(x), "d")
insert_left(get_right_child(get_right_child(x)), "e")

print(x)