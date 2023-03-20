class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class UnOrderedList_O_N():
    def __init__(self):
        self.head = None

    def __str__(self):
        current = self.head
        total = ""
        while current is not None:
            total += str(current.value) + ","
            current = current.next
        return total[:-1]

    def add(self, item):
        item = Node(item)
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

    def append(self, item):
        item = Node(item)

        if self.head is None:
            self.head = item
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = item

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

        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next
        return current.value

thing = UnOrderedList_O_N()

#testcase = [1,2,6,3,4,5,6]
#testcase = []
testcase = [6,6,6,6]

for i in testcase:
    thing.append(i)

head = thing.head


def removeElements(head, val):
    while head and head.value == val:
        head = head.next
    curr = head
    while curr and curr.next:
        if curr.next.value == val:
            curr.next = curr.next.next
            continue
        curr = curr.next
    return head

res: [Node] = removeElements(head,6)

while res:
    print(res.value)
    res = res.next

