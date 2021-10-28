from typing import Any


class StackClass:
    def __init__(self) -> None:
        self.list = []

    def size(self) -> int:
        return len(self.list)
    
    def is_empty(self) -> bool:
        return len(self.list) == 0

    def push(self, value: Any) -> None:
        self.list.append(value)

    def pop(self) -> Any:
        if not self.is_empty():
            return self.list.pop()

    def peek(self) -> Any:
        if not self.is_empty():
            return self.list[len(self.list)-1]

    def search(self, value: Any) -> int:
        if not self.is_empty():
            return self.list.index(value)

    def print(self) -> None:
        print(self.list)
    