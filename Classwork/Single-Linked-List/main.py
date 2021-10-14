from colorama import Fore
from numbers import NumbersClass

def menu_strings(numbers: NumbersClass) -> None:
  ask_user_call_method(numbers,
  Fore.MAGENTA+'\n\n||||||||||||||||||||||||||||||||||||||'+Fore.RESET
  +Fore.CYAN+'\n********** Single Linked List test **********\n\n'+Fore.RESET
  +Fore.YELLOW+'  1.'+Fore.RESET+' Add nodes\n'
  +Fore.YELLOW+'  2.'+Fore.RESET+' Get square root of Node\n'
  +Fore.YELLOW+'  3.'+Fore.RESET+' Get Node squared\n'
  +Fore.YELLOW+'  4.'+Fore.RESET+' Invert list\n'
  +Fore.YELLOW+'  5.'+Fore.RESET+' Exit\n'
  +Fore.YELLOW+'\nOption: '+Fore.RESET)

def ask_user_call_method(numbers: NumbersClass, text_input: str) -> None:
  result = False
  while result == False:
    answer = input(text_input)
    if answer == '1':
      color_text('\n|||||||||||||| Add nodes ||||||||||||||')
      numbers.fill_list()
      numbers.list.print()
    elif answer == '2':
      color_text('\n|||||||||||||| Get square root of Node ||||||||||||||')
      numbers.add_sqr_rt_to_list()
      numbers.list.print()
    elif answer == '3':
      color_text('\n|||||||||||||| Get Node squared ||||||||||||||')
      numbers.add_sqr_node()
      numbers.list.print()
    elif answer == '4':
      color_text('\n|||||||| Invert list ||||||||')
      numbers.list.invert()
      numbers.list.print()
    elif answer == '5':
      result = True
    else:
      print(Fore.RED+'\nNot a valid option'+Fore.RESET)

def color_text(text_input: str) -> None:
  print(Fore.MAGENTA+text_input+Fore.RESET)

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

if __name__ == "__main__":
  numbers = NumbersClass()
  menu_strings(numbers)