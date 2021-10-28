class CircularDoublyLinkedList:
    class _Node:
        def __init__(self, value) -> None:
            self.data = value
            self.prev = None
            self.next = None
    
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def is_empty(self) -> bool:
        return self.length == 0

    def print(self) -> None:
        print_list = []
        trav = self.head
        next = None
        while not next is self.head:
            next = trav.next
            print_list.append(trav.data)
            trav = next
        print(print_list)

    def print_inverse(self) -> None:
        print_list = []
        trav = self.tail
        prev = None
        while not prev is self.tail:
            prev = trav.prev
            print_list.append(trav.data)
            trav = prev
        print(print_list)
    
    def add_first(self, value) -> None:
        if self.is_empty():
            node = self._Node(value)
            self.head = node
            self.tail = node
            self.tail.next = self.head
            self.head.prev = self.tail
        else:
            self.head.prev = self._Node(value)
            self.head.prev.next = self.head
            self.head = self.head.prev
            self.tail.next = self.head
            self.head.prev = self.tail
        self.length += 1

    def add(self, value) -> None:
        if self.is_empty():
            self.add_first(value)
        else:
            self.tail.next = self._Node(value)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
            self.tail.next = self.head
            self.head.prev = self.tail
            self.length += 1

    def insert(self, index: int, value) -> None:
        if index > -1 and index <= self.length:
            if index == 0:
                self.add_first(value)
            elif index == self.length:
                self.add(value)
            else:
                trav = self.get_node(index-1)
                node = self._Node(value)
                node.prev = trav
                trav.next.prev = node
                node.next = trav.next
                trav.next = node
                self.length += 1
        else:
            raise RuntimeError('Invalid index.')

    def set(self, index: int, value) -> None:
        if index > -1 and index < self.length:
            node = self.get_node(index)
            node.data = value
        else:
            raise RuntimeError('Invalid index.')

    def clear_node(self, node:_Node) -> None:
        node.data = None
        node.prev = None
        node.next = None

    def clear(self) -> None:
        if not self.is_empty():
            trav = self.head
            next = None
            while not next is self.head:
                next = trav.next
                self.clear_node(trav)
                trav = next
            self.head = None
            self.tail = None
            self.length = 0
            
    def pop_back(self) -> None:
        if not self.is_empty():
            if self.length == 1:
                self.clear()
            else:
                prev = self.tail.prev
                self.clear_node(self.tail)
                self.tail = prev
                self.tail.next = self.head
                self.head.prev = self.tail
                self.length += -1
        else:
            raise RuntimeError('List is empty.')

    def pop_first(self) -> None:
        if not self.is_empty():
            if self.length == 1:
                self.clear()
            else:
                next = self.head.next
                self.clear_node(self.head)
                self.head = next
                self.head.prev = self.tail
                self.tail.next = self.head
                self.length += -1
        else:
            raise RuntimeError('List is empty.')

    def get_node(self, index: int) -> _Node:
        node = None
        if index > -1 and index < self.length:
            middle = self.length-1/2
            if index >= middle:
                trav = self.tail
                n = self.length-1
                while n != index and n >= middle:
                    prev = trav.prev
                    trav = prev
                    n += -1
                node = trav
            else:
                trav = self.head
                n = 0
                while n != index and n <= middle:
                    next = trav.next
                    trav = next
                    n += 1
                node = trav
        else:
            raise RuntimeError('Invalid index.')
        return node

    def pop(self, index: int) -> None:
        if index > -1 and index < self.length:
            if index == 0:
                self.pop_first()
            elif index == self.length-1:
                self.pop_back()
            else:
                node = self.get_node(index)
                node.prev.next = node.next
                node.next.prev = node.prev
                self.clear_node(node)
                self.length += -1
        else:
            raise RuntimeError('Invalid index.')

    def get(self, index: int):
        value = None
        if index > -1 and index < self.length:
            node = self.get_node(index)
            value = node.data
        else:
            raise RuntimeError('Invalid index.')
        return value

    def invert(self) -> None:
        if not self.is_empty():
            trav = self.head
            prev = None
            while (not self.tail.next is prev) or (not trav is self.head):
                prev = trav.prev
                trav.prev = trav.next
                trav.next = prev
                trav = trav.prev
            head = self.head
            self.head = self.tail
            self.tail = head
        else:
            raise RuntimeError('List is empty.')

    def sort(self) -> None:
        if not self.is_empty():
            trav = self.head.next
            prev = None
            while not trav is self.head:
                key = trav.data
                prev = trav.prev
                temp = trav
                while (not prev is self.tail) and key < prev.data:
                    prev.next.data = prev.data
                    temp = prev
                    prev = prev.prev
                temp.data = key
                trav = trav.next
        else:
            raise RuntimeError('List is empty.')