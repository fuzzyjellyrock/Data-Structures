class SimpleCircularList:
  class _Node:
    def __init__(self, value):
      self.data = value
      self.next = None

  def __init__(self):
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

  def add_first(self, value) -> None:
    if self.is_empty():
      node = self._Node(value)
      self.head = node
      self.tail = node
      self.tail.next = self.head
    else:
      temp = self.head
      self.head = self._Node(value)
      self.head.next = temp
      self.tail.next = self.head
    self.length += 1

  def add(self, value) -> None:
    if self.is_empty():
      self.add_first(value)
    else:
      self.tail.next = self._Node(value)
      self.tail = self.tail.next
      self.tail.next = self.head
      self.length += 1
  
  def insert(self, index: int, value) -> None:
    if index > -1 and index <= self.length:
      if index == 0:
        self.add_first(value)
      elif index == self.length:
        self.add(value)
      else:
        trav = self.get_node(index-1)
        next = trav.next
        trav.next = self._Node(value)
        trav.next.next = next
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
        trav = self.get_node(self.length-2)
        self.clear_node(self.tail)
        trav.next = self.head
        self.tail = trav
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
        self.tail.next = self.head
        self.length += -1
    else:
      raise RuntimeError('List is empty.')
  
  def pop(self, index: int) -> None:
    if index > -1 and index < self.length:
      if index == 0:
        self.pop_first()
      elif index == self.length-1:
        self.pop_back()
      else:
        trav = self.get_node(index-1)
        next = trav.next.next
        self.clear_node(trav.next)
        trav.next = next
        self.length += -1
    else:
      raise RuntimeError('Invalid index.')

  def get(self, index: int):
    value = None
    if index > -1 and index < self.length:
      trav = self.get_node(index)
      value = trav.data
    else:
      raise RuntimeError('Invalid index.')
    return value

  def get_node(self, index: int) -> _Node:
    node = None
    if index > -1 and index < self.length:
      trav = self.head
      n = 0
      while n < index:
        next = trav.next
        trav = next
        n += 1
      node = trav
    else:
      raise RuntimeError('Invalid index.')
    return node

  def invert(self):
    if not self.is_empty():
      temp = None
      trav = self.head
      next = None
      while not temp is self.tail:
        next = trav.next
        trav.next = temp
        temp = trav
        trav = next
      self.head = self.tail
      self.tail = trav
      self.tail.next = self.head
    else:
      raise RuntimeError('List is empty.')

  def sort(self) -> None:
    if not self.is_empty():
      i = 1
      key = None
      j = 0
      for i in range(1,self.length):
        key = self.get(i)
        j = i - 1
        while j >= 0 and self.get(j) > key:
          self.set(j+1, self.get(j))
          j += -1
        self.set(j+1, key)
    else:
      raise RuntimeError('List is empty.')