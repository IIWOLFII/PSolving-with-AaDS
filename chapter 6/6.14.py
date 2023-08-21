# Binary search tree map
from stuff import TreeDrawer
import random as rng

class TreeDrawerNoBalance(TreeDrawer):
    def __init__(self,tree):
        super().__init__(tree)

    def writefun(self,node):
        font = ("Times New Roman", 12, "normal")
        align = "center"
        text = f'Key: {node.key}\nVal: {node.value}\n'

        self.turtle.pendown()
        self.turtle.circle(20)
        self.turtle.write(arg=text, align=align, font=font)
        self.turtle.penup()

class TreeNode():
    def __init__(self, key, value, child_left=None, child_right=None, parent=None):
        self.key = key
        self.value = value
        self.child_left = child_left
        self.child_right = child_right
        self.parent = parent

    def is_child_left(self):
        return self.parent and self.parent.child_left == self

    def is_child_right(self):
        return self.parent and self.parent.child_right == self

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return not self.child_left and not self.child_right

    def has_one_child(self):
        return self.child_left or self.child_right

    def has_two_childs(self):
        return self.child_left and self.child_right

    def replace_value(self, key=None, value=None, left=None, right=None):
        for key, new in zip(['key', 'value'], [key, value]):
            if new:
                setattr(self, key, new)
        for key, new in zip(['child_left', 'child_right'], [left, right]):
            if new:
                new.parent = self
                setattr(self, key, new)

    def unplug(self):
        if self.is_leaf():
            if self.is_child_left():
                self.parent.child_left = None
            elif self.is_child_right():
                self.parent.child_right = None

        elif self.has_one_child():
            for child in ['child_left', 'child_right']:
                if child:
                    if self.is_child_left():
                        self.parent.child_left = getattr(self, child)
                    elif self.is_child_right():
                        self.parent.child_right = getattr(self, child)
                    break  # shouldnt we continue for both children?

    def find_min(self, node):
        if node.child_left:
            return self.find_min(node.child_left)
        else:
            return node

    def get_successor(self):
        successor = None
        # If the node has a right child, then the successor is the smallest key in the right subtree
        if self.child_right:
            successor = self.find_min(self.child_right)
        # If the node has no right child and is the left child of its parent, then the parent is the successor.
        elif self.parent and self.parent.child_left:
            successor = self.parent
        # # If the node has no right child and is the right child of its parent,, then the successor to this node is the successor of its parent, excluding this node.
        elif self.parent and self.parent.child_right:
            self.parent.child_right = None
            successor = self.get_successor()
            self.parent.child_right = self

        if successor is None:
            print('!!!!!!!!!!!!!!SUCCESSOR NOT FOUND SOMETHING WENT WRONG!!!!!!!!!!!!!!!!!')

        return successor

    def __iter__(self):
        if self:
            if self.child_left:
                for i in self.child_left:
                    yield i
            yield self.key
            if self.child_right:
                for j in self.child_right:
                    yield j


class BinSearchMap():
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if not self.root:
            self.root = TreeNode(key, val)
        else:
            self._put(key, val, self.root)
        self.size += 1

    def _put(self, key, val, node):
        if key >= node.key:
            if node.child_right:
                self._put(key, val, node.child_right)
            else:
                node.child_right = TreeNode(key, val, parent=node)
        else:
            if node.child_left:
                self._put(key, val, node.child_left)
            else:
                node.child_left = TreeNode(key, val, parent=node)

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        result = self._get(key)
        if result:
            return result.value
        return None

    def _get(self, key, node=None):
        if node is None:
            node = self.root
        if key == node.key:
            return node
        if key >= node.key:
            if node.child_right:
                return self._get(key, node.child_right)
        else:
            if node.child_left:
                return self._get(key, node.child_left)
        return None

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return not (self.get(key) is None)

    def delete(self, key):
        if self.size > 1:
            node_to_delete = self._get(key)
            if node_to_delete:
                self._delete(node_to_delete)
                self.size -= 1
            else:
                raise KeyError
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError

    def _delete(self, node: TreeNode):
        if not node.has_one_child():  # no children (the mountain goats)
            if node.is_child_left():
                node.parent.child_left = None
            elif node.is_child_right():
                node.parent.child_right = None

        elif node.has_two_childs():  # 2 childs
            successor = node.get_successor()
            successor.unplug()
            node.key = successor.key
            node.value = successor.value

        elif node.has_one_child():  # 1 child
            if node.child_left:
                child = node.child_left
            else:
                child = node.child_right

            if node.is_child_left():
                child.parent = node.parent
                node.parent.child_left = child
                del node
            elif node.is_child_right():
                child.parent = node.parent
                node.parent.child_right = child
                del node

            else:  # case for root
                node.replace_value(key=child.key,
                                   value=child.value,
                                   left=child.child_left,
                                   right=child.child_right)
        else:
            raise Exception('???? something went wrong')

    def __delete__(self, key):
        self.delete(key)

# testnode = TreeNode('key','value','cleft','cright')
# testnode.replace_value('lol','deez')
# childnode = TreeNode('iam','child')
# testnode.replace_value(left = childnode)
# print(testnode)
# print(testnode.child_left.parent)
# ==
# ==
# ==
# ==
# tree = BinSearchMap()
# tree.put(8, 80)
# tree.put(4, 40)
# tree.put(10, 100)
# tree.put(3, 30)
# tree.put(7, 60)
# tree.put(9, 90)
# tree.put(5, 50)
# tree.put(6, 60)
#
# tree.delete(4)

# my_tree = BinSearchMap()
# my_tree["a"] = "a"
# my_tree["q"] = "quick"
# my_tree["b"] = "brown"
# my_tree["f"] = "fox"
# my_tree["j"] = "jumps"
# my_tree["o"] = "over"
# my_tree["t"] = "the"
# my_tree["l"] = "lazy"
# my_tree["d"] = "dog"
#
# draw = TreeDrawerNoBalance(tree)
# draw.drawtree(1,verticaloffset=-200)
#
# print(my_tree["q"])
# print(my_tree["l"])
# print("There are {} items in this tree".format(len(my_tree)))
# my_tree.delete("a")
# print("There are {} items in this tree".format(len(my_tree)))
#
# for node in my_tree:
#     print(my_tree[node], end=" ")
#
# print()


my_tree = BinSearchMap()
ints = [i for i in range(10)]

print(ints)

for item in range(len(ints)):
    my_tree.put(ints[item],f"{item}'th")

draw = TreeDrawerNoBalance(my_tree)
draw.drawtree(rebuildcoordinates=True, plusdepth=4)