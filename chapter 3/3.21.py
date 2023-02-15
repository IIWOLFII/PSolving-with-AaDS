class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class UnOrderedList():
    def __init__(self):
        self.head = None

    def __str__(self):
        current = self.head
        total = ""
        while current is not None:
            total += str(current.value) + ","
            current = current.next
        return total[:-1]

    def add(self, item: Node):
        item.next = self.head
        self.head = item

    def remove(self, item):
        current = self.head
        previous = None

        while current is not None:
            if current.value == item:
                break
            previous = current
            current = current.next

        if current is None:
            raise ValueError(f"{item} is not in the list")

        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

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
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def append(self):
        pass

    def index(self, item):
        pass

    def insert(self, post, item):
        pass

    def pop(self, pos=None):
        pass


nodes = UnOrderedList()
print("Is empty? ", nodes.is_empty())
nodes.add(Node("First"))
nodes.add(Node("Second"))
nodes.add(Node("Third"))

print("Is empty? ", nodes.is_empty())

print("Size:", nodes.size())

print("Is Second in list? ", nodes.search("Second"))

print(nodes)

nodes.remove("Third")

print(nodes)

print("Size:", nodes.size())

nodes.remove("Balls")
