from things import BinAVLMap, TreeDrawer


class DelBinAVLMap(BinAVLMap):
    def __init__(self):
        super().__init__()

    def delete(self, key):
        if self.size > 1:
            node_to_delete = self._get(key)
            if node_to_delete:
                parent = node_to_delete.parent
                self._delete(node_to_delete)
                self.size -= 1
                if parent:
                    self.update_balance(parent)
                else:
                    self.update_balance(self.root)
            else:
                raise KeyError
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError

tree = DelBinAVLMap()
tree.put(40, 'E')
tree.put(50, 'F')
tree.put(30, 'C')
tree.put(35, 'D')
tree.put(20, 'B')
tree.put(10, 'A')
tree.put(42, 'E')
tree.put(54, 'F')
tree.put(36, 'C')
tree.put(31, 'D')
tree.put(26, 'B')
tree.put(18, 'A')

tree.delete(30)
draw = TreeDrawer(tree)
draw.drawtree()