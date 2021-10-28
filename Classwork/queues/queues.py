from typing import Any


class QueueClass:
    def __init__(self) -> None:
        self.list = []
    
    def is_empty(self) -> bool:
        return len(self.list) == 0

    def offer(self, value: Any) -> None:
        self.list.append(value)

    def poll(self) -> Any:
        if not self.is_empty():
            return self.list.pop(0)

    def clear(self) -> None:
        self.list.clear()

    def size(self) -> int:
        return len(self.list)

    def peek(self) -> Any:
        if not self.is_empty():
            return self.list[0]

    def print(self) -> None:
        print(self.list)