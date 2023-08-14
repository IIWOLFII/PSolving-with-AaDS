import operator as ops


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
            self.left.insert_left(child)

    def insert_right(self, val):
        child = self.right
        if self.right is None:
            self.right = binary_treeNAR(val)
        else:
            self.right = binary_treeNAR(val)
            self.right.insert_right(child)


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, z):
        return self.stack.append(z)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)


def handle_existingdigits(char, peek):
    if peek and isinstance(peek.get_root_val(), str):
        return peek.get_root_val() + char
    return char


def str_to_tree(val):
    tree = binary_treeNAR()
    treestack = Stack()
    treestack.push(tree)
    for char in val[1:len(val) - 1]:
        cur_tree = treestack.peek()
        if char == '(':
            if cur_tree.get_left_child() is None:
                cur_tree.insert_left(None)
                treestack.push(cur_tree.get_left_child())
            else:
                cur_tree.insert_right(None)
                treestack.push(cur_tree.get_right_child())
        elif char == ')':
            treestack.pop()
        elif char in '+-*/':
            cur_tree.set_root_val(char)
        elif char.isnumeric():
            if cur_tree.get_root_val() is None:
                insert = handle_existingdigits(char, cur_tree.get_left_child())
                cur_tree.left = None
                cur_tree.insert_left(insert)
            else:
                insert = handle_existingdigits(char, cur_tree.get_right_child())
                cur_tree.right = None
                cur_tree.insert_right(insert)
        elif char == ' ':
            continue
        else:
            raise Exception('Unhandled operator', char)
    return tree


def tree_to_eval(node):
    operators = {"+": ops.add,
                 "-": ops.sub,
                 "/": ops.truediv,
                 "*": ops.mul}

    if not node.get_right_child() and not node.get_left_child():
        return node.get_root_val()
    operator = operators[node.get_root_val()]
    operand1 = tree_to_eval(node.get_left_child())
    operand2 = tree_to_eval(node.get_right_child())
    return operator(int(operand1), int(operand2))
