class SingleLinkedList:
  class _Node:
    def __init__(self,value):
      self.data = value
      self.next_node = None
  
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def clear(self) -> None:
    if self.size > 0:
      trav = self.head
      while trav.next_node != None:
        next_node = trav.next_node
        trav.next_node = None
        trav.data = None
        trav = next_node
      trav.data = None
      self.head = None
      self.tail = None
      self.size = 0

  def size(self) -> int:
    return self.size

  def length(self) -> int:
    return self.size

  def is_empty(self) -> bool:
    return self.size == 0

  def add_first(self, value) -> None:
    if self.is_empty():
      self.head = self.tail = self._Node(value)
    else:
      node = self._Node(value)
      node.next_node = self.head
      self.head = node
    self.size += 1
  
  def add(self, value) -> None:
    if not self.is_empty():
      trav = self.head
      while trav.next_node != None:
        next_node = trav.next_node
        trav = next_node
      node = self._Node(value)
      trav.next_node = node
      self.tail = node
      self.size += 1
    else:
      self.add_first(value)

  def insert(self, index: int, value) -> None:
    if self.check_index_insert(index):
      if index == 0:
        self.add_first(value)
      elif index == self.size:
        self.add(value)
      else:
        n = 0
        trav = self.head
        prev_trav = None
        while trav.next_node != None and n < index:
          next_node = trav.next_node
          prev_trav = trav
          trav = next_node
          n += 1
        node = self._Node(value)
        node.next_node = trav
        prev_trav.next_node = node
        self.size += 1
    else:
      raise RuntimeError('Invalid index.')

  def check_index_insert(self, index: int) -> bool:
    result = False
    if index > -1 and index <= self.size:
      result = True
    return result

  def get_first(self):
    if self.is_empty():
      raise RuntimeError('List is Empty')
    else:
      print("yo ", )
      return self.head.data

  def get_last(self):
    if self.is_empty():
      raise RuntimeError('List is Empty')
    else:
      return self.tail.data

  def pop_back(self) -> None:
    if not self.is_empty():
      if self.size == 1:
        self.clear()
      else:
        trav = self.head
        prev_trav = None
        while trav.next_node != None:
          next_node = trav.next_node
          prev_trav = trav
          trav = next_node
        trav.data = None
        prev_trav.next_node = None
        self.tail = prev_trav
        self.size = self.size - 1
    else:
      raise RuntimeError('List is Empty')
  
  def pop_first(self) -> None:
    if not self.is_empty():
      if self.size == 1:
        self.clear()
      else:
        temp = self.head
        self.head = self.head.next_node
        temp.data = None
        temp.next_node = None
        self.size = self.size - 1
    else:
      raise RuntimeError('List is Empty')

  def remove(self, index: int) -> None:
    if index > -1 and index < self.size:
      if index == 0:
        self.pop_first()
      elif index == self.size-1:
        self.pop_back()
      else:
        n = 0
        trav = self.head
        prev_trav = None
        while trav.next_node != None and n < index:
          next_node = trav.next_node
          prev_trav = trav
          trav = next_node
          n += 1
        trav.data = None
        prev_trav.next_node = trav.next_node
        trav.next_node = None
        self.size = self.size - 1
    else:
      raise RuntimeError('IndexError')
    
  def print(self) -> None:
    if not self.is_empty():
      node_list = []
      trav = self.head
      n = 0
      while n < self.size:
        node_list.append(trav.data)
        next_node = trav.next_node
        trav = next_node
        n += 1
      print(node_list)
    else:
      print('[]')

  def get(self, index: int):
    if index > -1 and index < self.size:
      if index == 0:
        return self.get_first()
      elif index == self.size-1:
        return self.get_last()
      else:
        n = 0
        trav = self.head
        while trav.next_node != None and n < index:
          next_node = trav.next_node
          trav = next_node
          n += 1
        return trav.data
    else:
      raise RuntimeError('IndexError')

  def invert(self) -> None:
    temp = None
    trav = self.head
    while trav != None:
      trav_next = trav.next_node
      trav.next_node = temp
      temp = trav
      trav = trav_next
    self.head = temp