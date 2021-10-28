from double_linked_list import DoubleLinkedList
class SeriesClass:
  def __init__(self):
    self.list = DoubleLinkedList()

  def fill_list(self):
    print()

  def ask_user(self):
    while True:
      print("Add a number that follows the sequence")
      num = self.ask_int_data("Number",": ")
      if check_number(num):
        self.list.add(num)
        break
      else:
        print("Wrong number.")
      self.list.print()

  def check_number(self, number: int):
    result = False
    if
    return result

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