from typing import NamedTuple

class MinStack:
    class Element(NamedTuple):
        value: int
        current_min: int

    def __init__(self):
        self.stack = deque()


    def push(self, val: int) -> None:
        if len(self.stack):
            prev_min = self.stack[-1].current_min
            self.stack.append(self.Element(val, min(prev_min, val)))
        else:
            self.stack.append(self.Element(val, val))


    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1].value
        

    def getMin(self) -> int:
        return self.stack[-1].current_min
        
