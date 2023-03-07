class Node():
    def __init__(self, value):
        self.val = value
        self.next = None

    def __str__(self):
        return str(self.value)


class MyLinkedList:

    def __init__(self):
        self.__size = 0
        self.head = None
        self.tail = None

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self,value):
        self.__size = value

    def __str__(self):
        li = ""
        item = self.head
        while item is not None:
            li = li + str(item.val) + ","
            item = item.next
        return "[" + li[:-1] + "]"

    def get(self, index: int) -> int:
        if index < 0:
            return self.head
        current = self.head
        count = 0
        while current is not None:
            if count == index:
                return current.val
            current = current.next
            count += 1
        return -1

    def addAtHead(self, val: int) -> None:
        item = Node(val)
        self.__size += 1

        if self.head is None:
            self.head = item
            self.tail = item
            return

        item.next = self.head
        self.head = item

    def addAtTail(self, val: int) -> None:
        item = Node(val)
        self.__size += 1

        if self.head is None:
            self.head = item
            self.tail = item
            return

        self.tail.next = item
        self.tail = item

    def addAtIndex(self, index: int, val: int) -> None:
        if self.__size < index:
            return

        if index == self.__size:
            return self.addAtTail(val)

        if index < 0:
            return self.addAtHead(val)

        item = Node(val)
        self.__size += 1
        current = self.head
        previous = None
        count = 0

        while current is not None:
            if count >= index:
                break
            previous = current
            current = current.next
            count += 1
        item.next = current

        if previous is None:
            self.head = item
        else:
            previous.next = item

    def deleteAtIndex(self, index: int) -> None:
        if self.__size <= index:
            return
        self.__size -= 1
        current = self.head
        previous = None
        count = 0

        while current is not None:
            if count == index:
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
        return current.val

#Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()



#I built that


methods = ["addAtHead","deleteAtIndex","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtTail","get","deleteAtIndex","deleteAtIndex"]
values = [[2],[1],[2],[7],[3],[2],[5],[5],[5],[6],[4]]
for i,j in zip(methods,values):
    print(f"Action obj.{i}({j})")
    if len(j) == 1:
        print(eval(f"obj."+ i + f"({j[0]})"))
    else:
        print(eval(f"obj." + i + f"({j[0]},{j[1]})"))
    print("===================")
    print("Object:", obj)
    print("Array size:", obj.size)
    print("Array head:", obj.head.val, "Array tail:", obj.tail.val)
    print("===================")
