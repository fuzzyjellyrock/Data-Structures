from BinaryTree import BinaryTree

class userApp:
    def __init__(self) -> None:
        self.tree = None

    def create(self) -> None:
        if self.tree == None:
            arr = self.generate_list()
            self.tree = BinaryTree(True)
            self.add_binary(arr)
            self.print_tree()
        else:
            print("Tree is null")

    def check_root_value(self, number: int) -> bool:
        if number > 15 and number <= 20: return True
        else: return False

    def check_divisibility(self, num: int) -> bool:
        if num % 4 == 0: return True
        else: return False

    def check_repetition(self, num: int, arr: list) -> bool:
        add_to = False
        if arr.count(num) == 0:
            add_to = True
            if self.tree != None:
                if not self.tree.contains(num): add_to = True
                else: add_to = False
        return add_to

    def generate_list(self) -> list:
        arr = []
        done = False
        while not done:
            lim = self.ask_int_data("Number of nodes", ": ")
            if lim > 0:
                done = True
            else:
                print("You need to add at least one element.")
        done = False
        if self.tree == None:
            num = self.ask_root_node_value()
            arr.append(num)
            lim -= 1
        for i in range(lim):
            num = self.ask_node_value(arr)
            arr.append(num) 
        return arr

    def ask_root_node_value(self) -> int:
        while True:
            num = self.ask_int_data("Root Node",": ")
            if self.check_root_value(num) and self.check_divisibility(num):
                return num
            else: print("Number must be greater than 15 and less than or equal to 20\nAlso divisible by 4\n")
        
    def ask_node_value(self, arr: list) -> int:
        while True:
            num = self.ask_int_data("New Node ",": ")
            if self.check_divisibility(num) and self.check_repetition(num, arr):
                return num
            else: print("Numbers cannot be repeated\nThey also must be divisible by 4\n")
        
    def add(self) -> None:
        if self.tree != None:
            arr = self.generate_list()
            self.add_binary(arr)
            self.print_tree()

    def add_binary(self, arr: list) -> None:
        for num in arr:
            self.tree.add(num)

    def print_tree(self) -> None:
        print("******* CURRENT TREE *******")
        self.tree.inorder(self.tree.root)
        print("\n")

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