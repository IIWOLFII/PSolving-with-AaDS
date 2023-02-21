class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class OrderedList(): #min to max
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
        current = self.head
        previous = None

        while current is not None and item.value > current.value:
            previous = current
            current = current.next

        item.next = current

        if previous is None:
            self.head = item
        else:
            previous.next = item


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
            if current.value > item:
                return False
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

    def index(self, item):
        current = self.head
        count = 0
        while current is not None:
            if current.value == item:
                return count
            current = current.next
            count += 1
        return None

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

my_list = OrderedList()
my_list.add(31)
my_list.add(77)
my_list.add(17)
my_list.add(93)
my_list.add(26)
my_list.add(54)

print(my_list.size())
print(my_list.search(93))
print(my_list.search(100))
