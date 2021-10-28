from parking import ParkingSystem
from colorama import Fore

def menu(p: ParkingSystem) -> None:
  ask_user_call_method(p,
  Fore.MAGENTA+'\n\n||||||||||||||||||||||||||||||||||||||'+Fore.RESET
  +Fore.CYAN+'\n********** Vaccination **********\n\n'+Fore.RESET
  +Fore.YELLOW+'  1.'+Fore.RESET+' Add parking spot\n'
  +Fore.YELLOW+'  2.'+Fore.RESET+' Delete parking spot\n'
  +Fore.YELLOW+'  3.'+Fore.RESET+' Exit\n'
  +Fore.YELLOW+'\nOption: '+Fore.RESET)

def ask_user_call_method(p: ParkingSystem, text_input: str) -> None:
  while True:
    answer = input(text_input)
    if answer == '1':
      color_menu_text('\n|||||||||||||| Add people ||||||||||||||')
      p.add_parking_spot()
    elif answer == '2':
      color_menu_text('\n|||||||||||||| Total vaxxed people ||||||||||||||')
      p.delete_parking_spot()
    elif answer == '3':
      break
    else:
      print(Fore.RED+'\nNot a valid option'+Fore.RESET)

def color_menu_text(text_input: str) -> None:
  print(Fore.MAGENTA+text_input+Fore.RESET)

if __name__ == "__main__":
  p = ParkingSystem()
  menu(p)
  