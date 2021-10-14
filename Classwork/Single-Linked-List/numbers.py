from single_linked_list import SingleLinkedList
from colorama import Fore
import math

class NumbersClass:
  def __init__(self):
    self.list = SingleLinkedList()

  def fill_list(self) -> None:
    num = self.ask_int_data("Number of nodes to add", ": ")
    for i in range(num):
      value = self.ask_int_data("Node "+str(i+1)+" value", ": ")
      self.list.add(value)

  def add_sqr_rt_to_list(self) -> None:
    index = self.ask_int_data("Node index", ": ")
    if self.check_index(index):
      value = self.list.get(index)
      sqr_rt = math.sqrt(value)
      self.list.add_first(sqr_rt)

  def add_sqr_node(self) -> None:
    index = self.ask_int_data("Node index", ": ")
    if self.check_index(index):
      value = self.list.get(index)
      self.list.remove(index)
      sqr = math.pow(value,2)
      self.list.add(sqr)

  def ask_int_data(self, input_text: str, separator: str) -> int:
    result = False
    num = 0
    while result == False:
      try:
        num = int(input(input_text+Fore.YELLOW+separator+Fore.RESET))
        result = True
      except ValueError:
        print(Fore.RED+'User input was not a number'+Fore.RESET)
    return num

  def check_index(self, index: int) -> bool:
    result = False
    if index > -1 and index < self.list.length():
      result = True
    else:
      print(Fore.RED+'Invalid index'+Fore.RESET)
    return result