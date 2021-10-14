from double_linked_list import DoubleLinkedList

if __name__ == "__main__":
  list = DoubleLinkedList()
  
  print("Adding nodes...")
  list.add_first(7)
  list.add_first(1)
  list.add(3)
  list.add(5)
  list.add(9)
  list.print()

  print("Deleting index 3...")
  list.pop(3)
  list.print()

  print("Inverting list...")
  list.invert()
  list.print()
  
  print("List length: ", end = "")
  print(list.length)