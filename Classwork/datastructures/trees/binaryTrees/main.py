from BinaryTree import BinaryTree

if __name__ == "__main__":
    t = BinaryTree()
    t.add(5)
    t.add(3)
    t.add(2)
    t.add(4)
    t.inorder(t.root)