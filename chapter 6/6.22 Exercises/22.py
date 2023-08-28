from things import ParseTree, Stack, binary_treeNAR, NarDrawer
import operator as ops

class ParseTreeBool(ParseTree):  # tedious and lethally boring
    def __init__(self,value=None):
        super().__init__(value)

    def str_to_tree(self, val):
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
            elif char == '!':
                reversenode = binary_treeNAR(value=char)

                if cur_tree.get_root_val() is None:
                    cur_tree.left = reversenode
                else:
                    cur_tree.right = reversenode

                treestack.pop()
                treestack.push(reversenode)

            elif char in '+-*/&|!':
                cur_tree.set_root_val(char)
            elif char.isnumeric() or char in 'TruFalse':
                if cur_tree.get_root_val() is None:
                    insert = self.handle_existingdigits(char, cur_tree.get_left_child())
                    cur_tree.left = None
                    cur_tree.insert_left(insert)
                else:
                    insert = self.handle_existingdigits(char, cur_tree.get_right_child())
                    cur_tree.right = None
                    cur_tree.insert_right(insert)
            elif char == ' ':
                continue
            else:
                raise Exception('Unhandled operator', char)
        return tree

    def tree_to_str(self, node):
        res = ''

        operand1 = node.get_left_child()
        operand2 = node.get_right_child()

        if not (operand1 and operand2):  # if unary
            if not operand1 and not operand2:
                return node.get_root_val()
            elif operand1:
                res += node.get_root_val() + self.tree_to_str(operand1)
            elif operand2:
                res += node.get_root_val() + self.tree_to_str(operand2)

        else:  # if binary
            operand2 = node.get_right_child()
            if not operand1 and not operand2:
                return node.get_root_val()

            res += '(' + self.tree_to_str(operand1) + ' ' + node.get_root_val() + ' ' + self.tree_to_str(operand2) + ')'

        return res

    def operation_not(self, operand1, operand2):
        assert isinstance(operand1,bool)
        return not operand1


    def tree_to_eval(self, node):
        operators = {"+": ops.add,
                     "-": ops.sub,
                     "/": ops.truediv,
                     "*": ops.mul,
                     "&":ops.and_,
                     "|":ops.or_,
                     "!":self.operation_not}

        if not node.get_right_child() and not node.get_left_child():
            return node.get_root_val()

        operator = operators[node.get_root_val()]

        if node.get_root_val() == '!':
            if node.get_left_child() is not None:
                operands = [self.tree_to_eval(node.get_left_child()), None]
            else:
                operands = [self.tree_to_eval(node.get_right_child()), None]
        else:
            operands = [self.tree_to_eval(node.get_left_child()),self.tree_to_eval(node.get_right_child())]

        for idx in range(len(operands)):
            if operands[idx] in ('True','False'):
                if operands[idx] == 'True':
                    operands[idx] = True
                elif operands[idx] == 'False':
                    operands[idx] = False
            elif isinstance(operands[idx],bool) or operands[idx] is None:
                continue
            elif isinstance(operands[idx],int) or (isinstance(operands[idx],str) and operands[idx].isnumeric()):
                operands[idx] = int(operands[idx])
            else:
                raise Exception(f'Unrecognized keyword {operands[idx]}')

        return operator(operands[0],operands[1])

PTree = ParseTreeBool()

tree1 = PTree.str_to_tree('((7+3)*(5-2))') #30
tree2 = PTree.str_to_tree("( ( 10 + 5 ) * 3 )") #45
tree3 = PTree.str_to_tree("((3+4)*(4*5))") #140
tree4 = PTree.str_to_tree("(True | False)")
tree5 = PTree.str_to_tree("(True & !(True | False))")
tree6 = PTree.str_to_tree("(True & !False)")

activetree = tree6

draw = NarDrawer(activetree)
draw.drawtree()

print(PTree.tree_to_str(activetree))
print(PTree.tree_to_eval(activetree))
