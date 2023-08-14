import operator as ops

# traversals

from stuff import str_to_tree

def traversal_preorder(node):
    if node is not None:
        print(node.get_root_val())
        traversal_preorder(node.get_left_child())
        traversal_preorder(node.get_right_child())

def traversal_inorder(node):
    if node is not None:
        traversal_inorder(node.get_left_child())
        print(node.get_root_val())
        traversal_inorder(node.get_right_child())

def traversal_postorder(node):
    if node is not None:
        traversal_postorder(node.get_left_child())
        traversal_postorder(node.get_right_child())
        print(node.get_root_val())

def postorder_eval(node):
    global operators
    if node:
        operand1 = postorder_eval(node.get_left_child())
        operand2 = postorder_eval(node.get_right_child())
        if not operand1 and not operand2:
            return node.get_root_val()
        operator = node.get_root_val()
        return operators[operator](int(operand1),int(operand2))

def tree_to_str(node):
    res = ''
    operand1 = node.get_left_child()
    operand2 = node.get_right_child()
    if not operand1 and not operand2:
        return node.get_root_val() + ' '

    res += '(' + tree_to_str(operand1) + node.get_root_val() + ' ' + tree_to_str(operand2) + ')'
    return res

operators = {"+":ops.add,
             "-":ops.sub,
             "/":ops.truediv,
             "*":ops.mul}

tree1 = str_to_tree('(17+(20/5))')

# print(f'traversal_preorder(tree1)')
# traversal_preorder(tree1)
# print('====')
# print(f'traversal_inorder(tree1)')
# traversal_inorder(tree1)
# print('====')
# print(f'traversal_postorder(tree1)')
# traversal_postorder(tree1)
# print('====')

result = postorder_eval(tree1)
untree = tree_to_str(tree1)
print(untree)