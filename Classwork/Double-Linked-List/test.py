from double_linked_list import DoubleLinkedList
import math

class TestClass:
  def __init__(self):
    self.dll = DoubleLinkedList()
    self.nums = False
    self.abcs = False

  def fill_list_ints(self) -> None:
    if self.abcs == True:
      self.dll.clear()
      self.abcs = False
    num = self.ask_int_data("Number of nodes to add", " >>>> ")
    for i in range(num):
      data = self.ask_int_data("Node value", " >>>> ")
      self.dll.add(data)
    self.nums = True
    self.dll.print()

  def fill_list_abcs(self) -> None:
    if self.nums == True:
      self.dll.clear()
      self.nums = False
    num = self.ask_int_data("Number of nodes to add", " >>>> ")
    for i in range(num):
      data = input("Node value"+" >>>> ")
      self.dll.add(data)
    self.abcs = True
    self.dll.print()

  def square_it_up(self) -> None:
    for i in range(self.dll.length):
      value = self.dll.get(i)
      self.dll.set(i, pow(value,2))
    print("\n|||||||| squared elements list ||||||||")
    self.dll.print()
    self.dll.invert()
    print("\n|||||||| inverse of squared elements list ||||||||")
    self.dll.print()

  def greatest_value_node(self) -> int:
    grtst = -math.inf
    index = -1
    for i in range(self.dll.length):
      value = self.dll.get(i)
      if value > grtst:
        grtst = value
        index = i
    return index

  def remove_greatest_value(self):
    index = self.greatest_value_node()
    self.dll.pop(index)
    self.dll.print()

  def ask_int_data(self, input_text: str, separator: str) -> int:
    result = False
    num = 0
    while not result:
      try:
        num = int(input(input_text+separator))
        result = True
      except ValueError:
        print('User input was not a number')
    return num