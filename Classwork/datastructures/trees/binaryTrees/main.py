from BinaryTree import BinaryTree

if __name__ == "__main__":
    t = BinaryTree(True)
    t.add(50)
    t.add(30)
    t.add(20)
    t.add(40)
    t.add(41)
    t.add(32)
    t.add(34)
    t.add(36)
    t.add(70)
    t.add(60)
    t.add(65)
    t.add(80)
    t.add(75)
    t.add(85)

    print("Tree size: ",t.size)
    t.inorder(t.root)

    #print(t.remove(70))
    #print(t.remove(30))
    print(t.remove(50))
    #print(t.remove(20))

    print("Tree size: ",t.size)
    print("root from main: ", t.root.data)
    t.inorder(t.root)
