from simple_circular_list import SimpleCircularList

class GameClass:
  def __init__(self, start: int, step: int):
    self.list = SimpleCircularList()
    self.start = start
    self.step = step

  def fill_list(self) -> None:
    n = self.start
    self.list.add(n)
    for i in range(3):
      n = n+self.step
      self.list.add(n)
    for i in range(2):
      self.list.add(None)
      n += self.step
    for i in range(3):
      n = n+self.step
      self.list.add(n)
  
  def ask_user(self) -> None:
    index = 4
    exit = False
    n = 0
    while not exit:
      if n == 3:
        exit = True
      elif index < 6:
        print("Fill the remaining numbers (None)")
        self.list.print()
        num = self.ask_int_data("Number",": ")
        if self.check_number(num, index):
          self.list.set(index, num)
          index += 1
          n = 0
        else:
          n += 1
          print('Wrong number, strike ', n)
      else:
        exit = True
    if n > 2:
      print('You lost. Try next time.')
    else:
      self.list.print()
      print('You won.')

  def check_number(self, num: int, index: int) -> bool:
    result = False
    if(num == self.list.get(index-1)+self.step):
      result = True
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
