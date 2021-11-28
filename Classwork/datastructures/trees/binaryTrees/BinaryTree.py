class BinaryTree:
    class Node:
        def __init__(self, value: int) -> None:
            if isinstance(value,int):
                self.data = value
                self.left = None
                self.right = None
            else:
                raise TypeError("Node value is not an integer.")
    
    def __init__(self, remove_rule: bool) -> None:
        if isinstance(remove_rule,bool):
            self.root = None
            self.size = 0
            #True if findMinValueRightSubTree(), or False if findMaxValueLeftSubTree()
            self.remove_rule = remove_rule
        else:
                raise TypeError("Tree remove rule is not a boolean.")

    def add(self, value: int) -> bool:
        if self.root == None:
            self.root = self.Node(value)
            self.size += 1
            return True
        result = self.add_node(value, self.root)
        #print("Found: "+str(result))
        if result == value: return False
        return True 

    def add_node(self, value: int, node: Node) -> int:
        found = None
        if node == None: return node
        elif node.data > value:
            found = self.add_node(value, node.left)
            if found == None:
                node.left = self.Node(value)
                self.size += 1
                return node.data
        elif node.data < value:
            found = self.add_node(value, node.right)
            if found == None: 
                node.right = self.Node(value)
                self.size += 1
                return node.data
        else: return node.data
        return found

    def contains(self, value: int) -> bool:
        if self.root == None: return False
        result = self.contains_node(value, self.root)
        #print("Found: "+str(result))
        if result == value: return True
        else: return False

    def contains_node(self, value: int, node: Node) -> int:
        found = None
        if node == None: return node
        elif node.data > value:
            found = self.contains_node(value, node.left)
            if found == None:
                return node.data
        elif node.data < value:
            found = self.contains_node(value, node.right)
            if found == None: 
                return node.data
        else: return node.data
        return found

    def remove(self, value: int) -> bool:
        if self.root == None: return False
        #print("Root: ", self.root.data)
        if self.root.data == value:
            copy_left_branch = self.root.left
            copy_right_branch = self.root.right
            replacement = self.remove_replacement(self.root, value)
            if replacement != None:
                #print("copy_left_branch: ", copy_left_branch.data, "copy_right_branch: ", copy_right_branch.data)
                if copy_left_branch != None and copy_right_branch != None:
                    if replacement.data != copy_left_branch.data:
                        replacement.left = copy_left_branch
                    if replacement.data != copy_right_branch.data:
                        replacement.right = copy_right_branch
            self.clear_node(self.root)
            self.root = replacement
            self.size -= 1
            return True
        else:
            result = self.remove_node(value, self.root)
            #print("Found Remove: "+str(result))
            if result == value: return True
            else: return False

    def remove_node(self, value: int, node: Node) -> int:
        found = None
        if node == None: return node
        elif node.data > value:
            #print("trav left")
            found = self.remove_node(value, node.left)
            if found == None:
                return node.data
            elif node.left.data == value:
                copy_left_branch = node.left.left
                copy_right_branch = node.left.right
                replacement = self.remove_replacement(node.left, value)
                #print("current node: ", node.data, "node.left: ", node.left.data)
                #print("replacement --: ", replacement.data)
                if replacement != None:
                    #print("copy_left_branch: ", copy_left_branch.data, "copy_right_branch: ", copy_right_branch.data)
                    if copy_left_branch != None and copy_right_branch != None:
                        if replacement.data != copy_left_branch.data:
                            replacement.left = copy_left_branch
                        if replacement.data != copy_right_branch.data:
                            replacement.right = copy_right_branch
                self.clear_node(node.left)
                node.left = replacement
                self.size -= 1
                return found
        elif node.data < value:
            #print("trav right")
            found = self.remove_node(value, node.right)
            if found == None: 
                return node.data
            elif node.right.data == value:
                copy_left_branch = node.right.left
                copy_right_branch = node.right.right
                replacement = self.remove_replacement(node.right, value)
                #print("current node: ", node.data, "node.right: ", node.right.data)
                #print("replacement node: ",replacement.data)
                if replacement != None:
                    #print("copy_left_branch: ", copy_left_branch.data, "copy_right_branch: ", copy_right_branch.data)
                    if copy_left_branch != None and copy_right_branch != None:
                        if replacement.data != copy_left_branch.data:
                            replacement.left = copy_left_branch
                        if replacement.data != copy_right_branch.data:
                            replacement.right = copy_right_branch
                self.clear_node(node.right)
                node.right = replacement
                self.size -= 1
                return found
        else:
            return node.data
        return found

    def remove_replacement(self, node: Node, value: int) -> Node:
        #print("remove_replacement funct current node: ",node.data)
        if node.left != None and node.right != None:
            node_found = None
            if self.remove_rule:
                node_found = self.findMinValueRightSubTree(node.right, value)
                if node.right.left == None:
                    node.right = node.right.right
            else:
                node_found = self.findMaxValueLeftSubTree(node.left, value)
                if node.left.right == None:
                    node.left = node.left.left
                    #print("if it cant go right left: ", node.left.data)
            #print("node found remove_replacement: ", node_found.data)
            return node_found
        elif node.left != None: return node.left
        elif node.right != None: return node.right
        else: return None

    def findMaxValueLeftSubTree(self, node: Node, value: int) -> Node:
        node_found = None
        if node.right != None: 
            node_found = self.findMaxValueLeftSubTree(node.right, value)
            #print("findMax found: ",node_found.data)
            #print("findMax node.right.data: ",node.right.data)
            if node.right.data == node_found.data:
                #print("findMax condition: ",node.right.data)
                #print("findMax condition current node: ",node.data)
                node.right = node.right.left
                #print("findMax condition now: ",node.right.data)
        else: return node
        return node_found

    def findMinValueRightSubTree(self, node: Node, value: int) -> Node:
        node_found = None
        if node.left != None: 
            node_found = self.findMinValueRightSubTree(node.left, value)
            if node.left.data == node_found.data:
                node.left = node.left.right
        else: return node
        return node_found

    def clear_node(self, node: Node) -> None:
        node.data = None
        node.left = None
        node.right = None

    def preorder(self, node: Node) -> None:
        if node != None:
            print(node.data, end=", ")
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node: Node) -> None:
        if node != None:
            self.inorder(node.left)
            print(node.data, end=", ")
            self.inorder(node.right)

    def postorder(self, node: Node) -> None:
        if node != None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=", ")