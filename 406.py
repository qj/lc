class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minMap = {}
        self.minSoFar = float("inf")

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.minSoFar = min(self.minSoFar, x)
        self.minMap[len(self.stack)] = self.minSoFar


    def pop(self) -> None:
        top = self.stack[-1]
        if top == self.minSoFar:
            self.minSoFar = self.minMap[len(self.stack) - 1]
        self.minMap.pop(len(self.stack))
        top = self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minSoFar
