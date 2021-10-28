from simple_circular_list import SimpleCircularList

if __name__ == "__main__":
    l = SimpleCircularList()
    l.add('a')
    l.add('b')
    l.add_first('c')
    l.add('d')
    l.insert(2,'e')
    l.print()

    node = l.get_node(l.length-1)
    print("[0]: "+node.next.data)
    
    n = 1
    print("[",n,"] = "+l.get(n))
    print('list length: ',l.length)
    l.invert()
    l.print()
    node = l.get_node(l.length-1)
    print("[0]: "+node.next.data)