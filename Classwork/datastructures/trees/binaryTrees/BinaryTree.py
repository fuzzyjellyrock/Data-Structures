class BinaryTree:
    class Node:
        def __init__(self, value: int) -> None:
            if isinstance(value,int):
                self.data = value
                self.left = None
                self.right = None
            else:
                raise TypeError("Node value is not an integer.")
    
    def __init__(self) -> None:
        self.root = None
        self.size = 0

    def add(self, value: int) -> bool:
        if self.root == None:
            self.root = self.Node(value)
            self.size += 1
            return True
        result = self.add_node(value, self.root)
        if result == value: return False
        return True 

    def add_node(self, value: int, node: Node) -> int:
        if node == None: return node
        elif node.data > value:
            found = self.add_node(value, node.left)
            if found == None: 
                node.left = self.Node(value)
                self.size += 1
        elif node.data < value:
            found = self.add_node(value, node.right)
            if found == None: 
                node.right = self.Node(value)
                self.size += 1
        return node.data

    def inorder(self, node: Node) -> None:
        if node != None:
            self.inorder(node.left)
            print(node.data, end=", ")
            self.inorder(node.right)

