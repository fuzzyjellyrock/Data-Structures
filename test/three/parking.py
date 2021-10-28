from double_linked_list import DoubleLinkedList

class ParkingSystem:
    def __init__(self) -> None:
        self.list = DoubleLinkedList()
        self.capacity = 6

    def add_parking_spot(self) -> bool:
        print("Add parking spot")
        if self.list.length < self.capacity:
            while True:
                num = self.ask_int_data("Type the number of your parking spot", ": ")
                if self.check_number(num):
                    self.list.add(num)
                    self.list.sort()
                    self.list.print()
                    if self.list.length == self.capacity:
                        print('Max capacity reached.')
                    break
                else:
                    print('Wrong number')
        else:
            print('Max capacity reached.')

    def delete_parking_spot(self) -> bool:
        print("Delete parking spot")
        if not self.list.is_empty():
            while True:
              num = self.ask_int_data("Type the number of your parking spot",": ")
              if self.check_number(num):
                  if self.list.remove(num) == num:
                    self.list.print()
                    break
                  else:
                    print('Number not inside the list')
              else:
                  print('Wrong number')
        else:
            print('No parking spots available.')
    
    def check_number(self, number: int) -> int:
        result = False
        if(number > 85 and number < 92):
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