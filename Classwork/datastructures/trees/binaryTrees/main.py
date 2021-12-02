from BinaryTree import BinaryTree

if __name__ == "__main__":
    t = BinaryTree(True)
    t.add(3)
    t.add(1)
    t.add(7)
    t.add(2)
    t.add(6)
    t.add(5)
    t.add(4)
    t.add(9)
    t.add(8)

    print("Tree size: ",t.size)
    t.postorder(t.root)
    print("\n")
    t.preorder(t.root)

    """
    #print(t.remove(70))
    #print(t.remove(30))
    print(t.remove(50))
    #print(t.remove(20))

    print("Tree size: ",t.size)
    print("root from main: ", t.root.data)
    t.inorder(t.root)
    """
