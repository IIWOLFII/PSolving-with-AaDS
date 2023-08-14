from stuff import binary_treeNAR, Stack
import operator as ops

def handle_existingdigits(char, peek):
    if peek and isinstance(peek.get_root_val(), str):
        return peek.get_root_val() + char
    return char

# parse tree
def str_to_tree(val):
    tree = binary_treeNAR()
    treestack = Stack()
    treestack.push(tree)
    for char in val[1:len(val)-1]:
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
                insert = handle_existingdigits(char,cur_tree.get_left_child())
                cur_tree.left = None
                cur_tree.insert_left(insert)
            else:
                insert = handle_existingdigits(char,cur_tree.get_right_child())
                cur_tree.right = None
                cur_tree.insert_right(insert)
        elif char == ' ':
            continue
        else: raise Exception('Unhandled operator', char)
    return tree

def tree_to_eval(node):
    operators = {"+":ops.add,
                 "-":ops.sub,
                 "/":ops.truediv,
                 "*":ops.mul}

    if not node.get_right_child() and not node.get_left_child():
        return node.get_root_val()

    operator = operators[node.get_root_val()]
    operand1 = tree_to_eval(node.get_left_child())
    operand2 = tree_to_eval(node.get_right_child())

    return operator(int(operand1), int(operand2) )

tree1 = str_to_tree('((7+3)*(5-2))')
tree2 = str_to_tree("( ( 10 + 5 ) * 3 )")
tree3 = str_to_tree("(3+4(4*5))")
print(tree_to_eval(tree3))

