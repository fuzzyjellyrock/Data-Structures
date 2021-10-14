from double_linked_list import DoubleLinkedList
import math

class TestClass:
  def __init__(self):
    self.dll = DoubleLinkedList()
    self.nums = False
    self.abcs = False

  def fill_list_ints(self) -> None:
    num = self.ask_int_data("Number of nodes to add", " >>>> ")
    for i in range(num):
      data = self.ask_int_data("Node "+i+" value", " >>>> ")
      self.dll.add(data)
    self.nums = True

  def fill_list_abcs(self) -> None:
    num = self.ask_int_data("Number of nodes to add", " >>>> ")
    for i in range(num):
      data = input("Node "+i+" value"+" >>>> ")
      self.dll.add(data)
    self.abcs = True

  def square_it_up(self) -> None:
    for node in self.dll:
      node.data = pow(node.data, 2)

  def greatest_value_node(self) -> int:
    grtst = -math.inf
    index = -1
    n = 0
    for node in self.dll:
      if node.data > grtst:
        grtst = node.data
        index = n
      n += 1
    return index

  def remove_greatest_value(self):
    self.dll.print()
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