import random
from typing import Any

def search(value: Any, array: list) -> int:
    index = -1
    n = 0
    for current in array:
        if current == value:
            index = n
            break
        n += 1
    return index

if __name__ == "__main__":
    l = random.sample(range(30, 100),5)
    print(l)
    value = int(input("Type a number: "))
    print("Index: ", search(value, l))