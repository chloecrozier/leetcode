# https://leetcode.com/problems/design-a-stack-with-increment-operation/description/?envType=daily-question&envId=2024-09-30
class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return -1
        
    def increment(self, k: int, val: int) -> None:
        for i in range(0, min(k, len(self.stack))):
            self.stack[i] += val
