from typing import Any

class DoubleLinkedList:
  class _Node:
    def __init__(self, value):
      self.data = value
      self.prev = None
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
    while trav != None:
      next_node = trav.next
      print_list.append(trav.data)
      trav = next_node
    print(print_list)

  def add_first(self, value) -> None:
    if self.is_empty():
      self.head = self._Node(value)
      self.tail = self.head
    else:
      self.head.prev = self._Node(value)
      self.head.prev.next = self.head
      self.head = self.head.prev
    self.length += 1

  def add(self, value) -> None:
    if self.is_empty():
      self.add_first(value)
    else:
      self.tail.next = self._Node(value)
      self.tail.next.prev = self.tail
      self.tail = self.tail.next
      self.length += 1

  def insert(self, index: int,value) -> None:
    if index > -1 and index <= self.length:
      if self.is_empty() or index == 0:
        self.add_first(value)
      elif index == self.length:
        self.add(value)
      else:
        n = 0
        trav = self.head
        while n < index:
          next_node = trav.next
          trav = next_node
          n += 1
        trav.prev.next = self._Node(value)
        trav.prev.next.prev = trav.prev
        trav.prev = trav.prev.next
        trav.prev.next = trav
        self.length += 1
    else:
      raise RuntimeError('Invalid index.')
    
  def clear(self) -> None:
    if self.is_empty():
      self.print()
    else:
      trav = self.head
      while trav != None:
        next_node = trav.next
        self.clear_node(trav)
        trav = next_node
      self.head = None
      self.tail = None
      self.length = 0
  
  def clear_node(self, node: _Node) -> None:
    node.data = None
    node.prev = None
    node.next = None

  def pop_back(self) -> None:
    if not self.is_empty():
      if self.length == 1:
        self.clear()
      else:
        prev = self.tail.prev
        self.clear_node(self.tail)
        prev.next = None
        self.tail = prev
        self.length -= 1
    else:
      raise RuntimeError('List is empty.')

  def pop_first(self) -> None:
    if not self.is_empty():
      if self.length == 1:
        self.clear()
      else:
        next = self.head.next
        self.clear_node(self.head)
        next.prev = None
        self.head = next
    else:
      raise RuntimeError('List is empty.')  

  def pop(self, index: int) -> Any:
    value = None
    if not self.is_empty():
      if index > -1 and index < self.length:
        if self.length == 1:
          value = self.head.data
          self.clear()
        elif index == 0:
          value = self.head.data
          self.pop_first()
        elif index == self.length-1:
          value = self.tail.data
          self.pop_back()
        else:
          n = 0
          trav = self.head
          while n < index:
            next_node = trav.next
            trav = next_node
            n += 1
          value = trav.data
          trav.prev.next = trav.next
          trav.next.prev = trav.prev
          self.clear_node(trav)
          self.length -= 1
    else:
      raise RuntimeError('List is empty.')
    return value

  def remove(self, value: Any) -> Any:
    found = None
    n = 0
    index = -1
    if not self.is_empty():
      trav = self.head
      while found != value:
        next_node = trav.next
        if trav.data == value:
          found = trav.data
          index = n
        trav = next_node
        n += 1
      found = self.pop(index)
    else:
      raise RuntimeError('List is empty.')
    return found

  def get(self, index: int):
    node = None
    value = None
    if not self.is_empty():
      if index > -1 and index < self.length:
        if index == self.length-1:
          node = self.tail
        else:
          n = 0
          trav = self.head
          while n < index:
            next_node = trav.next
            trav = next_node
            n += 1
          node = trav
      else:
        raise RuntimeError('Invalid index.')
    else:
      raise RuntimeError('List is empty.')
    if node != None:
      value = node.data
    return value

  def set(self, index: int, value) -> None:
    if not self.is_empty():
      if index > -1 and index < self.length:
        if index == self.length-1:
          self.tail.data = value
        else:
          n = 0
          trav = self.head
          while n < index:
            next_node = trav.next
            trav = next_node
            n += 1
          trav.data = value
      else:
        raise RuntimeError('Invalid index.')
    else:
      raise RuntimeError('List is empty.')

  def invert(self) -> None:
    if not self.is_empty():
      trav = self.head
      while trav != None:
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
      while trav != None:
        key = trav.data
        prev = trav.prev
        temp = trav
        while prev != None and key < prev.data:
          prev.next.data = prev.data
          temp = prev
          prev = prev.prev
        temp.data = key
        trav = trav.next
    else:
      raise RuntimeError('List is empty.')