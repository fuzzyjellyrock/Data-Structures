from stack import StackClass

if __name__ == "__main__":
    s = StackClass()
    s.push(2)
    s.push('a')
    print(s.search(1))
    s.print()