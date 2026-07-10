class MinStack:

    def __init__(self):
        self.stack, self.minstk = [], []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minstk[-1] if self.minstk else val)
        self.minstk.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minstk.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstk[-1]
