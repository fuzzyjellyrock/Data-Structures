from userApp import userApp

def menu(t: userApp) -> None:
  ask_user_call_method(t,
  '\n\n||||||||||||||||||||||||||||||||||||||'
  +'\n********** Trees **********\n\n'
  +'  1.'+' Create Tree\n'
  +'  2.'+' Add nodes to tree\n'
  +'  3.'+' Print tree\n'
  +'  4.'+' Exit\n'
  +'\nOption: ')

def ask_user_call_method(t: userApp, text_input: str) -> None:
  while True:
    answer = input(text_input)
    if answer == '1':
      print('\n|||||||||||||| Create Tree ||||||||||||||')
      t.create()
    elif answer == '2':
      print('\n|||||||||||||| Add nodes ||||||||||||||')
      t.add()
    elif answer == '3':
      print('\n|||||||||||||| Print tree ||||||||||||||')
      t.print_tree()
    elif answer == '4':
      break
    else:
      print('\nNot a valid option')

if __name__ == "__main__":
    t = userApp()
    menu(t)