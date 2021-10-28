from test import TestClass

if __name__ == "__main__":
  test = TestClass()

  print("Create List with numbers")
  print("\n||||||||| Fill list |||||||||")
  test.fill_list_ints()
  print("\n||||||||| Sort list |||||||||")
  test.dll.sort()
  test.dll.print()
  test.square_it_up()
  print("\n|||||||| Remove greatest value ||||||||")
  test.remove_greatest_value()

  print("\nCreate List with letters")
  print("\n||||||||| Fill list |||||||||")
  test.fill_list_abcs()
  print("\n||||||||| Sort list |||||||||")
  test.dll.sort()
  test.dll.print()