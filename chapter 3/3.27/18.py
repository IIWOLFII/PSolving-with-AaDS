class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class UnOrderedList_O_1():
    def __init__(self):
        self.tail = None
        self.head = None
        self._size = 0

    def __str__(self):
        current = self.head
        total = ""
        while current is not None:
            total += str(current.value) + ","
            current = current.next
        return "[" + total[:-1] + "]"

    def add(self, item):
        item = Node(item)
        item.next = self.head
        if self.head is None:
            self.tail = item
        self.head = item
        self._size += 1

    def remove(self, item):
        current = self.head
        previous = None

        while current is not None:
            if current.value == item:
                break
            previous = current
            current = current.next

        if current is None: #if item is not found then remove last one i guess #13
            item = self.pop()
            return

        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

        if current == self.tail:
            self.tail = previous
        self._size -= 1

    def search(self, item):
        current = self.head
        while current is not None:
            if current.value == item:
                return True
            current = current.next
        return False

    def is_empty(self):
        return self.head is None

    def size(self):
        return self._size

    def append(self, item):
        item = Node(item)
        self._size += 1

        if self.head is None:
            self.head = item
            self.tail = item
            return

        self.tail.next = item
        self.tail = item

    def index(self, item):
        current = self.head
        count = 0
        while current is not None:
            if current.value == item:
                return count
            current = current.next
            count += 1
        return None

    def insert(self, pos, item):
        item = Node(item)
        current = self.head
        previous = None
        count = 0

        while current is not None:
            if count >= pos:
                break
            previous = current
            current = current.next
            count += 1

        self._size += 1
        item.next = current
        if previous is None:
            self.head = item
        else:
            previous.next = item

    def pop(self, pos=None):
        current = self.head
        previous = None
        count = 0

        if current is None:
            return None

        while current.next is not None:
            if count == pos:
                break
            previous = current
            current = current.next
            count += 1

        if current == self.tail:
            self.tail = previous

        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next
        self._size -= 1
        return current.value

    def slice(self,start,stop): #stop is excluded
        sliced = UnOrderedList_O_1()
        count = 0
        current = self.head

        while current.next is not None : #and not (count + 1 == stop)
            if count == stop:
                break

            if count >= start:
                sliced.append(current)

            current = current.next
            count += 1

        return sliced



nodes = UnOrderedList_O_1()

for i in ['cart', 'wheels', 'pickaxe', 'shovel', 'bow', 'creeper', 'brick', 'grass', 'tnt', 'ice']:
    nodes.append(i)

print(nodes)

print(nodes.slice(4,6))

#nodes = UnOrderedList_O_1()
#
# print(nodes)
#
# print("Is empty? ", nodes.is_empty())
# nodes.add("First")
# nodes.add("Second")
# nodes.add("Third")
#
# print(nodes)
#
# print("Is empty? ", nodes.is_empty())
#
# print("Size:", nodes.size())
# print(nodes)
#
#
# print("Is Second in list? ", nodes.search("Second"))
#
# print(nodes)
#
# nodes.remove("Third")
#
# print(nodes)
#
# print("Size:", nodes.size())
#
# nodes.append("BALLS")
#
# print(nodes)
#
# nodes.append("AND")
#
# nodes.append("COCK")
#
# print(nodes)
#
# print("Size:", nodes.size())
#
# print("Index of BALLS is", nodes.index("BALLS"))
# print("Index of COCK is", nodes.index("COCK"))
# print("Index of Second is", nodes.index("Second"))
# print("Index of Invalid is", nodes.index("Invalid"))
#
# nodes.insert(2,"test")
# print("Index of test is", nodes.index("test"))
# print(nodes)
#
# #nodes = UnOrderedList()
#
# print("POP THE COCK",nodes.pop())
#
# print(nodes)
#
# print("POP THE BALLS",nodes.pop(3))
#
# print(nodes)
#
# print("POP THE SECOND",nodes.pop(0))
#
# print(nodes)
#
# print("POP THE INVALID",nodes.pop(23))
#
# print(nodes)
#
# print("head and tail")
# print(nodes.head)
# print(nodes.tail)
#
# nodes.pop()
# nodes.pop()
# print("Popped two remaining")
# print("Printing nodes... ", end="")
# print(nodes)
#
# print("Adding nodes")
# nodes.append("Does it work")
#
# print(nodes.head)
# print(nodes.tail)
#
# nodes.append("bruh")
#
# print(nodes.head)
# print(nodes.tail)
#
# nodes.remove("bruh")
#
# print(nodes.head)
# print(nodes.tail)
# print(nodes.size())
# nodes.remove("Balls")
#
# print(nodes.size())
#
# print(nodes.append("thing"))
# print(nodes.append("thing"))
# print(nodes)
# print(nodes.size())
