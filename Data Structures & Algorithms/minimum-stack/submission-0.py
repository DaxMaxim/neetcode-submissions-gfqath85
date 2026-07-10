class MinStack:

    def __init__(self):
        self.stack, self.minstk = [], []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstk:
            self.minstk.append(min(self.minstk[-1], val))
        else:
            self.minstk.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minstk.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstk[-1]
